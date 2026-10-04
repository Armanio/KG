# Shared glass navigation. Does not change actions, story choices or save cards.
python early:
    import pygame_sdl2 as kg_glass_pygame
    import time as kg_glass_time

    class KGGlassButton(renpy.display.behavior.Button):
        def event(self, ev, x, y, st):
            pending = getattr(self, "kg_pending_until", None)
            if pending is not None:
                remaining = pending - kg_glass_time.monotonic()
                if remaining <= 0:
                    self.kg_pending_until = None
                    result = renpy.display.behavior.run(self.clicked)
                    if result is not None:
                        return result
                    raise renpy.display.core.IgnoreEvent()
                renpy.game.interface.timeout(remaining)
                if renpy.display.behavior.map_event(ev, "button_select"):
                    raise renpy.display.core.IgnoreEvent()
                return None
            if hasattr(self, "kg_projection") and not self.locked and self.is_sensitive() and self.is_focused() and self.clicked is not None and renpy.display.behavior.map_event(ev, "button_select"):
                self.kg_projection.flash()
                self.kg_pending_until = kg_glass_time.monotonic() + 0.18
                self.set_style_prefix(self.role + "activate_", True)
                renpy.redraw(self, 0)
                renpy.game.interface.timeout(0.18)
                raise renpy.display.core.IgnoreEvent()
            if self.is_sensitive() and self.is_focused():
                if (ev.type == kg_glass_pygame.MOUSEBUTTONDOWN and ev.button == 1) or (ev.type == kg_glass_pygame.KEYDOWN and ev.key in (kg_glass_pygame.K_RETURN, kg_glass_pygame.K_SPACE)):
                    if hasattr(self, "kg_projection"):
                        self.kg_projection.flash()
                    self.set_style_prefix(self.role + "activate_", True)
                    renpy.redraw(self, 0)
                elif ev.type in (kg_glass_pygame.MOUSEBUTTONUP, kg_glass_pygame.KEYUP):
                    self.set_style_prefix(self.role + "hover_", True)
                    renpy.redraw(self, 0)
            return super(KGGlassButton, self).event(ev, x, y, st)

    def kg_glass_button(label, clicked=None, style="kg_action", text_style=None, substitute=True, scope=None, frosted_y=None, frosted_dim=False, **kwargs):
        text_kwargs, button_kwargs = renpy.easy.split_properties(kwargs, "text_", "")
        if frosted_y is not None:
            for prefix, state in (("", "idle"), ("hover_", "hover"), ("activate_", "pressed"), ("insensitive_", "disabled"), ("selected_idle_", "idle"), ("selected_hover_", "hover")):
                button_kwargs[prefix + "background"] = KGButtonGlass(frosted_y, state, frosted_dim)
        rv = KGGlassButton(style=style, clicked=clicked, **button_kwargs)
        text = renpy.text.text.Text(label, style=text_style or "kg_action_text", substitute=substitute, scope=scope, **text_kwargs)
        rv.add(text)
        rv._main = text
        rv._composite_parts = [text]
        return rv

    reg = renpy.register_sl_displayable("kg_glass_button", kg_glass_button, "kg_action", 0, scope=True)
    reg.add_positional("label")
    for keyword in ("action", "clicked", "hovered", "unhovered", "alternate", "text_style", "substitute", "scope", "frosted_y", "frosted_dim"):
        reg.add_property(keyword)
    for group in ("window", "button"):
        reg.add_property_group(group)
    for group in ("position", "text"):
        reg.add_property_group(group, "text_")

init 20:
    style kg_action:
        background Frame("gui/kg_glass/idle.png", 18, 18)
        hover_background Frame("gui/kg_glass/hover.png", 18, 18)
        activate_background Frame("gui/kg_glass/pressed.png", 18, 18)
        insensitive_background Frame("gui/kg_glass/disabled.png", 18, 18)
        selected_idle_background Frame("gui/kg_glass/idle.png", 18, 18)
        selected_hover_background Frame("gui/kg_glass/hover.png", 18, 18)
        padding (16, 8)

python early:
    class KGProjectionIcon(renpy.Displayable):
        def __init__(self, icon):
            super(KGProjectionIcon, self).__init__()
            self.frames = [renpy.display.im.Image("gui/kg_glass/icon_" + icon + suffix + ".png") for suffix in ("", "_pulse_a", "_pulse_b")]
            self.started = None

        def flash(self):
            self.started = kg_glass_time.monotonic()
            renpy.redraw(self, 0)

        def render(self, width, height, st, at):
            elapsed = kg_glass_time.monotonic() - self.started if self.started is not None else 1.0
            index = (1 if elapsed < 0.06 else (0 if elapsed < 0.085 else 2)) if elapsed < 0.16 else 0
            if elapsed < 0.18:
                renpy.redraw(self, 0.02)
            return renpy.render(self.frames[index], width, height, st, at)

        def visit(self):
            return self.frames

    def kg_glass_icon(icon, style="kg_nav_icon", **kwargs):
        rv = KGGlassButton(style=style, **kwargs)
        rv.kg_projection = KGProjectionIcon(icon)
        rv.add(rv.kg_projection)
        return rv

    icon_reg = renpy.register_sl_displayable("kg_glass_icon", kg_glass_icon, "kg_nav_icon", 0)
    icon_reg.add_positional("icon")
    for keyword in ("action", "clicked", "hovered", "unhovered", "alternate"):
        icon_reg.add_property(keyword)
    for group in ("window", "button"):
        icon_reg.add_property_group(group)

