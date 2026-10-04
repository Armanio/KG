label scene_8_7:
    $ previous_scene = "scene_8_6"
    $ next_scene = "scene_8_8"
    $ current_scene = "scene_8_7"
    call fade_to_black(1.2, 0.8)
    scene bg lecture_hall at bg_fullscreen with dissolve

    n "Утро началось с урагана. В лице Вирта. Он влетел в лекционный зал, как будто его швырнуло внутрь потоком воздуха." (show_side="none", show_kind="speech")
    n "Пальцы сжаты в кулаки, взгляд острый, как лезвие. Он не поздоровался. Лишь скользнул по аудитории взглядом — и задержался на ней." (show_side="none", show_kind="speech")

    show eveina normal at eveina_left
    ev_thought "Ой-ой… это точно не просто так." (show_side="left", show_kind="thought")
    hide eveina

    n "Он тут же отвернулся и начал лекцию. Голос разносился по аудитории — ровный, холодный, с таким леденящим акцентом на окончаниях, будто каждое слово было приговором. Он отскакивал эхом от стен и наполнял зал тяжелой атмосферой." (show_side="none", show_kind="speech")
    n "За спиной она услышала знакомый шепот." (show_side="none", show_kind="speech")

    show tero normal at tero_right
    te "Что-то он не в духе сегодня. Чай закончился?" (show_side="right", show_kind="speech")
    hide tero

    n "Эвейна не улыбнулась. Наоборот, ей захотелось сжаться, исчезнуть, вжаться в кресло. Вирт не смотрел на неё. Но она знала — дело в ней." (show_side="none", show_kind="speech")

    show noa intrigued at noa_right
    no "Не знаю, кто его так вывел из себя, но не хотел бы я быть этим кем-то..." (show_side="right", show_kind="speech")
    hide noa

    show eveina upset at eveina_left
    ev_thought "Я тоже, Ноа, я тоже..." (show_side="left", show_kind="thought")
    hide eveina

    n "Вся лекция — каждое отточенное, жёсткое предложение — летело в её сторону, как тонкие, невидимые иглы." (show_side="none", show_kind="speech")
    n "С ужасом она отсчитывала минуты. Когда Вирт закончил, это прозвучало как выстрел." (show_side="none", show_kind="speech")

    show virt serious at virt_right
    vi "Все свободны." (show_side="right", show_kind="speech")
    hide virt

    n "Он резко отвернулся к проекционному экрану. Эвейна медленно встала и направилась к выходу вместе с остальными." (show_side="none", show_kind="speech")

    show virt serious at virt_right
    vi "Мисс Хейла, задержитесь." (show_side="right", show_kind="speech")
    hide virt

    n "Фраза прозвучала глухо, коротко, без выражения. Но от этого — только страшнее. Ноа, проходя мимо, присвистнул:" (show_side="none", show_kind="speech")

    show noa intrigued at noa_right
    no "Не повезло, красавица." (show_side="right", show_kind="speech")
    hide noa

    n "Эвейна остановилась в центре зала. Дождалась, пока последний студент выйдет и за ним закроются двери. А после медленно обернулась." (show_side="none", show_kind="speech")
    n "Аурелиан стоял, опершись о край кафедры, и смотрел прямо на неё. Лицо было непроницаемым, но раздражение сквозило слишком явственно в его позе." (show_side="none", show_kind="speech")

    show virt serious at virt_right
    vi "Кто-то проник в личное облако профессора Кайстра. Пытался украсть данные его переписок." (show_side="right", show_kind="speech")
    hide virt

    n "Профессор медленно прошёлся вдоль ряда, делая долгую паузу." (show_side="none", show_kind="speech")

    show virt angry at virt_right
    vi "Звучит знакомо, правда?" (show_side="right", show_kind="speech")
    hide virt
    show virt thinking at virt_right
    vi "Я же просил тебя не лезть в неприятности." (show_side="right", show_kind="speech")
    hide virt

    n "Он резко провёл рукой по волосам, и в этом движение не было обычного изящества, лишь нервная привычка." (show_side="none", show_kind="speech")

    show virt serious at virt_right
    vi "Ведётся официальное расследование. Я отвечаю за его результаты." (show_side="right", show_kind="speech")
    hide virt
    show virt upset at virt_right
    vi "Ты хоть понимаешь, в какую ситуацию ты меня поставила?" (show_side="right", show_kind="speech")
    hide virt

    n "Эвейна молчала, опустив глаза. Пальцы предательски дрожали." (show_side="none", show_kind="speech")

    show eveina upset at eveina_left
    ev_thought "Ну вот и конец." (show_side="left", show_kind="thought")
    hide eveina

    jump scene_8_8
