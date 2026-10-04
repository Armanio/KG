# One-shot cover at startup, before the main menu. All art stays static; only overlays move.
transform kg_cover_frame:
    xysize (720, 1280)

transform kg_cover_enter:
    xysize (720, 1280)
    alpha 0.0
    linear 0.4 alpha 1.0

transform kg_cover_door:
    xysize (720, 1280)
    alpha 1.0
    pause 1.15
    ease 1.0 alpha 0.0

transform kg_cover_first:
    xysize (720, 1280)
    alpha 0.0
    pause 2.4
    ease 0.4 alpha 1.0

transform kg_cover_second:
    xysize (720, 1280)
    alpha 0.0
    pause 3.05
    linear 0.12 alpha 1.0
    xoffset 0
    pause 0.08
    xoffset -2
    pause 0.06
    xoffset 2
    pause 0.06
    xoffset 0

transform kg_cover_slice(delay, displacement):
    xysize (720, 1280)
    alpha 0.0
    pause delay
    alpha 0.8
    xoffset displacement
    pause 0.07
    xoffset -displacement
    pause 0.06
    alpha 0.0

transform kg_cover_node(delay, px, py):
    pos (px, py)
    xysize (32, 32)
    alpha 0.0
    pause delay
    ease 0.25 alpha 0.85
    ease 0.5 alpha 0.0

screen kg_cover_intro_screen():
    modal True
    zorder 200
    add Solid("#000000")
    fixed:
        at kg_cover_enter
        add "images/cover_intro/cover.png" at kg_cover_frame
        add "images/cover_intro/door-veil-v2.png" at kg_cover_door
        add "images/cover_intro/node-glow.png" at kg_cover_node(0.45, 17, 113)
        add "images/cover_intro/node-glow.png" at kg_cover_node(0.8, 62, 174)
        add "images/cover_intro/node-glow.png" at kg_cover_node(1.15, 99, 228)
        add "images/cover_intro/node-glow.png" at kg_cover_node(1.5, 63, 334)
        add "images/cover_intro/title-shade.png" at kg_cover_first
        add "images/cover_intro/title-first.png" at kg_cover_first
        add "images/cover_intro/title-second.png" at kg_cover_second
        add "images/cover_intro/glitch-a.png" at kg_cover_slice(3.2, 7)
        add "images/cover_intro/glitch-b.png" at kg_cover_slice(3.28, -5)
    timer 6.0 action Return()
    key "dismiss" action Return()
    key "game_menu" action Return()

label kg_cover_intro:
    window hide
    call screen kg_cover_intro_screen
    scene black
    with Dissolve(0.35)
    return
