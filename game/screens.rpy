init python:
    # style.say_window.background = "#836303"  # тёмный фон
    style.menu_window.background = "gui/menu_bg.png"  # тёмный фон
    # style.say_window.xalign = 0.5
    # style.say_window.ypos = 0.9
    # style.say_window.xpadding = 40
    # style.say_window.ypadding = 40
    # style.say_window.size = 400
    # style.say_window.xsize = 720
    # style.say_window.ysize = None
    # style.say_window.ymargin = 10
    # style.say_window.left_margin = 20
    # style.say_window.right_margin = 20
    # style.say_window.top_margin = 10
    # style.say_window.bottom_margin = 20
    # style.say_window.outlines = [(2, "#d1a03d", 0, 0)]  # золотая рамка

    # style.say_label.color = "#FFD700"
    # style.say_label.size = 60
    # style.say_label.bold = True
    # style.say_label.outlines = [(1, "#000000")]

    # style.say_dialogue.color = "#FFFFFF"
    # style.say_dialogue.size = 44

screen navigation_buttons():
    zorder 200   # поверх спрайтов
    frame:
        style "default"
        xalign 0.5
        yalign 0.98  # почти у самого низа
        padding (20, 20)
        background "gui/overlay.png"
        xsize 1.0
        hbox:
            spacing 40
            xalign 0.5

            if current_scene != "prolog":
                kg_glass_icon "prev":
                    action Jump(previous_scene)
                    xysize (80, 80)
                

            # imagebutton:
            #     idle "gui/button/prev.png"
            #     hover "gui/button/prev_hover.png"
            #     action Rollback()
            #     xysize (80, 80)


            kg_glass_icon "menu":
                action ShowMenu("main_overlay_menu")
                xysize (80, 80)


            # imagebutton:
            #     idle "gui/button/next.png"
            #     hover "gui/button/next_hover.png"
            #     action Return()
            #     xysize (80, 80)

            if current_scene not in ("scene_2_9", "scene_8_9") and next_scene in tuple(KG_SCENES) + ("start_chapter_1", "start_chapter_2", "kg_end_chapter_1"):
                kg_glass_icon "next":
                    action Jump("kg_end_chapter_1" if current_scene == "scene_1_6" else next_scene)
                    xysize (80, 80)




# --- glass dialogue UI: additive version, old screen say is untouched ---

transform glass_tail_left_pos:
    xpos 30
    ypos -72
    xysize (180, 110)

transform glass_tail_right_pos:
    xpos 140
    ypos -72
    xysize (180, 110)
    xzoom -1.0


screen say(who, what, side=None, kind=None):
    timer 0.15 repeat True action Function(kg_safe_tick)
    zorder 100
    $ bubble_side, bubble_kind = kg_dialogue_mode(who, side, kind)
    if what:
        vbox:
            xalign 0.5
            ypos (940 if not who else 1100)
            yanchor 1.0
            use kg_dialogue_content(who, what, bubble_side, bubble_kind)
        use navigation_buttons

screen say_offscreen(who, what, side="none", kind="speech"):
    timer 0.15 repeat True action Function(kg_safe_tick)
    zorder 100
    if what:
        vbox:
            xalign 0.5
            ypos 1100
            yanchor 1.0
            use kg_dialogue_content(who, what, side, kind)
        use navigation_buttons

# --- glass dialogue UI: additive version, old screen say is untouched ---


transform scene_note_transition:
    on show:
        alpha 0.0
        yoffset -25
        easeout 0.35 alpha 1.0 yoffset 0

    on hide:
        easein 0.6 alpha 0.0 yoffset -20


screen scene_note(title, details=None, duration=4.0):
    tag scene_note
    zorder 110

    frame:
        at scene_note_transition

        xalign 0.5
        ypos 60
        xsize 0.6
        yminimum 140

        background "#876500b3"
        xpadding 30
        ypadding 18

        vbox:
            spacing 6
            xalign 0.5
            yalign 0.5

            text title:
                xalign 0.5
                textalign 0.5
                color "#ffffff"
                size 28
                font "gui/fonts/Montserrat-Bold.ttf"

            if details:
                text details:
                    xalign 0.5
                    textalign 0.5
                    color "#e8ba31"
                    size 24
                    font "gui/fonts/Montserrat-Regular.ttf"

    timer duration action Hide("scene_note")


