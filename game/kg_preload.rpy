# Scene-aware web prefetch. Uses the downloader shipped with this Ren'Py SDK.
# Runtime requests live on renpy, never inside the saved/rollback store.
init -9 python:
    import json as kg_pre_json
    import os as kg_pre_os
    import time as kg_pre_time
    import types as kg_pre_types
    import renpy.webloader as kg_webloader

    KG_SCENE_FILES = kg_pre_json.loads(renpy.file("kg_scene_assets.json").read().decode("utf-8"))
    KG_SCENE_ORDER = tuple(KG_SCENE_FILES)
    renpy.kg_preload = kg_pre_types.SimpleNamespace(
        scene=None, required=(), targets=(), previous=(), requests={}, errors={}, owned=set(), aliases={})

    def kg_pre_present(filename):
        # Only files listed as remote need a network request. Packed assets are ready.
        return filename not in renpy.loader.remote_files or kg_pre_os.path.isfile(
            kg_pre_os.path.join(config.gamedir, filename))

    def kg_pre_pump():
        if not renpy.emscripten:
            return
        state = renpy.kg_preload
        now = kg_pre_time.monotonic()
        for filename, (request, started) in list(state.requests.items()):
            if request.readyState != 4 and now - started < 30:
                continue
            if request.readyState != 4:
                renpy.emscripten.run_script("RenPyWeb.dl_get(%d).abort()" % request.id)
            if kg_pre_os.path.isfile(kg_pre_os.path.join(config.gamedir, filename)):
                state.errors.pop(filename, None)
                state.owned.add(filename)
                for alias in state.aliases.pop(filename, ()):
                    renpy.flush_cache_file(alias)
                renpy.flush_cache_file(filename)
                if filename.startswith("images/"):
                    renpy.flush_cache_file(filename[7:])
            else:
                state.errors[filename] = True
            del state.requests[filename]
        keep = set(state.targets) | set(state.previous)
        for filename in list(state.owned):
            fullpath = kg_pre_os.path.join(config.gamedir, filename)
            if filename in keep:
                # Prevent the engine expiring current/next-scene files while reading.
                kg_webloader.to_unlink[fullpath] = kg_pre_time.time() + 120
            elif filename not in state.requests:
                # These are disposable, downloaded image files in the web filesystem.
                if kg_pre_os.path.isfile(fullpath):
                    kg_pre_os.unlink(fullpath)
                kg_webloader.to_unlink.pop(fullpath, None)
                state.owned.discard(filename)
        for filename in state.targets:
            if len(state.requests) >= 4:
                break
            if filename in state.requests or filename in state.errors or kg_pre_present(filename):
                continue
            state.requests[filename] = (kg_webloader.XMLHttpRequest(filename), now)

    def kg_pre_ready():
        return all(kg_pre_present(f) for f in renpy.kg_preload.required)

    def kg_pre_failed():
        return any(f in renpy.kg_preload.errors for f in renpy.kg_preload.required)

    def kg_pre_retry():
        renpy.kg_preload.errors.clear()
        kg_pre_pump()
        renpy.restart_interaction()

    def kg_pre_wait_tick():
        kg_pre_pump()
        if kg_pre_ready():
            renpy.end_interaction(True)
        else:
            renpy.restart_interaction()

    def kg_prepare_scene(scene, wait=True):
        # This subscene shares the lecture asset bundle, including on save restore.
        if scene == "scene_2_3_after_lecture":
            scene = "scene_2_3"
        if not renpy.emscripten or scene not in KG_SCENE_FILES:
            return
        state = renpy.kg_preload
        if state.scene != scene:
            state.previous = state.required
        state.scene = scene
        state.required = tuple(KG_SCENE_FILES[scene])
        index = KG_SCENE_ORDER.index(scene)
        upcoming = KG_SCENE_FILES[KG_SCENE_ORDER[index + 1]] if index + 1 < len(KG_SCENE_ORDER) else []
        state.targets = tuple(dict.fromkeys(list(state.required) + upcoming))
        # Keep decoding prediction small; scene downloads don't inflate the image cache.
        renpy.stop_predict(*(f for files in KG_SCENE_FILES.values() for f in files))
        kg_pre_pump()
        if wait and not kg_pre_ready():
            if not renpy.call_screen("kg_scene_loading"):
                renpy.full_restart()
        renpy.start_predict(*(list(state.required[:2]) + upcoming[:2]))

    def kg_chapter_wait_tick(started):
        kg_pre_pump()
        if kg_pre_time.monotonic() - started >= 3.0 and (not renpy.emscripten or kg_pre_ready()):
            renpy.end_interaction(True)
        else:
            renpy.restart_interaction()

    def kg_open_chapter(number, name, scene):
        kg_prepare_scene(scene, wait=False)
        if not renpy.call_screen("chapter_title", "Глава %d" % number, name, loading=True):
            renpy.full_restart()

    def kg_pre_main_menu():
        # Release runtime requests/targets on restart; never touch saves.
        if renpy.emscripten:
            state = renpy.kg_preload
            state.targets = ()
            state.previous = ()
            state.required = ()
            state.scene = None
            state.errors.clear()

    def kg_pre_enqueue(relpath, rtype, data):
        # Let managed images share one bounded downloader. Otherwise the native
        # predictor starts duplicate requests and raises before our Retry UI.
        if rtype == "image" and relpath in KG_MANAGED_IMAGES:
            renpy.kg_preload.aliases.setdefault(relpath, set()).add(data)
            return
        kg_webloader.kg_original_enqueue(relpath, rtype, data)

    KG_MANAGED_IMAGES = set(f for files in KG_SCENE_FILES.values() for f in files)
    if renpy.emscripten:
        if not hasattr(kg_webloader, "kg_original_enqueue"):
            kg_webloader.kg_original_enqueue = kg_webloader.enqueue
        kg_webloader.enqueue = kg_pre_enqueue
        config.predict_statements = 64
        config.overlay_screens.append("kg_scene_prefetch_tick")

