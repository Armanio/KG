label scene_6_7:
    $ previous_scene = "scene_6_6"
    $ next_scene = "scene_6_8"
    $ current_scene = "scene_6_7"
    call fade_to_black(1.2, 0.8)
    scene bg lecture_hall at bg_fullscreen

    n "Утром в лекционном зале пахло кофе и чужими ожиданиями. Эвейна сидела в центре амфитеатра, уткнувшись в планшет." (show_side="none", show_kind="speech")
    n "Глаза слегка слипались — но дисциплина держала её вертикально. Пока пальцы листали материалы по курсу, мозг лениво искал смысл между строк." (show_side="none", show_kind="speech")

    show eveina normal at eveina_left
    ev_thought "Утро. Лекция. Новый предмет. Новое лицо." (show_side="left", show_kind="thought")
    hide eveina
    show eveina eyeroll at eveina_left
    ev_thought "Пожалуйста, пусть будет скучная лекция. Хватит с меня экстраординарных личностей." (show_side="left", show_kind="thought")
    hide eveina

    n "В этот момент дверь открылась. Мужчина уверенно прошёл до кафедры, оглядел аудиторию — взглядом, который не искал лица, а ранжировал полезность." (show_side="none", show_kind="speech")

    show kaistr normal at kaistr_right
    kr "Доброе утро. Профессор Лоренс Кайстр." (show_side="right", show_kind="speech")
    kr "Для тех, кто не запомнит — вы всё равно не сдадите мой курс." (show_side="right", show_kind="speech")
    hide kaistr
    show kaistr intrigued at kaistr_right
    kr "Ноа. Теро. Рад видеть знакомые лица." (show_side="right", show_kind="speech")
    kr "Как поживают ваши семьи?" (show_side="right", show_kind="speech")
    hide kaistr

    n "Оба парня замерли от удивления, не ожидая к себе такого внимания." (show_side="none", show_kind="speech")

    show noa normal at noa_right
    no "Здравствуйте, профессор. Всё хорошо." (show_side="right", show_kind="speech")
    hide noa   

    show tero normal at noa_right
    te "Живее всех живых, профессор." (show_side="right", show_kind="speech")
    hide tero   

    n "Некоторые студенты зашептались — уж слишком внятный сигнал подал Кайстр: он из «тех кругов»." (show_side="none", show_kind="speech")

    show kaistr intrigued at kaistr_right
    kr "Сайлас, и ты здесь. Давно тебя не видел." (show_side="right", show_kind="speech")
    hide kaistr

    show silas normal at silas_right
    si "Доброе утро, профессор. Я был в отъезде." (show_side="right", show_kind="speech")
    hide silas

    n "Кайстр кивнул, будто поставил галочку в списке дел, и продолжил." (show_side="none", show_kind="speech")

    show kaistr normal at kaistr_right
    kr "Я здесь, чтобы провести для вас курс — «Когнитивные конфликты и социальное поведение»." (show_side="right", show_kind="speech")
    kr "В народе — «Как управлять толпой, не пачкая рук»." (show_side="right", show_kind="speech")
    hide kaistr

    n "По залу прошёл легкий смешок, в ответ на который Лоренс удовлетворенно хмыкнул, видимо, довольный произведённым эффектом." (show_side="none", show_kind="speech")
    n "Он начал лекцию, не открывая планшета и не включая проекционный экран, будто всё, что ему нужно — уже было в его голове. И он собирался поместить это во все остальные головы в лектории без посредников." (show_side="none", show_kind="speech")
    n "Прохаживаясь перед аудиторией, профессор говорил уверенно, убедительно и... уж слишком красиво." (show_side="none", show_kind="speech")


    show kaistr normal at kaistr_right
    kr "Согласно теории Мелис-Сандерс, устойчивое поведенческое моделирование возможно на основе доверительной эмпатии и прецедентной памяти." (show_side="right", show_kind="speech")
    kr "Её цитата: {i}«Создание эмоционального зеркала усиливает способность к когнитивной коррекции»{/i}." (show_side="right", show_kind="speech")
    hide kaistr

    n "Он остановился, сделал паузу. И посмотрел в зал с такой улыбкой, будто сейчас расскажет отличную шутку." (show_side="none", show_kind="speech")

    show kaistr normal at kaistr_right
    kr "Интересный подход. Особенно если учесть, что он работает..." (show_side="right", show_kind="speech")
    kr "На выборочных группах. При условии отсутствия внешнего давления." (show_side="right", show_kind="speech")
    kr "И только если участник находится в состоянии полного доверия." (show_side="right", show_kind="speech")
    hide kaistr
    show kaistr intrigued at kaistr_right
    kr "Забавно, как часто в психологию идут те, кому не хватило баллов на нейрофизику." (show_side="right", show_kind="speech")
    kr "Особенно представительницы прекрасного пола." (show_side="right", show_kind="speech")
    hide kaistr
    show kaistr normal at kaistr_right
    kr "Профессор Мелис... исключение, конечно же." (show_side="right", show_kind="speech")
    hide kaistr

    n "Он учтиво кивнул — не невидимому профессору, а самой идее того, что женщину можно считать исключением." (show_side="none", show_kind="speech")
    n "И с легкостью в голосе продолжил, как будто только что не уронил в зал весь груз патриархального превосходства." (show_side="none", show_kind="speech")
    n "Кто-то из студентов сразу понял, что он только что унизил коллегу. Но большинство просто ловили интонации." (show_side="none", show_kind="speech")
    n "Эвейна поморщилась, но промолчала." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev_thought "Пожалуй, незаметность — тут лучшая тактика. За права женщин поборюсь у себя в комнате." (show_side="left", show_kind="thought")
    hide eveina

    n "Интерес к лекции пропал окончательно. Эвейна блуждала в своих мыслях, не задерживая внимания на словах профессора." (show_side="none", show_kind="speech")
    n "Спустя ещё десять минут она внезапно зевнула. Беззвучно и почти незаметно. Но к несчастью девушки, не для него." (show_side="none", show_kind="speech")
    n "Кайстр замолчал на полуслове, посмотрел поверх аудитории. Его цепкий взгляд задержался на Эвейне." (show_side="none", show_kind="speech")

    show kaistr normal at kaistr_right
    kr "Статистика, увы, подтверждается: при одинаковом уровне стресса женщины усваивают материал медленнее." (show_side="right", show_kind="speech")
    kr "Видимо, природа решила, что им полезнее сохранять ресурсы… для других задач." (show_side="right", show_kind="speech")
    hide kaistr
    show kaistr intrigued at kaistr_right
    kr "Ну, вы понимаете." (show_side="right", show_kind="speech")
    hide kaistr

    n "За спиной у Эвейны какой-то недалёкий ехидно захихикал, очевидно, спутав себя с гиеной. Другой студент шикнул на хихикающего, когда Эвейна медленно поднялась с своего места." (show_side="none", show_kind="speech")
    n "Её лицо налилось краской, а ладони сжались в кулаки, будто она собралась отстаивать честь всех женщин на ринге, но голос оставался чётким." (show_side="none", show_kind="speech")

    show eveina angry at eveina_left
    ev "Конечно. Природа." (show_side="left", show_kind="speech")
    hide eveina
    show eveina annoyed at eveina_left
    ev "Она же как раз помогла Марии Кюри открыть радиоактивность." (show_side="left", show_kind="speech")
    ev "Гипатии — рассчитать планетарные движения." (show_side="left", show_kind="speech")
    ev "Джейн Гудолл — переписать представления о приматах." (show_side="left", show_kind="speech")
    ev "Ну и ещё с десяток «неадаптированных» дамочек могу вспомнить, если хотите." (show_side="left", show_kind="speech")
    ev "Но да, конечно. Лучше сослаться на эволюцию." (show_side="left", show_kind="speech")
    ev "Особенно, когда другие доводы не выдерживают критики." (show_side="left", show_kind="speech")
    hide eveina
    show eveina angry at eveina_left
    ev "Ну, вы понимаете." (show_side="left", show_kind="speech")
    hide eveina
    show eveina thinking at eveina_left
    ev_thought "Я сейчас что, зевающую себя с Гипатией сравнила? Неплохо." (show_side="left", show_kind="thought")
    hide eveina

    n "В зале повисло хрустящее молчание, все замерли в ожидании. Кайстр слегка прищурился и наклонил голову, глядя на неё, как на муху, попавшую в его суп." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev_thought "А сейчас полетят камни..." (show_side="left", show_kind="thought")
    hide eveina

    show kaistr normal at kaistr_right
    kr "Напомните своё имя, мисс...?" (show_side="right", show_kind="speech")
    hide kaistr

    show eveina normal at eveina_left
    ev "Мисс Хейла, профессор." (show_side="left", show_kind="speech")
    hide eveina

    n "На мгновение брови Кайстра сошлись на переносице, а изучающий взгляд пробежался по хрупкой фигурке и вернулся к её лицу." (show_side="none", show_kind="speech")

    show kaistr annoyed at kaistr_right
    kr "Мисс Хейла, значит..." (show_side="right", show_kind="speech")
    hide kaistr
    show kaistr normal at kaistr_right
    kr "Что ж, мисс Хейла, агрессивная реакция на критику — тоже часть статистики." (show_side="right", show_kind="speech")
    hide kaistr
    show kaistr intrigued at kaistr_right
    kr "Особенно у тех, кто всё ещё воспринимает интеллект как вызов, а не как инструмент." (show_side="right", show_kind="speech")
    hide kaistr

    n "Профессор отвернулся от неё, давая понять, что этот диалог окончен." (show_side="none", show_kind="speech")
    n "Именно так: не проиграл спор, а перестал в нём участвовать. Погрузился обратно в лекцию, как будто этот диалог не имел значения." (show_side="none", show_kind="speech")

    show eveina normal at eveina_left
    ev_thought "Ну вот и познакомились.\nПрофессор «Превосходство»." (show_side="left", show_kind="thought")
    ev_thought "Верит в мужчин. Входить в элиту. Терпеть не может, когда ему дерзят." (show_side="left", show_kind="thought")
    hide eveina

    n "К концу лекции он снова вернулся к тону наставника." (show_side="none", show_kind="speech")

    show kaistr normal at kaistr_right
    kr "Напоследок хочу лишь проговорить очевидное: связи — это не коррупция. Это капитал." (show_side="right", show_kind="speech")
    kr "Умеете дружить с нужными людьми — и ваши идеи услышат." (show_side="right", show_kind="speech")
    kr "Не умеете — станете очередным исследователем, чьи работы пылятся в архивах." (show_side="right", show_kind="speech")
    hide kaistr

    n "Некоторые зааплодировали. И правда — он был харизматичен. Говорил красиво, звучал, как будто точно знает, что делать, чтобы завоевать признание публики." (show_side="none", show_kind="speech")
    n "Эвейна фыркнула, смахивая планшет в режим ожидания, и поспешила к выходу." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev_thought "Мир, где связи важнее сути.\nГде тебе ежедневно вежливо объясняют, что ты ошибка." (show_side="left", show_kind="thought")
    ev_thought "Добро пожаловать в Академию Мемории." (show_side="left", show_kind="thought")
    hide eveina

    jump scene_6_8
