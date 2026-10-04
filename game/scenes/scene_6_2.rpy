label scene_6_2:
    $ previous_scene = "scene_6_1"
    $ next_scene = "scene_6_3"
    $ current_scene = "scene_6_2"
    call fade_to_black(1.2, 0.8)
    scene bg eveina_room at bg_fullscreen with dissolve
    
    if erian_first_kiss == True:
        n "Остаток ночи прошёл в беспокойных мыслях о касаниях Эриана к её губам и коже. О его непроницаемом взгляде, когда он услышал об отчёте. О его сияющих глазах, которым вторила вся природа вокруг." (show_side="none", show_kind="speech")
    else: 
        n "Остаток ночи прошёл в беспокойных мыслях об Эриане. О его непроницаемом взгляде, когда он услышал об отчёте. О его сияющих глазах, которым вторила вся природа вокруг." (show_side="none", show_kind="speech")
    
    show eveina thinking at eveina_left
    ev_thought "Я будто на мгновение заглянула под маску человека, который совсем не похож на типичного Эриана..." (show_side="left", show_kind="thought")
    hide eveina
    show eveina eyeroll at eveina_left
    ev_thought "И тому, кто был под этой маской это, кажется, не очень понравилось." (show_side="left", show_kind="thought")
    hide eveina
    show eveina eyebrow at eveina_left
    ev_thought "А что, если я уже подписала себе приговор, действуя так импульсивно?" (show_side="left", show_kind="thought")
    hide eveina

    n "Ответа в воспалённом мозгу не находилось. Эвейна всё ещё лежала в постели, уткнувшись лбом в подушку. Усталость тянула вниз, но браслет на запястье завибрировал. Новое сообщение." (show_side="none", show_kind="speech")

    show eveina normal at eveina_left
    ev_thought "Пожалуйста… пусть это что-то незначительное." (show_side="left", show_kind="thought")
    hide eveina

    n "Она нехотя потянулась за браслетом, разблокировала проекцию — и сердце тут же сжалось." (show_side="none", show_kind="speech")
    n "Сообщение от отца. Видеозапись. Она села, прижав колени к груди, и активировала экран." (show_side="none", show_kind="speech")

    n "На голограмме — его лицо. Но не то, каким она его помнила. Оно стало измождённым, кожа — сероватой, губы пересохшие." (show_side="none", show_kind="speech")
    n "Он смотрел куда-то чуть в сторону камеры, будто с трудом ориентировался в пространстве." (show_side="none", show_kind="speech")

    show rian sad at rian_right
    ri "Дорогая… ты, э-э… как ты там? Я всё жду, когда ты… вернёшься…" (show_side="right", show_kind="speech")
    hide rian

    n "Он отвел взгляд, потом снова повернулся к камере." (show_side="none", show_kind="speech")

    show rian sad at rian_right
    ri "Не задерживайся у друзей, слышишь? Я… волнуюсь. Не приходи поздно." (show_side="right", show_kind="speech")
    ri "Тебе ведь завтра в колледж? Или… в институт…" (show_side="right", show_kind="speech")
    hide rian
    n "Он замолк, потом попробовал улыбнуться, но вышло криво." (show_side="none", show_kind="speech")

    show rian normal at rian_right
    ri "Как же быстро ты выросла. Как будто… время так пролетело. Хе…" (show_side="right", show_kind="speech")
    hide rian

    n "Он засмеялся — тихо, устало. Потом вдруг осёкся, и запись оборвалась." (show_side="none", show_kind="speech")
    n "Эвейна сидела, не двигаясь. Голограмма растворилась в воздухе. Комната наполнилась тишиной, слишком звонкой, чтобы её игнорировать." (show_side="none", show_kind="speech")

    show eveina upset at eveina_left
    ev_thought "Он забывает. Меня. Академию. Самого себя.\nА я… я сижу тут, в комнате, и не могу даже обнять его." (show_side="left", show_kind="thought")
    hide eveina

    n "Она сжала руками одеяло, ногти впились в ткань. Горло сжалось от беззвучного крика. Слёзы не текли — только мелкая дрожь в плечах выдавали её состояние." (show_side="none", show_kind="speech")

    show eveina sad at eveina_left
    ev_thought "Я должна быть рядом. Должна быть с ним." (show_side="left", show_kind="thought")
    ev_thought "Но если я уйду — никогда не узнаю, как остановить это. Как спасти его." (show_side="left", show_kind="thought")
    hide eveina

    n "Она поднялась с кровати, шагнула к столу, потом остановилась." (show_side="none", show_kind="speech")
    n "Посмотрела в пустоту, туда, где минуту назад был его образ." (show_side="none", show_kind="speech")

    show eveina normal at eveina_left
    ev_thought "Ты подожди ещё чуть-чуть, ладно?" (show_side="left", show_kind="thought") 
    ev_thought "Я найду способ. Я клянусь, папа. Только… не исчезай раньше времени." (show_side="left", show_kind="thought")
    hide eveina

    n "Она вытерла лицо и направилась к двери. Но прежде чем успела выйти наружу, браслет снова завибрировал." (show_side="none", show_kind="speech")

    show eveina annoyed at eveina_left
    ev_thought "Ну что там ещё?" (show_side="left", show_kind="thought")
    hide eveina

    n "Проекция высветила сообщение:" (show_side="none", show_kind="speech")

    n "📩 {i}Входящее сообщение{/i}\n{i}Отправитель: Аурелиан Вирт\nТема: Срочный вызов{/i}" (show_side="none", show_kind="speech")
    n "{i}Мисс Хейла,\nНастоящим уведомляю вас о необходимости немедленно явиться в мой кабинет по вопросу нарушения протокола доступа к архивным данным.\nПрошу вас не затягивать.\nС уважением,\nА. Вирт{/i}" (show_side="none", show_kind="speech")

    show eveina upset thinking at eveina_left
    ev_thought "Вот и всё. Финал шпионской карьеры." (show_side="left", show_kind="thought")
    hide eveina

    jump scene_6_3