layeredimage flashback_overlay_layer:
    always "bg/clouds_2.jpeg":
        alpha 0.5

style say_dialogue:
    size 35
    font "gui/fonts/Montserrat-SemiBold.ttf"

style default:
    size 35
    font "gui/fonts/Montserrat-SemiBold.ttf"

style narrator is default:
    size 35
    font "gui/fonts/Montserrat-SemiBold.ttf"

style window_thought:
    size 35
    font "gui/fonts/Montserrat-SemiBold.ttf"

style who_name_text:
    color "#24200d"
    size 35
    font "gui/fonts/Montserrat-Bold.ttf"

screen chapters_screen(from_main_menu=False):
    tag menu
    zorder 300
    modal True
    default glass_scroll = ui.adjustment()
    add "gui/menu_bg.png"
    viewport:
        xalign 0.5 ypos 40 xsize 600 ysize 1090
        yadjustment glass_scroll
        draggable True mousewheel True
        vbox:
            spacing 20
            fixed:
                ysize 80
                text "Оглавление" style "menu_title" xalign 0.5
            for chapter_index, chapter_name in enumerate(KG_CHAPTER_NAMES):
                button:
                    xysize (600, 240)
                    padding (26, 20)
                    background KG_CHAPTER_CARDS[chapter_index]
                    hover_background KG_CHAPTER_HOVER[chapter_index]
                    insensitive_background KG_CHAPTER_CARDS[chapter_index]
                    action (Start("start_chapter_%d" % (chapter_index + 1)) if chapter_index < 2 else NullAction())
                    sensitive (chapter_index < 2)
                    vbox:
                        yalign 0.5
                        xsize 315
                        spacing 14
                        text (("ГЛАВА %d" % (chapter_index + 1)) + (" · В РАЗРАБОТКЕ" if chapter_index >= 2 else "")) size 20 font "gui/fonts/Montserrat-SemiBold.ttf" color "#d5ac73" xsize 548
                        text chapter_name size 28 font "gui/fonts/Montserrat-SemiBold.ttf" color ("#ffffff" if chapter_index < 2 else "#b9bcb8")
    kg_glass_button "Назад":
        frosted_y 1164
        style "kg_action"
        xalign 0.5 ypos 1164
        action (ShowMenu("main_menu") if from_main_menu else ShowMenu("main_overlay_menu"))

screen chapter_title(chapter_number, chapter_name, loading=False):
    tag chapter_title
    zorder 100
    modal True
    default load_started = kg_pre_time.monotonic()
    if loading:
        timer 0.15 repeat True action Function(kg_chapter_wait_tick, load_started)
        key "dismiss" action NullAction()
        key "game_menu" action NullAction()

    add "gui/menu_bg.png"

    add Solid("#0006")

    vbox:
        at kg_chapter_enter
        spacing 50
        xalign 0.5
        yalign 0.45

        use kg_chapter_logo

        text "–":
            size 55
            color "#FFFFFF"
            font "gui/fonts/Montserrat-Regular.ttf"
            xalign 0.5
            textalign 0.5


        text chapter_number:
            size 80
            color "#FFFFFF"
            font "gui/fonts/Montserrat-Bold.ttf"
            xalign 0.5
            textalign 0.5

        text chapter_name:
            size 40
            color "#FFFFFF"
            font "gui/fonts/Montserrat-Bold.ttf"
            xalign 0.5
            textalign 0.5

    if loading and renpy.emscripten and not kg_pre_ready():
        vbox:
            xalign 0.5 ypos 980 spacing 20
            if kg_pre_failed():
                text "Не удалось загрузить главу" size 26 xalign 0.5 ysize 34
                kg_glass_button "Повторить" frosted_y 1034 frosted_dim True action Function(kg_pre_retry)
            else:
                text "Загрузка…" size 26 xalign 0.5 ysize 34 at kg_chapter_loading_pulse
            kg_glass_button "В меню" frosted_y (1130 if kg_pre_failed() else 1034) frosted_dim True action Return(False)

transform kg_chapter_enter:
    alpha 0.0
    linear 0.4 alpha 1.0

