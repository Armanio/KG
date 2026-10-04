label scene_3_7:
    $ previous_scene = "scene_3_6"
    $ next_scene = "start_chapter_4"
    $ current_scene = "scene_3_7"
    call fade_to_black(1.2, 0.8)

    scene bg eveina_room_night at bg_fullscreen with dissolve
    # play music "bgm/quiet_room.ogg" fadein 2.0

    n "Вечером, переступив порог комнаты, Эвейна позволила себе не торопиться — сбросила сумку, потянулась, по привычке сняла обувь прямо посреди комнаты." (show_side="none", show_kind="speech")
    n "Всё здесь напоминало о малых радостях одиночества: мягкий плед на кровати, едва тёплый свет настольной лампы, отсутствие Леи, которая, видимо, задержалась в архиве." (show_side="none", show_kind="speech")
    n "Эвейна села на край кровати, и позволила себе пару секунд смотреть в никуда." (show_side="none", show_kind="speech")

    show eveina normal at eveina_left
    ev_thought "Ещё один слишком долгий день." (show_side="left", show_kind="thought")
    hide eveina 

    n "На автомате рука потянулась к терминалу на столе. Просто привычка — проверить сообщения, вдруг что-то важное. И там, конечно, было сообщение. От папы." (show_side="none", show_kind="speech")
    n "Девушка включила видео — и на экране тут же появилось его лицо. Родное, тёплое. Но… что-то в нём было не так." (show_side="none", show_kind="speech")
    n "Он улыбался, бодро и тепло. В руках держал деревянную ложку, за спиной — кастрюли и огоньки кухонных панелей." (show_side="none", show_kind="speech")

    scene bg home_dining_room at bg_fullscreen with dissolve

    show rian normal at rian_right 
    ri "Вейна! Я приготовил её любимый суп. Помнишь, тот самый — с тмином и корнем аури?" (show_side="right", show_kind="speech")
    ri "Запах... до сих пор не могу понять, почему именно он делает его особенным." (show_side="right", show_kind="speech")
    ri "Как думаешь, во сколько она придёт сегодня? Я поставил ещё одну тарелку." (show_side="right", show_kind="speech")
    ri "Она наверно… опаздывает." (show_side="right", show_kind="speech")
    hide rian 

    n "Его улыбка стала немного виноватой, будто он извинялся за собственную растерянность." (show_side="none", show_kind="speech")

    show eveina sad at eveina_left 
    ev_thought "Пап…" (show_side="left", show_kind="thought")
    hide eveina 

    show rian sad at rian_right
    ri "Эти смены такие длинные. Я сам уже путаюсь, какой сегодня день." (show_side="right", show_kind="speech")
    hide rian

    show eveina sad at eveina_left
    ev_thought "Она не придёт, пап. Уже много лет, как..." (show_side="left", show_kind="thought")
    hide eveina 

    show rian sad at rian_right
    ri "Я ждал её вчера. И, кажется, позавчера. Или…" (show_side="right", show_kind="speech")
    hide rian

    n "Он на мгновение замер, на лице мелькнула растерянность — короткая, как вспышка." (show_side="none", show_kind="speech")

    show rian sad at rian_right
    ri "Главное — я не забыл рецепт." (show_side="right", show_kind="speech")
    ri "Это уже что-то, правда?" (show_side="right", show_kind="speech")
    hide rian

    n "Отец попытался улыбнуться. Но улыбка вышла кривой, неловкой, — словно растянутая тень былой силы." (show_side="none", show_kind="speech")

    show rian normal at rian_right
    ri "Не волнуйся за меня, Вейна." (show_side="right", show_kind="speech")
    ri "Правда. Я… я справляюсь. Всё хорошо." (show_side="right", show_kind="speech")
    ri "Главное, чтобы у тебя всё получалось. Ты ведь учишься, да?" (show_side="right", show_kind="speech")
    ri "Слушаешь профессоров или споришь с ними, как в детстве со мной?" (show_side="right", show_kind="speech")
    hide rian

    n "На этих словах его голос чуть дрогнул — то ли от смеха, то ли от слёз, которые не принято показывать детям." (show_side="none", show_kind="speech")

    show rian normal at rian_right
    ri "Я горжусь тобой." (show_side="right", show_kind="speech")
    ri "Даже если иногда путаюсь в днях и лицах… твоё я помню." (show_side="right", show_kind="speech")
    ri "Обещай, что не бросишь. Не свернёшь с пути." (show_side="right", show_kind="speech")
    hide rian

    n "Он замолк, посмотрел чуть в сторону, как будто прислушивался к чему-то." (show_side="none", show_kind="speech")

    show rian normal at rian_right
    ri "Я оставлю суп на подогреве. Вдруг она всё-таки заглянет." (show_side="right", show_kind="speech")
    hide rian

    n "На прощание он подмигнул, помахал рукой и видео оборвалось." (show_side="none", show_kind="speech")

    scene bg eveina_room_night at bg_fullscreen with dissolve

    n "Эвейна смотрела в пустой экран, пока не почувствовала, как ком подступает к горлу. Тёплая слеза скатилась по щеке — непрошеная, но настоящая." (show_side="none", show_kind="speech")
    n "В ответ она записала короткое видео:" (show_side="none", show_kind="speech")

    show eveina normal at eveina_left
    ev "Папа… суп звучит отлично." (show_side="left", show_kind="speech")
    ev "Обещаю, когда я приеду, мы приготовим его вместе." (show_side="left", show_kind="speech")
    hide eveina
    show eveina smile at eveina_left
    ev "Я тебя люблю." (show_side="left", show_kind="speech")
    hide eveina 

    n "Запись отправилась. Губы Эвейны чуть дрожали, она устало рухнула на кровать и уткнулась в подушку." (show_side="none", show_kind="speech")

    show eveina normal at eveina_left
    ev_thought "Ещё немного. Только немного тишины." (show_side="left", show_kind="thought")
    hide eveina 

    n "Но тишина оказалась короткой. Браслет на её запястье мягко завибрировал. Напоминание. Или…" (show_side="none", show_kind="speech")

    show eveina wondered at eveina_left
    ev_thought "Файл!" (show_side="left", show_kind="thought")
    hide eveina 

    n "Она резко поднялась от мысли о памяти браслета, где лежал тот самый файл, что она забрала из лаборатории профессора Эзари." (show_side="none", show_kind="speech")
    n "Усталость мгновенно потонула, уступая место возбуждению. Эвейна открыла интерфейс браслета, запустила распаковку." (show_side="none", show_kind="speech")
    n "Проекция вспыхнула ярким светом. В её центре появилось голографическое лицо — нет, не лицо даже, а абстрактная структура: сверкающая маска с узором, меняющимся от её дыхания." (show_side="none", show_kind="speech")

    show sf at ai_right
    ai "ИИ-ассистент активирован." (show_side="right", show_kind="speech")
    hide sf
    
    jump start_chapter_4
