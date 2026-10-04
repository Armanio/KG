label scene_2_3:
    $ previous_scene = "scene_2_2"
    $ next_scene = "scene_2_3_after_lecture"
    $ current_scene = "scene_2_3"
    $ kg_prepare_scene("scene_2_3")

    # =========================================================
    # СЦЕНА 3 — «ОТКРЫТИЕ ПЛАНЕТЫ» (лекция Вирта)
    # =========================================================

    call fade_to_black(1.2, 0.8)
    # play music "bgm/lecture.ogg" fadein 2.0

    scene bg lecture hall at bg_fullscreen with dissolve

    n "У входа в лекционный зал студенты по одному прикладывали академические браслеты к сканеру." (show_side="none", show_kind="speech")
    n "Проверка занимала несколько секунд, но очередь всё равно двигалась нервно: кто-то раздражённо вздыхал, кто-то вполголоса обсуждал очередную временную меру безопасности." (show_side="none", show_kind="speech")

    scene bg lecture hall students at bg_fullscreen with dissolve

    n "Эвейна нашла место у прохода, открыла на планшете академическую базу и вбила несколько запросов подряд: нейродегенерация, биополе, когнитивная терапия." (show_side="none", show_kind="speech")
    n "Через пару минут стало ясно: доступ с её студенческого профиля отличался от публичного примерно ничем." (show_side="none", show_kind="speech")
    n "Те же аннотации. Те же обрезанные выводы. Те же закрытые ссылки." (show_side="none", show_kind="speech")

    show eveina eyeroll at eveina_left, sprite_warm_light
    ev_thought "Прекрасно. Тот же запертый шкаф, только теперь с эмблемой Академии на дверце." (show_side="left", show_kind="thought")
    hide eveina

    n "Она изменила параметры поиска, добавила архивные публикации и внутренние проекты." (show_side="none", show_kind="speech")
    n "Система послушно выдала больше результатов — и закрыла доступ к каждому, который выглядел хоть немного полезным." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left, sprite_warm_light
    ev_thought "Значит, материалы существуют." (show_side="left", show_kind="thought")
    ev_thought "Осталось выяснить, где Академия прячет ключ." (show_side="left", show_kind="thought")
    hide eveina

    n "Рядом внезапно плюхнулся кто-то ещё." (show_side="none", show_kind="speech")

    show noa smile at noa_right, sprite_warm_light
    no "Успела соскучиться? Спасибо, что заняла для меня место!" (show_side="right", show_kind="speech")
    hide noa

    n "Эвейна погасила экран и молча уставилась в другую сторону." (show_side="none", show_kind="speech")

    show noa intrigued at noa_right, sprite_warm_light
    no "Ну хотя бы сделай вид, что рада меня видеть. Люди же смотрят." (show_side="right", show_kind="speech")
    hide noa

    show eveina eyeroll at eveina_left, sprite_warm_light
    ev_thought "Вот перед людьми и неудобно." (show_side="left", show_kind="thought")
    hide eveina
    
    scene bg lecture hall 2 at bg_fullscreen with dissolve

    n "Дверь бесшумно открылась — и на центральный подиум ступил Вирт." (show_side="none", show_kind="speech")
    n "Студенты замолчали без предупреждения и просьб." (show_side="none", show_kind="speech")

    show virt normal at virt_right, sprite_warm_light
    vi "Добро пожаловать на курс истории планеты Иннаки и её народа." (show_side="right", show_kind="speech")
    vi "Прежде чем вы начнёте работать здесь, вы должны понять, где именно находитесь." (show_side="right", show_kind="speech")
    hide virt

    n "Взгляд профессора скользнул по рядам, не задерживаясь ни на ком." (show_side="none", show_kind="speech")

    show virt normal at virt_right, sprite_warm_light
    vi "Всем вам знакома история Джонатана Ли — исследователя, открывшего планету, окружённую уникальным полем." (show_side="right", show_kind="speech")
    hide virt
    show virt thinking at virt_right, sprite_warm_light
    vi "Но некоторые подробности его экспедиции отсутствуют в общедоступной версии." (show_side="right", show_kind="speech")
    hide virt
    show virt normal at virt_right, sprite_warm_light
    vi "Первые отчёты Ли описывали Иннаки как необитаемую." (show_side="right", show_kind="speech")
    vi "При этом члены экспедиции испытывали необъяснимую тревогу, страдали от бессонницы, теряли концентрацию и обнаруживали провалы в памяти." (show_side="right", show_kind="speech")
    vi "Команде приказали прервать миссию и вернуться для медицинского обследования." (show_side="right", show_kind="speech")
    hide virt
    show virt upset thinking at virt_right, sprite_warm_light
    vi "Через несколько часов от Ли поступил ещё один отчёт, в котором было всего две фразы." (show_side="right", show_kind="speech")
    hide virt
    show virt normal at virt_right, sprite_warm_light
    vi "{i}«Они вокруг нас. И мы их не помним»{/i}." (show_side="right", show_kind="speech")
    hide virt

    scene bg lecture hall students at bg_fullscreen with dissolve

    n "Несколько секунд в аудитории никто не произносил ни слова." (show_side="none", show_kind="speech")

    show noa eyebrow at noa_right, sprite_warm_light
    no "Думаю, выражу общее мнение: кто — они?" (show_side="right", show_kind="speech")
    hide noa

    scene bg lecture hall 2 at bg_fullscreen with dissolve

    show virt normal at virt_right, sprite_warm_light
    vi "Инналу." (show_side="right", show_kind="speech")
    hide virt
    show virt upset thinking at virt_right, sprite_warm_light
    vi "Исследователям понадобилось несколько дней, чтобы установить: источником поля была не планета, а населявшие её люди." (show_side="right", show_kind="speech")
    hide virt
    show virt normal at virt_right, sprite_warm_light
    vi "Вместе с этим обнаружилось ещё одно свойство поля." (show_side="right", show_kind="speech")
    hide virt
    show virt thinking at virt_right, sprite_warm_light
    vi "Человеческий мозг не сохраняет воспоминания о непосредственном контакте с инналу." (show_side="right", show_kind="speech")
    hide virt
    show virt normal at virt_right, sprite_warm_light
    vi "Мы буквально их не помним." (show_side="right", show_kind="speech")
    hide virt

    scene bg lecture hall students at bg_fullscreen
    n "В аудитории стало тихо." (show_side="none", show_kind="speech")
    n "Эвейна смотрела на Вирта, ожидая пояснения, которое вернёт сказанное в пределы разумного." (show_side="none", show_kind="speech")

    show eveina surprized at eveina_left, sprite_warm_light
    ev "Как, черт возьми, это возможно?" (show_side="left", show_kind="speech")
    hide eveina

    scene bg lecture hall 2 at bg_fullscreen with dissolve

    show virt normal at virt_right, sprite_warm_light
    vi "Биополе инналу воздействует на гиппокамп — структуру мозга, ответственную за перевод краткосрочной памяти в долгосрочную." (show_side="right", show_kind="speech")
    vi "При непосредственном контакте с инналу оно блокирует консолидацию памяти." (show_side="right", show_kind="speech")
    hide virt
    show virt upset thinking at virt_right, sprite_warm_light
    vi "Вы можете видеть инналу, слышать их и взаимодействовать с ними." (show_side="right", show_kind="speech")
    hide virt
    show virt normal at virt_right, sprite_warm_light
    vi "Но после завершения контакта не сможете вспомнить ни лица, ни голоса, ни самого факта встречи." (show_side="right", show_kind="speech")
    hide virt

    scene bg scene 2_3 support at bg_fullscreen with dissolve

    n "Эвейна открыла рот, но не произнесла ни звука." (show_side="none", show_kind="speech")
    n "Ноа скосил на неё взгляд, легко коснулся её плеча своим и повернулся к Вирту." (show_side="none", show_kind="speech")

    no "Профессор, вы же шутите, да?" (show_side="right", show_kind="speech")

    scene bg lecture hall 2 at bg_fullscreen with dissolve

    show virt normal at virt_right, sprite_warm_light
    vi "Я похож на шутника, мистер Антерос?" (show_side="right", show_kind="speech")
    hide virt

    scene bg lecture hall students at bg_fullscreen with dissolve
    
    show noa upset thinking at noa_right, sprite_warm_light
    no "Нет, извините, профессор." (show_side="right", show_kind="speech")
    hide noa

    n "Ноа склонил голову, но как только взгляд профессора изменил траекторю, тут же повернулся к Эвейне." (show_side="none", show_kind="speech")

    show noa intrigued at noa_right, sprite_warm_light
    no "Поддержка – важная часть дружеских отношений!" (show_side="right", show_kind="speech")
    hide noa

    show eveina wrinkled at eveina_left, sprite_warm_light
    ev "Тишина – важная часть лекции." (show_side="left", show_kind="speech")
    hide eveina

    n "Позади послышался шум отодвигающегося стула." (show_side="none", show_kind="speech")

    scene bg scene 2_3 lecture hall 10 at bg_fullscreen
    sa "Я ведь правильно поняла?" (show_side="right", show_kind="speech")
    sa "На этой планете живут представители расы, чья суперспособность — вызывать провалы в нашей памяти?" (show_side="right", show_kind="speech")

    scene bg lecture hall 2 at bg_fullscreen with dissolve

    show virt normal at virt_right, sprite_warm_light    
    vi "Это не способность, а неизбежное свойство их биополя, мисс Вайс." (show_side="right", show_kind="speech") 
    hide virt
    show virt upset thinking at virt_right, sprite_warm_light
    vi "Инналу не могут произвольно включить или отключить его воздействие. Как только ваш контакт закончится — вы забудете о том, что он произошёл." (show_side="right", show_kind="speech")
    hide virt

    sa_offscreen "Почему об этом ничего не было сказано при поступлении?" (show_side="none", show_kind="speech")

    show virt normal at virt_right, sprite_warm_light
    vi "Потому что информация об инналу недоступна широкой общественности." (show_side="right", show_kind="speech")
    hide virt
    show virt thinking at virt_right, sprite_warm_light
    vi "Их природа привлекла бы не только исследователей, но и авантюристов, охотников за редкостями и тех, кто захотел бы использовать их поле." (show_side="right", show_kind="speech")
    hide virt
    show virt upset thinking at virt_right, sprite_warm_light
    vi "Открытое распространение этих сведений поставило бы под угрозу и научную работу, и самих инналу." (show_side="right", show_kind="speech")
    hide virt

    scene bg scene 2_3 lecture hall 10 at bg_fullscreen

    n "Девушку такой ответ не устроил." (show_side="none", show_kind="speech")

    sa "Моя мать знает обо всём этом?" (show_side="right", show_kind="speech")

    scene bg lecture hall 2 at bg_fullscreen with dissolve

    show virt eyebrow at virt_right, sprite_warm_light
    vi "Вы спрашиваете, знает ли глава корпорации, построившей аварийный контур Академии и курирующей исследования на Иннаки, об особенностях местной расы?" (show_side="right", show_kind="speech")
    hide virt
    show virt serious at virt_right, sprite_warm_light
    vi "Предполагаю, вы без труда и сами найдёте ответ на этот вопрос." (show_side="right", show_kind="speech")
    hide virt

    n "Сайрен поджала губы и опустилась на своё место." (show_side="none", show_kind="speech")

    show virt thinking at virt_right, sprite_warm_light
    vi "А мы, пожалуй, продолжим лекцию." (show_side="right", show_kind="speech")
    hide virt

    scene bg lecture hall students at bg_fullscreen with dissolve

    show eveina eyebrow at eveina_left, sprite_warm_light
    ev "Подождите, разве не разумнее было бы скрывать сведения об инналу и от студентов тоже?" (show_side="left", show_kind="speech")
    hide eveina

    n "Сзади тут же послышался язвительный смешок." (show_side="none", show_kind="speech")

    show sairen angry at sairen_right, sprite_warm_light
    sa "Точно, давайте скроем от студентов информацию, которая напрямую влияет на их безопасность! Браво!" (show_side="right", show_kind="speech")
    hide sairen

    scene bg lecture hall 2 at bg_fullscreen with dissolve

    n "Аурелиан Вирт перевёл короткий сдержанный взгляд на Сайрен, заставив её замолкнуть." (show_side="none", show_kind="speech")

    show virt normal at virt_right, sprite_warm_light
    vi "Изначально Академия придерживалась именно такой политики." (show_side="right", show_kind="speech")
    hide virt
    show virt eyebrow at virt_right, sprite_warm_light
    vi "Но молодые исследователи проявляли удивительную изобретательность в попытках изучать то, что от них скрывали." (show_side="right", show_kind="speech")
    hide virt
    show virt upset thinking at virt_right, sprite_warm_light
    vi "Незнание не останавливало их. Оно лишь делало последствия опаснее." (show_side="right", show_kind="speech")
    hide virt

    scene bg lecture hall students at bg_fullscreen with dissolve

    show eveina thinking at eveina_left, sprite_warm_light
    ev_thought "Логично." (show_side="left", show_kind="thought")
    ev_thought "Запреты обычно помогают ровно до появления первого любопытного идиота." (show_side="left", show_kind="thought")
    hide eveina

    show sairen intrigued at sairen_right, sprite_warm_light
    sa "Тогда объясните слухи о недавнем техническом сбое." (show_side="right", show_kind="speech")
    hide sairen

    vi_offscreen "Слухи?" (show_side="none", show_kind="speech")

    show sairen thinking at sairen_right, sprite_warm_light
    sa "Старшекурсники говорят, что около месяца назад в одном из корпусов несколько человек одновременно потеряли память." (show_side="right", show_kind="speech")
    hide sairen
    show sairen angry at sairen_right, sprite_warm_light
    sa "Если это правда, почему никто не проверяет связь с инналу?" (show_side="right", show_kind="speech")
    hide sairen

    n "По залу прошёл приглушённый гул." (show_side="none", show_kind="speech")
    n "Несколько студентов переглянулись. Кто-то недоверчиво усмехнулся." (show_side="none", show_kind="speech")

    scene bg lecture hall 2 at bg_fullscreen with dissolve

    show virt serious at virt_right, sprite_warm_light
    vi "Около месяца назад в Академии произошёл технический сбой." (show_side="right", show_kind="speech")
    vi "Версии о массовой потере памяти распространяются студентами и официально не подтверждены." (show_side="right", show_kind="speech")
    hide virt

    scene bg lecture hall students at bg_fullscreen with dissolve

    show eveina thinking at eveina_left, sprite_warm_light
    ev_thought "Снова этот инцидент... что же там такого произошло?" (show_side="left", show_kind="thought")
    hide eveina

    show sairen thinking at sairen_right, sprite_warm_light
    sa_offscreen "Очень удобная формулировка." (show_side="none", show_kind="speech")

    scene bg lecture hall 2 at bg_fullscreen with dissolve

    show virt normal at virt_right, sprite_warm_light
    vi "Осторожная формулировка, мисс Вайс." (show_side="right", show_kind="speech")
    hide virt
    show virt serious at virt_right, sprite_warm_light
    vi "Сходство симптомов ещё не доказывает общую причину." (show_side="right", show_kind="speech")
    hide virt
    show virt serious at virt_right, sprite_warm_light
    vi "Однако ваш вопрос позволяет обсудить более важную проблему." (show_side="right", show_kind="speech")
    hide virt
    show virt normal at virt_right, sprite_warm_light
    vi "Если человек знает о природе инналу, добровольно остаётся на планете и всё же вступает с ними в контакт, кто несёт ответственность за последующий провал памяти?" (show_side="right", show_kind="speech")
    vi "Человек или инналу?" (show_side="right", show_kind="speech")
    hide virt

    scene bg lecture hall students at bg_fullscreen with dissolve

    n "Студентка за спиной Эвейны недовольно цокнула. Ответ ей был очевиден." (show_side="none", show_kind="speech")

    show sairen intrigued at sairen_right, sprite_warm_light
    sa "Инналу, конечно." (show_side="right", show_kind="speech")
    sa "Отсутствие контроля не делает их воздействие менее опасным." (show_side="right", show_kind="speech")
    hide sairen

    scene bg lecture hall 2 at bg_fullscreen with dissolve

    n "Вирт спокойно выслушал её и оглядел аудиторию." (show_side="none", show_kind="speech")

    show virt thinking at virt_right, sprite_warm_light
    vi "Разумное замечание." (show_side="right", show_kind="speech")
    hide virt

    show virt serious at virt_right, sprite_warm_light
    vi "У кого-то есть другая точка зрения?" (show_side="right", show_kind="speech")
    hide virt

    n "Взгляд профессора пробежался по залу и остановился на Эвейне." (show_side="none", show_kind="speech")
    n "Под десятками взглядов Эвейна медленно поднялась." (show_side="none", show_kind="speech")

    scene bg scene 2_3 choice at bg_fullscreen with dissolve

    #show eveina eyeroll at eveina_left
    ev_thought "Разумеется. Почему бы не втянуть в спор именно меня?" (show_side="left", show_kind="thought")
    #hide eveina


    $ eveina_innalu_position = renpy.call_screen(
        "choice",
        items=[
            ("Ответственность лежит на инналу.", "responsible"),
            ("Нельзя винить их в природе поля.", "not_guilty")
        ],
        who="Эвейна",
        what="Я думаю, что...",
        _last_say_who="ev"
    )

    if eveina_innalu_position == "responsible":

        ev "Отсутствие намерения не отменяет последствий." (show_side="left", show_kind="speech")
        ev "Если присутствие инналу объективно опасно для людей, ответственность за это воздействие лежит и на них." (show_side="left", show_kind="speech")
        ev "Правила контакта должны соблюдать обе стороны — насколько каждая из них вообще способна что-то контролировать." (show_side="left", show_kind="speech")

        n "Сайрен фыркнула." (show_side="none", show_kind="speech")

        #show sairen intrigued at sairen_right
        sa "Я не просила мне поддакивать." (show_side="right", show_kind="speech")
        #hide sairen

        n "Короткий взгляд Вирта заставил её замолчать." (show_side="none", show_kind="speech")

        scene bg lecture hall 2 at bg_fullscreen with dissolve



        show virt thinking at virt_right, sprite_warm_light
        vi "Ответственность действительно не всегда требует намерения." (show_side="right", show_kind="speech")
        hide virt

        show virt normal at virt_right, sprite_warm_light
        vi "Но прежде чем назначать виновных, полезно установить, кто и что способен контролировать." (show_side="right", show_kind="speech")
        hide virt

    elif eveina_innalu_position == "not_guilty":

        ev "Агрессия предполагает хотя бы возможность выбора." (show_side="left", show_kind="speech")
        ev "Если инналу не управляют собственным полем, их нельзя считать виновными только за то, что они существуют." (show_side="left", show_kind="speech")
        ev "Тем более мы прибыли на их планету, а не наоборот." (show_side="left", show_kind="speech")

        n "Сайрен фыркнула." (show_side="none", show_kind="speech")

        #show sairen intrigued at sairen_right
        sa_offscreen "Типичная позиция защитника мелких собачонок: «Он просто испугался, поэтому и укусил»." (show_side="none", show_kind="speech")
        sa_offscreen "Страх не делает укус менее болезненным." (show_side="none", show_kind="speech")
        #hide sairen

        n "Хмурый взгляд профессора заставил её притихнуть." (show_side="none", show_kind="speech")

        scene bg lecture hall 2 at bg_fullscreen with dissolve

        show virt thinking at virt_right, sprite_warm_light
        vi "Вы отделяете опасность от вины." (show_side="right", show_kind="speech")
        hide virt

        show virt normal at virt_right, sprite_warm_light
        vi "Полезный навык. Пока сочувствие не заставляет забыть об осторожности." (show_side="right", show_kind="speech")
        hide virt

    n "Вирт продолжил лекцию, перейдя к известным случаям провалов памяти и протоколам безопасного взаимодействия с инналу." (show_side="none", show_kind="speech")

    call fade_to_black(0.8, 0.4)
    scene bg lecture hall at bg_fullscreen with dissolve

    n "Когда лекция закончилась, студенты не спешили расходиться." (show_side="none", show_kind="speech")
    n "Одни спорили о природе инналу. Другие вполголоса обсуждали технический сбой и то, насколько можно верить старшекурсникам." (show_side="none", show_kind="speech")

    n "Эвейна поднялась и опёрлась рукой на соседнее кресло." (show_side="none", show_kind="speech")
    n "Запястье снова прошило болью." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left, sprite_warm_light
    ev_thought "Контакт, который невозможно вспомнить." (show_side="left", show_kind="thought")
    hide eveina

    n "Она остановилась посреди прохода." (show_side="none", show_kind="speech")

    show eveina worried at eveina_left, sprite_warm_light
    ev_thought "А если и тогда в саду я была не одна?" (show_side="left", show_kind="thought")
    hide eveina

    n "Девушка обернулась на Вирта, оставшегося у кафедры." (show_side="none", show_kind="speech")
    n "Сообщить о провале памяти означало получить осмотр, наблюдение и чужое решение, пригодна ли она к дальнейшему обучению." (show_side="none", show_kind="speech")
    n "А ещё — риск услышать диагноз, который сделает сходство с отцом чем-то большим, чем ночная паника." (show_side="none", show_kind="speech")
    n "Эвейна предпочитала проблемы, которые можно исследовать на безопасном расстоянии." (show_side="none", show_kind="speech")
    n "Поэтому выбрала более безопасный вариант." (show_side="none", show_kind="speech")

    jump scene_2_3_after_lecture