transform kg_chapter_loading_pulse:
    alpha 0.5
    linear 0.8 alpha 1.0
    linear 0.8 alpha 0.5
    repeat

transform kg_chapter_word_glitch:
    # Same reveal and jitter as kg_cover_second; first pulse fits the 3s title.
    alpha 0.0
    pause 0.8
    block:
        linear 0.12 alpha 1.0
        xoffset 0
        pause 0.08
        xoffset -2
        pause 0.06
        xoffset 2
        pause 0.06
        xoffset 0
        pause 4.68
        alpha 0.0
        repeat

transform kg_chapter_slice_glitch(displacement, delay):
    alpha 0.0
    pause delay
    block:
        alpha 0.8
        xoffset displacement
        pause 0.07
        xoffset -displacement
        pause 0.06
        alpha 0.0
        xoffset 0
        pause 4.87
        repeat

screen kg_chapter_logo():
    # Shared cover layers retain the exact lettering and relative proportions.
    fixed:
        xysize (476, 145)
        xalign 0.5
        add Transform(Crop((162, 982, 610, 71), "images/cover_intro/title-first.png"), zoom=0.78)
        fixed:
            ypos 64
            xysize (476, 81)
            add Transform(Crop((162, 1064, 610, 104), "images/cover_intro/title-second.png"), zoom=0.78) at kg_chapter_word_glitch
            add Transform(Crop((162, 1064, 610, 104), "images/cover_intro/glitch-a.png"), zoom=0.78) at kg_chapter_slice_glitch(7, 0.95)
            add Transform(Crop((162, 1064, 610, 104), "images/cover_intro/glitch-b.png"), zoom=0.78) at kg_chapter_slice_glitch(-5, 1.03)

screen chapter_ends(chapter_number, next_label=None):
    modal True
    zorder 200
    default attempted = False
    add "gui/menu_bg.png"
    add Solid("#0006")
    key "game_menu" action NullAction()
    key "dismiss" action NullAction()
    if not attempted and not kg_chapter_end_saved:
        timer 0.2 action [SetScreenVariable("attempted", True), Function(kg_begin_chapter_save_notice)]
    vbox:
        xalign 0.5 yalign 0.38 spacing 48
        use kg_chapter_logo
        text "–" size 55 color "#FFFFFF" xalign 0.5
        text ("Конец %d главы" % chapter_number):
            font "gui/fonts/Montserrat-Bold.ttf"
            size 52 color "#FFFFFF" xalign 0.5 textalign 0.5
    default save_notice_until = kg_pre_time.monotonic() + (0.7 if not kg_chapter_end_saved else 0.0)
    $ save_notice_active = kg_pre_time.monotonic() < save_notice_until
    if save_notice_active:
        timer 0.1 action Function(renpy.restart_interaction) repeat True
    vbox:
        xalign 0.5 ypos 1000 spacing 20
        kg_glass_button "Продолжить":
            frosted_y 1000
            frosted_dim True
            style "kg_action"
            text_insensitive_color "#8a9398"
            sensitive kg_chapter_end_saved and not renpy.kg_io.busy and not save_notice_active and next_label is not None
            action Return(True)
        kg_glass_button "Сохранить и выйти":
            frosted_y 1096
            frosted_dim True
            style "kg_action"
            sensitive kg_chapter_end_saved and not renpy.kg_io.busy and not save_notice_active
            action MainMenu(confirm=False, save=False)
    if save_notice_active or renpy.kg_io.busy or not attempted and not kg_chapter_end_saved:
        text "Сохранение…" size 26 xalign 0.5 ypos 1190
    elif not kg_chapter_end_saved:
        text "Не удалось сохранить" size 24 xalign 0.5 ypos 1182
        kg_glass_button "Повторить сохранение":
            ypos 1220 xalign 0.5 ysize 50
            frosted_y 1220 frosted_dim True
            action [SetScreenVariable("save_notice_until", kg_pre_time.monotonic() + 0.5), Function(kg_begin_chapter_save_notice)]
    elif next_label is None:
        text "Продолжение пока недоступно" size 24 xalign 0.5 ypos 1190

