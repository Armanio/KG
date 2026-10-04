# Touch debounce only. No event recording or log export.
init 30 python:
    import time as kg_touch_time
    import types as kg_touch_types

    renpy.kg_touch_guard = kg_touch_types.SimpleNamespace(
        last_accept=-100.0, touch=renpy.variant("touch"), browser_ready=False)
    kg_previous_allow_dismiss = config.say_allow_dismiss

    def kg_touch_detect_browser():
        state = renpy.kg_touch_guard
        if not renpy.emscripten or state.browser_ready:
            return
        try:
            state.touch = renpy.emscripten.run_script_string("String(navigator.maxTouchPoints > 0 || 'ontouchstart' in window)") == "true"
            state.browser_ready = True
        except Exception:
            pass

    def kg_touch_allow_dismiss():
        state = renpy.kg_touch_guard
        now = kg_touch_time.monotonic()
        elapsed = now - state.last_accept
        if kg_previous_allow_dismiss is not None and not kg_previous_allow_dismiss():
            return False
        if state.touch and elapsed < 0.250:
            return False
        state.last_accept = now
        return True

    config.interact_callbacks.append(kg_touch_detect_browser)
    config.say_allow_dismiss = kg_touch_allow_dismiss
