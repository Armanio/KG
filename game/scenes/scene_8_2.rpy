label scene_8_2:
    $ previous_scene = "scene_8_1"
    $ next_scene = "scene_8_3"
    $ current_scene = "scene_8_2"
    call fade_to_black(1.2, 0.8)
    scene bg shuttle at bg_fullscreen with dissolve

    n "Утро застало Эвейну в странном состоянии: между сном и усталостью, между мыслями о Вирте и тяжестью грядущего." (show_side="none", show_kind="speech")
    n "Аурелиан снова был собран, сдержан и вежлив, как будто она не провела весь прошлый вечер, прижавшись к его груди." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev_thought "Мне б твою выдержку, профессор." (show_side="left", show_kind="thought")
    hide eveina

    n "На выходе с шаттла Эвейна невольно поёжилась от прохладного влажного воздуха." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev_thought "Разве на этой планете не постоянная температура воздуха?" (show_side="left", show_kind="thought")
    hide eveina

    n "Заметив, как Эвейна дрожит, Вирт накинул на её плечи свою мантию и подтолкнул в сторону здания Академии." (show_side="none", show_kind="speech")

    show virt normal jacket at virt_right
    vi "Тут прохладно. Пойдём скорее, пока ты не получила переохлаждение." (show_side="right", show_kind="speech")
    hide virt

    scene bg eveina_room at bg_fullscreen with dissolve
    
    n "По прибытии в Академию профессор молча проводил Эвейну до комнаты. У двери они столкнулись с Леей." (show_side="none", show_kind="speech")

    show virt normal jacket at virt_right
    vi "Доброе утро, мисс Таласа." (show_side="right", show_kind="speech")
    hide virt
    show virt intrigued jacket at virt_right
    vi "Мисс Хейла, хорошего дня." (show_side="right", show_kind="speech")
    hide virt

    n "Эвейна быстрым движением сбросила мантию сплеч и аккуратно отдала декану. Он в ответ невозмутимо передал студентке сумку с лёгким кивком и ушёл." (show_side="none", show_kind="speech")
    n "Когда дверь закрылась за ним, Лея ещё несколько секунд пристально смотрела на неё." (show_side="none", show_kind="speech")

    show leya eyebrow at leya_right
    le "Это что сейчас было?" (show_side="right", show_kind="speech")
    hide leya

    n "Эвейна бросила сумку на кровать с усталым вздохом." (show_side="none", show_kind="speech")

    show eveina eyeroll at eveina_left
    ev "Не спрашивай. Я его об этом не просила." (show_side="left", show_kind="speech")
    hide eveina

    show leya normal at leya_right
    le "Этот факт делает ситуацию только более интригующей." (show_side="right", show_kind="speech")
    hide leya
    show leya eyebrow at leya_right
    le "Что ж такого произошло между вами за эти дни, что декан теперь кутает тебя в мантию и носит сумку?" (show_side="right", show_kind="speech")
    hide leya

    show eveina eyeroll at eveina_left
    ev "Разговор о границах в отношениях." (show_side="left", show_kind="speech")
    hide eveina

    n "Тон был достаточно отчётливый, чтобы Лея поняла — тему лучше не развивать. Вместо этого оглядела озябшую подругу и молча начала заваривать чай." (show_side="none", show_kind="speech")

    show eveina eyebrow at eveina_left
    ev "Что случилось с погодой? Какие-то эксперименты с климатом вышли из под контроля?" (show_side="left", show_kind="speech")
    hide eveina
    show eveina upset thinking at eveina_left
    ev "Я чуть себе язык не откусила, пока мы добрались до здания." (show_side="left", show_kind="speech")
    hide eveina

    show leya normal at leya_right
    le "Последние три дня вот так... Не знаю, с чем это связано." (show_side="right", show_kind="speech")
    hide leya
    show leya thinking at leya_right
    le "Может, и эксперименты, но нам об этом не говорят." (show_side="right", show_kind="speech")
    hide leya

    n "Эвейна с благодарностью приняла горячую кружку и, обхватив её ладонями, начала рассказывать о самом важном." (show_side="none", show_kind="speech")

    show eveina normal at eveina_left
    ev "Папа выглядит хуже. Слабее. Но он меня узнал. Он всё ещё… мой отец." (show_side="left", show_kind="speech")
    hide eveina
    show eveina thinking at eveina_left
    ev "Не знаю, сколько времени у него осталось... но мне точно стоит поторопиться." (show_side="left", show_kind="speech")
    hide eveina

    n "Лея слушала внимательно, почти не перебивая. Только один раз сжала ладонью колено Эвейны." (show_side="none", show_kind="speech")

    show leya smile at leya_right
    le "Хорошо, что ты повидалась с ним. Это самое главное." (show_side="right", show_kind="speech")
    hide leya

    n "Эвейна не нашлась, что сказать на это. Вместо этого просто поставила чашку на стол и неожиданно обняла Лею — коротко, но крепко." (show_side="none", show_kind="speech")
    n "Та, казалось, не удивилась и только крепче прижалась в ответ." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev_thought "Иногда я забываю, насколько важно просто знать, что кто-то рядом." (show_side="left", show_kind="thought")
    ev_thought "Лея никогда не требует объяснений, не давит. Просто есть. Просто держит меня на плаву." (show_side="left", show_kind="thought")
    hide eveina
    show eveina smile at eveina_left
    ev "Спасибо, Лея. Не представляю, что бы я без тебя делала." (show_side="left", show_kind="speech")
    hide eveina

    n "Они ещё немного посидели, обмениваясь историями: кто поскользнулся на лестнице и попал в больничное крыло, кто проспал лекцию Раукт, какие слухи ходят об ИИ-ассистенте, который якобы разговаривает с акцентом." (show_side="none", show_kind="speech")
    n "Глаза Эвейны вдруг напонились светом, появилась улыбка на губах. А спустя ещё какое-то время смех стал лёгким, почти как в те дни, когда жизнь ещё не казалась ловушкой." (show_side="none", show_kind="speech")
    n "Когда чай закончился, Эвейна медленно встала. Её взгляд упал на лежащую на столе книгу — ту самую, из Архива. Она подошла, взяла её, прижала к груди и кивнула Лее." (show_side="none", show_kind="speech")

    show eveina normal at eveina_left
    ev "Мне нужно сделать кое-что важное." (show_side="left", show_kind="speech")
    hide eveina
    
    show eveina normal at eveina_left
    ev_thought "Пора платить по счетам." (show_side="left", show_kind="thought")
    hide eveina

    jump scene_8_3
