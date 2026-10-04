label scene_4_7:
    $ previous_scene = "scene_4_6"
    $ next_scene = "start_chapter_5"
    $ current_scene = "scene_4_7"

    # =========================================================
    # СЦЕНА 4_7 — «АРХИВ / ФАЙЛ / РАЗВИЛКА / ФИНАЛ»
    # Источник: оригинальная scene_4_3, строки 306–654.
    # Изменения: header; jump в конце → финал flaw → start_chapter_5;
    #            опечатка «лестице» → «лестнице».
    # =========================================================

    call fade_to_black(1.2, 0.8)
    scene bg archive_hall at bg_fullscreen with dissolve

    n "Пройдя один поворот и спустившись вниз по лестнице, они вошли в тёмное помещение, где на полках пылились старые книги, а на столах были разбросаны забытые носители." (show_side="none", show_kind="speech")
    n "Эвейна сразу направилась к цифровому терминалу. Эриан — к архивным личным делам сотрудников." (show_side="none", show_kind="speech")
    n "Стирая серый налёт с экрана и запуская программу, она косо поглядывала на то, как парень уверенно перебирал папки у стеллажа." (show_side="none", show_kind="speech")

    show eveina eyebrow at eveina_left
    ev "Ты всегда так уверенно шаришься по старым досье? Как будто там есть что-то полезнее покрывающей их пыли." (show_side="left", show_kind="speech")
    hide eveina

    show erian thinking at erian_right
    er "Ты ещё слишком молода и неопытна. Некоторые из них интереснее любого живого собеседника." (show_side="right", show_kind="speech")
    hide erian

    show eveina eyeroll at eveina_left
    ev "Смешно слышать подобные фразы от человека, которому кажется, столько же лет, сколько и мне." (show_side="left", show_kind="speech")
    hide eveina

    n "Эриан поднял на неё долгий, спокойный взгляд." (show_side="none", show_kind="speech")

    show erian normal at erian_right
    er "Уверена?" (show_side="right", show_kind="speech")
    hide erian

    n "От его интонации по спине пробежал холодок. Девушка опустила глаза, продолжая пересматривать документы в терминале." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev_thought "Уверена? А в чём я могу быть уверена, когда дело касается Эриана?" (show_side="left", show_kind="thought")
    ev_thought "Что я вообще о нём знаю?" (show_side="left", show_kind="thought")
    hide eveina
    show eveina annoyed at eveina_left
    ev_thought "Ну, кроме особой любви к сарказму и умения совать свой нос, куда не следует..." (show_side="left", show_kind="thought")
    ev_thought "Что вообще ему здесь нужно..." (show_side="left", show_kind="thought")
    hide eveina

    n "Взгляд зацепился за знакомое имя в файле. {i}«NR-Δ3. Первые испытания. Имя: К.Далон»{/i}" (show_side="none", show_kind="speech")
    n "Сердце забилось быстрее. Она быстро нажала пару сенсорных кнопок и скопировала файл в браслет." (show_side="none", show_kind="speech")
    n "В этот же момент за спиной материализовался Эриан. Он хмурился и выглядел недовольным." (show_side="none", show_kind="speech")

    show erian normal at erian_right
    er "Пора уходить." (show_side="right", show_kind="speech")
    hide erian

    n "Они двинулись к выходу." (show_side="none", show_kind="speech")

    scene bg forbidden_corridor at bg_fullscreen with dissolve

    n "Выйдя в коридор, парень задержался, глядя на неё исподлобья." (show_side="none", show_kind="speech")

    show erian annoyed at erian_right
    er "В следующий раз будь умнее и не суйся, куда не следует." (show_side="right", show_kind="speech")
    er "Спасать тебя от тебя самой не входит в мои приоритеты." (show_side="right", show_kind="speech")
    hide erian
    show erian intrigued at erian_right
    er "Если, конечно, ты не решишь меня отблагодарить..." (show_side="right", show_kind="speech")
    hide erian

    n "Глаза девушки сверкнули яростью в темноте. Эриан хмыкнул, закатил глаза и направился прочь." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    $ erian_walk_eveina = renpy.call_screen("choice",
    items=[
    ("сказать спасибо?", False),
    ("попросить проводить меня?", True)
    ], who="Эвейна", what="Может, стоит...", _last_say_who="ev_thought")
    hide eveina

    if erian_walk_eveina == False:
        n "Но прежде чем решиться, Эвейна осталась одна. Воздух вдруг стал тяжелее. А вместе с ним — тишина. Только теперь до неё дошло: он не объяснил, зачем пришёл. И главное — куда ей теперь идти." (show_side="none", show_kind="speech")

        show eveina angry at eveina_left
        ev_thought "Прекрасно. Просто великолепно." (show_side="left", show_kind="thought")
        ev_thought "Чёртов рыцарь, бросил принцессу в лабиринте и даже не удосужился оставить клубок ниток." (show_side="left", show_kind="thought")
        ev_thought "У тебя, Эриан, талант. Даже благодарность превратить в насмешку." (show_side="left", show_kind="thought")
        hide eveina
        show eveina eyebrow at eveina_left
        ev_thought "И как теперь выбраться из этой чёртовой мышеловки?" (show_side="left", show_kind="thought")
        hide eveina

        n "Эвейна закрутилась на месте, пытаясь вспомнить маршрут. Глаза выхватывали знакомые черты — но ни одна не подсказывала верный путь." (show_side="none", show_kind="speech")
        n "Тогда она вспомнила о нём. ИИ. Спорный, надоедливый, но, увы, единственный способ не заблудиться навечно." (show_side="none", show_kind="speech")
        n "Она нажала сенсорную кнопку на браслете." (show_side="none", show_kind="speech")

        show sf at ai_right
        ai "Ты отключила меня. Это… грубо. И немного ранит чувства." (show_side="right", show_kind="speech")
        hide sf

        show eveina normal at eveina_left
        ev "Если бы ты тогда не замолчал, нас бы застукали." (show_side="left", show_kind="speech")
        hide eveina

        show sf at ai_right
        ai "А если бы я молчал, тебя бы застукали раньше. В следующий раз — выбирай: безопасность или моя компания." (show_side="right", show_kind="speech")
        hide sf

        show eveina eyeroll at eveina_left
        ev "Очень смешно говорить мне о выборе, когда ты буквально захватил мой браслет." (show_side="left", show_kind="speech")
        hide eveina
        show eveina normal at eveina_left
        ev "Ладно, сейчас не об этом. Подскажи дорогу?" (show_side="left", show_kind="speech")
        hide eveina

        show sf at ai_right
        ai "Справа, потом налево. И не забудь, где здесь вверх." (show_side="right", show_kind="speech")
        hide sf

        n "Она пошла, почти на цыпочках, будто тишина могла укусить." (show_side="none", show_kind="speech")

        show eveina smile at eveina_left
        ev "Знаешь, закрытые секции оказались не такими уж закрытыми. Немного настойчивости — и даже стены Академии начинают выдавать свои секреты." (show_side="left", show_kind="speech")
        hide eveina

        show sf at ai_right
        ai "О, у нас хорошее настроение? Или просто посттравматический сарказм?" (show_side="right", show_kind="speech")
        ai "Ты что-то нашла." (show_side="right", show_kind="speech")
        hide sf

        show eveina thinking at eveina_left
        ev "Может быть. А может — только больше вопросов." (show_side="left", show_kind="speech")
        hide eveina

        show sf at ai_right
        ai "Налево. И если ты опять соберёшься в ночной поход, я включу тебе голос навигатора с рекламой." (show_side="right", show_kind="speech")
        ai "С бесящей интонацией и постоянными джинглами." (show_side="right", show_kind="speech")
        hide sf

        show eveina thinking at eveina_left
        ev "Звучит угрожающе. А мне только начал нравиться твой голос..." (show_side="left", show_kind="speech")
        ev "Спасибо. Без тебя я бы всю ночь бродила в темноте и ругалась со стенами." (show_side="left", show_kind="speech")
        hide eveina

        show sf at ai_right
        ai "Не благодари. Я не ассистент. Не навигатор. Не носитель истины. Я — голос в твоей голове, который не просил быть призванным." (show_side="right", show_kind="speech")
        ai "А ещё я слишком умён, чтобы мириться с ролью спасателя твоей неугомонной задницы." (show_side="right", show_kind="speech")
        hide sf

        show eveina annoyed at eveina_left
        ev "Моя задница прекрасна и сама по себе справляется с вызовами!" (show_side="left", show_kind="speech")
        hide eveina

        show sf at ai_right
        ai "Несомненно. Вон как уверенно направляется к выходу. В конце коридора — налево. Дальше — ты справишься." (show_side="right", show_kind="speech")
        hide sf

        n "ИИ замолчал. Осталась только пульсация в ушах и тяжесть в животе. В браслете лежал файл. А в душе — нечто куда менее структурированное, чем архивные записи." (show_side="none", show_kind="speech")

    if erian_walk_eveina == True:
        show eveina normal at eveina_left
        ev "Эриан, подожди..." (show_side="left", show_kind="speech")
        hide eveina

        n "Парень обернулся, вопросительно выгнув бровь." (show_side="none", show_kind="speech")

        show erian intrigued at erian_right
        er "Всё-таки решила, что благодарность тебе не чужда?" (show_side="right", show_kind="speech")
        hide erian

        show eveina normal at eveina_left
        ev "Нет, я... то есть..." (show_side="left", show_kind="speech")
        hide eveina

        n "Она глубоко вздохнула, собираясь с мыслями." (show_side="none", show_kind="speech")

        show eveina thinking at eveina_left
        ev "Я не знаю дороги обратно." (show_side="left", show_kind="speech")
        hide eveina

        n "В тусклом свете коридора нахальная ухмылка стала самым ярким источником света." (show_side="none", show_kind="speech")

        show erian intrigued at erian_right
        er "Ты что, просишь меня проводить тебя, словно мы влюбленная парочка, задержавшаяся на свидании?" (show_side="right", show_kind="speech")
        er "А у двери меня ждёт робкий поцелуй?" (show_side="right", show_kind="speech")
        hide erian

        n "Эвейна вспыхнула, чувствуя, как её щёки краснеют — то ли от возмущения, то ли от мысли о поцелуе." (show_side="none", show_kind="speech")

        show eveina angry at eveina_left
        ev "Боже, забудь! Найду дорогу сама." (show_side="left", show_kind="speech")
        hide eveina

        n "Только одному Эриану было известно, что творится в его голове, но самодовольная ухмылка продолжала освещать пространство вокруг." (show_side="none", show_kind="speech")
        n "Он подошёл к ней, подставив локоть, и с нетерпением посмотрел ей в глаза." (show_side="none", show_kind="speech")

        show eveina eyebrow at eveina_left
        ev_thought "Он это серьёзно? Ожидает, что я возьму его под руку?" (show_side="left", show_kind="thought")
        hide eveina

        n "Эвейна демонстративно обогнула его и направилась по коридору, с облегчением заметив, что парень всё же двинулся следом за ней." (show_side="none", show_kind="speech")

        show eveina eyebrow at eveina_left
        ev_thought "Может, стоит воспользоваться случаем и вытащить из него хоть какие-то ответы?" (show_side="left", show_kind="thought")
        hide eveina
        show eveina thinking at eveina_left
        ev_thought "Если Эриану что-то известно, возможно, я смогу подобраться поближе и понять, что именно…" (show_side="left", show_kind="thought")
        hide eveina
        show eveina normal at eveina_left
        ev_thought "Нужно только разговорить его. И желательно не дать ему понять, что это допрос." (show_side="left", show_kind="thought")
        hide eveina

        show eveina normal at eveina_left
        ev "Ты не скажешь никому, что застал меня там?" (show_side="left", show_kind="speech")
        hide eveina

        show erian intrigued at erian_right
        er "А что я получу за молчание?" (show_side="right", show_kind="speech")
        hide erian

        show eveina eyebrow at eveina_left
        ev "Право быть моим личным провожатым по тёмным коридорам?" (show_side="left", show_kind="speech")
        hide eveina

        show erian eyebrow at erian_right
        er "О, да, я же всю жизнь мечтал быть телохранителем безумной женщины без инстинкта самосохранения." (show_side="right", show_kind="speech")
        hide erian

        show eveina thinking at eveina_left
        ev_thought "Да что ты знаешь о безумных женщинах..." (show_side="left", show_kind="thought")
        hide eveina

        n "Эвейна невольно поморщилась от мысли, бередящей старую рану." (show_side="none", show_kind="speech")
        n "Пристальный взгляд Эриана, без сомнения, отметивший изменение в её настроении, заставил быстро сменить тему." (show_side="none", show_kind="speech")

        show eveina eyebrow at eveina_left
        ev "Ты ведь не в первый раз там? Что ты вообще делаешь в таких местах посреди ночи?" (show_side="left", show_kind="speech")
        hide eveina

        show erian intrigued at erian_right
        er "Возможно, ищу заблудших студенток, которые не умеют читать указатели." (show_side="right", show_kind="speech")
        hide erian

        show eveina annoyed at eveina_left
        ev "И швыряешь их в стену в качестве наказания?" (show_side="left", show_kind="speech")
        hide eveina

        show erian intrigued at erian_right
        er "Только если они задают слишком много вопросов." (show_side="right", show_kind="speech")
        hide erian

        show eveina annoyed at eveina_left
        ev "Значит, мне стоит помалкивать и просто позволить себя провожать?" (show_side="left", show_kind="speech")
        hide eveina

        show erian normal at erian_right
        er "Ты слишком любопытна, чтобы молчать. Даже если очень захочешь." (show_side="right", show_kind="speech")
        hide erian

        show eveina annoyed at eveina_left
        ev_thought "Это неправда!" (show_side="left", show_kind="thought")
        hide eveina
        show eveina thinking at eveina_left
        ev_thought "Хотя, может, доля истины в этом есть..." (show_side="left", show_kind="thought")
        hide eveina

        n "Они прошли несколько шагов молча, пока Эвейна прокручивала в голове разговор, начатый в архиве." (show_side="none", show_kind="speech")

        show eveina eyebrow at eveina_left
        ev "Сколько тебе лет, Эриан?" (show_side="left", show_kind="speech")
        hide eveina

        n "Эриан некоторое время продолжал идти молча, будто не услышал вопрос. И когда Эвейна уже готова была задать следующий, он наконец произнёс." (show_side="none", show_kind="speech")

        show erian thinking at erian_right
        er "Я старше тебя." (show_side="right", show_kind="speech")
        hide erian

        show eveina annoyed at eveina_left
        ev_thought "А то я не догадалась... просто кладезь секретов!" (show_side="left", show_kind="thought")
        hide eveina
        show eveina eyebrow at eveina_left
        ev "Нашёл то, что там искал?" (show_side="left", show_kind="speech")
        hide eveina

        show erian thinking at erian_right
        er "Нет." (show_side="right", show_kind="speech")
        hide erian

        show eveina thinking at eveina_left
        ev_thought "Ну, хотя бы моя ночь сложилась удачнее..." (show_side="left", show_kind="thought")
        hide eveina

        n "Эвейна невольно сжала рукой запястье с браслетом, что опять не ускользнуло от взгляда Эриана. Впрочем, он так ничего и не сказал." (show_side="none", show_kind="speech")

        show eveina eyebrow at eveina_left
        ev "Ты давно в Академии?" (show_side="left", show_kind="speech")
        hide eveina

        show erian thinking at erian_right
        er "Достаточно, чтобы понять, что здесь все либо пытаются что-то скрыть, либо узнать то, что скрывают другие." (show_side="right", show_kind="speech")
        hide erian

        show eveina eyebrow at eveina_left
        ev "И к какой категории относишься ты?" (show_side="left", show_kind="speech")
        hide eveina

        n "Эриан вдруг остановился, чуть развернувшись к ней." (show_side="none", show_kind="speech")

        show erian intrigued at erian_right
        er "А ты сама как думаешь?" (show_side="right", show_kind="speech")
        hide erian

        show eveina intrigued at eveina_left
        ev "Думаю... ты относишься и к тем, и другим. Явно что-то скрываешь, но также постоянно ищешь какие-то ответы." (show_side="left", show_kind="speech")
        hide eveina

        show erian smile wild at erian_right
        er "Да я просто загадка!" (show_side="right", show_kind="speech")
        er "Бьюсь об заклад, твоя любопытная натура уже строит планы, как меня разгадать." (show_side="right", show_kind="speech")
        hide erian

        show eveina normal at eveina_left
        ev "Я могла бы попробовать. Если ты обещаешь отвечать прямо на мои вопросы." (show_side="left", show_kind="speech")
        hide eveina

        show erian intrigued at erian_right
        er "А ты уверена, что справишься с моей прямотой?" (show_side="right", show_kind="speech")
        hide erian

        show eveina intrigued at eveina_left
        ev "Думаю, я могу рискнуть." (show_side="left", show_kind="speech")
        hide eveina

        show erian normal at erian_right
        er "Тогда рискни в следующий раз. Этот коридор выведет тебя к общежитию. Тебе пора." (show_side="right", show_kind="speech")
        hide erian

        show eveina annoyed at eveina_left
        ev "Так всегда. Самое интересное — и сразу сбегаешь." (show_side="left", show_kind="speech")
        hide eveina

        n "Эриан прищурился, сделал шаг в её сторону и навис над ней. Эвейна сглотнула, с трудом удержавшись от того, чтобы не отступить под его взглядом." (show_side="none", show_kind="speech")
        n "Кажется, это его даже позабавило, потому что в следующий миг в глазах парня загорелся огонь. Он медленно поднял руку к её лицу, будто давая ей время на то, чтобы отступить." (show_side="none", show_kind="speech")
        n "Замерев, Эвейна наблюдала, как его пальцы тянутся к скуле, мягко проводят по ней, очерчивая овал лица и заставляя сердце девушки стучать всё быстрее." (show_side="none", show_kind="speech")
        n "Пальцы коснулись её подбородка, аккуратно приподнимая и надавливая на него, из-за чего губы девушки приоткрылись." (show_side="none", show_kind="speech")
        n "Эвейна продолжала зачарованно смотреть ему в глаза, прекрасно осознавая, чем всё может закончиться, но уже была не уверена, что не хочет этого." (show_side="none", show_kind="speech")
        n "Чёртов Эриан буквально гипнотизировал своим пронзительным, смотрящим прямо внутрь неё взглядом." (show_side="none", show_kind="speech")
        n "Не отстранилась она и тогда, когда его лицо стало медленно приближаться к её, пока их носы чуть не столкнулись." (show_side="none", show_kind="speech")
        n "А потом Эриан медленно улыбнулся самой хищной улыбкой из своего арсенала." (show_side="none", show_kind="speech")

        show erian smile wild at erian_right
        er "Терпение, Эвейна. Я никогда не бросаю игру на полпути." (show_side="right", show_kind="speech")
        hide erian

        n "Его губы были так близко, что она почувствовала его дыхание на своих, почти ощущая, каким будет их прикосновение. Предвкушая его." (show_side="none", show_kind="speech")
        n "Но уже в следующий миг Эриан сделал шаг назад и, легко стукнув пальцем по её подбородку, захлопнул так жаждущий поцелуя рот." (show_side="none", show_kind="speech")
        n "Ещё секунда — и он исчез в тени коридора, оставив Эвейну стоять с учащённым пульсом и совершенно новой уверенностью в том, что эта игра действительно только начинается." (show_side="none", show_kind="speech")
        n "И с огромным сомнением, что она способна в ней победить." (show_side="none", show_kind="speech")

    # --- Финал — flaw ---

    scene bg eveina_room_night at bg_fullscreen with dissolve

    n "Она стояла у двери комнаты. Браслет мерцал на запястье." (show_side="none", show_kind="speech")
    n "В голове — не мысли. Образы. Вирт с салфеткой у её щеки. Каэль — «это была ошибка». Эриан с «терпение, Эвейна» или молчание ИИ рядом в темноте." (show_side="none", show_kind="speech")
    n "Она стояла и ждала, когда что-то внутри скажет ей, что это не так. Что один из них — не расчёт." (show_side="none", show_kind="speech")
    n "Ничего не сказало." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev_thought "Ни один из них не друг и не партнёр. Лишь инструменты. Папа, мне нельзя думать иначе." (show_side="left", show_kind="thought")
    hide eveina

    n "Пауза." (show_side="none", show_kind="speech")

    show eveina upset thinking at eveina_left
    ev_thought "Жаль, что всё это так похоже на правду." (show_side="left", show_kind="thought")
    hide eveina

    n "Она открыла дверь. Вошла. Браслет погас." (show_side="none", show_kind="speech")

    jump start_chapter_5
