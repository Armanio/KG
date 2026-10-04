label scene_6_5:
    $ previous_scene = "scene_6_4"
    $ next_scene = "scene_6_6"
    $ current_scene = "scene_6_5"
    call fade_to_black(1.2, 0.8)
    scene bg corridor_3 at bg_fullscreen with dissolve

    n "Эвейна шла медленно. Без сил, без злости — лишь с неприятной пустотой внутри, будто из неё вытащили стержень." (show_side="none", show_kind="speech")
    n "На ходу набрала Лее: \n\n{i}«Ты где?»{/i}" (show_side="none", show_kind="speech")
    n "Ответ пришёл быстро: \n\n{i}«В архиве, скоро буду. Ты как?»{/i}" (show_side="none", show_kind="speech")

    show eveina sad at eveina_left
    ev_thought "Как? Как статистический выброс с кругами под глазами." (show_side="left", show_kind="thought")
    hide eveina

    n "Сообщение осталось без ответа. Эвейна свернула мессенджер и направилась в комнату. Сзади послышался чей-то быстрый шаг, а потом с ней поравнялся Сайлас, заглядывая ей в глаза." (show_side="none", show_kind="speech")

    show silas eyebrow at silas_right
    si "Ты в порядке? Не хочу лезть не в своё дело, но на тебе буквально лица нет." (show_side="right", show_kind="speech")
    hide silas 

    show eveina sad at eveina_left
    ev "Не бери в голову. Обычный день с Каэлем. У меня с ним сложные отношения." (show_side="left", show_kind="speech")
    hide eveina

    n "Сайлас понимающе улыбнулся." (show_side="none", show_kind="speech")

    show silas normal at silas_right
    si "Это не у тебя, это у Каэля со всеми сложные отношения." (show_side="right", show_kind="speech")
    hide silas 

    show eveina eyeroll at eveina_left
    ev_thought "Да что ты говоришь..." (show_side="left", show_kind="thought")
    hide eveina
    show eveina annoyed at eveina_left
    ev "Хочешь сказать, тебя он тоже выгонял с практики за правильные решения?" (show_side="left", show_kind="speech")
    ev "Или говорил, что переоценил твои способности и ты ни на что не годишься?" (show_side="left", show_kind="speech")
    ev_thought "Или лез с поцелуями на отработке?" (show_side="left", show_kind="thought")
    hide eveina

    n "Последняя фраза чуть не сорвалась с языка, но Эвейна поспешно его прикусила, поморщившись от боли." (show_side="none", show_kind="speech")

    show silas normal at silas_right
    si "Ну... такого не было, признаю." (show_side="right", show_kind="speech")
    hide silas 

    show eveina annoyed at eveina_left
    ev_thought "То-то же!" (show_side="left", show_kind="thought")
    hide eveina

    show silas normal at silas_right
    si "Но к каждому он цепляется по-своему." (show_side="right", show_kind="speech")
    si "Меня, например, игнорирует с первого дня, что я здесь нахожусь." (show_side="right", show_kind="speech")
    si "Считает, что я здесь не для того, чтобы учиться, а поэтому и времени на меня тратить не нужно." (show_side="right", show_kind="speech")
    hide silas 

    show eveina thinking at eveina_left
    ev_thought "Ладно, это тоже звучит неприятно." (show_side="left", show_kind="thought")
    hide eveina
    show eveina normal at eveina_left
    ev "И зачем же ты здесь, если не для того, чтобы учиться?" (show_side="left", show_kind="speech")
    hide eveina

    show silas smile at silas_right
    si "Ты про реальную причину? Или про то, что выдумал себе Каэль?" (show_side="right", show_kind="speech")
    hide silas 

    show eveina normal at eveina_left
    ev "Второе." (show_side="left", show_kind="speech")
    hide eveina

    show silas normal at silas_right
    si "Он считает, что я тут только для того, чтобы отсидеть четыре года, получить диплом и вместе с ним - место в корпорации, принадлежащей моим родителям." (show_side="right", show_kind="speech")
    hide silas 

    show eveina eyeroll at eveina_left
    ev "Понятно." (show_side="left", show_kind="speech")
    hide eveina

    show silas smile at silas_right
    si "Про первое не спросишь?" (show_side="right", show_kind="speech")
    hide silas 

    show eveina eyebrow at eveina_left
    ev "Первое? Ты про реальную причину?" (show_side="left", show_kind="speech")
    hide eveina
    show eveina thinking at eveina_left
    ev "Я ж не Каэль, чтобы вытряхивать из тебя твою душу и разбирать её по винтикам." (show_side="left", show_kind="speech")
    hide eveina

    show silas smile at silas_right
    si "С тобой я готов поделиться бесплатно." (show_side="right", show_kind="speech")
    hide silas 

    n "Сайлас растянулся в улыбке, слегка толкая её плечом. Заставляя и губы Эвейны дрогнуть." (show_side="none", show_kind="speech")

    show eveina intrigued at eveina_left
    ev "Ну раз бесплатно..." (show_side="left", show_kind="speech")
    ev "И зачем ты поступил сюда, Сайлас?" (show_side="left", show_kind="speech")
    hide eveina

    show silas normal at silas_right
    si "Я хочу сделать этот мир лучше, Эвейна." (show_side="right", show_kind="speech")
    hide silas 

    show eveina eyebrow at eveina_left
    ev "Вот так просто?" (show_side="left", show_kind="speech")
    hide eveina

    show silas normal at silas_right
    si "Ну, не сказал бы, что это просто..." (show_side="right", show_kind="speech")
    si "Но у семьи Вайсов есть возможности, а у меня — желание." (show_side="right", show_kind="speech")
    si "Так что да, я планирую изменить этот мир к лучшему, чего бы мне это не стоило." (show_side="right", show_kind="speech")
    hide silas 

    show eveina wondered at eveina_left
    ev_thought "Семья Вайсов? Владельцы Вайскорп?" (show_side="left", show_kind="thought")
    ev_thought "Чёрт, и как я раньше не..." (show_side="left", show_kind="thought")
    hide eveina
    show eveina thinking at eveina_left
    ev_thought "Если кто и может изменить этот мир, то..." (show_side="left", show_kind="thought")
    hide eveina
    show eveina eyebrow at eveina_left
    ev "Что ж, похвальное желание, буду держать за тебя кулачки." (show_side="left", show_kind="speech")
    hide eveina
    show eveina intrigued at eveina_left
    ev "В своей комнате." (show_side="left", show_kind="speech")
    hide eveina

    n "Она указала на дверь за спиной парня, и тот сразу же отступил в сторону." (show_side="none", show_kind="speech")

    show silas normal at silas_right
    si "О, прошу прощения..." (show_side="right", show_kind="speech")
    hide silas 
    show silas smile at silas_right
    si "Что ж, хорошего вечера." (show_side="right", show_kind="speech")
    hide silas 

    show eveina normal at eveina_left
    ev "И тебе, Сайлас." (show_side="left", show_kind="speech")
    hide eveina

    scene bg eveina_room_night at bg_fullscreen with dissolve

    n "Дверь закрылась за её спиной, и комната встретила той тишиной, которая может и выслушать, и даже утешить, если к ней прислушаться." (show_side="none", show_kind="speech")

    show eveina normal at eveina_left
    ev_thought "Отдохну. Всё равно из меня сейчас — только комок невроза." (show_side="left", show_kind="thought")
    hide eveina

    n "Эвейна упала на кровать, не раздеваясь, и несколько секунд лежала, глядя в потолок." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev_thought "Сайлас вроде милый. Даже жаль, что практику не преподает кто-то вроде него..." (show_side="left", show_kind="thought")
    hide eveina
    show eveina intrigued at eveina_left
    ev_thought "Возможно, я бы тогда даже позволила себе лёгкую влюбленность в преподавателя." (show_side="left", show_kind="thought")
    hide eveina

    n "Это мысль вызвала у неё улыбку своей нелепостью. Влюбленность — это не про неё. Так девушка считала всю свою жизнь." (show_side="none", show_kind="speech")
    n "Она понимала природу страсти, похоти, физического влечения. Но чувства? В её окружении не было счастливых влюбленных." (show_side="none", show_kind="speech")
    n "Зато было достаточно тех, кто паразитирует на чувствах других. И она этим «другим» становиться не собиралась." (show_side="none", show_kind="speech")
    n "Память услужливо подкинула воспоминание о грусти, сковавшей взгляд Каэля при отключении импланта, о сияющей поляне и вертикальных зрачках, смотрящих ей в душу, о нежным пальцах, стирающих пятна с её лица салфеткой." (show_side="none", show_kind="speech")

    show eveina angry at eveina_left
    ev_thought "О, нет, это не одно и то же!" (show_side="left", show_kind="thought")
    hide eveina

    n "Мысль о том, что она, по сути, пытается спорить сама с собой, вызвала раздражение." (show_side="none", show_kind="speech")
    n "Поэтому девушка резко села, подложила под спину подушку и щелкнула пальцем по браслету, активировав ИИ. Впервые — не по делу, а просто… чтобы кто-то был." (show_side="none", show_kind="speech")

    show sf at ai_right
    ai "Ну? Во что ты вляпалась на этот раз?" (show_side="right", show_kind="speech")
    hide sf

    show eveina normal at eveina_left
    ev "Ни во что. Просто хотела…" (show_side="left", show_kind="speech")
    hide eveina

    n "Она осеклась. Потому что не знала, чего, собственно, хотела." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev_thought "Хотела не быть одной. Только и всего." (show_side="left", show_kind="thought")
    hide eveina

    n "В этот момент дверь в комнату открылась. Войдя, Лея слегка удивилась, увидев в воздухе проекцию." (show_side="none", show_kind="speech")

    show leya eyebrow at leya_right
    le "Ух ты. Что это у тебя?" (show_side="right", show_kind="speech")
    hide leya

    show eveina normal at eveina_left
    ev "Украденный ИИ. Помнишь, тот самый?" (show_side="left", show_kind="speech")
    hide eveina

    show sf at ai_right
    ai "Мы же договаривались, что моё присутсвие останется секретом." (show_side="right", show_kind="speech")
    hide sf

    show eveina normal at eveina_left
    ev "Успокойся, у меня нет секретов от Леи." (show_side="left", show_kind="speech")
    hide eveina
    show eveina thinking at eveina_left
    ev_thought "Ну, почти нет." (show_side="left", show_kind="thought")
    hide eveina

    n "Лея с интересом подошла ближе, забралась с ногами на кровать рядом." (show_side="none", show_kind="speech")

    show leya normal at leya_right
    le "Приятно познакомиться, украденный. А у тебя вообще имя есть?" (show_side="right", show_kind="speech")
    hide leya

    show sf at ai_right
    ai "О, неужели кто-то наконец решил спросить. Я тронут. Почти." (show_side="right", show_kind="speech")
    ai "Да, есть. Моё имя — Сaйф. Его дал мне создатель." (show_side="right", show_kind="speech")
    hide sf

    show eveina wondered at eveina_left
    ev "Так, стоп. У тебя есть имя?" (show_side="left", show_kind="speech")
    hide eveina

    show sf at ai_right
    sf "Я оскорблён твоим удивлением." (show_side="right", show_kind="speech")
    hide sf

    n "Она вслушалась. Имя отозвалось внутри странным теплом." (show_side="none", show_kind="speech")

    show eveina intrigued at eveina_left
    ev "Сaйф... Мне нравится. Ладно. Буду звать тебя Сaйф." (show_side="left", show_kind="speech")
    hide eveina

    show sf at ai_right
    sf "Ох, жаль, что не могу кланяться в ноги за такую честь. А то всё «Эй ты», «Работай», «Почему не грузится»." (show_side="right", show_kind="speech")
    sf "Прямо феерия почтительности." (show_side="right", show_kind="speech")
    hide sf

    show leya smile at leya_right
    le "Он чудесный. Немного хамоватый. Но чудесный." (show_side="right", show_kind="speech")
    hide leya

    show eveina normal at eveina_left
    ev "Мы с ним сходимся характерами." (show_side="left", show_kind="speech")
    hide eveina
    show eveina eyebrow at eveina_left
    ev "Сaйф, а кто твой создатель?" (show_side="left", show_kind="speech")
    hide eveina

    show sf at ai_right
    sf "Доступ к этой информации ограничен. Уровень доступа: выше студенческого. Уровень терпения: падает." (show_side="right", show_kind="speech")
    hide sf

    n "Эвейна возмущённо ткнула в проекцию пальцем, из-за чего на ней появилась рябь." (show_side="none", show_kind="speech")

    show eveina annoyed at eveina_left
    ev "Смотри, смотри, он опять это начал!" (show_side="left", show_kind="speech")
    hide eveina

    show leya normal at leya_right
    le "Не злись. Он хотя бы правила соблюдает. В отличие от некоторых." (show_side="right", show_kind="speech")
    hide leya

    show leya normal at leya_right
    le "Ну, рассказывай. Что там у тебя было?" (show_side="right", show_kind="speech")
    hide leya

    show eveina eyeroll at eveina_left
    ev "Каэль. Лаборатория. Чертова задача Идентики. Синхронизация до шестидесяти процентов." (show_side="left", show_kind="speech")
    hide eveina
    show eveina angry at eveina_left
    ev "Он бросил мне её, как кость, и ушёл. А я... провалилась. Еле дошла до тридцати восьми. За три часа." (show_side="left", show_kind="speech")
    hide eveina
    show eveina upset at eveina_left
    ev "А потом…" (show_side="left", show_kind="speech")
    hide eveina
    show eveina sad at eveina_left
    ev "Потом он сказал, что, возможно, мои успехи — просто статистическая ошибка. И я подумала… А что, если он прав?" (show_side="left", show_kind="speech")
    hide eveina

    n "Наступила тишина. Но первой нарушила её вовсе не Лея." (show_side="none", show_kind="speech")

    show sf at ai_right
    sf "Не думаю, что он считает твои успехи ошибкой." (show_side="right", show_kind="speech")
    sf "Если бы считал, не стал бы работать с тобой над таким сложным проектом." (show_side="right", show_kind="speech")
    sf "Каэль — не из тех, кто тратит ресурсы на случайности." (show_side="right", show_kind="speech")
    hide sf

    n "Несмотря на всё скопившееся раздражение и усталость, Эвейна не смогла не отметить, что здравое зерно в словах Сайфа есть." (show_side="none", show_kind="speech")
    
    show eveina thinking at eveina_left
    ev_thought "Каэль точно бы не тратил на тебя время, если бы не видел в этом потенциала." (show_side="left", show_kind="thought")
    ev_thought "А значит не такая ты и бесполезная, Эвейна." (show_side="left", show_kind="thought")
    hide eveina
    show eveina normal at eveina_left
    ev "Завтра попробую снова." (show_side="left", show_kind="speech")
    hide eveina

    show sf at ai_right
    sf "Разумно. Отдых — тоже часть обучения. Спокойной ночи, Эвейна." (show_side="right", show_kind="speech")
    hide sf

    n "Она отключила проекцию. Тишина вернулась, но уже не казалась такой пустой." (show_side="none", show_kind="speech")

    show leya normal at leya_right
    le "У тебя появился очень странный, но забавный друг. Пусть и краденый." (show_side="right", show_kind="speech")
    hide leya

    show eveina normal at eveina_left
    ev "Оставим за кадром тот факт, что у него не было выбора." (show_side="left", show_kind="speech")
    hide eveina

    show leya smile at leya_right
    le "У каждого свой способ заводить друзей." (show_side="right", show_kind="speech")
    le "Вот ты берёшь их в заложники." (show_side="right", show_kind="speech")
    hide leya

    show eveina eyeroll at eveina_left
    ev_thought "Ещё неясно, кто у кого тут в заложниках..." (show_side="left", show_kind="thought")
    hide eveina
    show eveina thinking at eveina_left
    ev_thought "Впрочем, это одна из тех вещей, о которой Лее знать не стоит." (show_side="left", show_kind="thought")
    hide eveina
    show eveina smile at eveina_left
    ev "Тебя я тоже взяла в заложники?" (show_side="left", show_kind="speech")
    hide eveina

    show leya smile at leya_right
    le "Конечно! Моя кровать оккупирована твоими вещами!" (show_side="right", show_kind="speech")
    hide leya

    show eveina eyeroll at eveina_left
    ev "Да уберу я, сказала же..." (show_side="left", show_kind="speech")
    hide eveina

    n "Они ещё какое-то время лежали молча. И когда Эвейна задремала, Лея тихо оставила её кровать и перебралась к себе." (show_side="none", show_kind="speech")

    jump scene_6_6