transform fade_in_out:
    alpha 0.0
    linear 1.5 alpha 1.0  # плавное появление
    pause 2.5
    linear 1.0 alpha 0.0  # плавное исчезновение

screen main_overlay_menu():
    zorder 300
    tag menu
    modal True

    frame:
        background KGMenuGlass()
        xalign 0.5
        yalign 0.5
        xsize 600
        ypadding 40

        vbox:
            spacing 30
            xalign 0.5

            kg_glass_button "Сохранить":
                action ShowMenu("save")
                style "kg_action"

            kg_glass_button "Загрузить":
                action ShowMenu("load")
                style "kg_action"
            
            kg_glass_button "Оглавление":
                action ShowMenu("chapters_screen")
                style "kg_action"

            kg_glass_button "Сохранить и выйти в меню":
                action Function(kg_exit_menu)
                style "kg_action"

            kg_glass_button "Закрыть":
                action Return()
                style "kg_action"

            # textbutton "💾 Сохранить":
            #     action ShowMenu("save")
            #     style "overlay_button"

            # textbutton "📂 Загрузить":
            #     action ShowMenu("load")
            #     style "overlay_button"

            # textbutton "📖 Оглавление":
            #     action Call("chapters_screen")
            #     style "overlay_button"

            # textbutton "✖ Закрыть":
            #     action Return()
            #     style "overlay_button"

screen save():
    zorder 400
    tag menu
    modal True
    use kg_files("Сохранить игру", "save")

screen load(from_main_menu=False):
    zorder 400
    tag menu
    modal True
    use kg_files("Загрузить игру", "load", from_main_menu)

style menu_title:
    size 42
    color "#ffffff"
    font "gui/fonts/Montserrat-SemiBold.ttf"
    xalign 0.5

style overlay_button is default:
    size 30
    xsize 500
    xalign 0.5
    background Frame("gui/button/btn_idle.png", 40, 16, 40, 16)
    hover_background Frame("gui/button/btn_hover.png", 40, 16, 40, 16)
    padding (35, 20) 
    color "#ffffff"
    hover_color "#BC9112"

init python:
    def kg_is_pwa_standalone():
        if not renpy.emscripten:
            return False

        return renpy.emscripten.run_script_string(
            "((window.matchMedia && ['standalone','minimal-ui','fullscreen','window-controls-overlay'].some(function(mode){return window.matchMedia('(display-mode: '+mode+')').matches && (mode !== 'fullscreen' || (!document.fullscreenElement && !document.webkitFullscreenElement));})) || window.navigator.standalone === true) ? 'yes' : 'no'"
        ) == "yes"


    def kg_install_pwa():
        if not renpy.emscripten:
            renpy.show_screen("pwa_install_unavailable", platform="desktop")
            return

        platform = renpy.emscripten.run_script_string(
            "window.kgPwaPlatform ? window.kgPwaPlatform() : 'other'"
        )

        if platform == "ios":
            renpy.show_screen("pwa_ios_install")
            return

        result = renpy.emscripten.run_script_string(
            "window.kgRequestPwaInstall ? window.kgRequestPwaInstall() : 'unavailable'"
        )

        if result == "installed":
            renpy.notify("Игра уже установлена на устройство.")
        elif result != "prompted":
            renpy.show_screen("pwa_install_unavailable", platform=platform)


screen pwa_ios_install():
    default glass_source = kg_menu_blurred
    on "show" action Function(kg_capture_modal_glass)
    tag pwa_install
    modal True
    zorder 500

    add Solid("#0005")

    frame:
        background KGMenuGlass(source=glass_source)
        xalign 0.5
        yalign 0.5
        xsize 660
        xpadding 25
        ypadding 25

        vbox:
            spacing 18
            xalign 0.5

            text "Установить как PWA":
                style "menu_title"

            text "В Safari нажмите: Поделиться → Показать больше → На экран «Домой»." :
                size 23
                color "#ffffff"
                xalign 0.5
                textalign 0.5

            add "gui/pwa_ios_install.png":
                xysize (600, 744)
                xalign 0.5

            kg_glass_button "Закрыть":
                action Hide("pwa_ios_install")
                style "kg_action"


