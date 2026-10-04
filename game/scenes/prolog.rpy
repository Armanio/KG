label prolog:

    $ previous_scene = "prolog"
    $ next_scene = "start_chapter_1"
    $ current_scene = "prolog"
    $ kg_prepare_scene("prolog")

    call fade_to_black(1.2, 0.8)
    show screen scene_note("Семнадцать лет назад")

    scene bg prolog_1 at bg_fullscreen with dissolve
    pause(0.5)

    ev_prolog "Пап..." (show_side="none", show_kind="speech")

    ri_prolog "М?" (show_side="none", show_kind="speech")

    ev_prolog "Ты знаешь, что такое меньшее зло?" (show_side="none", show_kind="speech")

    scene bg prolog_2 at bg_fullscreen with dissolve
    pause(0.5)

    ri_prolog "Ох... В школе услышала?" (show_side="none", show_kind="speech")

    ev_prolog "Да, нам сегодня мисс Поттс рассказывала." (show_side="none", show_kind="speech")
    ev_prolog "Что иногда правильных решений не бывает и приходится выбирать из двух зол." (show_side="none", show_kind="speech")
    ev_prolog "И привела пример. Как же там было…" (show_side="none", show_kind="speech")

    scene bg prolog_3 at bg_fullscreen with dissolve
    pause(0.5)

    ev_prolog "Можно спасти либо одного человека, но он тебе близкий." (show_side="none", show_kind="speech")
    ev_prolog "Либо много людей, но ты их вообще не знаешь." (show_side="none", show_kind="speech")

    ri_prolog "И не рановато вам такие темы объяснять?" (show_side="none", show_kind="speech")

    ev_prolog "Она сказала, что я умная и всё пойму!" (show_side="none", show_kind="speech")

    ri_prolog "Кто б сомневался... А обо мне она подумала?" (show_side="none", show_kind="speech")

    ev_prolog "И что бы ты выбрал? Какой правильный ответ?" (show_side="none", show_kind="speech")


    scene bg prolog_4 at bg_fullscreen with dissolve
    pause(0.5)


    ri_prolog "Это сложно объяснить. С точки зрения социума выбор одного в пользу многих был бы аморальным." (show_side="none", show_kind="speech")
    ri_prolog "А с точки зрения нравственности конкретного человека – единственным возможным." (show_side="none", show_kind="speech")

    ev_prolog "Пап, я ничё не поняла... в реальной жизни ты бы что выбрал?" (show_side="none", show_kind="speech")

    ri_prolog "Ну... в жизни ты обычно выбираешь то решение, с которым сможешь жить дальше." (show_side="none", show_kind="speech")

    ev_prolog "Это кого, получается?" (show_side="none", show_kind="speech")

    ri_prolog "Себя." (show_side="none", show_kind="speech")

    scene bg prolog_5 at bg_fullscreen with dissolve
    pause(0.5)

    ev_prolog "Нет. Это неправильный ответ! Вы с мисс Поттс неправы." (show_side="none", show_kind="speech")

    ri_prolog "Ну хоть не я один налажал. Так ей и надо." (show_side="none", show_kind="speech")

    ev_prolog "Ну пап!" (show_side="none", show_kind="speech")
    
    ri_prolog "Ладно, ладно... А кто тогда прав?" (show_side="none", show_kind="speech")

    ev_prolog "Капитан Пирс никогда бы так не поступил." (show_side="none", show_kind="speech")

    ri_prolog "Ох уж этот капитан..." (show_side="none", show_kind="speech")
    ri_prolog "Может, это потому что он из книжки, которую сам же и написал? Не думаешь?" (show_side="none", show_kind="speech")
    #ri_prolog "Да и история его ничем хорошим не кончилась, помнится..."

    ev_prolog "Пап, ты такой взрослый... но так ничего и не понял, да?" (show_side="none", show_kind="speech") 

    ri_prolog "Эм..." (show_side="none", show_kind="speech")

    ev_prolog "Правильный ответ — спасти всех, не выбирая. Как капитан Пирс!" (show_side="none", show_kind="speech")


    scene bg prolog_6 at bg_fullscreen with dissolve

    ri_prolog "Что ж, когда придёт твоё время…" (show_side="none", show_kind="speech")
    ri_prolog "Надеюсь, ты сможешь сделать правильный выбор." (show_side="none", show_kind="speech")

    call fade_to_black(1.2, 0.8)
    #scene black with dissolve

    ri_prolog_offscreen "Я вот не смог." (show_side="none", show_kind="speech")

    call fade_to_black(1.2, 0.8)
    jump start_chapter_1


