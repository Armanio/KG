default eveina_shared_medical_data = False

label scene_1_6:
    $ previous_scene = "scene_1_5"
    $ next_scene = "kg_end_chapter_1"
    $ current_scene = "scene_1_6"
    $ kg_prepare_scene("scene_1_6")

    call fade_to_black(1.2, 0.8)
    scene bg room night at bg_fullscreen with dissolve
    # play music "bgm/dorm_evening.ogg" fadein 2.0

    n "Было уже давно за полночь. Тишина в комнате прерывалась лишь ровным дыханием Леи, спящей на соседней кровати." (show_side="none", show_kind="speech")
    n "Эвейна лежала с открытыми глазами, уставившись в стену из мха над головой, где были еле различимы контуры биоэлектрических артерий Академии." (show_side="none", show_kind="speech")
    n "Сон не шёл, а уставший от избытка событий разум никак не хотел успокаиваться, подкидывая одну тревожную мысль за другой." (show_side="none", show_kind="speech")


    show eveina normal tshirt at eveina_left, sprite_night
    ev_thought "Все ниточки вели сюда: если нужные мне разработки где-то и существовали, искать следовало здесь." (show_side="left", show_kind="thought")
    hide eveina
    show eveina eyebrow tshirt at eveina_left, sprite_night
    ev_thought "И пока всё идёт по плану: я на кафедре, доступ к базе у меня на запястье." (show_side="left", show_kind="thought")
    hide eveina

    show eveina eyeroll tshirt at eveina_left, sprite_night
    ev_thought "Если я всё равно не сплю..." (show_side="left", show_kind="thought")
    hide eveina

    n "Эвейна подняла руку и открыла внутреннюю базу Академии." (show_side="none", show_kind="speech")

    show eveina normal tshirt at eveina_left, sprite_night
    ev "Поле Иннаки. Восстановление когнитивных функций." (show_side="left", show_kind="speech")
    hide eveina

    n "Над браслетом развернулся список результатов." (show_side="none", show_kind="speech")
    n "Первые названия Эвейна узнала сразу. Те же публикации и обзорные статьи она уже читала в открытом доступе." (show_side="none", show_kind="speech")

    show eveina annoyed tshirt at eveina_left, sprite_night
    ev_thought "Не смешно." (show_side="left", show_kind="thought")
    hide eveina

    n "Ниже обнаружился материал без открытой версии." (show_side="none", show_kind="speech")

    show eveina normal tshirt at eveina_left, sprite_night
    ev "Открыть полный отчёт." (show_side="left", show_kind="speech")
    hide eveina

    show ai at ai_right
    ai "Полная версия недоступна для вашего уровня допуска." (show_side="right", show_kind="speech")
    hide ai

    show eveina eyebrow tshirt at eveina_left, sprite_night
    ev "Тогда покажи методику исследования и исходные данные." (show_side="left", show_kind="speech")
    hide eveina

    show ai at ai_right
    ai "Запрошенные материалы недоступны." (show_side="right", show_kind="speech")
    hide ai

    n "Эвейна вернулась к результатам. На первой странице не оказалось ничего, чего она ещё не видела." (show_side="none", show_kind="speech")

    show eveina thinking tshirt at eveina_left, sprite_night
    ev_thought "Хм, ладно. Допустим, один запрос ещё ничего не доказывает." (show_side="left", show_kind="thought")
    hide eveina

    n "Она закрыла базу, на браслете тут же отобразился обратный отсчёт." (show_side="none", show_kind="speech")

    show eveina upset thinking tshirt at eveina_left, sprite_night
    ev_thought "Двести тридцать один день до момента, когда болезнь лишит меня отца." (show_side="left", show_kind="thought")
    ev_thought "А пока Академия предлагает мне те же аннотации, ради которых не требовалось лететь на другую планету." (show_side="left", show_kind="thought")
    hide eveina

    show eveina normal tshirt at eveina_left, sprite_night
    ev_thought "Утром узнаю, что они всё-таки готовы мне показать." (show_side="left", show_kind="thought")
    hide eveina

    n "Эвейна натянула одеяло и закрыла глаза." (show_side="none", show_kind="speech")
    n "Она повторяла про себя пункты утреннего поиска, пока слова не перестали складываться в осмысленные фразы." (show_side="none", show_kind="speech")
    n "Мысли закручивались всё медленней, растекаясь в бесформенных образах. И девушка провалилась в сон." (show_side="none", show_kind="speech")

    # =========================================================
    # СОН — голосовой шум
    # =========================================================
    # play sound "sfx/dream_overlap.ogg"
    call fade_to_black(1.2, 0.8)
    scene bg scene 1_6 dream 1 at bg_fullscreen with dissolve

    n "Сначала был шум. Голоса накладывались друг на друга, фразы путались, теряли смысл, превращались в поток, в котором всё чужое и одновременно близкое." (show_side="none", show_kind="speech")

    scene bg scene 1_6 dream 2 at bg_fullscreen with dissolve

    #show sairen angry at sairen_right
    unknown "Это она? Та, что с периферии..." (show_side="right", show_kind="speech")
    #hide sairen

    scene bg scene 1_6 dream 3 at bg_fullscreen with dissolve

    #show tero smile at tero_right
    unknown "Да вы ж её живьём сожрёте..." (show_side="right", show_kind="speech")
    #hide tero

    scene bg scene 1_6 dream 4 at bg_fullscreen with dissolve

    #show leya sad at leya_right
    unknown "Ты не одна." (show_side="right", show_kind="speech")
    #hide leya

    scene bg scene 1_6 dream 5 at bg_fullscreen with dissolve

    #show virt serious at virt_right
    unknown "Что вы знаете об этой планете, мисс Хейла?" (show_side="right", show_kind="speech")
    #hide virt

    scene bg scene 1_6 dream 6 at bg_fullscreen with dissolve

    #show noa sad at rian_right
    no "Это Академия или тюрьма?" (show_side="right", show_kind="speech")
    #hide noa

    scene bg scene 1_6 dream 7 at bg_fullscreen with dissolve

    #show eveina upset thinking at eveina_left
    ev "Двести тридцать один день." (show_side="left", show_kind="speech")
    #hide eveina

    scene bg scene 1_6 dream 8 at bg_fullscreen with dissolve
    pause (1.0)
    n "Лица размытые, голоса приглушённые, в них не было ни пола, ни возраста. Картинки сменяли друг друга, как обрывки чужих, давно забытых воспоминаний." (show_side="none", show_kind="speech")

    scene bg scene 1_6 dream 9 at bg_fullscreen with dissolve
    pause (1.0)
    n "Эвейна кричала что-то, но не могла вспомнить ни слов, ни причины." (show_side="none", show_kind="speech")

    scene bg scene 1_6 dream 10 at bg_fullscreen with dissolve
    pause (1.0)

    n "Что-то схватило её за запястье." (show_side="none", show_kind="speech")
    n "Эвейна вырывалась, пока хватало сил. Потом — пока оставался страх." (show_side="none", show_kind="speech")

    scene bg scene 1_6 dream 11 at bg_fullscreen with dissolve
    pause (1.0)
    n "Опора исчезла из-под ног. Голоса смолкли один за другим." (show_side="none", show_kind="speech")
    n "В пустоте, куда она провалилась, остался только далёкий шёпот." (show_side="none", show_kind="speech")

    call fade_to_black(1.0, 0.8)

    un_offscreen "Кто т... Эвейна? Поче... здесь?" (show_side="none", show_kind="speech")

    n "Голос дёрнул её обратно." (show_side="none", show_kind="speech")
    n "Эвейна вскинула руки — и ладони ударились о влажную траву." (show_side="none", show_kind="speech")

    # =========================================================
    # ПРОБУЖДЕНИЕ В САДУ — продолжение (перенесено из scene_2_1)
    # =========================================================

    scene bg scene 0 awakeness 2 at bg_fullscreen with dissolve
    # play music "bgm/morning_mist.ogg" fadein 2.0

    #show eveina wondered at eveina_left
    ev_thought "Ка... какого, блять, чёрта?" (show_side="left", show_kind="thought")
    #hide eveina

    n "Над головой — не потолок комнаты. Только бездонное небо, освещённое светом голубой звезды." (show_side="none", show_kind="speech")
    n "Ладони тонули в прохладной, влажной траве. Рядом стояло одинокое дерево, то самое, у которого начиналась граница купола." (show_side="none", show_kind="speech")
    n "Ещё вечером сад казался самым спокойным местом в Академии. Теперь знакомый пейзаж делал невозможное до обидного реальным." (show_side="none", show_kind="speech")

    #show eveina wondered at eveina_left
    ev_thought "Как я здесь оказалась?" (show_side="left", show_kind="thought")
    #hide eveina

    scene bg scene 0 awakeness 3 at bg_fullscreen with dissolve

    n "Эвейна медленно села. Сон отпустил сознание, но не тело." (show_side="none", show_kind="speech")
    n "Сердце то срывалось в частый стук, то пропускало удар." (show_side="none", show_kind="speech")

    #show eveina wondered at eveina_left
    ev_thought "Ауч..." (show_side="left", show_kind="thought")
    #hide eveina

    scene bg scene 0 awakeness 4 at bg_fullscreen with dissolve

    n "Она опустила глаза — на руке след, похожий на синяк от захвата. Красноватый, чёткий. Реальный." (show_side="none", show_kind="speech")
    n "Машинальным движением дотронулась до него — и пальцы замерли. Сердце лихорадочно набирало ритм." (show_side="none", show_kind="speech")

    #show eveina eyebrow at eveina_left
    ev_thought "Мне это не приснилось." (show_side="left", show_kind="thought")
    #hide eveina

    n "Только сейчас она почувствовала, как футболка насквозь пропиталась росой, а холодная ткань липла к коже." (show_side="none", show_kind="speech")
    n "Зубы стучали. Тело колотило мелкой, противной дрожью — той, которую невозможно остановить усилием воли." (show_side="none", show_kind="speech")

    scene bg scene 0 awakeness 6 at bg_fullscreen with dissolve

    #show eveina thinking at eveina_left
    ev_thought "Со мной вроде кто-то говорил во сне... Голос. Чей-то голос." (show_side="left", show_kind="thought")
    ev_thought "Кто это был? Что он сказал?" (show_side="left", show_kind="thought")
    #hide eveina

    scene bg scene 0 awakeness 5 at bg_fullscreen with dissolve

    #show eveina angry at eveina_left
    ev_thought "И как, чёрт возьми, я оказалась в саду?" (show_side="left", show_kind="thought")
    #hide eveina

    scene bg scene 0 awakeness 7 at bg_fullscreen with dissolve

    n "Эвейна медленно встала и поднесла браслет к лицу." (show_side="none", show_kind="speech")

    show eveina normal tshirt at eveina_left, sprite_night
    ev "Покажи историю моих перемещений за эту ночь." (show_side="left", show_kind="speech")
    hide eveina

    show ai at ai_right
    ai "Формирую маршрут." (show_side="right", show_kind="speech")
    hide ai

    n "Над браслетом появилась схема жилого блока и садов Академии." (show_side="none", show_kind="speech")
    n "Светящаяся линия начиналась у комнаты Эвейны, проходила по коридорам и заканчивалась возле дерева." (show_side="none", show_kind="speech")

    show eveina eyebrow tshirt at eveina_left, sprite_night
    ev "На маршруте есть разрывы?" (show_side="left", show_kind="speech")
    hide eveina

    show ai at ai_right
    ai "Нет. Перемещение зафиксировано непрерывно." (show_side="right", show_kind="speech")
    hide ai

    show eveina thinking tshirt at eveina_left, sprite_night
    ev "Скорость?" (show_side="left", show_kind="speech")
    hide eveina

    show ai at ai_right
    ai "Соответствует обычному передвижению пешком." (show_side="right", show_kind="speech")
    hide ai

    n "Эвейна увеличила схему. Никаких скачков, посторонних остановок или отклонений." (show_side="none", show_kind="speech")
    n "Судя по браслету, она сама встала с кровати, вышла из комнаты и дошла до сада." (show_side="none", show_kind="speech")

    show eveina upset thinking tshirt at eveina_left, sprite_night
    ev_thought "И не помню ни секунды." (show_side="left", show_kind="thought")
    hide eveina

    n "В памяти всплыл разговор в холле." (show_side="none", show_kind="speech")

    show eveina upset thinking tshirt at eveina_left, sprite_night
    ev_thought "После того случая месяц назад люди тоже не могли вспомнить, что произошло." (show_side="left", show_kind="thought")
    hide eveina

    show eveina thinking tshirt at eveina_left, sprite_night
    ev_thought "Если это не байка старшекурсников." (show_side="left", show_kind="thought")
    hide eveina

    show eveina eyebrow tshirt at eveina_left, sprite_night
    ev_thought "Что тогда это было? Дурацкое посвящение новичков?" (show_side="left", show_kind="thought")
    hide eveina
    show eveina intrigued tshirt at eveina_left, sprite_night
    ev_thought "Я закатила самую дикую вечеринку для первокурсников, и слегка перебрала?" (show_side="left", show_kind="thought")
    hide eveina
    show eveina surprized tshirt at eveina_left, sprite_night
    ev_thought "Или случайно заснула здесь, а остальное мне приснилось?" (show_side="left", show_kind="thought")
    hide eveina

    n "Но одну мысль она упорно отгоняла с самого пробуждения." (show_side="none", show_kind="speech")

    show eveina thinking tshirt at eveina_left, sprite_night
    ev_thought "Лунатизм. Провал памяти. Дезориентация." (show_side="left", show_kind="thought")
    hide eveina

    n "Последние месяцы Эвейна читала о нарушениях памяти больше, чем ей хотелось бы." (show_side="none", show_kind="speech")
    n "Она помнила, как отец забывал недавние разговоры, путал дни и обнаруживал собственные поступки уже по их последствиям." (show_side="none", show_kind="speech")
    n "Руки, которые только начали согреваться, снова похолодели. На этот раз — изнутри." (show_side="none", show_kind="speech")

    show eveina upset thinking tshirt at eveina_left, sprite_night
    ev_thought "Нет. Один провал ещё ничего не доказывает." (show_side="left", show_kind="thought")
    hide eveina

    n "Она заставила себя вернуться к фактам." (show_side="none", show_kind="speech")

    show eveina thinking tshirt at eveina_left, sprite_night
    ev_thought "Вирт сказал, что неконтролируемое поле вызывает провалы памяти и расстройства восприятия." (show_side="left", show_kind="thought")
    hide eveina

    n "Эвейна посмотрела на дерево. Граница купола проходила всего в нескольких шагах." (show_side="none", show_kind="speech")

    show eveina eyebrow tshirt at eveina_left, sprite_night
    ev_thought "А я проснулась именно здесь." (show_side="left", show_kind="thought")
    hide eveina

    show eveina upset thinking tshirt at eveina_left, sprite_night
    ev "Маршрут пересекал границу купола?" (show_side="left", show_kind="speech")
    hide eveina

    show ai at ai_right
    ai "Нет." (show_side="right", show_kind="speech")
    hide ai

    show eveina eyebrow tshirt at eveina_left, sprite_night
    ev_thought "Значит, либо причина не в поле, либо ночью защита дала сбой." (show_side="left", show_kind="thought")
    hide eveina

    show eveina upset thinking tshirt at eveina_left, sprite_night
    ev_thought "Чертовщина какая-то..." (show_side="left", show_kind="thought")
    hide eveina

    n "Синяк болел, мокрая одежда липла к телу, но всё это можно было принять. Провал памяти — нет." (show_side="none", show_kind="speech")

    scene bg scene 0 awakeness 8 at bg_fullscreen with dissolve

    n "Пальцы впились в собственные плечи. Сердце колотилось так, будто пыталось выбраться из грудной клетки." (show_side="none", show_kind="speech")
    n "Она знала, что один провал ещё ничего не доказывает. Но тело в медицинские доводы не поверило." (show_side="none", show_kind="speech")
    n "Перед глазами возник отец: пауза перед знакомым именем, растерянный взгляд, попытка сделать вид, что ничего не произошло." (show_side="none", show_kind="speech")
    n "Желудок скрутило резко, без предупреждения — будто тело наконец осознало то, что разум пытался до него донести." (show_side="none", show_kind="speech")
    n "Эвейна согнулась, стараясь удержаться на ногах. Горло сжалось, а рот наполнился горькой слюной." (show_side="none", show_kind="speech")

    #show eveina angry at eveina_left
    ev_thought "Нет. Нет, это не то же самое..." (show_side="left", show_kind="thought")
    #hide eveina

    n "Она стиснула зубы. Задержала дыхание. Сосчитала до пяти." (show_side="none", show_kind="speech")
    n "Пальцы, которыми она сжимала плечи, кажется, оставили отметины на коже." (show_side="none", show_kind="speech")

    scene bg scene 0 awakeness 7 at bg_fullscreen with dissolve

    show ai at ai_right
    ai "Зафиксированы повышенная частота сердечных сокращений и снижение температуры тела." (show_side="right", show_kind="speech")
    ai "Передать показатели медицинскому модулю?" (show_side="right", show_kind="speech")
    hide ai

    show eveina worried tshirt at eveina_left, sprite_night
    ev "Что именно ты передашь?" (show_side="left", show_kind="speech")
    hide eveina

    show ai at ai_right
    ai "Показатели и время эпизода. Передача запустит протокол наблюдения за повторными отклонениями. Медицинский осмотр рекомендуется." (show_side="right", show_kind="speech")
    hide ai

    n "Маршрут останется на её браслете. О том, что она не помнит ни минуты ночной прогулки, запись тоже ничего не скажет. Но кто-нибудь обязательно увидит, что с ней произошло {i}что-то{/i}." (show_side="none", show_kind="speech")
    n "Перед Эвейной появились две кнопки." (show_side="none", show_kind="speech")

    show eveina upset thinking tshirt at eveina_left, sprite_night
    $ eveina_shared_medical_data = renpy.call_screen(
        "choice",
        items=[
            ("Передать показатели", True),
            ("Отказаться от передачи", False),
        ],
        what=""
    )
    hide eveina

    if eveina_shared_medical_data:
        show ai at ai_right
        ai "Данные сохранены в медицинском профиле. Протокол наблюдения активирован. Вы можете записаться на осмотр." (show_side="right", show_kind="speech")
        hide ai

        n "Она посмотрела на дрожащие пальцы. Осмотр означал вопросы, на которые у неё пока не было ответов. Но скрытие факта могло обойтись куда дороже. Пусть пока останутся цифры." (show_side="none", show_kind="speech")


    else:
        show ai at ai_right
        ai "Подтвердите отказ от передачи медицинских показателей." (show_side="right", show_kind="speech")
        hide ai

        show eveina normal tshirt at eveina_left, sprite_night
        ev "Подтверждаю." (show_side="left", show_kind="speech")
        hide eveina

        show ai at ai_right
        ai "Передача отменена." (show_side="right", show_kind="speech")
        hide ai

        n "Двести тридцать один день. Она не собиралась тратить их, объясняя чужому врачу, почему проснулась в саду и не помнит дороги туда." (show_side="none", show_kind="speech")


    n "Сначала выяснить, что произошло. Потом решать, кому об этом рассказывать." (show_side="none", show_kind="speech")
    n "Она накрыла синяк ладонью, сделала ещё один вдох и через усилие выпрямилась." (show_side="none", show_kind="speech")

    scene bg scene 0 awakeness 9 at bg_fullscreen with dissolve

    n "Вместо кратчайшего пути к общежитию Эвейна выбрала собственный ночной маршрут." (show_side="none", show_kind="speech")
    n "Пошла по светящейся линии обратно, внимательно осматривая дорогу, которую уже преодолела..." (show_side="none", show_kind="speech")

    call fade_to_black(1.0, 0.8)

    n "...и совершенно не помнила." (show_side="none", show_kind="speech")


    # =========================================================
    # КОНЕЦ ГЛАВЫ 1
    # =========================================================

    call fade_to_black(1.5, 1.0)

    jump kg_end_chapter_1
