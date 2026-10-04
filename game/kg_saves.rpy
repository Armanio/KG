default kg_chapter_end_saved = False
# Save UI and policy for the first two chapters. Existing 1-0 .. 1-5 slots are preserved.
default kg_read_count = 0
default kg_save_scene = "prolog"
default kg_resume_pending = False
default kg_checkpoint_pending = False

init -10 python:
    from renpy.rollback import UnfreezeException as KGUnfreeze
    import time as kg_time
    import json as kg_json
    import types as kg_types
    import zipfile as kg_zip
    import io as kg_io
    import base64 as kg_base64
    import os as kg_os

    renpy.kg_io = kg_types.SimpleNamespace(busy=False, next_action=None, error=None, staged=None, choice_seen=None, last_write=0.0, loaded_scene=None)
    KG_MANUAL = tuple("1-" + str(i) for i in range(6))
    KG_HISTORY = ("kg-checkpoint-0", "kg-checkpoint-1", "kg-checkpoint-2")
    KG_RESUME = "kg-resume"
    KG_SLOTS = KG_MANUAL + (KG_RESUME,) + KG_HISTORY
    KG_SCENES = {
        "prolog": "Пролог · Меньшее зло",
        "kg_end_chapter_1": "Конец 1 главы",
        "kg_end_chapter_2": "Конец 2 главы",
        "scene_1_1": "Глава 1 · Шаттл",
        "scene_1_2": "Глава 1 · Собеседование",
        "scene_1_3": "Глава 1 · Общий сбор",
        "scene_1_4": "Глава 1 · Прогулка в саду",
        "scene_1_5": "Глава 1 · Незнакомец",
        "scene_1_6": "Глава 1 · Пропавшие часы",
        "scene_2_1": "Глава 2 · Сообщение отца",
        "scene_2_2": "Глава 2 · Завтрак",
        "scene_2_3": "Глава 2 · Лекция Вирта",
        "scene_2_3_after_lecture": "Глава 2 · Лекция Вирта",
        "scene_2_4": "Глава 2 · Поиски архива",
        "scene_2_5": "Глава 2 · Практика Каэля",
        "scene_2_6": "Глава 2 · Задача Каэля",
        "scene_2_7": "Глава 2 · Вечер в архиве",
        "scene_2_8": "Глава 2 · Разговор с наставником",
        "scene_2_9": "Глава 2 · Верни книгу",
    }

    def kg_title():
        return KG_SCENES.get(getattr(store, "current_scene", kg_save_scene), KG_SCENES.get(kg_save_scene, "Сохранение игры"))

    def kg_metadata(data):
        data["kg_title"] = kg_title()
        data["kg_schema"] = 1

    def kg_entries():
        slots = [s for s in KG_SLOTS if renpy.can_load(s)]
        return sorted(slots, key=lambda s: (renpy.slot_mtime(s) or 0, s), reverse=True)

    def kg_continue_slot():
        if renpy.can_load(KG_RESUME):
            return KG_RESUME
        # Old autosaves remain on disk; use the newest as a migration fallback.
        old = renpy.list_saved_games(regexp=r"^(1-[0-5]|auto-[0-9]+|quick-[0-9]+|kg-.*)$", fast=True)
        return max(old, key=lambda x: renpy.slot_mtime(x) or 0) if old else None

    def kg_slot_title(slot):
        data = renpy.slot_json(slot) or {}
        return data.get("kg_title") or data.get("_save_name") or "Сохранение игры"

    def kg_date(slot):
        stamp = renpy.slot_mtime(slot)
        return kg_time.strftime("%d.%m.%Y  %H:%M", kg_time.localtime(stamp)) if stamp else ""

    def kg_error(message):
        renpy.kg_io.error = message
        renpy.show_screen("kg_save_error", message=message)

    def kg_sync(after=None, error_message=None):
        state = renpy.kg_io
        state.next_action = after
        state.sync_error_message = error_message
        if renpy.emscripten:
            state.busy = True
            renpy.emscripten.run_script("window.kgSyncStatus='pending'; try { FS.syncfs(false, function(e){window.kgSyncStatus=e?'error':'ok';}); } catch(e) { window.kgSyncStatus='error'; }")
            renpy.show_screen("kg_sync_wait")
        else:
            state.busy = False
            if after:
                after()

    def kg_poll_sync():
        result = renpy.emscripten.run_script_string("window.kgSyncStatus || 'error'")
        if result == "pending":
            return
        state = renpy.kg_io
        state.busy = False
        renpy.hide_screen("kg_sync_wait")
        action = state.next_action
        state.next_action = None
        if result == "ok":
            if action:
                action()
        else:
            kg_error(getattr(state, "sync_error_message", None) or "Браузер не смог записать сохранение. Игра остаётся открытой. Освободи место или скачай сохранения в файл и повтори попытку.")

    def kg_write(slot, screenshot=False, after=None, history=False):
        if renpy.kg_io.busy or main_menu:
            return False
        try:
            if screenshot:
                renpy.take_screenshot()
            # Save the resume slot before rotating history; manual slots never participate.
            renpy.save(slot, extra_info=kg_title())
            if history:
                target = min(KG_HISTORY, key=lambda s: renpy.slot_mtime(s) or 0)
                renpy.copy_save(slot, target)
                renpy.loadsave.location.scan()
                renpy.loadsave.clear_slot(target)
            renpy.kg_io.last_write = kg_time.monotonic()
            kg_sync(after)
            return True
        except (renpy.game.FullRestartException, renpy.game.QuitException):
            raise
        except Exception as e:
            renpy.log("KG save failed: " + repr(e))
            kg_error("Не удалось сохранить игру. Предыдущее сохранение не следует считать обновлённым. Попробуй ещё раз.")
            return False

    def kg_resume(after=None):
        store.kg_read_count = 0
        store.kg_resume_pending = False
        return kg_write(KG_RESUME, after=after)

    def kg_exit_menu():
        kg_resume(lambda: renpy.full_restart())

    def kg_quit():
        if main_menu:
            renpy.quit()
        else:
            renpy.take_screenshot(keep_existing=bool(renpy.get_screen("main_overlay_menu")))
            kg_resume(lambda: renpy.quit())

    def kg_manual(slot):
        if renpy.can_load(slot):
            renpy.show_screen("kg_confirm", title="Перезаписать сохранение?", message=kg_slot_title(slot) + "\n" + kg_date(slot), yes=Function(kg_manual_commit, slot))
        else:
            kg_manual_commit(slot)

    def kg_manual_commit(slot):
        kg_write(slot, after=lambda: renpy.notify("Игра сохранена"))

    def kg_delete_prompt(slot):
        if renpy.kg_io.busy or slot not in KG_SLOTS or not renpy.can_load(slot):
            return
        renpy.show_screen("kg_confirm", title="Удалить сохранение?",
            message=kg_slot_title(slot) + "\n" + kg_date(slot) + "\n\nЭту запись нельзя будет восстановить без скачанной копии.",
            yes=Function(kg_delete_commit, slot), yes_text="Удалить")

    def kg_delete_commit(slot):
        if renpy.kg_io.busy or slot not in KG_SLOTS or not renpy.can_load(slot):
            return
        try:
            renpy.unlink_save(slot)
            renpy.loadsave.location.scan()
            renpy.loadsave.clear_slot(slot)
            kg_sync(after=kg_deleted, error_message="Не удалось подтвердить удаление в хранилище браузера. После перезапуска запись может появиться снова. Попробуй удалить её ещё раз.")
        except Exception as e:
            renpy.log("KG delete failed: " + repr(e))
            kg_error("Не удалось удалить сохранение. Попробуй ещё раз.")
        renpy.restart_interaction()

    def kg_deleted():
        renpy.notify("Сохранение удалено")
        renpy.restart_interaction()

    def kg_load(slot):
        try:
            renpy.load(slot)
        except KGUnfreeze:
            raise
        except Exception as e:
            renpy.log("KG load failed: " + repr(e))
            kg_error("Не удалось загрузить сохранение. Выбери другую запись.")

    def kg_new_game():
        if kg_continue_slot():
            renpy.show_screen("kg_confirm", title="Начать новую игру?", message="«Продолжить» будет вести в новое прохождение. Ручные сохранения и предыдущие контрольные точки останутся.", yes=Start())
        else:
            renpy.run(Start())

    def kg_label(name, abnormal):
        if name in KG_SCENES:
            restored_boundary = renpy.kg_io.loaded_scene == name
            renpy.kg_io.loaded_scene = None
            store.kg_save_scene = name
            if not restored_boundary and name in ("prolog", "scene_1_1"):
                store.kg_resume_pending = True
                store.kg_checkpoint_pending = True

    def kg_character(event, interact=True, **kwargs):
        if event == "end" and interact and not main_menu and not renpy.is_init_phase():
            store.kg_read_count += 1
            if kg_read_count >= 20:
                store.kg_resume_pending = True

    def kg_safe_tick():
        if main_menu or renpy.kg_io.busy or renpy.get_screen("main_overlay_menu"):
            return
        if kg_resume_pending or kg_checkpoint_pending:
            if renpy.is_skipping() and not kg_checkpoint_pending and kg_time.monotonic() - renpy.kg_io.last_write < 1.0:
                return
            history = kg_checkpoint_pending
            store.kg_resume_pending = False
            store.kg_checkpoint_pending = False
            store.kg_read_count = 0
            if not kg_write(KG_RESUME, screenshot=True, history=history):
                store.kg_resume_pending = True
                store.kg_checkpoint_pending = history

    def kg_choice_checkpoint():
        # A screen timer runs once the actual choice frame has been drawn.
        if not main_menu and not renpy.kg_io.busy:
            kg_write(KG_RESUME, screenshot=True, history=True)

    def kg_choice_done():
        store.kg_resume_pending = True

    def kg_chapter_saved():
        store.kg_chapter_end_saved = True
        renpy.restart_interaction()

    def kg_begin_chapter_save_notice():
        renpy.set_screen_variable("save_notice_until", kg_time.monotonic() + 0.5)
        kg_save_chapter_end()

    def kg_save_chapter_end():
        if renpy.kg_io.busy:
            return
        store.kg_read_count = 0
        store.kg_resume_pending = False
        store.kg_checkpoint_pending = False
        # Retain the screen flag across Ren'Py load rollback.
        renpy.retain_after_load()
        # The saved snapshot must reopen this screen without another autosave.
        store.kg_chapter_end_saved = True
        ok = kg_write(KG_RESUME, screenshot=True, history=True, after=kg_chapter_saved)
        if not ok or renpy.kg_io.busy:
            store.kg_chapter_end_saved = False
        renpy.restart_interaction()

    def kg_after_load():
        store.kg_chapter_end_saved = getattr(store, "current_scene", "") in ("kg_end_chapter_1", "kg_end_chapter_2")
        # Loading an older manual slot makes it the current playthrough immediately.
        store.kg_resume_pending = getattr(store, "current_scene", "") not in ("kg_end_chapter_1", "kg_end_chapter_2")
        store.kg_checkpoint_pending = False
        store.kg_read_count = 0
        renpy.kg_io.busy = False
        renpy.kg_io.next_action = None
        renpy.kg_io.loaded_scene = getattr(store, "current_scene", kg_save_scene)

    def kg_export():
        if renpy.emscripten:
            renpy.emscripten.run_script("window.onSavegamesExport()")

    def kg_import_pick():
        if not renpy.emscripten:
            return
        script = renpy.file("kg_import.js").read().decode("utf-8")
        font = kg_base64.b64encode(renpy.file("gui/fonts/Montserrat-SemiBold.ttf").read()).decode("ascii")
        renpy.emscripten.run_script(script.replace("__KG_FONT__", font))

    def kg_stage_import(encoded):
        try:
            staged = {}
            total = 0
            with kg_zip.ZipFile(kg_io.BytesIO(kg_base64.b64decode(encoded))) as archive:
                for entry in archive.infolist():
                    name = entry.filename
                    if "/" in name:
                        prefix, name = name.split("/", 1)
                        if prefix != config.save_directory:
                            continue
                    if name not in [s + renpy.savegame_suffix for s in KG_SLOTS]:
                        continue
                    total += entry.file_size
                    if total > 32 * 1024 * 1024 or name in staged:
                        raise ValueError("Invalid archive size or duplicate")
                    payload = archive.read(entry)
                    with kg_zip.ZipFile(kg_io.BytesIO(payload)) as save:
                        if save.getinfo("json").file_size > 65536:
                            raise ValueError("Oversized metadata")
                        meta = kg_json.loads(save.read("json"))
                        if "log" not in save.namelist():
                            raise ValueError("Missing save state")
                    staged[name] = payload
            if not staged:
                raise ValueError("No supported slots")
            renpy.kg_io.staged = staged
            overlaps = sum(kg_os.path.exists(kg_os.path.join(config.savedir, n)) for n in staged)
            renpy.show_screen("kg_confirm", title="Загрузить сохранения из файла?", message="Найдено записей: %d. Совпадающих мест: %d.\nЗаписи в совпадающих местах будут заменены. Загружай только собственные сохранения. Настройки игры не изменятся." % (len(staged), overlaps), yes=Function(kg_apply_import))
            renpy.restart_interaction()
        except Exception as e:
            renpy.log("KG import rejected: " + repr(e))
            kg_error("В файле нет подходящих сохранений или архив повреждён. Ничего не изменено.")

    def kg_apply_import():
        staged = renpy.kg_io.staged
        if not staged:
            return
        backups = {}
        try:
            for name, payload in staged.items():
                path = kg_os.path.join(config.savedir, name)
                backups[path] = open(path, "rb").read() if kg_os.path.exists(path) else None
                with open(path + ".importing", "wb") as stream:
                    stream.write(payload)
                kg_os.replace(path + ".importing", path)
            renpy.loadsave.location.scan()
            for slot in KG_SLOTS:
                renpy.loadsave.clear_slot(slot)
            renpy.kg_io.staged = None
            kg_sync(lambda: renpy.notify("Сохранения загружены"))
        except Exception as e:
            for path, data in backups.items():
                if data is not None:
                    with open(path, "wb") as stream:
                        stream.write(data)
                elif kg_os.path.exists(path):
                    kg_os.remove(path)
            renpy.log("KG import failed: " + repr(e))
            kg_error("Не удалось восстановить сохранения. Предыдущие записи восстановлены.")

    config.quit_action = Function(kg_quit)
    config.has_autosave = False
    config.autosave_frequency = 0
    config.autosave_on_choice = False
    config.autosave_on_quit = False
    config.save_json_callbacks.append(kg_metadata)
    config.label_callbacks.append(kg_label)
    config.all_character_callbacks.append(kg_character)