screen kg_scene_prefetch_tick():
    if renpy.emscripten:
        timer 0.25 repeat True action Function(kg_pre_pump)

screen kg_scene_loading():
    modal True
    zorder 900
    add "gui/menu_bg.png"
    key "game_menu" action NullAction()
    key "dismiss" action NullAction()
    timer 0.15 repeat True action Function(kg_pre_wait_tick)
    $ kg_loading_failed = kg_pre_failed()
    $ kg_loading_text_h = renpy.render(Text("Не удалось загрузить сцену" if kg_loading_failed else "Загрузка сцены…", style="menu_title", textalign=0.5), config.screen_width, config.screen_height, 0, 0).height
    $ kg_loading_hint_h = renpy.render(Text("Проверь соединение и попробуй ещё раз.", size=26, textalign=0.5), config.screen_width, config.screen_height, 0, 0).height if kg_loading_failed else 0
    $ kg_loading_total = kg_loading_text_h + 104 if not kg_loading_failed else kg_loading_text_h + kg_loading_hint_h + 236
    $ kg_loading_back_y = (config.screen_height + kg_loading_total) / 2 - 76
    vbox:
        xalign 0.5 yalign 0.5 spacing 28
        if kg_pre_failed():
            text "Не удалось загрузить сцену" style "menu_title" textalign 0.5
            text "Проверь соединение и попробуй ещё раз." size 26 xalign 0.5 textalign 0.5
            kg_glass_button "Повторить" frosted_y (kg_loading_back_y - 104) style "kg_action" action Function(kg_pre_retry)
        else:
            text "Загрузка сцены…" style "menu_title" textalign 0.5
        kg_glass_button "В меню" frosted_y kg_loading_back_y style "kg_action" action Return(False)
