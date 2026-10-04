default erian_corridor_strategy = None

label scene_1_5:
    $ previous_scene = "scene_1_4"
    $ next_scene = "scene_1_6"
    $ current_scene = "scene_1_5"
    $ kg_prepare_scene("scene_1_5")

    # --- Коридор ---

    call fade_to_black(1.2, 0.8)
    scene bg room corridor dark at bg_fullscreen with dissolve

    n "Когда Эвейна добралась до жилого блока, возникла одна проблема." (show_side="none", show_kind="speech")

    show eveina annoyed at eveina_left, sprite_warm
    $ room_number = renpy.call_screen(
        "choice",
        items=[
            ("3Б.", "3Б"),
            ("4Б.", "4Б"),
            ("4B.", "4B"),
        ],
        who="Эвейна",
        what="Чёрт... Какой же там был номер комнаты?",
        _last_say_who="ev"
    )
    hide eveina

    if room_number == "4B":
        show eveina thinking at eveina_left, sprite_warm
        ev "Проверим..." (show_side="left", show_kind="speech")
        hide eveina

        n "Дверь мягко засветилась по периметру, подтверждая её правоту и освещая часть коридора." (show_side="none", show_kind="speech")
        n "Эвейна даже подпрыгнула от восторга, а затем сделала несколько победных танцевальных па." (show_side="none", show_kind="speech")

        show eveina intrigued at eveina_left, sprite_warm
        ev "Ха, с первой попытки! Так держать, Эвейна! Сегодня дверь комнаты — завтра ответы на все воп..." (show_side="left", show_kind="speech")
        hide eveina

    else:
        n "Эвейна подошла к выбранной двери, но та на неё не отреагировала." (show_side="none", show_kind="speech")

        show eveina thinking at eveina_left, sprite_warm
        ev "Хм..." (show_side="left", show_kind="speech")
        hide eveina

        n "Для убедительности она помахала перед дверью браслетом. Никакого эффекта." (show_side="none", show_kind="speech")
        n "Браслет услужливо вывел перед ней назначенный номер: 4B." (show_side="none", show_kind="speech")

        show eveina eyeroll at eveina_left, sprite_warm
        ev "Да поняла я. Не эта." (show_side="left", show_kind="speech")
        hide eveina

        n "Нужная дверь обнаружилась дальше по коридору и засветилась мягким светом, стоило девушке подойти." (show_side="none", show_kind="speech")
        n "Эвейна раздосадованно шлёпнула себя по лбу." (show_side="none", show_kind="speech")

        show eveina annoyed at eveina_left, sprite_warm
        ev "Ну и как ты собираешься добраться до закрытых исследований, если проигрываешь две..." (show_side="left", show_kind="speech")
        hide eveina

    n "Девушка осеклась – свет от двери выхватил из темноты фигуру у противоположной стены." (show_side="none", show_kind="speech")

    scene bg scene 1_5 corridor 2 at bg_fullscreen with dissolve
    pause (1.0)

    n "Он стоял неподвижно, почти сливаясь с тенью. Не прятался и не пытался сделать вид, что оказался здесь случайно." (show_side="none", show_kind="speech")
    n "Он наблюдал. И это стало неприятным открытием." (show_side="none", show_kind="speech")

    ev_thought "И давно ты здесь стоишь?" (show_side="left", show_kind="thought")
    ev_thought "Только не говори, что видел представление с дверью." (show_side="left", show_kind="thought")

    n "Судя по ленивой ухмылке, видел." (show_side="none", show_kind="speech")

    ev "Ммм... Привет?" (show_side="left", show_kind="speech")

    unknown "..." (show_side="right", show_kind="speech")

    ev_thought "Скажи что-нибудь. Или уйди. Любой вариант будет менее стрёмным." (show_side="left", show_kind="thought")

    ev "Что ты здесь делаешь? Если заблудился..." (show_side="left", show_kind="speech")

    unknown "А ты?" (show_side="right", show_kind="speech")

    ev "Эм... а что я?" (show_side="left", show_kind="speech")

    n "Он недовольно прищурился." (show_side="none", show_kind="speech")

    unknown "Что {i}ты{/i} здесь делаешь, Эвейна?" (show_side="right", show_kind="speech")

    ev "Откуда ты..." (show_side="left", show_kind="speech")

    n "Не удосужившись дослушать, парень хмыкнул, развернулся и молча двинулся прочь по коридору." (show_side="none", show_kind="speech")

    scene bg scene 1_5 corridor 3 at bg_fullscreen with dissolve

    ev "О, ещё один образец дружелюбия!" (show_side="left", show_kind="speech")
    ev "Вас таких милых специально на этой планете собрали, чтобы херануть по ней импульсным зарядом?" (show_side="left", show_kind="speech")

    n "Удаляющаяся фигура застыла, развернулась и двинулась обратно." (show_side="none", show_kind="speech")

    scene bg room corridor dark at bg_fullscreen with dissolve

    show eveina fear at eveina_left, sprite_warm
    ev_thought "Да чёрт тебя дери, Эвейна! Не могла прокомментировать потише?" (show_side="left", show_kind="thought")
    hide eveina

    n "Он настиг её в несколько шагов. Наклонился, внимательно рассматривая испуганное лицо." (show_side="none", show_kind="speech")

    show erian eyebrow at erian_right, sprite_warm
    unknown "Чего так испугалась?" (show_side="right", show_kind="speech")
    hide erian

    show eveina annoyed at eveina_left, sprite_warm
    ev "За мной следит какой-то стрёмный тип. Есть причины нервничать." (show_side="left", show_kind="speech")
    hide eveina

    n "Он усмехнулся краем губ." (show_side="none", show_kind="speech")

    show erian intrigued at erian_right, sprite_warm
    unknown "Страшный тип? Обидно. Мне говорили, я красавчик." (show_side="right", show_kind="speech")
    hide erian

    show eveina wrinkled at eveina_left, sprite_warm
    ev "Я сказала стрёмный." (show_side="left", show_kind="speech")
    hide eveina

    show erian eyeroll at erian_right, sprite_warm
    unknown "Ну, это полностью меняет дело." (show_side="right", show_kind="speech")
    hide erian

    n "Он сделал ещё шаг вперёд. Эвейна попятилась, пока спиной не упёрлась в стену." (show_side="none", show_kind="speech")

    show eveina fear at eveina_left, sprite_warm
    ev "Ты, кажется, куда-то очень спешил?" (show_side="left", show_kind="speech")
    hide eveina

    show erian intrigued at erian_right, sprite_warm
    unknown "А ты так настойчиво умоляла остаться." (show_side="right", show_kind="speech")
    hide erian

    show eveina wrinkled at eveina_left, sprite_warm
    ev "Я не умоляла!" (show_side="left", show_kind="speech")
    hide eveina

    show erian intrigued at erian_right, sprite_warm
    unknown "А я так услышал." (show_side="right", show_kind="speech")
    hide erian

    n "Эвейну догнала запоздалая мысль." (show_side="none", show_kind="speech")

    show eveina annoyed at eveina_left, sprite_warm
    ev "Это ты был в саду?" (show_side="left", show_kind="speech")
    hide eveina

    show erian smile at erian_right, sprite_warm
    unknown "Ты там, кажется, разговаривала с деревьями. Я решил не мешать." (show_side="right", show_kind="speech")
    hide erian

    show eveina wrinkled at eveina_left, sprite_warm
    ev "Я же буквально спросила, есть ли там кто-нибудь!" (show_side="left", show_kind="speech")
    hide eveina

    show erian eyebrow at erian_right, sprite_warm
    unknown "Ну я ж не знал, что ты меня спрашиваешь." (show_side="right", show_kind="speech")
    hide erian

    show eveina annoyed at eveina_left, sprite_warm
    ev "Откуда ты знаешь, как меня зовут?" (show_side="left", show_kind="speech")
    hide eveina

    show erian intrigued at erian_right, sprite_warm
    unknown "Не помнишь?" (show_side="right", show_kind="speech")
    hide erian

    n "Эвейна перебрала в голове события долгого дня. Ни одного знакомого лица, похожего на это." (show_side="none", show_kind="speech")
    n "Зато ей вдруг показалось, что вопрос он задал не из праздного любопытства." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left, sprite_warm
    $ erian_corridor_strategy = renpy.call_screen(
        "choice",
        items=[
            ("Поймать его на реакции.", "pressure"),
            ("Сделать вид, что вспомнила.", "probe"),
            ("Потребовать расстояния.", "boundary"),
        ],
        what=""
    )
    hide eveina

    if erian_corridor_strategy == "pressure":
        show eveina annoyed at eveina_left, sprite_warm
        ev "Нет. Но ты явно рассчитывал на другой ответ." (show_side="left", show_kind="speech")
        hide eveina

        n "Ухмылка исчезла с его лица." (show_side="none", show_kind="speech")

        show erian annoyed at erian_right, sprite_warm
        unknown "Уверена?" (show_side="right", show_kind="speech")
        hide erian

        show eveina wrinkled at eveina_left, sprite_warm
        ev "Таких стрёмных типов я обычно запоминаю." (show_side="left", show_kind="speech")
        hide eveina

    elif erian_corridor_strategy == "probe":
        show eveina thinking at eveina_left, sprite_warm
        ev "Возможно. Напомни." (show_side="left", show_kind="speech")
        hide eveina

        n "Он замер. Всего на мгновение, но Эвейна успела заметить, как внимательно он следит за её лицом." (show_side="none", show_kind="speech")

        show erian eyebrow at erian_right, sprite_warm
        unknown "Что именно?" (show_side="right", show_kind="speech")
        hide erian

        show eveina eyebrow at eveina_left, sprite_warm
        ev "Откуда мы знакомы." (show_side="left", show_kind="speech")
        hide eveina

        show erian eyebrow at erian_right, sprite_warm
        unknown "А что помнишь ты?" (show_side="right", show_kind="speech")
        hide erian

        show eveina annoyed at eveina_left, sprite_warm
        ev "Пока — как ты пытаешься заставить меня ответить первой." (show_side="left", show_kind="speech")
        hide eveina

        n "Он выпрямился. Уловка сработала ровно настолько, чтобы выдать его ожидание, — и недостаточно, чтобы получить ответ." (show_side="none", show_kind="speech")

        show erian annoyed at erian_right, sprite_warm
        unknown "Значит, не помнишь?" (show_side="right", show_kind="speech")
        hide erian

        show eveina wrinkled at eveina_left, sprite_warm
        ev "Помню стрёмного типа, который следил за мной в тёмном коридоре." (show_side="left", show_kind="speech")
        hide eveina

    elif erian_corridor_strategy == "boundary":
        show eveina annoyed at eveina_left, sprite_warm
        ev "Прежде чем я отвечу, тебе придётся сделать шаг назад." (show_side="left", show_kind="speech")
        hide eveina

        n "Он посмотрел на её лицо, потом на стену за её спиной. Шагнул назад, оставляя пространство между ними." (show_side="none", show_kind="speech")

        show erian eyeroll at erian_right, sprite_warm
        unknown "Так лучше?" (show_side="right", show_kind="speech")
        hide erian

        show eveina annoyed at eveina_left, sprite_warm
        ev "Для начала." (show_side="left", show_kind="speech")
        hide eveina

        show erian eyebrow at erian_right, sprite_warm
        unknown "Так что? Вспомнила?" (show_side="right", show_kind="speech")
        hide erian

        show eveina wrinkled at eveina_left, sprite_warm
        ev "Нет. Такого стрёмного типа я бы точно запомнила." (show_side="left", show_kind="speech")
        hide eveina

    n "Незнакомец прищурился, будто ожидал внезапного озарения." (show_side="none", show_kind="speech")
    n "И не дождавшись, резко развернулся и пошёл дальше по коридору." (show_side="none", show_kind="speech")

    show erian eyeroll at erian_right, sprite_warm
    unknown "Твоё имя объявили на весь холл." (show_side="right", show_kind="speech")
    hide erian

    show eveina thinking at eveina_left, sprite_warm
    ev_thought "Логично. И всё равно ничерта не объясняет." (show_side="left", show_kind="thought")
    hide eveina
    
    show eveina annoyed at eveina_left, sprite_warm
    ev_thought "Имя он мог услышать в холле. Но какого хрена ему понадобилось следить за мной?" (show_side="left", show_kind="thought")
    hide eveina
    show eveina wrinkled at eveina_left, sprite_warm
    ev_thought "Это такие отвратительные методы знакомства?" (show_side="left", show_kind="thought")
    hide eveina

    n "Эвейна посмотрела ему вслед, затем перевела взгляд на дверь своей комнаты." (show_side="none", show_kind="speech")

    show eveina eyeroll at eveina_left, sprite_warm
    ev_thought "Чёрт с ним... Ещё бы об этом моя голова не болела." (show_side="left", show_kind="thought")
    hide eveina


    # --- Комната ---
    scene bg room evening at bg_fullscreen with dissolve
    # play music "bgm/dorm_evening.ogg" fadein 2.0

    n "Устало вздохнув, студентка шагнула в комнату — и тут же наткнулась на заинтересованный взгляд." (show_side="none", show_kind="speech")

    show leya eyebrow at leya_right, sprite_warm
    unknown "С кем-то ещё успела повоевать?" (show_side="right", show_kind="speech")
    hide leya

    show eveina eyebrow at eveina_left, sprite_warm
    ev "Что?" (show_side="left", show_kind="speech")
    hide eveina

    show leya normal at leya_right, sprite_warm
    unknown "Я слышала голоса за дверью." (show_side="right", show_kind="speech")
    hide leya

    #n "Эвейна нахмурилась."

    show eveina eyeroll at eveina_left, sprite_warm
    ev "А, да я... завожу новые знакомства." (show_side="left", show_kind="speech")
    hide eveina

    n "Соседка окинула её скептичным взглядом, но настаивать не стала. Повисла короткая пауза." (show_side="none", show_kind="speech")

    # --- Знакомство ---
    show eveina normal at eveina_left, sprite_warm
    ev "Эвейна." (show_side="left", show_kind="speech")
    hide eveina

    show leya normal at leya_right, sprite_warm
    unknown "Да, знаю. Я Лея." (show_side="right", show_kind="speech")
    hide leya
    show leya eyebrow at leya_right, sprite_warm
    le "Мы уже пересекались — в холле, помнишь?" (show_side="right", show_kind="speech")
    hide leya

    show leya normal at leya_right, sprite_warm
    le "Ты выглядела так, будто собиралась кого-то похоронить прямо там. Решила, тебе не помешает поддержка." (show_side="right", show_kind="speech")
    hide leya

    show eveina normal at eveina_left, sprite_warm
    ev "Да, помню... спасибо." (show_side="left", show_kind="speech")
    hide eveina

    show leya smile at leya_right, sprite_warm
    le "Без проблем. Ты только... не суди их строго. Первый день — он у всех такой." (show_side="right", show_kind="speech")
    le "Все по-разному справляются со стрессом. У кого-то просыпается желание что-то доказать, у кого-то — выместить на других избыток эмоций." (show_side="right", show_kind="speech")
    hide leya
    show leya eyebrow at leya_right, sprite_warm
    le "У тебя, судя по всему, желание дать кому-нибудь в морду." (show_side="right", show_kind="speech")
    hide leya

    show eveina eyeroll at eveina_left, sprite_warm
    ev "Да, это был очень длинный день." (show_side="left", show_kind="speech")
    hide eveina

    show leya smile at leya_right, sprite_warm
    le "Что ж, хорошая новость в том, что он закончился." (show_side="right", show_kind="speech")
    hide leya

    n "Она махнула на свободную кровать." (show_side="none", show_kind="speech")

    show leya normal at leya_right, sprite_warm
    le "Занимай, она твоя. Свет можно настроить голосом или с браслета, но он иногда упрямится. Если будет мерцать — не пугайся." (show_side="right", show_kind="speech")
    hide leya

    n "Эвейна кивнула и направилась к своей половине, где уже стоял её чемодан." (show_side="none", show_kind="speech")
    n "Раскладывая вещи, скользнула взглядом по комнате. Стандартная мебель, мягкий свет, большое окно." (show_side="none", show_kind="speech")
    n "На подоконнике у соседней кровати стоял небольшой горшок с чем-то, что напоминало мох — только темнее, плотнее, с едва заметным бежевым отливом на отростках." (show_side="none", show_kind="speech")

    show eveina eyebrow at eveina_left, sprite_warm
    ev "Это... что за уродец?" (show_side="left", show_kind="speech")
    hide eveina

    show leya smile at leya_right, sprite_warm
    le "Эй, чего сразу уродец? Разве он не прекрасен? Нашла в саду после вводных экскурсий — рос прямо на корнях одного из деревьев." (show_side="right", show_kind="speech")
    hide leya

    show eveina eyebrow at eveina_left, sprite_warm
    ev "Ну, допустим... И что это?" (show_side="left", show_kind="speech")
    hide eveina

    show leya normal at leya_right, sprite_warm
    le "Симбиотический мох. Он не просто растёт на дереве — он с ним взаимодействует. Обменивается питательными веществами, подстраивается под биоритмы хозяина." (show_side="right", show_kind="speech")
    hide leya

    show eveina eyebrow at eveina_left, sprite_warm
    ev "Ты ботаник?" (show_side="left", show_kind="speech")
    hide eveina

    show leya smile at leya_right, sprite_warm
    le "Да. Семейное, можно сказать — родители оба учёные, старшая сестра тоже здесь училась." (show_side="right", show_kind="speech")
    le "Она и рассказала мне про этот мох. Говорила, что местная флора удивительна." (show_side="right", show_kind="speech")
    hide leya
    show leya eyebrow at leya_right, sprite_warm
    le "Ты знала, что все растения на этой планете по сути своей и не растения вовсе, а видоизмененные грибы?" (show_side="right", show_kind="speech")
    hide leya

    show leya normal at leya_right, sprite_warm
    le "И вот, смотри — видишь серебристо-бежевый налёт? Это не пигмент. Мох адаптируется к окружению буквально за несколько часов." (show_side="right", show_kind="speech")
    le "Я его потрогала... и вот." (show_side="right", show_kind="speech")
    le "А если поместить его рядом с повреждённым стволом дерева..." (show_side="right", show_kind="speech")
    hide leya

    n "На словах о биоритмах Эвейна ещё пыталась следить за объяснением. Где-то между растениями-грибами и налётом окончательно перестала." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left, sprite_warm
    ev_thought "Как только останусь одна, нужно проверить внутреннюю базу. Интересно, будет ли там что-то по запросу инналу..." (show_side="left", show_kind="thought")
    hide eveina

    show leya thinking at leya_right, sprite_warm
    le "В общем, есть теория, что такие симбиотические организмы способны восстанавливать повреждённые тк..." (show_side="right", show_kind="speech")
    hide leya

    n "Лея осеклась." (show_side="none", show_kind="speech")

    show leya eyebrow at leya_right, sprite_warm
    le "Эвейна?" (show_side="right", show_kind="speech")
    hide leya

    show eveina surprized at eveina_left, sprite_warm
    ev "А? Прости, я..." (show_side="left", show_kind="speech")
    hide eveina

    n "Блондинка посмотрела на неё — внимательно, без обиды. Потом мягко улыбнулась." (show_side="none", show_kind="speech")

    show leya smile at leya_right, sprite_warm
    le "Ладно, я увлеклась. Расскажу как-нибудь потом, когда ты не будешь засыпать на ходу." (show_side="right", show_kind="speech")
    hide leya

    n "Эвейна открыла рот, чтобы возразить, но вместо этого зевнула. Лея была права — голова уже не воспринимала новую информацию." (show_side="none", show_kind="speech")
    n "Она плюхнулась на кровать. Соседка вернулась к своему планшету, но через минуту тихо её позвала." (show_side="none", show_kind="speech")

    show leya normal at leya_right, sprite_warm
    le "Эвейна. Если вдруг что... не держи в себе. Не все здесь акулы с планами на мировое господство." (show_side="right", show_kind="speech")
    le "Иногда просто хочется с кем-то перекинуться парой слов." (show_side="right", show_kind="speech")
    hide leya

    show eveina smile at eveina_left, sprite_warm
    ev "Рада, что мне не приходится делить комнату с акулой." (show_side="left", show_kind="speech")
    hide eveina

    show leya smile at leya_right, sprite_warm
    le "Доброй ночи." (show_side="right", show_kind="speech")
    hide leya

    n "Эвейна вытянулась на прохладной постели и закрыла глаза." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left, sprite_warm
    ev_thought "А если бы делила комнату с акулой – поселили бы в аквариуме?" (show_side="left", show_kind="thought")
    hide eveina
    show eveina eyeroll at eveina_left, sprite_warm
    ev_thought "Так, всё, пора отключать это больное сознание..." (show_side="left", show_kind="thought")
    hide eveina

    jump scene_1_6  # Переход к следующей сцене
