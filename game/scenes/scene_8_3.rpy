label scene_8_3:
    $ previous_scene = "scene_8_2"
    $ next_scene = "scene_8_4"
    $ current_scene = "scene_8_3"
    call fade_to_black(1.2, 0.8)
    scene bg archive at bg_fullscreen with dissolve

    show eveina thinking at eveina_left
    ev_thought "Не знаю, почему я так боялась этого момента..." (show_side="left", show_kind="thought")
    ev_thought "Будто архиву не всё равно, что я пришла вернуть то, что не должна была брать." (show_side="left", show_kind="thought")
    hide eveina

    n "Эвейна уверенно положила книгу на стол и коснулась интерфейса вызова. С лёгким звоном на экране появилось подтверждение: {i}«Архивариус направляется»{/i}." (show_side="none", show_kind="speech")
    n "Сдерживая дрожь в кончиках пальцев, девушка стояла, молча глядя на книгу, как на признание вины." (show_side="none", show_kind="speech")
    n "Через минуту из глубины зала выехал робот, его движение было выверенным, ритмичным, как у того, кто знает цену времени." (show_side="none", show_kind="speech")
    n "Когда он приблизился к столу, один из манипуляторов плавно потянулся вперёд, скользнул под книгу, приподнял её…" (show_side="none", show_kind="speech")

    show eveina normal at eveina_left
    ev_thought "Ну вот и всё. Ещё мгновение — и назад пути не будет." (show_side="left", show_kind="thought")
    hide eveina

    n "Второй манипулятор сомкнулся сверху — осторожно, почти с уважением. Книга исчезла в контейнере. И вместе с ней — часть чего-то важного." (show_side="none", show_kind="speech")
    n "Эвейна смотрела, как робот отъезжает, и чувствовала, как где-то глубоко внутри, под рёбрами, что-то сжимается." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev_thought "Сожаление? Поздно. Ты знала, что так будет. И всё равно пошла на это. Так и должно быть." (show_side="left", show_kind="thought")
    hide eveina

    n "Она вздохнула и оглянулась, инстинктивно ища взглядом знакомую фигуру." (show_side="none", show_kind="speech")

    show eveina normal at eveina_left
    ev_thought "Эриан? Ты же обычно появляешься без предупреждения." (show_side="left", show_kind="thought")
    ev_thought "Ну же. Появись." (show_side="left", show_kind="thought")
    hide eveina

    n "Ответа на её немую просьбу не последовало, но она всё равно обошла архив по кругу. Провела пальцами по каждому креслу, по спинкам, по стенам." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev_thought "Здесь я боролась с зашифрованным отчётом, а он усмехался над моими способностями взлома." (show_side="left", show_kind="thought") 
    ev_thought "А тут мы вместе рассматривали фото выпускников." (show_side="left", show_kind="thought")
    hide eveina

    n "Эриан не появился. Не съязвил в обычной манере, не напугал внезапным появлением, в которых был мастером. Даже тень его не скользнула в отражении." (show_side="none", show_kind="speech")
    n "Тогда Эвейна направилась в cад." (show_side="none", show_kind="speech")

    scene bg garden at bg_fullscreen with dissolve

    n "Знакомые тропинки были пусты, что неудивительно в такой-то холод. Листья на деревьях шелестели от пронизывающего ветра. Тишина в садах была живее, чем в архиве, но не менее гнетущей." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev_thought "Может, он просто занят? Или избегает, потому что знает, что я на него зла? Или с ним что-то..." (show_side="left", show_kind="thought")
    ev_thought "Нет. Не думай об этом." (show_side="left", show_kind="thought")
    hide eveina

    n "Она прошла в самую глубь, иногда останавливаясь и размышляя, где он мог бы быть." (show_side="none", show_kind="speech")
    n "Наконец, она подошла к их месту — знакомое дерево с покосившейся веткой, рядом с озером. Села под него, поджав ноги и согревая замерзшие пальцы своим дыханием." (show_side="none", show_kind="speech")

    show eveina sad at eveina_left
    ev_thought "Если ты появишься сейчас, я обещаю выслушать." (show_side="left", show_kind="thought")
    ev_thought "Постараюсь не злиться..." (show_side="left", show_kind="thought")
    hide eveina

    n "Время тянулось, тени медленно двигались, напоминая о времени, которое неуклонно двигалось к вечеру." (show_side="none", show_kind="speech")
    n "Эвейна наклонилась, провела пальцами по траве… и почти машинально потянулась за знакомой травинкой, уже поднеся её к губам, как в тот день." (show_side="none", show_kind="speech")
    n "Только в последний момент осознала, что делает, и резко остановилась." (show_side="none", show_kind="speech")

    show eveina annoyed at eveina_left
    ev_thought "Стоп." (show_side="left", show_kind="thought")
    hide eveina

    n "Она одёрнула себя, рука замерла в воздухе. А в горле внезапно завязался горький комок." (show_side="none", show_kind="speech")

    show eveina angry at eveina_left
    ev_thought "Тебя жизнь вообще хоть чему-то учит, Эвейна?" (show_side="left", show_kind="thought")
    ev_thought "Ждешь эпитафии: «Эвейна Хейла. Причина смерти — дикая глупость и пренебрежение советами неоднозначного, но всё же чертовски правого инопланетянина.»" (show_side="left", show_kind="thought")
    hide eveina

    n "Сумерки сползали на деревья, превращая сад в затонувший мираж. Эриан так и не пришёл." (show_side="none", show_kind="speech")

    show eveina upset at eveina_left
    ev_thought "А если с ним и правда что-то случилось?" (show_side="left", show_kind="thought")
    ev_thought "Если он не может прийти?" (show_side="left", show_kind="thought")
    hide eveina

    n "Понимая, что дальнейшее ожидание бессмысленно, Эвейна неторопливо встала. Пальцы беспокойно сжимали край одежды." (show_side="none", show_kind="speech")
    n "С тяжестью на сердце она пошла обратно, по знакомым тропинкам, которые вдруг стали длиннее." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev_thought "Эриан, надеюсь, ты не вляпался во что-то, из чего мне придётся тебя вытаскивать." (show_side="left", show_kind="thought")
    hide eveina
    show eveina intrigued at eveina_left
    ev_thought "Хотя, честно говоря… это было бы забавно." (show_side="left", show_kind="thought")
    hide eveina

    n "Сад, здание Академии, к которому она направлялась — всё выглядело прежним, словно застывшие декорации." (show_side="none", show_kind="speech")
    n "Но Эвейна чувствовала, что что-то изменилось — внутри поселился новый виток тревоги, не дающий покоя." (show_side="none", show_kind="speech")

    jump scene_8_4
