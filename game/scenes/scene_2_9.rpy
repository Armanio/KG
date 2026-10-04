default bite_reaction = None
default eveina_response_balance = 0

label scene_2_9:
    $ previous_scene = "scene_2_8"
    $ next_scene = "to_be_continued"
    $ current_scene = "scene_2_9"
    $ kg_prepare_scene("scene_2_9")

    # =========================================================
    # СЦЕНА 9 — «ТРОФЕЙ»
    # Структура: пропажа книги → погоня за Эрианом
    #            → датчик → борьба за книгу → вопросы о Далоне
    #            → взаимная эскалация → победа Эвейны
    #            → сон и сомнение в собственной памяти
    # =========================================================

    call fade_to_black(1.2, 0.8)
    scene bg hall at bg_fullscreen with dissolve
    # play music "bgm/corridor_tension.ogg" fadein 2.0

    n "Выйдя из кабинета Вирта, Эвейна сразу направилась в холл." (show_side="none", show_kind="speech")
    n "Она просунула руку между спинкой дивана и стеной." (show_side="none", show_kind="speech")

    n "Пусто." (show_side="none", show_kind="speech")

    show eveina fear at eveina_left, sprite_warm_light
    ev_thought "Нет." (show_side="left", show_kind="thought")
    hide eveina

    n "Эвейна проверила ещё раз. Потом заглянула под диван — на случай, если книга решила самостоятельно усугубить её унижение." (show_side="none", show_kind="speech")

    show eveina fear at eveina_left, sprite_warm_light
    ev_thought "Кто мог её забрать за несколько минут?" (show_side="left", show_kind="thought")
    hide eveina

    n "Ответ пришёл раньше, чем паника успела развернуться во всю ширину." (show_side="none", show_kind="speech")
    n "Только один человек знал про книгу." (show_side="none", show_kind="speech")


    show eveina annoyed at eveina_left, sprite_warm_light
    ev_thought "Только попробуй." (show_side="left", show_kind="thought")
    hide eveina

    n "Эвейна бросилась к архиву." (show_side="none", show_kind="speech")

    # --- Эриан и книга ---

    scene bg archive corridor night at bg_fullscreen with dissolve

    n "Она заметила его у очередного поворота." (show_side="none", show_kind="speech")
    n "Эриан неторопливо шёл в сторону архива, держа под мышкой украденный том." (show_side="none", show_kind="speech")

    show eveina angry at eveina_left, sprite_night_mixed
    ev "Стой!" (show_side="left", show_kind="speech")
    hide eveina

    n "Он остановился и обернулся. Судя по лицу, встреча не стала для него приятным сюрпризом." (show_side="none", show_kind="speech")

    show erian annoyed at erian_right, sprite_night_mixed
    er "Только тебя не хватало." (show_side="right", show_kind="speech")
    hide erian

    show eveina angry at eveina_left,sprite_night_mixed
    ev "Отдай мою книгу." (show_side="left", show_kind="speech")
    hide eveina

    show erian eyebrow at erian_right,sprite_night_mixed
    er "Твою?" (show_side="right", show_kind="speech")
    hide erian

    show eveina annoyed at eveina_left, sprite_night_mixed
    ev "Ты прекрасно понял." (show_side="left", show_kind="speech")
    hide eveina

    show erian eyeroll at erian_right, sprite_night_mixed
    er "Архив будет тронут твоим стремительным чувством собственности." (show_side="right", show_kind="speech")
    hide erian

    n "Эвейна протянула руку. Эриан поднял книгу выше." (show_side="none", show_kind="speech")

    show eveina angry at eveina_left, sprite_night_mixed
    ev "Я сказала — отдай." (show_side="left", show_kind="speech")
    hide eveina

    show erian annoyed at erian_right, sprite_night_mixed
    er "А я решил, что тебе и одного нарушения на сегодня достаточно." (show_side="right", show_kind="speech")
    hide erian

    show eveina eyebrow at eveina_left, sprite_night_mixed
    ev "Ты вытащил её из моего тайника." (show_side="left", show_kind="speech")
    hide eveina

    show erian smile wild at erian_right, sprite_night_mixed
    er "Запихнуть книгу за общественный диван — не тайник." (show_side="right", show_kind="speech")
    er "Это приглашение забрать её первому человеку, которому понадобится мелочь между подушками." (show_side="right", show_kind="speech")
    hide erian

    n "Эвейна снова потянулась к книге. Эриан без особого труда поднял руку ещё выше." (show_side="none", show_kind="speech")

    show eveina annoyed at eveina_left, sprite_night_mixed
    ev "Зачем она тебе?" (show_side="left", show_kind="speech")
    hide eveina

    show erian normal at erian_right, sprite_night_mixed
    er "Спасаю её от бездарной воровки. Ну и бездарную воровку заодно." (show_side="right", show_kind="speech")
    hide erian

    show eveina angry at eveina_left, sprite_night_mixed
    ev "Что?" (show_side="left", show_kind="speech")
    hide eveina

    show erian annoyed at erian_right, sprite_night_mixed
    er "В корешок встроен датчик." (show_side="right", show_kind="speech")
    er "Ты вынесла книгу из архива и даже не попыталась его отключить." (show_side="right", show_kind="speech")
    hide erian

    show eveina fear at eveina_left, sprite_night_mixed
    ev_thought "Всё-таки Вирт знал, что я её взяла!" (show_side="left", show_kind="thought")
    hide eveina

    show erian eyeroll at erian_right, sprite_night_mixed
    er "Потрясающий план." (show_side="right", show_kind="speech")
    hide erian
    show erian annoyed at erian_right, sprite_night_mixed
    er "Ещё немного — и ты могла бы оставить на месте преступления подписанную фотографию." (show_side="right", show_kind="speech")
    hide erian

    show eveina thinking at eveina_left, sprite_night_mixed
    ev "Ты отключил датчик?" (show_side="left", show_kind="speech")
    hide eveina

    show erian normal at erian_right, sprite_night_mixed
    er "Да." (show_side="right", show_kind="speech")
    er "А теперь верну книгу на место. Утром её найдут на полке и спишут на неисправность." (show_side="right", show_kind="speech")
    hide erian

    show eveina annoyed at eveina_left, sprite_night_mixed
    ev "Она мне нужна." (show_side="left", show_kind="speech")
    hide eveina

    show erian eyebrow at erian_right, sprite_night_mixed
    er "Ты уже нашла в ней всё, что искала." (show_side="right", show_kind="speech")
    hide erian

    n "Злость мгновенно уступила тревоге." (show_side="none", show_kind="speech")

    show eveina fear at eveina_left, sprite_night_mixed
    ev_thought "Как много ему известно?" (show_side="left", show_kind="thought")
    hide eveina
    show eveina eyebrow at eveina_left, sprite_night_mixed
    ev "Откуда ты знаешь, что я нашла эту сноску?" (show_side="left", show_kind="speech")
    hide eveina

    n "По медленно расползшейся ухмылке Эвейна поняла, что сказала лишнее." (show_side="none", show_kind="speech")

    show eveina fear at eveina_left, sprite_night_mixed
    ev_thought "Чёрт, он и не знал!" (show_side="left", show_kind="thought")
    hide eveina
    show eveina upset thinking at eveina_left, sprite_night_mixed
    ev_thought "Я сама ему это подтвердила. Блять." (show_side="left", show_kind="thought")
    hide eveina

    n "Скрывать дальше свою находку не имело смысла, поэтому Эвейна пошла в нападение." (show_side="none", show_kind="speech")

    show eveina angry at eveina_left, sprite_night_mixed
    ev "Как ты узнал про эту книгу?" (show_side="left", show_kind="speech")
    ev "Как понял, что я ищу? Почему принёс её мне? Что тебе от меня надо?" (show_side="left", show_kind="speech")
    hide eveina

    show erian intrigued at erian_right, sprite_night_mixed
    er "Тебе на какой вопрос ответить?" (show_side="right", show_kind="speech")
    hide erian

    show eveina wrinkled at eveina_left, sprite_night_mixed
    ev_thought "А ещё более раздражающим ты можешь быть?" (show_side="left", show_kind="thought")
    hide eveina
    show eveina eyeroll at eveina_left, sprite_night_mixed
    ev "На первый." (show_side="left", show_kind="speech")
    hide eveina

    show erian normal at erian_right, sprite_night_mixed
    er "Неудачный выбор." (show_side="right", show_kind="speech")
    hide erian

    n "Эвейна уже решила было, что останется без ответа, но он продолжил." (show_side="none", show_kind="speech")

    show erian normal at erian_right, sprite_night_mixed
    er "Видел её ранее." (show_side="right", show_kind="speech")
    hide erian

    show eveina eyebrow at eveina_left, sprite_night_mixed
    ev "Ты обвёл сноску?" (show_side="left", show_kind="speech")
    hide eveina

    show erian intrigued at erian_right, sprite_night_mixed
    er "Хочешь уличить меня в вандализме?" (show_side="right", show_kind="speech")
    hide erian

    show eveina annoyed at eveina_left, sprite_night_mixed
    ev "Хочу услышать хоть один нормальный ответ." (show_side="left", show_kind="speech")
    hide eveina

    show erian intrigued at erian_right, sprite_night_mixed
    er "Нет. Это не я." (show_side="right", show_kind="speech")
    hide erian

    show eveina eyebrow at eveina_left, sprite_night_mixed
    ev "Тогда кто?" (show_side="left", show_kind="speech")
    hide eveina

    n "Улыбка исчезла с его лица." (show_side="none", show_kind="speech")

    show erian annoyed at erian_right, sprite_night_mixed
    er "Ты задаёшь много вопросов. И все неправильные." (show_side="right", show_kind="speech")
    er "Может, начнёшь быть хоть немного полезной?" (show_side="right", show_kind="speech")
    hide erian

    n "Эвейна на мгновение опешила от такой смены настроения, но сдаваться не собиралась." (show_side="none", show_kind="speech")

    scene bg scene 2_9 book reach at bg_fullscreen with dissolve

    n "Она шагнула ближе и снова потянулась к книге." (show_side="none", show_kind="speech")
    n "Эриан опять поднял руку. Пришлось привстать на носки и почти навалиться на него грудью." (show_side="none", show_kind="speech")
    n "До обоих с небольшим опозданием дошло, насколько тесным стал их спор." (show_side="none", show_kind="speech")

    #show eveina worried at eveina_left
    ev_thought "Вот дерьмо." (show_side="none", show_kind="thought")
    #hide eveina

    n "С такого расстояния Эвейна различала тёмные крапинки в его радужке." (show_side="none", show_kind="speech")
    n "Совершенно бесполезное наблюдение. Поэтому мозг, разумеется, вцепился именно в него." (show_side="none", show_kind="speech")

    n "Ухмылка Эриана на мгновение дрогнула." (show_side="none", show_kind="speech")
    n "Значит, неловкость досталась не только ей. Уже неплохо." (show_side="none", show_kind="speech")

    #show erian intrigued at erian_right
    er "Удобно?" (show_side="none", show_kind="speech")
    #hide erian

    #show eveina annoyed at eveina_left
    ev "Бывало и лучше." (show_side="none", show_kind="speech")
    #hide eveina

    scene bg archive corridor night at bg_fullscreen

    n "Эвейна отступила ровно настолько, чтобы снова посмотреть ему в лицо. И угрожающе наставила на него палец." (show_side="none", show_kind="speech")

    show eveina annoyed at eveina_left, sprite_night_mixed
    ev "Отдай." (show_side="left", show_kind="speech")
    hide eveina

    show erian eyeroll at erian_right, sprite_night_mixed
    er "Нет." (show_side="right", show_kind="speech")
    hide erian

    show eveina wrinkled at eveina_left, sprite_night_mixed
    ev "Я не просила тебя меня спасать." (show_side="left", show_kind="speech")
    hide eveina

    show erian thinking at erian_right, sprite_night_mixed
    er "А я не собираюсь смотреть, как тебя вышвыривают из Академии из-за преступной беспомощности." (show_side="right", show_kind="speech")
    hide erian

    show eveina annoyed at eveina_left, sprite_night_mixed
    ev "Это моя проблема." (show_side="left", show_kind="speech")
    hide eveina

    show erian eyebrow at erian_right, sprite_night_mixed
    er "Ты удивительно щедро делаешь её чужой." (show_side="right", show_kind="speech")
    hide erian

    show eveina angry at eveina_left, sprite_night_mixed
    ev "Какого чёрта ты решил тут сыграть в непрошенную благотворительность?" (show_side="left", show_kind="speech")
    hide eveina

    show erian normal at erian_right, sprite_night_mixed
    er "Ты привлекаешь слишком много внимания." (show_side="right", show_kind="speech")
    hide erian
    show erian eyebrow at erian_right, sprite_night_mixed
    er "А нам ведь это ни к чему, верно?" (show_side="right", show_kind="speech")
    hide erian

    show eveina wrinkled at eveina_left, sprite_night_mixed
    ev "Каким ещё к чёрту «нам»?" (show_side="left", show_kind="speech")
    hide eveina

    n "Эриан ухмыльнулся, но не ответил." (show_side="none", show_kind="speech")

    show eveina angry at eveina_left, sprite_night_mixed
    ev "Тебе что-то от меня нужно?" (show_side="left", show_kind="speech")
    hide eveina

    show erian normal at erian_right, sprite_night_mixed
    er "Я этого не говорил." (show_side="right", show_kind="speech")
    hide erian

    show eveina annoyed at eveina_left, sprite_night_mixed
    ev "Но и книгу ты принёс не из внезапной любви к исторической литературе, так ведь?" (show_side="left", show_kind="speech")
    hide eveina

    show erian eyebrow at erian_right, sprite_night_mixed
    er "Продолжай. Когда-нибудь случайно доберёшься до правильного вопроса." (show_side="right", show_kind="speech")
    hide erian
    show erian normal at erian_right, sprite_night_mixed
    er "И хватит тыкать в меня своим пальцем, а то он может случайно пострадать." (show_side="right", show_kind="speech")
    hide erian

    show eveina annoyed at eveina_left, sprite_night_mixed
    ev "Куда хочу, туда и тыкаю своим пальцем! Я прошла курс проктологии в университете." (show_side="left", show_kind="speech")
    hide eveina
    show eveina eyeroll at eveina_left, sprite_night_mixed
    ev_thought "Боже, что я несу..." (show_side="left", show_kind="thought")
    hide eveina

    show erian annoyed at erian_right, sprite_night_mixed
    er "Прекрасно. Придётся выбросить рубашку." (show_side="right", show_kind="speech")
    hide erian

    show eveina annoyed at eveina_left, sprite_night_mixed
    ev "Не увиливай от ответа! Что тебе от меня нужно?" (show_side="left", show_kind="speech")
    hide eveina

    show erian eyebrow at erian_right, sprite_night_mixed
    er "Не говори мне, что делать. Что за манера вообще такая, нападать на тех, кто тебе помогает?" (show_side="right", show_kind="speech")
    hide erian
    show erian annoyed at erian_right, sprite_night_mixed
    er "Последний раз говорю, убери чёртов палец." (show_side="right", show_kind="speech")
    hide erian

    show eveina annoyed at eveina_left, sprite_night_mixed
    ev "Мой палец останется там, куда я его положила." (show_side="left", show_kind="speech")
    hide eveina

    n "На скулах Эриана заиграли желваки. Кажется, аргументы закончились у обоих." (show_side="none", show_kind="speech")
    n "Впрочем, он не учёл, что у Эвейны ещё оставались зубы." (show_side="none", show_kind="speech")

    show eveina angry at eveina_left, sprite_night_mixed
    ev_thought "Ну, придурок, ты сам напросился..." (show_side="left", show_kind="thought")
    hide eveina

    n "Она резко подпрыгнула и обеими руками вцепилась в книгу." (show_side="none", show_kind="speech")
    n "Эриан удержал том над головой, а свободной ладонью попытался отстранить её от себя." (show_side="none", show_kind="speech")
    n "Эвейна не раздумывала." (show_side="none", show_kind="speech")

    scene bg scene 2_9 book bite at bg_fullscreen with dissolve

    n "И впилась зубами в его запястье." (show_side="none", show_kind="speech")

    #show erian angry at erian_right
    er "Твою мать!" (show_side="right", show_kind="speech")
    #hide erian

    n "Рука дёрнулась. Книга опустилась всего на мгновение — Эвейне хватило." (show_side="none", show_kind="speech")
    n "Она вырвала том, прижала его к груди и отскочила." (show_side="none", show_kind="speech")
    pause

    scene bg archive corridor night at bg_fullscreen with dissolve

    show erian angry at erian_right, sprite_night_mixed
    er "Совсем из ума выжила, придурочная?" (show_side="right", show_kind="speech")
    er "Кто-нибудь, пристрелите эту женщину, у неё бешенство!" (show_side="right", show_kind="speech")
    hide erian

    show eveina angry at eveina_left, sprite_night_mixed
    ev "Сам ты бешеный!" (show_side="left", show_kind="speech")
    hide eveina

    n "И в доказательство своей абсолютной нормальности Эвейна клацнула зубами." (show_side="none", show_kind="speech")
    n "Раздавшийся звук слегка сбил спесь с обоих." (show_side="none", show_kind="speech")

    show eveina annoyed at eveina_left, sprite_night_mixed
    ev_thought "Зато книга у меня." (show_side="left", show_kind="thought")
    hide eveina

    n "Воспользовавшись заминкой, девушка торопливо спрятала том в сумку и отвела её за спину." (show_side="none", show_kind="speech")
    n "Эриан посмотрел на след от зубов. Потом — на неё, словно заново оценивал масштаб проблемы." (show_side="none", show_kind="speech")
    n "Он недобро усмехнулся и шагнул вперёд." (show_side="none", show_kind="speech")
    n "Девушка отступила, удерживая сумку за спиной. Ещё шаг — и лопатки упёрлись в стену." (show_side="none", show_kind="speech")

    scene bg scene 2_9 wall standoff at bg_fullscreen with dissolve
    pause (1.0)

    n "Она выставила ладонь, останавливая его." (show_side="none", show_kind="speech")

    er "Ты, может, не заметила очевидной вещи, но я сильнее тебя." (show_side="right", show_kind="speech")
    er "Не приходило в твою невесомую черепушку, что злить человека сильнее тебя — плохая идея?" (show_side="right", show_kind="speech")

    n "Страх требовал отступить. Упрямство напоминало о книге." (show_side="none", show_kind="speech")
    n "А между ними шевельнулось совсем неуместное любопытство: что он сделает?" (show_side="none", show_kind="speech")

    ev "Не угрожай мне, придурок." (show_side="left", show_kind="speech")

    n "Книга за спиной была куда важнее того, насколько близко он стоял." (show_side="none", show_kind="speech")
    n "По крайней мере, Эвейна очень старалась в это верить." (show_side="none", show_kind="speech")
    n "Ладонь на его груди дрогнула. Парень опустил взгляд на её пальцы." (show_side="none", show_kind="speech")

    #show erian angry at erian_right
    er "У тебя точно нет тормозов." (show_side="right", show_kind="speech")
    #hide erian

    n "Он снова посмотрел ей в глаза, всем своим видом говоря: «Ну, попробуй останови»." (show_side="none", show_kind="speech")
    n "А затем приблизился." (show_side="none", show_kind="speech")

    scene bg scene 2_9 bite aftermath at bg_fullscreen with dissolve
    pause (1.0)

    n "Когда его дыхание коснулось её волос, Эвейна наконец поняла: к книге он не тянулся." (show_side="none", show_kind="speech")
    n "Эриан склонился к её уху и, чуть помедлив, прошептал:" (show_side="none", show_kind="speech")

    er "Хочешь знать, что мне от тебя нужно?" (show_side="right", show_kind="speech")

    ev_thought "Уже хочу просто поскорее отсюда убраться." (show_side="left", show_kind="thought")

    er "Тогда отдай кни..." (show_side="right", show_kind="speech")

    n "Ответ Эвейны вырвался ещё до того, как он успел закончить фразу." (show_side="none", show_kind="speech")

    ev "Обойдёшься." (show_side="left", show_kind="speech")

    n "В следующий момент его зубы сомкнулись на мочке уха." (show_side="none", show_kind="speech")
    n "Не сильно — но вполне достаточно, чтобы Эвейна резко втянула воздух и несколько секунд не могла выдохнуть." (show_side="none", show_kind="speech")

    $ bite_reaction = renpy.call_screen("choice",
    items=[
    ("Размахнулась.", "slap"),
    ("Крепче вцепилась в сумку.", "book")
    ], what="А потом...")

    if bite_reaction == "slap":

        $ eveina_response_balance = 1

        n "Ладонь встретилась с его скулой звонко и без малейших сомнений." (show_side="none", show_kind="speech")

        scene bg scene 2_9 choice slap at bg_fullscreen with dissolve
        pause (1.0)

        n "Голову Эриана мотнуло в сторону от удара. Но пальцы тут же сомкнулись на запястье Эвейны." (show_side="none", show_kind="speech")
        n "Эвейна попыталась вырвать руку и злобно прошипела:" (show_side="none", show_kind="speech")

        #show eveina angry at eveina_left
        ev "Ты меня укусил!" (show_side="left", show_kind="speech")
        #hide eveina

        #show erian thinking at erian_right
        er "Ты первая это начала." (show_side="right", show_kind="speech")
        er "Боже, как же ты умеешь выводить из себя. Просто талант!" (show_side="right", show_kind="speech")
        #hide erian

        #show eveina angry at eveina_left
        ev "Ты совсем рехнулся? Отпусти меня сейчас же! Или я..." (show_side="left", show_kind="speech")
        #hide eveina

        #show erian wild smile at erian_right
        er "Или ты что, Эвейна?" (show_side="right", show_kind="speech")
        #hide erian

        n "Девушка закусила губу, впервые трезво оценив габариты соперника и свои шансы на реванш." (show_side="none", show_kind="speech")

        er "Так уж и быть, дам тебе совет." (show_side="right", show_kind="speech")
        er "Не угрожай, если не готова привести угрозу в исполнение." (show_side="right", show_kind="speech")

        scene bg archive corridor night at bg_fullscreen with dissolve

        n "Эриан потянулся свободной рукой к её сумке. Эвейна дёрнулась в ответ, снова клацнув зубами прямо у его носа." (show_side="none", show_kind="speech")
        n "Страх никуда не делся, но и проиграть она не могла." (show_side="none", show_kind="speech")

        show erian wild smile at erian_right, sprite_night_mixed
        er "Точно бешеная." (show_side="right", show_kind="speech")
        hide erian

        show eveina angry at eveina_left, sprite_night_mixed
        ev "Можешь хоть всю меня покусать, книгу я не отдам!" (show_side="left", show_kind="speech")
        hide eveina

        show erian eyebrow at erian_right, sprite_night_mixed
        er "Сомнительное удовольствие." (show_side="right", show_kind="speech")
        hide erian

        n "Она дёрнула руку снова, ещё резче. Старый след от пробуждения в саду отозвался знакомой тупой болью, заставив Эвейну поморщиться." (show_side="none", show_kind="speech")
        n "Эриан заметил перемену в её лице и выпустил её руку из захвата." (show_side="none", show_kind="speech")
        n "Отступил на шаг, потирая укушенное запястье." (show_side="none", show_kind="speech")


    elif bite_reaction == "book":

        $ eveina_response_balance = -1

        scene bg scene 2_9 choice book at bg_fullscreen with dissolve

        n "Первым порывом было ударить." (show_side="none", show_kind="speech")
        n "Но для этого пришлось бы выпустить ремень сумки." (show_side="none", show_kind="speech")

        ev_thought "Ещё чего." (show_side="left", show_kind="thought")

        n "Эвейна не отвела взгляда и сильнее прижала сумку к спине." (show_side="none", show_kind="speech")

        ev "Ты меня укусил!" (show_side="left", show_kind="speech")

        #show erian thinking at erian_right
        er "Согласен, слегка перестарался, но ты первая начала." (show_side="right", show_kind="speech")
        er "И боже, как же ты умеешь выводить из себя. Просто талант!" (show_side="right", show_kind="speech")
        #hide erian

        ev "Можешь хоть всю меня покусать, книгу я не отдам!" (show_side="left", show_kind="speech")

        n "Страх никуда не исчез, просто победа была важнее." (show_side="none", show_kind="speech")

        er "Сомнительное удовольствие." (show_side="right", show_kind="speech")

        n "Эриан отступил на шаг и потёр укушенное запястье." (show_side="none", show_kind="speech")
        n "Окинул её долгим раздражённым взглядом." (show_side="none", show_kind="speech")

    scene bg archive corridor night at bg_fullscreen with dissolve
    pause (1.0)

    show erian eyeroll at erian_right, sprite_night_mixed
    er "Подавись своей книгой." (show_side="right", show_kind="speech")
    hide erian
    show erian annoyed at erian_right, sprite_night_mixed
    er "И постарайся больше никого не кусать. Второй раз тебе может так не повезти." (show_side="right", show_kind="speech")
    hide erian

    show eveina eyeroll at eveina_left, sprite_night_mixed
    ev "Спасибо за совет. Постарайся больше не воровать у воров." (show_side="left", show_kind="speech")
    hide eveina

    n "Он коротко выругался и направился прочь. Девушка осталась стоять посреди коридора, крепко прижимая к себе сумку." (show_side="none", show_kind="speech")
    n "Только когда его шаги совсем стихли за поворотом, Эвейна заметила, что всё ещё прислушивается." (show_side="none", show_kind="speech")

    show eveina annoyed at eveina_left, sprite_night_mixed
    ev_thought "Знает про датчик. Знал, что я найду в книге. Вероятно, следил за мной, когда я прятала книгу." (show_side="left", show_kind="thought")
    hide eveina
    show eveina thinking at eveina_left, sprite_night_mixed
    ev_thought "И очень не хочет говорить, что ему от меня нужно." (show_side="left", show_kind="thought")
    hide eveina

    show eveina normal at eveina_left, sprite_night_mixed
    ev_thought "Хотя бы один ответ сегодня я получила." (show_side="left", show_kind="thought")
    hide eveina

    # --- Сон ---

    call fade_to_black(1.2, 0.8)
    scene bg room night at bg_fullscreen with dissolve
    n "Позже, уже в комнате, Эвейна ещё раз перечитала отмеченную сноску." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left, sprite_night
    ev_thought "Кайр Далон. Чёртов призрак." (show_side="left", show_kind="thought")
    hide eveina

    n "Она закрыла книгу и убрала её подальше от чужих глаз." (show_side="none", show_kind="speech")
    n "Сон пришёл быстро. Спокойствия с собой он не принёс." (show_side="none", show_kind="speech")

    scene bg scene 1_6 dream 1 at bg_fullscreen with dissolve

    n "Вода холодила босые ноги. Где-то в конце коридора виднелся тусклый свет." (show_side="none", show_kind="speech")
    n "Эвейна уже видела это место." (show_side="none", show_kind="speech")

    n "Далёкие голоса смешивались с шумом пульса в ушах." (show_side="none", show_kind="speech")
    n "Она знала, что её ждёт и попыталась отступить." (show_side="none", show_kind="speech")

    n "Но пальцы снова сомкнулись на её запястье." (show_side="none", show_kind="speech")

    scene bg scene 1_6 dream 10 at bg_fullscreen with dissolve

    ev "Что тебе нужно?" (show_side="right", show_kind="speech")

    n "В этот раз голос прозвучал совсем рядом." (show_side="none", show_kind="speech")

    call fade_to_black(0.2, 0.1)

    unknown "Кто такой Кайр Далон, Эвейна?" (show_side="none", show_kind="speech")

    scene bg room night at bg_fullscreen with dissolve

    n "Эвейна резко села в кровати." (show_side="none", show_kind="speech")

    show eveina fear tshirt at eveina_left, sprite_night
    ev_thought "Я уже слышала этот вопрос." (show_side="left", show_kind="thought")
    hide eveina

    n "Уверенность продержалась всего несколько секунд." (show_side="none", show_kind="speech")

    show eveina thinking tshirt at eveina_left, sprite_night
    ev_thought "Нет. Тогда я не разобрала слов." (show_side="left", show_kind="thought")
    hide eveina

    show eveina upset thinking tshirt at eveina_left, sprite_night
    ev_thought "Или разобрала?" (show_side="left", show_kind="thought")
    hide eveina

    n "Имя она узнала только сегодня." (show_side="none", show_kind="speech")
    n "Но теперь в её памяти оно звучало и в прежнем сне." (show_side="none", show_kind="speech")
    n "Пальцы вцепились в одеяло, будто это могло помочь найти ответ." (show_side="none", show_kind="speech")

    show eveina fear tshirt at eveina_left, sprite_night
    ev_thought "Что же изменилось — сон или моя память о нём?" (show_side="left", show_kind="thought")
    hide eveina

    jump to_be_continued
