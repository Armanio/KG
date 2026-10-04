label scene_5_5:
    $ previous_scene = "scene_5_4"
    $ next_scene = "scene_5_6"
    $ current_scene = "scene_5_5"
    call fade_to_black(1.2, 0.8)
    scene bg lab at bg_fullscreen with dissolve

    n "Практики по нейроанализу отменялись уже несколько раз. И каждый раз — без объяснений." (show_side="none", show_kind="speech")
    n "Именно поэтому сегодня, увидев её в расписании и не получив привычного уведомления об отмене, Эвейна пришла в лабораторию с лёгким напряжением в теле, будто предчувствовала нападение с тыла." (show_side="none", show_kind="speech")
    n "Резкий голос. Оценивающий взгляд. Уголок губ, приподнятый в надменной полуулыбке, которую невозможно не заметить." (show_side="none", show_kind="speech")
    n "Но вместо всего этого — тишина. На месте у консоли стоял не Каэль." (show_side="none", show_kind="speech")

    show ezari normal at ezari_right
    ez "Прошу занять места." (show_side="right", show_kind="speech")
    ez "Сегодняшняя практика будет сосредоточена на стандартной процедуре синхронизации между структурами когнитивного отклика и сенсорной обратной связью. Начнём." (show_side="right", show_kind="speech")
    hide ezari

    show eveina wondered at eveina_left
    ev_thought "Погодите… а где Каэль?" (show_side="left", show_kind="thought")
    hide eveina
    show eveina  thinking at eveina_left
    ev_thought "Перешёл в автономный режим, чтобы не перегреться от эмоционального перегруза?" (show_side="left", show_kind="thought")
    ev_thought "Или… кто-то наконец обновил его до версии, которой не нужно ломать людей по вторникам?" (show_side="left", show_kind="thought")
    hide eveina

    n "Каэль не появился ни в начале, ни в середине, ни в финале практики." (show_side="none", show_kind="speech")
    n "Профессор Эзари, с его хрипловатым голосом и убаюкивающей интонацией, проводил занятие так, будто читает лекцию по садоводству, а не проводит практику по нейроанализу." (show_side="none", show_kind="speech")

    show eveina eyeroll at eveina_left
    ev_thought "Слишком подробно. Слишком методично." (show_side="left", show_kind="thought")
    hide eveina
    show eveina thinking at eveina_left
    ev_thought "Я даже не чувствую, что думаю. Просто следую инструкциям." (show_side="left", show_kind="thought")
    hide eveina
    show eveina normal at eveina_left
    ev_thought "У Каэля на практике хоть был шанс потеряться в хаосе." (show_side="left", show_kind="thought")
    hide eveina
    show eveina eyeroll at eveina_left
    ev_thought "А здесь — инструкция, как починить сознание с завязанными глазами c помощью обычной домашней..." (show_side="left", show_kind="thought")
    hide eveina

    n "Работа шла — медленно, уверенно и невероятно скучно." (show_side="none", show_kind="speech")
    n "Эвейна добросовестно выполняла задание, хотя и ловила себя на том, что её мысли то и дело возвращаются к другому." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev_thought "Если Каэль не вернётся, я разучусь думать." (show_side="left", show_kind="thought")
    hide eveina
    show eveina eyebrow at eveina_left
    ev_thought "С ним же точно всё в порядке?" (show_side="left", show_kind="thought")
    ev_thought "Его отсутсвие ведь никак не связано с нашим... с его поцелуем?" (show_side="left", show_kind="thought")
    hide eveina
    show eveina thinking at eveina_left
    ev_thought "Почему меня вообще это беспокоит?" (show_side="left", show_kind="thought")
    hide eveina
    show eveina annoyed at eveina_left
    ev_thought "Это он повёл себя, как заносчивый придурок, а не я." (show_side="left", show_kind="thought")
    hide eveina

    n "В конце занятия профессор Эзари неспешно подошёл к центральному терминалу и обвёл взглядом студентов." (show_side="none", show_kind="speech")

    show ezari normal at ezari_right
    ez "Завтра утром состоится лекция по нейроимплантам. Всем быть." (show_side="right", show_kind="speech")
    ez "Особенно тем, кто мечтает когда-нибудь вмешиваться в чужое сознание с помощью аугментаций без катастрофических последствий." (show_side="right", show_kind="speech")
    hide ezari

    n "Эвейна быстро собрала свои вещи. Мозг отказывался работать — не из-за практики." (show_side="none", show_kind="speech")
    n "Из-за нарастающей тревоги, что именно она — причина отсутствия Каэля." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev_thought "Надеюсь, ты не исчез. Хотя бы не насовсем." (show_side="left", show_kind="thought")
    ev_thought "Считать тебя высокомерным придурком, пока ты находишься рядом, было гораздо проще." (show_side="left", show_kind="thought")
    hide eveina

    jump scene_5_6