label scene_2_3_after_lecture:
    $ previous_scene = "scene_2_3"
    $ next_scene = "scene_2_4"
    $ current_scene = "scene_2_3_after_lecture"
    $ kg_prepare_scene("scene_2_3_after_lecture")

    # =========================================================
    # СЦЕНА 3Б — «ПРОВЕРКА ВЕРСИИ»
    # Функция: Эвейна проверяет гипотезу об инналу,
    # получает повод не доверять Вирту и находит Архив.
    # =========================================================

    n "Большая часть студентов уже направилась к выходу. Она вернулась к кафедре." (show_side="none", show_kind="speech")

    scene bg lecture hall 2 at bg_fullscreen with dissolve

    show virt normal at virt_right, sprite_warm_light
    vi "Мисс Хейла." (show_side="right", show_kind="speech")
    hide virt

    show eveina normal at eveina_left, sprite_warm_light
    ev "Профессор, какова вероятность, что инналу может находиться внутри Академии?" (show_side="left", show_kind="speech")
    hide eveina

    n "Вирт посмотрел на неё внимательнее." (show_side="none", show_kind="speech")

    show virt serious at virt_right, sprite_warm_light
    vi "После недавнего технического сбоя — крайне мала." (show_side="right", show_kind="speech")
    hide virt

    show eveina eyebrow at eveina_left, sprite_warm_light
    ev "Почему именно после него?" (show_side="left", show_kind="speech")
    hide eveina

    show virt normal at virt_right, sprite_warm_light
    vi "Купол существовал с момента строительства Академии как аварийный защитный контур." (show_side="right", show_kind="speech")
    vi "До недавних событий он находился в резервном режиме." (show_side="right", show_kind="speech")
    hide virt
    show virt serious at virt_right, sprite_warm_light
    vi "Теперь контур активирован постоянно." (show_side="right", show_kind="speech")
    vi "С момента активации система не зафиксировала ни одного пересечения границы." (show_side="right", show_kind="speech")
    hide virt

    show eveina eyebrow at eveina_left, sprite_warm_light
    ev "А до активации?" (show_side="left", show_kind="speech")
    hide eveina

    n "Вирт ответил не сразу." (show_side="none", show_kind="speech")

    show virt thinking at virt_right, sprite_warm_light
    vi "Инналу всегда жили обособленно." (show_side="right", show_kind="speech")
    hide virt
    show virt normal at virt_right, sprite_warm_light
    vi "Они избегают территории Академии и никогда не выходят на контакт первыми без острой необходимости." (show_side="right", show_kind="speech")
    hide virt

    show eveina thinking at eveina_left, sprite_warm_light
    ev_thought "То есть раньше войти могли." (show_side="left", show_kind="thought")
    ev_thought "Просто, по его мнению, не стали бы." (show_side="left", show_kind="thought")
    hide eveina

    show virt eyebrow at virt_right, sprite_warm_light
    vi "Чем вызван этот вопрос?" (show_side="right", show_kind="speech")
    hide virt

    show eveina smile at eveina_left, sprite_warm_light
    ev "Исключительно любопытством, профессор." (show_side="left", show_kind="speech")
    hide eveina

    show virt smile at virt_right, sprite_warm_light
    vi "Что ж, любопытство в этих стенах приветствуется." (show_side="right", show_kind="speech")
    hide virt

    n "Вирт больше ничего не добавил. Лёгкий жест рукой — и Эвейна была свободна." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left, sprite_warm_light
    ev_thought "Версия не доказана." (show_side="left", show_kind="thought")
    ev_thought "Но невозможной она тоже не стала." (show_side="left", show_kind="thought")
    hide eveina

    n "Эвейна развернулась и тут же уткнулась в чьё-то плечо." (show_side="none", show_kind="speech")

    show kaistr normal at kaistr_right, sprite_warm_light
    unknown "Внимательнее, мисс." (show_side="right", show_kind="speech")
    hide kaistr

    show eveina upset thinking at eveina_left, sprite_warm_light
    ev "Извините." (show_side="left", show_kind="speech")
    hide eveina

    n "Мужчина на секунду задержал на ней взгляд. В его лице мелькнуло раздражение — слишком резкое для случайного столкновения." (show_side="none", show_kind="speech")
    n "Но уже через мгновение он потерял к ней всякий интерес и направился к Вирту." (show_side="none", show_kind="speech")
    n "Эвейна сделала несколько шагов к выходу." (show_side="none", show_kind="speech")

    show kaistr eyebrow at kaistr_right, sprite_warm_light
    unknown "Это твоя подопечная?" (show_side="right", show_kind="speech")
    hide kaistr

    show virt normal at virt_right, sprite_warm_light
    vi "Да." (show_side="right", show_kind="speech")
    hide virt

    show kaistr normal at kaistr_right, sprite_warm_light
    unknown "Сочувствую." (show_side="right", show_kind="speech")
    hide kaistr
    show kaistr thinking at kaistr_right, sprite_warm_light
    unknown "Она тебе никого не напоминает?" (show_side="right", show_kind="speech")
    hide kaistr

    n "Эвейна замедлила шаг." (show_side="none", show_kind="speech")

    scene bg scene 2_3 lecture door eveina at bg_fullscreen with dissolve

    n "Можно было уйти. Вместо этого она остановилась по другую сторону двери." (show_side="none", show_kind="speech")

    #show virt eyebrow at virt_right, sprite_warm_light
    vi_offscreen  "С каких пор ты замечаешь студентов, чьи родители не являются спонсорами твоих исследований?" (show_side="none", show_kind="speech")
    #hide virt

    #show kaistr intrigued at kaistr_right, sprite_warm_light
    un_offscreen  "Просто стало интересно, с чего ты вдруг снова решил поучаствовать в наставничестве." (show_side="none", show_kind="speech")
    #hide kaistr
    #show kaistr eyebrow at kaistr_right, sprite_warm_light
    un_offscreen "Что в ней такого особенного?" (show_side="none", show_kind="speech")
    #hide kaistr

    #show eveina thinking at eveina_left, sprite_warm_light
    ev_thought "О чём это он? Вирт сам меня выбрал?" (show_side="left", show_kind="thought")
    #hide eveina

    scene bg lecture hall 2 at bg_fullscreen with dissolve

    show virt thinking at virt_right, sprite_warm_light
    vi "Даже не знаю." (show_side="right", show_kind="speech")
    show virt eyebrow at virt_right, sprite_warm_light
    vi "Тяга к знаниям? Отличное рекомендательное письмо?" (show_side="right", show_kind="speech")
    hide virt

    show kaistr smile at kaistr_right, sprite_warm_light
    unknown "Ага. А ещё неподдельный интерес в глазах и богатый послужной список." (show_side="right", show_kind="speech")
    hide kaistr
    show kaistr thinking at kaistr_right, sprite_warm_light
    unknown "Ха, кажется, понял..." (show_side="right", show_kind="speech")
    hide kaistr

    show virt serious at virt_right, sprite_warm_light
    vi "Понял что?" (show_side="right", show_kind="speech")
    hide virt

    show kaistr thinking at kaistr_right, sprite_warm_light
    unknown "Кого она мне напоминает." (show_side="right", show_kind="speech")
    hide kaistr
    show kaistr normal at kaistr_right, sprite_warm_light
    unknown "То-то я думаю: вижу впервые, а уже раздражает." (show_side="right", show_kind="speech")
    hide kaistr
    show kaistr eyebrow at kaistr_right, sprite_warm_light
    unknown "Ты ведь тоже заметил сходство?" (show_side="right", show_kind="speech")
    hide kaistr

    show virt thinking at virt_right, sprite_warm_light
    vi "Даже представлять не хочу, что ты там себе выдумал." (show_side="right", show_kind="speech")
    hide virt

    show kaistr intrigued at kaistr_right, sprite_warm_light
    unknown "Аурелиан, ты же понимаешь, что тебя в лучшем случае ждут те же грабли?" (show_side="right", show_kind="speech")
    hide kaistr
    show kaistr normal at kaistr_right, sprite_warm_light
    unknown "А в худшем — снова нож в спину." (show_side="right", show_kind="speech")
    hide kaistr

    show virt normal at virt_right, sprite_warm_light
    vi "Чушь несёшь." (show_side="right", show_kind="speech")
    hide virt
    show virt eyebrow at virt_right, sprite_warm_light
    vi "Зачем пришёл? Полагаю, не студенток обсуждать..." (show_side="right", show_kind="speech")
    hide virt

    scene bg scene 2_3 lecture door eveina at bg_fullscreen with dissolve

    n "Чья-то ладонь коснулась плеча Эвейны." (show_side="none", show_kind="speech")
    n "Она вздрогнула и резко обернулась." (show_side="none", show_kind="speech")

    scene bg lecture door at bg_fullscreen with dissolve

    show leya eyebrow at leya_right, sprite_warm_light
    le "Ви, ты чего тут?" (show_side="right", show_kind="speech")
    hide leya

    show eveina fear at eveina_left, sprite_warm_light
    ev "Ох, чёрт! Напугала..." (show_side="left", show_kind="speech")
    hide eveina

    show leya eyebrow at leya_right, sprite_warm_light
    le "Как первая лекция?" (show_side="right", show_kind="speech")
    hide leya

    show eveina eyeroll at eveina_left, sprite_warm_light
    ev "Познавательно." (show_side="left", show_kind="speech")
    ev "Возможно, нажила себе ещё пару приятелей." (show_side="left", show_kind="speech")
    hide eveina

    show leya eyebrow at leya_right, sprite_warm_light
    le "Приятелей, говоришь? Мне уже стоит переживать?" (show_side="right", show_kind="speech")
    hide leya

    show eveina thinking at eveina_left, sprite_warm_light
    ev "Пока рано." (show_side="left", show_kind="speech")
    hide eveina

    n "Эвейна ещё раз посмотрела на открытую дверь, откуда доносился приглушённый разговор." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left, sprite_warm_light
    ev_thought "С чего бы Вирту становиться моим наставником?" (show_side="left", show_kind="thought")
    ev_thought "И оба считают, что я кого-то им напоминаю." (show_side="left", show_kind="thought")
    hide eveina
    show eveina intrigued at eveina_left, sprite_warm_light
    ev_thought "Очевидно, какую-то любительницу ножевых ранений и садоводства?" (show_side="left", show_kind="thought")
    hide eveina
    show eveina eyeroll at eveina_left, sprite_warm_light
    ev_thought "Очень интересно, но ни хрена не понятно." (show_side="left", show_kind="thought")
    hide eveina

    show leya eyebrow at leya_right, sprite_warm_light
    le "Ви?" (show_side="right", show_kind="speech")
    le "Ты сейчас выглядишь так, будто мысленно вскрываешь сейф." (show_side="right", show_kind="speech")
    hide leya

    show eveina normal at eveina_left, sprite_warm_light
    ev "Почти." (show_side="left", show_kind="speech")
    hide eveina
    show eveina eyeroll at eveina_left, sprite_warm_light
    ev_thought "Впрочем, какое мне дело до воспоминаний двух седеющих мужиков?" (show_side="left", show_kind="thought")
    hide eveina

    n "Эвейна снова открыла академическую базу." (show_side="none", show_kind="speech")
    n "На экране всё ещё висели утренние запросы и закрытые ссылки." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left, sprite_warm_light
    ev "Студенческий профиль почти ничем не отличается от публичного." (show_side="left", show_kind="speech")
    hide eveina
    show eveina eyebrow at eveina_left, sprite_warm_light
    ev "Лея, если в общей базе чего-то нет, где ищут внутренние материалы?" (show_side="left", show_kind="speech")
    hide eveina

    show leya thinking at leya_right, sprite_warm_light
    le "Сестре я ещё не успела написать." (show_side="right", show_kind="speech")
    hide leya
    show leya normal at leya_right, sprite_warm_light
    le "Но она раньше говорила, что общая база — это витрина." (show_side="right", show_kind="speech")
    hide leya

    show eveina eyebrow at eveina_left, sprite_warm_light
    ev "Витрина?" (show_side="left", show_kind="speech")
    hide eveina

    show leya normal at leya_right, sprite_warm_light
    le "То, что удобно показывать первокурсникам, проверяющим комиссиям и людям, которые любят слово «прозрачность»." (show_side="right", show_kind="speech")
    le "А если ей нужны были старые отчёты или внутренняя академическая муть, она шла в архив." (show_side="right", show_kind="speech")
    hide leya

    show eveina normal at eveina_left, sprite_warm_light
    ev "Там другой уровень доступа?" (show_side="left", show_kind="speech")
    hide eveina

    show leya eyeroll at leya_right, sprite_warm_light
    le "Не совсем. Скорее другой слой мусора." (show_side="right", show_kind="speech")
    hide leya
    show leya normal at leya_right, sprite_warm_light
    le "Старые терминалы, первичные отчёты, кривой поиск." (show_side="right", show_kind="speech")
    le "То, что не попало в нормальную базу или попало так, что лучше бы не попадало." (show_side="right", show_kind="speech")
    hide leya

    show leya normal at leya_right, sprite_warm_light
    le "Иногда там находились вещи, которых в общей базе не было." (show_side="right", show_kind="speech")
    hide leya

    show eveina thinking at eveina_left, sprite_warm_light
    ev_thought "Старые отчёты. Первичные материалы. То, что не успели вычистить." (show_side="left", show_kind="thought")
    hide eveina

    show eveina eyebrow at eveina_left, sprite_warm_light
    ev "Архив, значит..." (show_side="left", show_kind="speech")
    hide eveina

    show leya intrigued at leya_right, sprite_warm_light
    le "Вот этот тон мне уже не нравится." (show_side="right", show_kind="speech")
    hide leya

    jump scene_2_4