screen kg_sync_wait():
    zorder 700
    modal True
    timer 0.1 repeat True action Function(kg_poll_sync)

screen kg_save_error(message):
    default glass_source = kg_menu_blurred
    on "show" action Function(kg_capture_modal_glass)
    zorder 800
    modal True
    add Solid("#00000055")
    frame:
        background KGMenuGlass(source=glass_source)
        xalign 0.5 yalign 0.5
        xsize 630 padding (30, 30)
        vbox:
            spacing 24
            text message size 28 outlines [(1, "#0009", 0, 1)]
            kg_glass_button "Понятно" style "kg_action" action Hide("kg_save_error")

screen kg_confirm(title, message, yes, yes_text="Подтвердить"):
    default glass_source = kg_menu_blurred
    on "show" action Function(kg_capture_modal_glass)
    zorder 650
    modal True
    add Solid("#00000055")
    frame:
        background KGMenuGlass(source=glass_source)
        xalign 0.5 yalign 0.5
        xsize 630 padding (30, 30)
        vbox:
            spacing 24
            text title style "menu_title" textalign 0.5
            text message size 26 outlines [(1, "#0009", 0, 1)]
            kg_glass_button yes_text style "kg_action" action [Hide("kg_confirm"), yes]
            kg_glass_button "Отмена" style "kg_action" action Hide("kg_confirm")

