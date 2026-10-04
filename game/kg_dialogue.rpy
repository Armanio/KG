# Per-line API: ev "Text" (show_side="left", show_kind="speech")
# side: left/right/none; kind: speech/thought. Old saves retain a fallback.
init -2 python:
    class KGDialoguePanel(renpy.Displayable):
        def __init__(self, side="none", kind="speech", **kwargs):
            super(KGDialoguePanel, self).__init__(**kwargs)
            self.side, self.kind = side, kind
            self.panel = Frame("gui/kg_dialogue/panel.png", 12, 12)
            self.pointer = renpy.displayable("gui/kg_dialogue/%s_%s.png" % (kind, side)) if side != "none" else None

        def visit(self):
            return [self.panel] + ([self.pointer] if self.pointer else [])

        def render(self, width, height, st, at):
            width, height = int(width), int(height)
            rv = renpy.Render(width, height)
            rv.blit(renpy.render(self.panel, width, height, st, at), (0, 0))
            # Top/left: 2px. Bottom/right: 1px. Gaps stay fixed at 14px.
            left, right = int(width * .23), int(width * .09)
            if self.side == "right":
                left, right = int(width * .09), int(width * .23)
            pw, ph = (54, 44) if self.kind == "speech" else (74, 80)
            offset = int(width * (.22 if self.kind == "speech" else .23))
            px = offset if self.side == "left" else width-offset-pw
            if self.pointer and self.kind == "speech":
                # End at the outer foot, never draw beneath the open triangle.
                if self.side == "left":
                    left = px + 12
                else:
                    right = width - (px + 41)
            strokes = ((0, 0, left, 2), (width-right, 0, right, 2),
                       (0, 0, 2, height-14),
                       (0, height-1, int(width*.08), 1),
                       (int(width*.53), height-1, width-int(width*.53), 1),
                       (width-1, 14, 1, height-14))
            for x, y, w, h in strokes:
                rv.blit(renpy.render(Solid("#e6bb65", xsize=w, ysize=h), w, h, st, at), (x, y))
            if self.pointer:
                py = -40 if self.kind == "speech" else -ph+3
                rv.blit(renpy.render(self.pointer, pw, ph, st, at), (px, py))
            return rv

    def kg_dialogue_mode(who, side, kind):
        speaker = getattr(store, "_last_say_who", None)
        if side is None:
            side = "none" if not who else ("left" if speaker in ("ev", "ev_thought", "ev_prolog") or who == "Эвейна" else "right")
        if kind is None:
            kind = "thought" if speaker in ("ev_thought", "er_thought") else "speech"
        return (side if side in ("left", "right", "none") else "none", kind if kind in ("speech", "thought") else "speech")

style kg_dialogue_window is default:
    xsize 664
    xpadding 36
    ypadding 36
    background None

style kg_dialogue_text is default:
    font "gui/fonts/Montserrat-SemiBold.ttf"
    size 34
    color "#faf5e9"
    line_spacing 9
    outlines []

style kg_dialogue_name is default:
    font "gui/fonts/Montserrat-Bold.ttf"
    size 29
    color "#eac06f"
    outlines []

screen kg_dialogue_content(who, what, side, kind):
    window:
        id "window"
        style "kg_dialogue_window"
        background KGDialoguePanel(side, kind)
        vbox:
            spacing 20
            if who:
                hbox:
                    spacing 22
                    text who id "who" style "kg_dialogue_name"
                    add Solid("#d4a558") xsize 37 ysize 2 yalign 0.5
            text what id "what" style "kg_dialogue_text" font ("gui/fonts/Montserrat-SemiBoldItalic.ttf" if kind == "thought" else "gui/fonts/Montserrat-SemiBold.ttf")