screen pwa_install_unavailable(platform="other"):
    default glass_source = kg_menu_blurred
    on "show" action Function(kg_capture_modal_glass)
    tag pwa_install
    modal True
    zorder 500

    add Solid("#0005")

    frame:
        background KGMenuGlass(source=glass_source)
        xalign 0.5
        yalign 0.5
        xsize 640
        xpadding 45
        ypadding 45

        vbox:
            spacing 30
            xalign 0.5

            text "Установить как PWA":
                style "menu_title"

            if platform == "android":
                text "Автоматическая установка сейчас недоступна. Откройте меню браузера и выберите «Установить приложение» или «Добавить на главный экран»." :
                    size 26
                    color "#ffffff"
                    xalign 0.5
                    textalign 0.5
            elif platform == "desktop":
                text "Установка PWA доступна только в браузерной версии игры." :
                    size 26
                    color "#ffffff"
                    xalign 0.5
                    textalign 0.5
            else:
                text "Этот браузер не предоставил автоматическую установку. Откройте его меню и выберите добавление приложения на главный экран." :
                    size 26
                    color "#ffffff"
                    xalign 0.5
                    textalign 0.5

            kg_glass_button "Закрыть":
                action Hide("pwa_install_unavailable")
                style "kg_action"

screen main_menu():
    on "show" action Function(kg_pre_main_menu)

    tag menu
    zorder 300
    modal True

    add "gui/menu_bg.png"  # твой фон (замени путь при необходимости)

    $ kg_main_count = 3 + bool(kg_continue_slot()) + bool(renpy.emscripten and not kg_is_pwa_standalone()) + bool(not renpy.emscripten)
    $ kg_main_top = (config.screen_height - (kg_main_count * 76 + (kg_main_count - 1) * 30)) / 2
    frame:
        # background "#071c2690"  # полупрозрачный фон, можно заменить на PNG
        xalign 0.5
        yalign 0.5
        xsize 600
        ypadding 40

        vbox:
            spacing 30
            xalign 0.5

            if kg_continue_slot():
                kg_glass_button "Продолжить":
                    frosted_y (kg_main_top + (0) * 106)
                    xsize 560
                    action Function(kg_load, kg_continue_slot())
                    style "kg_action"

            kg_glass_button "Новая игра":
                frosted_y (kg_main_top + (int(bool(kg_continue_slot()))) * 106)
                xsize 560
                action Function(kg_new_game)
                style "kg_action"

            kg_glass_button "Загрузить":
                frosted_y (kg_main_top + (int(bool(kg_continue_slot())) + 1) * 106)
                xsize 560
                action ShowMenu("load", from_main_menu=True)
                style "kg_action"

            kg_glass_button "Оглавление":
                frosted_y (kg_main_top + (int(bool(kg_continue_slot())) + 2) * 106)
                xsize 560
                action ShowMenu("chapters_screen", from_main_menu=True)
                style "kg_action"

            if renpy.emscripten and not kg_is_pwa_standalone():
                kg_glass_button "Установить как PWA":
                    frosted_y (kg_main_top + (int(bool(kg_continue_slot())) + 3) * 106)
                    xsize 560
                    action Function(kg_install_pwa)
                    style "kg_action"

            if not renpy.emscripten:
                kg_glass_button "Выйти из игры":
                    frosted_y (kg_main_top + (int(bool(kg_continue_slot())) + 3) * 106)
                    xsize 560
                    style "kg_action"
                    action Quit(confirm=False)

screen choice(items, who=None, what=None, _last_say_who=None, side=None, kind=None):
    timer 0.1 action Function(kg_choice_checkpoint)
    zorder 100
    $ bubble_side, bubble_kind = kg_dialogue_mode(who, side, kind)
    vbox:
        xalign 0.5
        ypos 1100
        yanchor 1.0
        spacing 20
        if what and what != "...":
            use kg_dialogue_content(who, what, bubble_side, bubble_kind)
        for i in items:
            textbutton i[0] action [Function(kg_choice_done), Return(i[1])]:
                background KGDialoguePanel("none", "speech")
                hover_background "#453a26ed"
                padding (28, 24)
                xsize 664
                text_font "gui/fonts/Montserrat-Regular.ttf"
                text_size 32
                text_color "#faf5e9"
                xalign 0.5
