default virt_conversation_approach = None

label scene_2_8:
    $ previous_scene = "scene_2_7"
    $ next_scene = "scene_2_9"
    $ current_scene = "scene_2_8"
    $ kg_prepare_scene("scene_2_8")


    # =========================================================
    # СЦЕНА 8 — «КАБИНЕТ ВИРТА»
    # Структура: уведомление на браслет → кабинет → Вирт замечает
    #            → Эвейна почти спрашивает о Далоне → не может
    #            → отказ от помощи → чувство вины → коридор
    # По настроению и диалогу — близко к оригинальной scene_2_8
    # Ключевое: украденная книга в холле, Вирт не глуп, он запоминает
    # Эмоция: двойственность — тепло доверия и холод лжи одновременно
    # =========================================================

    call fade_to_black(1.2, 0.8)
    scene bg virt cabinet corridor night at bg_fullscreen with dissolve
    # play music "bgm/quiet_reflection.ogg" fadein 2.0

    n "По дороге к кабинету Вирта Эвейна оставила книгу в холле — затолкнула между спинкой дальнего дивана и стеной." (show_side="none", show_kind="speech")
    n "Прятать украденный архивный том в общественном месте было глупо. Входить с ним в кабинет декана казалось ещё глупее." (show_side="none", show_kind="speech")
    n "Теперь Эвейна стояла у двери в кабинет, не решаясь постучать." (show_side="none", show_kind="speech")


    show eveina upset thinking at eveina_left, sprite_night_mixed
    ev_thought "Десять минут от кражи до вызова к декану." (show_side="left", show_kind="thought")
    hide eveina
    show eveina annoyed at eveina_left, sprite_night_mixed
    ev_thought "Очень убедительное совпадение." (show_side="left", show_kind="thought")
    hide eveina
    show eveina thinking at eveina_left, sprite_night_mixed
    ev_thought "А вдруг в архиве есть какая-то защита?" (show_side="left", show_kind="thought")
    hide eveina
    show eveina upset at eveina_left, sprite_night_mixed
    ev_thought "Камеры? Сигнализация? Робот-архивариус – стукач?" (show_side="left", show_kind="thought")
    hide eveina

    n "Дверь, как и положено двери декана, от комментариев воздержалась." (show_side="none", show_kind="speech")

    show eveina eyeroll at eveina_left, sprite_night_mixed
    ev_thought "Наверно, стоило ответить на эти вопросы, прежде чем нарушать правила." (show_side="left", show_kind="thought")
    hide eveina
    show eveina worried at eveina_left, sprite_night_mixed
    ev_thought "Ладно, не будь трусихой, Эвейна. Просто пойди и выясни." (show_side="left", show_kind="thought")
    hide eveina

    if eveina_shared_medical_data:
        n "Браслет коротко завибрировал." (show_side="none", show_kind="speech")

        show ai at ai_right
        ai "Зафиксировано повторное повышение частоты сердечных сокращений. Данные переданы в медицинский профиль согласно протоколу наблюдения." (show_side="right", show_kind="speech")
        hide ai

        show eveina angry at eveina_left, sprite_night_mixed
        ev "Ты не ИИ, ты – чёртов стукач!" (show_side="left", show_kind="speech")
        hide eveina

    n "Девушка дотронулась до двери и та согласно зашелестела." (show_side="none", show_kind="speech")

    # --- Кабинет Вирта ---

    call fade_to_black(1.2, 0.8)
    scene bg virt cabinet night at bg_fullscreen with dissolve
    # play music "bgm/interview_theme.ogg" fadein 1.5

    n "Вирт сидел за столом, но при её появлении неспешно поднялся." (show_side="none", show_kind="speech")

    show virt normal at virt_right, sprite_warm
    vi "Рад, что вы нашли время." (show_side="right", show_kind="speech")
    hide virt

    show eveina eyeroll at eveina_left, sprite_warm
    ev_thought "Будто вы оставили мне выбор, профессор." (show_side="left", show_kind="thought")
    hide eveina

    show virt normal at virt_right, sprite_warm
    vi "Прошу, присаживайтесь." (show_side="right", show_kind="speech")
    hide virt

    n "Он жестом указал на кресло напротив и снова опустился в своё. Эвейна села, не выпуская его из виду." (show_side="none", show_kind="speech")
    n "Несколько секунд профессор просто смотрел на неё — без осуждения, без спешки. Словно раздумывая, как начать непростой диалог." (show_side="none", show_kind="speech")

    show eveina worried at eveina_left, sprite_warm
    ev_thought "Это молчание нервирует ещё больше." (show_side="left", show_kind="thought")
    hide eveina

    show virt serious at virt_right, sprite_warm
    vi "Я наблюдал за вашей работой. Вы изматываете себя." (show_side="right", show_kind="speech")
    hide virt

    show eveina eyebrow at eveina_left, sprite_warm
    ev "Наблюдали?" (show_side="left", show_kind="speech")
    hide eveina

    n "Она не стала оправдываться. Вирт едва заметно приподнял бровь." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left, sprite_warm
    ev "Насколько внимательно?" (show_side="left", show_kind="speech")
    hide eveina

    show virt thinking at virt_right, sprite_warm
    vi "Достаточно, чтобы заметить: программой курса ваши интересы не ограничиваются." (show_side="right", show_kind="speech")
    hide virt

    show virt serious at virt_right, sprite_warm
    vi "Вы проводите в архиве почти всё свободное время." (show_side="right", show_kind="speech")
    vi "Такой темп редко заканчивается чем-нибудь полезным." (show_side="right", show_kind="speech")
    hide virt

    show eveina annoyed at eveina_left, sprite_warm
    ev_thought "Он ответил, что заметил. Не ответил — как." (show_side="left", show_kind="thought")
    hide eveina

    show eveina normal at eveina_left, sprite_warm
    ev "Я пытаюсь наверстать пробелы." (show_side="left", show_kind="speech")
    hide eveina

    show virt normal at virt_right, sprite_warm
    vi "Для этого не обязательно доводить себя до истощения." (show_side="right", show_kind="speech")
    hide virt

    show virt eyebrow at virt_right, sprite_warm
    vi "Тем более если вы ищете что-то конкретное." (show_side="right", show_kind="speech")
    hide virt

    n "Эвейна дёрнула плечом, мысленно поблагодарив себя, что книга сейчас не с ней. К сожалению, вопросы от этого никуда не делись." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left, sprite_warm
    ev "В старых материалах встречаются проекты, которых нет в общей базе." (show_side="left", show_kind="speech")
    hide eveina

    show virt serious at virt_right, sprite_warm
    vi "Некоторые исследования закрыты для общего доступа." (show_side="right", show_kind="speech")
    vi "Часть записей всё ещё восстанавливают после недавнего технического сбоя." (show_side="right", show_kind="speech")
    hide virt

    show eveina eyebrow at eveina_left, sprite_warm
    ev "Вместе с именами исследователей?" (show_side="left", show_kind="speech")
    hide eveina

    n "Вирт посмотрел на неё внимательнее." (show_side="none", show_kind="speech")

    show virt thinking at virt_right, sprite_warm
    vi "Если речь идёт о конкретном проекте, назовите его." (show_side="right", show_kind="speech")
    hide virt

    show virt normal at virt_right, sprite_warm
    vi "Я выясню, сохранились ли материалы, и помогу оформить доступ." (show_side="right", show_kind="speech")
    hide virt

    n "Вот оно. Эвейне оставалось только произнести два слова." (show_side="none", show_kind="speech")
    n "Кайр Далон." (show_side="none", show_kind="speech")

    show eveina upset thinking at eveina_left, sprite_warm
    ev_thought "И тогда он узнает, что я нашла имя, которое кто-то старательно вычистил из базы." (show_side="left", show_kind="thought")
    hide eveina
    show eveina thinking at eveina_left, sprite_warm
    ev_thought "Если это случайность — он поможет." (show_side="left", show_kind="thought")
    ev_thought "Если нет — я сама предупрежу того, кто хотел его спрятать." (show_side="left", show_kind="thought")
    hide eveina

    n "Вирт ждал. Спокойно, без нажима." (show_side="none", show_kind="speech")
    n "Именно поэтому довериться ему хотелось особенно сильно." (show_side="none", show_kind="speech")

    show virt normal at virt_right, sprite_warm
    vi "В чём бы ни была ваша цель, я могу быть полезен." (show_side="right", show_kind="speech")
    hide virt
    show virt eyebrow at virt_right, sprite_warm
    vi "В конце концов, я ваш наставник. К кому ещё вам обращаться?" (show_side="right", show_kind="speech")
    hide virt

    n "Эвейна вспомнила его разговор с мужчиной в лектории. Вирт сам вызвался стать её наставником — и тогда не объяснил почему." (show_side="none", show_kind="speech")
    n "Сейчас он претендовал на доверие, но заслуживал ли его — Эвейна не знала." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left, sprite_warm
    $ virt_conversation_approach = renpy.call_screen(
        "choice",
        items=[
            ("Рассказать, почему её поиски важны", "personal"),
            ("Спросить, почему он выбрал её", "counterquestion"),
        ],
        what=""
    )
    hide eveina
    if virt_conversation_approach == "personal":
        show eveina normal at eveina_left, sprite_warm
        ev "Я изучаю нейродегенеративные заболевания. Это не случайно." (show_side="left", show_kind="speech")
        ev "Болезнь отца стала одной из причин, по которым я поступила в Академию." (show_side="left", show_kind="speech")
        hide eveina

        n "Вирт не перебил. Его взгляд задержался на ней чуть дольше." (show_side="none", show_kind="speech")

        show virt thinking at virt_right, sprite_warm
        vi "Теперь понимаю, почему вы проводите столько времени в архиве." (show_side="right", show_kind="speech")
        hide virt

        show eveina normal at eveina_left, sprite_warm
        ev "Но конкретных исследований я пока не нашла." (show_side="left", show_kind="speech")
        hide eveina

        n "Она не назвала ни проект, ни имя. И всё же несколько честных фраз оставили после себя ощущение незапертой двери." (show_side="none", show_kind="speech")
        n "Вирт провёл рукой по волосам, убирая их с лица." (show_side="none", show_kind="speech")

        show virt upset thinking at virt_right, sprite_warm
        vi "Не стану просить вас бросить поиски." (show_side="right", show_kind="speech")
        hide virt
        show virt normal at virt_right, sprite_warm
        vi "Но доводить себя до изнеможения необязательно." (show_side="right", show_kind="speech")
        hide virt

    else:
        show eveina normal at eveina_left, sprite_warm
        ev "Спасибо. Возможно, ваша помощь мне пригодится." (show_side="left", show_kind="speech")
        hide eveina
        show eveina eyebrow at eveina_left, sprite_warm
        ev "Только я всё ещё не понимаю: почему моим наставником стали вы?" (show_side="left", show_kind="speech")
        hide eveina

        n "Казалось, профессор на секунду потерял нить разговора. Он потёр пальцами переносицу, прежде чем снова взглянуть на девушку." (show_side="none", show_kind="speech")

        show virt normal at virt_right, sprite_warm
        vi "Вы способная студентка. Я подумал, что мне будет интересно с вами работать." (show_side="right", show_kind="speech")
        hide virt

        show eveina eyebrow at eveina_left, sprite_warm
        ev "Настолько способная, что смогла заинтересовать декана?" (show_side="left", show_kind="speech")
        hide eveina

        n "Вирт чуть улыбнулся." (show_side="none", show_kind="speech")

        show virt smile at virt_right, sprite_warm
        vi "Как видите." (show_side="right", show_kind="speech")
        hide virt

        n "Ответ был вежливым и совершенно неполным. Эвейна уже собиралась спросить ещё раз, но он заговорил первым." (show_side="none", show_kind="speech")

        show virt normal at virt_right, sprite_warm
        vi "Именно поэтому я прошу вас не доводить себя до истощения." (show_side="right", show_kind="speech")
        hide virt

        n "Больше вопросов он не задавал. Разговор вернулся на безопасную территорию, где оба хранили свои тайны и делали вид, что это доверие." (show_side="none", show_kind="speech")

    show virt normal at virt_right, sprite_warm
    vi "Если понадобится помощь, приходите. Желательно до того, как любознательность окончательно лишит вас сна." (show_side="right", show_kind="speech")
    hide virt

    show eveina normal at eveina_left, sprite_warm
    ev "Спасибо, профессор." (show_side="left", show_kind="speech")
    hide eveina

    n "Она вышла из кабинета. Книга осталась ждать её в холле." (show_side="none", show_kind="speech")

    # =========================================================
    # СМЕНА ТОЧКИ ЗРЕНИЯ — ВИРТ
    # =========================================================

    call fade_to_black(1.2, 0.8)
    scene bg scene 2_8 virt alone 1 at bg_fullscreen with dissolve
    pause (1.0)

    n "Вирт долго смотрел на дверь, за которой она скрылась. Потом опустил взгляд на планшет." (show_side="none", show_kind="speech")

    scene bg scene 2_8 virt alone 2 at bg_fullscreen with dissolve
    pause (1.0)

    n "На экране — уведомление из архива, которое он так и не закрыл." (show_side="none", show_kind="speech")

    n "{i}«Том №АМ-0247 «История исследований планеты Иннаки, т. I» покинул помещение Архива. Дата и время выдачи не зафиксированы.»{/i}" (show_side="none", show_kind="speech")

    if eveina_shared_medical_data:
        n "В углу экрана мигала ещё одна отметка — обновление медицинского профиля Эвейны." (show_side="none", show_kind="speech")
        n "Вирт открыл запись. Два эпизода за последние сутки: ночной и совсем недавний — прямо перед её появлением." (show_side="none", show_kind="speech")

        #show virt thinking at virt_right
        vi "И осмотр ты, разумеется, не назначила." (show_side="right", show_kind="speech")
        #hide virt

        n "Он закрыл медицинскую запись не сразу." (show_side="none", show_kind="speech")

    #show virt thinking at virt_right
    vi "..." (show_side="right", show_kind="speech")
    #hide virt

    n "Палец медленно проскользил по экрану." (show_side="none", show_kind="speech")

    if virt_conversation_approach == "counterquestion":
        #show virt serious at virt_right
        vi "Что же ты там так ищешь, Эвейна Хейла?" (show_side="right", show_kind="speech")
        #hide virt
        #show virt thinking at virt_right
        vi "Зачем ты её взяла?" (show_side="right", show_kind="speech")
        #hide virt
        #show virt normal at virt_right
        vi "Почему решила, что мне об этом знать не следует?" (show_side="right", show_kind="speech")
        #hide virt
    else:
        #show virt serious at virt_right
        vi "Что ты надеялась найти в этой книге для своего отца?" (show_side="right", show_kind="speech")
        #hide virt
        #show virt thinking at virt_right
        vi "Зачем ты её взяла?" (show_side="right", show_kind="speech")
        #hide virt

    n "Вирт потёр переносицу и закрыл уведомление." (show_side="none", show_kind="speech")
    n "Под ним осталось открыто личное дело Эвейны." (show_side="none", show_kind="speech")
    n "Он пролистал анкету, результаты вступительных экзаменов и открыл один из приложенных файлов." (show_side="none", show_kind="speech")

    scene bg scene 2_8 virt alone 3 at bg_fullscreen with dissolve
    pause (1.0)

    #show virt normal at virt_right
    vi "И как ты с ним связана?" (show_side="right", show_kind="speech")
    #hide virt

    jump scene_2_9