init 21:
    style kg_nav_icon is kg_action:
        background "gui/kg_glass/nav_idle.png"
        hover_background "gui/kg_glass/nav_hover.png"
        activate_background "gui/kg_glass/nav_pressed.png"
        insensitive_background "gui/kg_glass/nav_disabled.png"
        selected_idle_background "gui/kg_glass/nav_idle.png"
        selected_hover_background "gui/kg_glass/nav_hover.png"
        xysize (80, 80)
        padding (0, 0)

init 22 python:
    import weakref as kg_glass_weakref
    renpy.kg_scroll_surfaces = kg_glass_weakref.WeakSet()

    def kg_glass_scroll_changed(value):
        # Invalidate only the small sampled surfaces. Do not rebuild screens,
        # query save metadata, or recreate the shared blurred source on scroll.
        for surface in list(renpy.kg_scroll_surfaces):
            renpy.redraw(surface, 0)

    class KGGlassRegion(renpy.Displayable):
        def __init__(self, scene, rect):
            super(KGGlassRegion, self).__init__()
            self.scene, self.rect = scene, rect
        def render(self, width, height, st, at):
            full = renpy.render(self.scene, config.screen_width, config.screen_height, st, at)
            x, y, w, h = self.rect
            region = renpy.Render(w, h)
            region.blit(full, (-x, -y))
            return region.subsurface((0, 0, w, h))
        def visit(self):
            return [self.scene]

    class KGMenuGlass(renpy.Displayable):
        def __init__(self, source=None, origin=None, shadow=True, highlight=False, **kwargs):
            super(KGMenuGlass, self).__init__(**kwargs)
            self.scene = source if source is not None else Transform(Layer("master"), blur=8.0)
            self.origin = origin
            self.use_shadow = shadow
            self.mask = Frame("gui/kg_glass/panel_mask.png", 32, 32)
            self.rim = Frame("gui/kg_glass/panel_frost_hover.png" if highlight else "gui/kg_glass/panel_frost.png", 32, 32)
            self.shadow = Frame("gui/kg_glass/panel_shadow.png", 64, 64)
            self.cached_size = None

        def per_interact(self):
            if callable(self.origin):
                renpy.kg_scroll_surfaces.add(self)
                renpy.redraw(self, 0)

        def render(self, width, height, st, at):
            w, h = int(width), int(height)
            origin = self.origin() if callable(self.origin) else self.origin
            key = (w, h, origin)
            if self.cached_size != key:
                # This menu is centered; sample the same coordinates on the scene layer.
                x = int((config.screen_width - w) / 2)
                y = int((config.screen_height - h) / 2)
                if origin is not None:
                    x, y = map(int, origin)
                self.region = AlphaMask(KGGlassRegion(self.scene, (x, y, w, h)), self.mask)
                self.cached_size = key
            rv = renpy.Render(w, h)
            if self.use_shadow:
                rv.blit(renpy.render(self.shadow, w+64, h+64, st, at), (-32, -32))
            rv.blit(renpy.render(self.region, w, h, st, at), (0, 0))
            rv.blit(renpy.render(self.rim, w, h, st, at), (0, 0))
            return rv

        def visit(self):
            return [self.scene, self.mask, self.rim, self.shadow]

init 23 python:
    kg_menu_blurred = Transform("gui/menu_bg.png", xysize=(config.screen_width, config.screen_height), blur=8.0)

    def kg_capture_modal_glass():
        data = renpy.screenshot_to_bytes((config.screen_width, config.screen_height))
        source = Transform(im.Data(data, "kg-modal.png"), blur=14.0)
        renpy.set_screen_variable("glass_source", source)
        renpy.restart_interaction()


init 24 python:
    # One cached blurred menu source, sampled only by stationary buttons.
    kg_menu_blurred_dim = Composite((config.screen_width, config.screen_height),
        (0, 0), kg_menu_blurred, (0, 0), Solid("#0006"))

    class KGButtonGlass(KGMenuGlass):
        def __init__(self, y, state="idle", dim=False):
            super(KGButtonGlass, self).__init__(
                source=kg_menu_blurred_dim if dim else kg_menu_blurred,
                origin=(int((config.screen_width - 560) / 2), int(y)), shadow=False)
            self.mask = Frame("gui/kg_glass/panel_mask.png", 18, 18)
            self.rim = Frame("gui/kg_glass/" + state + ".png", 18, 18)