style kg_action is overlay_button:
    xsize 560
    ysize 76
style kg_action_text is default:
    font "gui/fonts/Montserrat-SemiBold.ttf"
    size 30
    yalign 0.5
    color "#ffffff"
    hover_color "#f3f2ed"
    activate_color "#f4d7a8"
    insensitive_color "#899397"
    xalign 0.5
    textalign 0.5
style kg_card is button:
    xsize 640
    padding (2, 2)
    background Frame("gui/kg_saves/card.png", 24, 24)
    hover_background Frame("gui/kg_saves/card_hover.png", 24, 24)
style kg_card_text is default:
    color "#ffffff"

screen kg_files(title, mode, from_main_menu=False):
    default glass_scroll = ui.adjustment()
    add "gui/menu_bg.png"
    text title style "menu_title" xalign 0.5 ypos 60
    $ entries = KG_MANUAL if mode == "save" else kg_entries()
    $ newest = kg_entries()[0] if kg_entries() else None
    viewport:
        yadjustment glass_scroll
        xpos 40 ypos 145 xsize 650
        ysize (815 if mode == "load" and renpy.emscripten else 1000)
        mousewheel True draggable True
        vbox:
            spacing 16
            for index, slot in enumerate(entries):
                $ exists = renpy.can_load(slot)
                fixed:
                    xysize (640, 246)
                    button:
                        style "kg_card"
                        background Frame("gui/kg_glass/card_static_idle.png", 32, 32)
                        hover_background Frame("gui/kg_glass/card_static_hover.png", 32, 32)
                        action (Function(kg_manual, slot) if mode == "save" else Function(kg_load, slot))
                        frame:
                            background None
                            padding (14, 14)
                            xfill True
                            hbox:
                                spacing 24
                                if exists:
                                    add FileScreenshot(slot, slot=True) xysize (120, 214)
                                else:
                                    frame:
                                        xysize (120, 214)
                                        background "gui/kg_saves/empty_preview.png"
                                        text "+" size 48 color "#d5ac73" align (0.5, 0.5)
                                vbox:
                                    yalign 0.5
                                    xsize 420 spacing 14
                                    if exists:
                                        text (("РУЧНОЕ" if slot in KG_MANUAL else "АВТО") + (" · ПОСЛЕДНЕЕ" if slot == newest else "")) size 20 color "#d5ac73"
                                        text kg_slot_title(slot) size 28
                                        text kg_date(slot) size 23
                                    else:
                                        text "Пустое сохранение" size 28
                    if exists:
                        imagebutton:
                            idle "gui/kg_saves/delete.png"
                            hover "gui/kg_saves/delete_hover.png"
                            xpos 568 ypos 6
                            xysize (64, 64)
                            focus_mask None
                            alt "Удалить сохранение"
                            action Function(kg_delete_prompt, slot)
            if not entries:
                text "Пока нет сохранений" size 28 xalign 0.5
    vbox:
        xalign 0.5 ypos 1240 yanchor 1.0 spacing 16
        if mode == "load" and renpy.emscripten:
            kg_glass_button "Скачать сохранения" frosted_y 980 style "kg_action" action Function(kg_export)
            kg_glass_button "Загрузить сохранения" frosted_y 1072 style "kg_action" action Function(kg_import_pick)
        kg_glass_button "Назад" frosted_y 1164 style "kg_action" action (ShowMenu("main_menu") if from_main_menu else ShowMenu("main_overlay_menu"))

label after_load:
    $ kg_after_load()
    $ kg_prepare_scene(getattr(store, "current_scene", kg_save_scene))
    return
