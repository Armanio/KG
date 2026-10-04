
default kael_critique_response = None

label scene_2_5:
    $ previous_scene = "scene_2_4"
    $ next_scene = "scene_2_6"
    $ current_scene = "scene_2_5"
    $ kg_prepare_scene("scene_2_5")

    # =========================================================
    # СЦЕНА 5 — «ПРАКТИКА У КАЭЛЯ / ЗАДАЧА ИДЕНТИКИ»
    # Структура: вход → задача без объяснений → студенты сдаются
    #            → Каэль замечает Эвейну → подначка
    #            → Эвейна продавливает модель → Каэль диагностирует её дефект
    # Эмоция: уязвлённая гордость, злость на себя, начало одержимости задачей
    # =========================================================

    call fade_to_black(1.2, 0.8)
    scene bg lab at bg_fullscreen with dissolve
    # play music "bgm/lab_intro.ogg" fadein 2.0

    # --- Вход ---

    n "Эвейна вошла в лабораторию за десять минут до начала практики." (show_side="none", show_kind="speech")
    n "Лаборатория нейросетевого анализа встретила её прохладой, тишиной и ровным гулом терминалов." (show_side="none", show_kind="speech")

    scene bg scene 2_5 kael 1 at bg_fullscreen with dissolve
    pause(1.0)

    n "У дальней консоли уже кто-то сидел." (show_side="none", show_kind="speech")
    n "Длинные пальцы двигались по панели быстро и точно, словно были продолжением самого терминала." (show_side="none", show_kind="speech")

    scene bg lab at bg_fullscreen with dissolve

    show eveina normal at eveina_left
    ev "Привет." (show_side="left", show_kind="speech")
    hide eveina

    n "Парень не отреагировал." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev_thought "Тоже из неразговорчивых? Ла-адно." (show_side="left", show_kind="thought")
    hide eveina

    n "Она села за соседний терминал и открыла интерфейс." (show_side="none", show_kind="speech")
    n "Через несколько минут в лабораторию вошли ещё двое студентов. Один остановился у двери и хмыкнул." (show_side="none", show_kind="speech")

    show m01 smile at student_right
    unknown "А у нас теперь форму носить необязательно?" (show_side="right", show_kind="speech")
    hide m01

    show m02 smile at student_right
    unknown "Видимо, если очень хочется выглядеть гением, можно сразу начинать с нарушения дресс-кода." (show_side="right", show_kind="speech")
    hide m02

    scene bg scene 2_5 kael 2 at bg_fullscreen with dissolve

    n "Парень у консоли поднял голову." (show_side="none", show_kind="speech")

    # show kael normal at kael_right
    unknown "..." (show_side="left", show_kind="speech")
    # hide kael

    n "Эвейна нахмурилась. Какие бы нарушения ни числились за молчуном, чужое желание самоутвердиться они явно не оправдывали." (show_side="none", show_kind="speech")

    scene bg scene 2_5 kael 3 at bg_fullscreen with dissolve

    # show eveina annoyed at eveina_left
    ev "Не трать на них реакцию. Они просто ищут, за что зацепиться." (show_side="right", show_kind="speech")
    # hide eveina

    n "Он посмотрел на неё — коротко, без выражения. И снова опустил взгляд к терминалу." (show_side="none", show_kind="speech")

    scene bg scene 2_5 kael 4 at bg_fullscreen with dissolve

    n "Но даже за это короткое мгновение Эвейна успела заметить то, чего увидеть не ожидала." (show_side="none", show_kind="speech")
    n "Один глаз был живой — тёплый, зелёно-карий. Второй — ярко-голубой — ловил свет иначе, словно отполированная поверхность." (show_side="none", show_kind="speech")

    # show eveina surprized at eveina_left
    ev_thought "Это имплант? Откуда у студента механический имплант..." (show_side="right", show_kind="thought")
    # hide eveina

    scene bg lab at bg_fullscreen with dissolve

    n "Лаборатория постепенно заполнялась. Преподаватель всё не появлялся." (show_side="none", show_kind="speech")

    show m01 annoyed at student_right
    unknown "Отличное начало. Сам опаздывает, а потом будет рассказывать нам про дисциплину." (show_side="right", show_kind="speech")
    hide m01

    show m02 smile at student_right
    unknown "Может, преподаватель надеется, что мы сами себя обучим? Говорят, тут любят эксперименты." (show_side="right", show_kind="speech")
    hide m02

    n "У дальней консоли раздался тихий, почти усталый выдох. Парень поднялся." (show_side="none", show_kind="speech")

    show kael normal at kael_right
    unknown "Вы двое." (show_side="right", show_kind="speech")
    hide kael

    n "Студенты обернулись." (show_side="none", show_kind="speech")

    show kael normal at kael_right
    unknown "Свободны." (show_side="right", show_kind="speech")
    hide kael

    show m01 annoyed at student_right
    unknown "Что?" (show_side="right", show_kind="speech")
    hide m01

    show kael eyebrow at kael_right
    unknown "Вы ошиблись дверью." (show_side="right", show_kind="speech")
    unknown "Здесь работают с сознанием. Людям, которые не способны удержать собственный язык без присмотра, я не доверю даже учебную симуляцию." (show_side="right", show_kind="speech")
    hide kael

    n "Студенты переглянулись. На их лицах по очереди отразились возмущение, понимание и запоздалое желание провалиться под пол." (show_side="none", show_kind="speech")
    n "Пол такой опции не предоставил, поэтому пришлось воспользоваться дверью." (show_side="none", show_kind="speech")

    n "Эвейна проводила их взглядом и медленно повернулась к парню." (show_side="none", show_kind="speech")
    n "Вздёрнув подбородок, тот меланхолично оглядел оставшихся." (show_side="none", show_kind="speech")
    n "Только тогда она поняла. Он не ждал преподавателя. Он и был тем, кого ждали." (show_side="none", show_kind="speech")

    # --- Начало практики ---

    show kael normal at kael_right
    unknown "Это лаборатория нейросетевого анализа." (show_side="right", show_kind="speech")
    unknown "И я бы предпочёл вас здесь не видеть." (show_side="right", show_kind="speech")
    hide kael
    show kael thinking at kael_right
    unknown "К сожалению, программа курса не учитывает мои предпочтения." (show_side="right", show_kind="speech")
    hide kael

    show eveina eyebrow at eveina_left
    ev_thought "Воу, впечатляющее начало..." (show_side="left", show_kind="thought")
    hide eveina

    show kael normal at kael_right
    unknown "Здесь мы разбираем механизмы, из которых складывается то, что вы называете сознанием." (show_side="right", show_kind="speech")
    unknown "И ломаем их. Иногда случайно. Иногда намеренно." (show_side="right", show_kind="speech")
    hide kael

    n "В наступившей паузе кто-то сдавленно вздохнул." (show_side="none", show_kind="speech")

    show kael eyebrow at kael_right
    unknown "Вы, возможно, думаете, что пришли учиться." (show_side="right", show_kind="speech")
    unknown "Но ошибка в этой лаборатории — не тройка в аттестате." (show_side="right", show_kind="speech")
    unknown "Это чужая личность, разрушенная по вашей вине." (show_side="right", show_kind="speech")
    hide kael

    show kael thinking at kael_right
    unknown "До конца курса дойдёт лишь каждый четвёртый." (show_side="right", show_kind="speech")
    unknown "По статистике, пятнадцать процентов из вас не вернётся уже после этой практики." (show_side="right", show_kind="speech")
    hide kael

    show eveina eyeroll at eveina_left
    ev_thought "Да мы с первой фразы поняли, что просто не будет." (show_side="left", show_kind="thought")
    hide eveina

    show kael normal at kael_right
    unknown "Предлагаю не тратить время друг друга и провести отсев прямо сейчас." (show_side="right", show_kind="speech")
    hide kael

    n "За спиной послышались шаги. Кто-то счёл предупреждение исчерпывающей учебной программой." (show_side="none", show_kind="speech")
    n "Эвейна не двинулась с места. Не потому, что такое начало особенно мотивировало остаться. Просто уйти она себе позволить не могла." (show_side="none", show_kind="speech")

    show kael normal at kael_right
    unknown "Меня зовут Каэль. Те, кто остался, запускайте терминалы." (show_side="right", show_kind="speech")
    ka "Сегодня — ваша первая игрушка. Протокол конфликтующих личностей." (show_side="right", show_kind="speech")
    hide kael

    # --- Протокол конфликтующих личностей (НЕ задача идентики) ---

    n "Интерфейсы ожили. На экранах появился текст задачи." (show_side="none", show_kind="speech")

    show eveina normal at eveina_left
    ev_thought "«Две автономные личности существуют в одном носителе и одновременно претендуют на управление." (show_side="left", show_kind="thought")
    ev_thought "Удаление, объединение или подавление любой из них нарушит целостность носителя." (show_side="left", show_kind="thought")
    ev_thought "Стабилизируйте управление, сохранив обе личности»." (show_side="left", show_kind="thought")
    hide eveina

    n "Эвейна перечитала условия дважды. Потом ещё раз — исключительно из уважения к человеку, который сумел уместить столько издевательства в трёх строках." (show_side="none", show_kind="speech")

    show kael normal at kael_right
    ka "Восемьдесят три попытки до вас. Лишь одна формально успешная." (show_side="right", show_kind="speech")
    hide kael

    show kael intrigued at kael_right
    ka "Сегодня у вас есть шанс улучшить эту статистику." (show_side="right", show_kind="speech")
    hide kael

    show eveina eyeroll at eveina_left
    ev_thought "Очень вдохновляет. Мотивация уровня «прыгни с обрыва — вдруг полетишь»." (show_side="left", show_kind="thought")
    hide eveina

    n "Рядом кто-то тихо выругался." (show_side="none", show_kind="speech")

    # --- Попытки ---

    n "Эвейна открыла модель." (show_side="none", show_kind="speech")

    n "Обе личности обладали собственной памятью, системой ценностей и центром принятия решений." (show_side="none", show_kind="speech")
    n "Проблема начиналась всякий раз, когда носителю требовалось совершить одно действие, а личности отдавали две противоречащие команды." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev_thought "Значит, сначала нужно убрать одновременный перехват управления." (show_side="left", show_kind="thought")
    hide eveina

    n "Эвейна настроила поочерёдный доступ." (show_side="none", show_kind="speech")
    n "Первая личность выбрала действие. Вторая получила управление следом, оценила результат и немедленно всё отменила." (show_side="none", show_kind="speech")
    n "Через три цикла носитель по-прежнему стоял на месте, зато внутренне проделал огромную работу." (show_side="none", show_kind="speech")

    show eveina annoyed at eveina_left
    ev_thought "Хорошо. Очерёдность только растягивает конфликт." (show_side="left", show_kind="thought")
    hide eveina

    n "Она разделила области ответственности." (show_side="none", show_kind="speech")
    n "Одна личность получила контроль над привычными и безопасными действиями. Вторая — над ситуациями, требующими риска и быстрой адаптации." (show_side="none", show_kind="speech")
    n "Модель продержалась до первой ситуации, которая оказалась одновременно привычной, опасной и срочной." (show_side="none", show_kind="speech")

    show eveina wrinkled at eveina_left
    ev_thought "Разумеется. Зачем реальности укладываться в две аккуратные категории?" (show_side="left", show_kind="thought")
    hide eveina

    n "Следующей Эвейна попробовала синхронизацию." (show_side="none", show_kind="speech")
    n "Если обе личности будут одинаково оценивать входящие данные, возможно, конфликт исчезнет ещё до выбора действия." (show_side="none", show_kind="speech")

    n "На первых циклах расхождение действительно уменьшилось." (show_side="none", show_kind="speech")
    n "Вместе с ним начали стираться различия между самими личностями." (show_side="none", show_kind="speech")

    show eveina upset thinking at eveina_left
    ev_thought "Нет. Это уже почти слияние." (show_side="left", show_kind="thought")
    hide eveina

    n "Она отменила изменения." (show_side="none", show_kind="speech")

    show m03 normal at student_right
    st "Мы пришли учиться. Дайте хоть какую-то подсказку." (show_side="right", show_kind="speech")
    hide m03

    n "Каэль, проходя мимо, удостоил его коротким взглядом." (show_side="none", show_kind="speech")

    show kael normal at kael_right
    ka "Если вы хотели готовых ответов — выбрали не ту профессию." (show_side="right", show_kind="speech")
    hide kael

    n "Он остановился у терминала Эвейны." (show_side="none", show_kind="speech")
    n "На её экране обе личности оставались автономными, целыми и совершенно неспособными договориться." (show_side="none", show_kind="speech")

    show kael normal at kael_right
    ka "Надо же, в твоих попытках наблюдается какая-то логика. Любопытно." (show_side="right", show_kind="speech")
    hide kael

    show kael eyebrow at kael_right
    ka "Хотя результат пока тот же." (show_side="right", show_kind="speech")
    hide kael

    show kael intrigued at kael_right
    ka "Иногда побег — тоже решение. Особенно если шансов на победу нет." (show_side="right", show_kind="speech")
    hide kael

    show eveina wrinkled at eveina_left
    ev "Возможно, я просто не люблю сбегать." (show_side="left", show_kind="speech")
    hide eveina

    n "Каэль чуть прищурился. В его взгляде не появилось ни одобрения, ни насмешки. Только интерес исследователя, у которого образец внезапно отказался вести себя прилично." (show_side="none", show_kind="speech")

    show kael eyebrow at kael_right
    ka "Тогда покажи, на что способна." (show_side="right", show_kind="speech")
    hide kael

    n "Он отошёл. Эвейна снова повернулась к модели." (show_side="none", show_kind="speech")


    n "Студенты переглядывались. Кто-то нервно листал конспекты. Кто-то смотрел в экран с выражением человека, уже подсчитавшего стоимость неверно выбранной профессии." (show_side="none", show_kind="speech")
    n "Каэль двигался между терминалами. Он не помогал. Лишь наблюдал и время от времени ронял по слову, чтобы никто не принял его молчание за милосердие." (show_side="none", show_kind="speech")

    show kael normal at kael_right
    ka "Шаблон." (show_side="right", show_kind="speech")
    hide kael

    n "Студент рядом тихо выдохнул." (show_side="none", show_kind="speech")

    show kael eyebrow at kael_right
    ka "Поверхностно." (show_side="right", show_kind="speech")
    hide kael

    n "Другой откинулся на спинку кресла и закрыл глаза." (show_side="none", show_kind="speech")

    show kael annoyed at kael_right
    ka "Это даже не смешно." (show_side="right", show_kind="speech")
    hide kael

    n "Третий собрал вещи и вышел, бормоча под нос весь перечень известных ему нецензурных выражений." (show_side="none", show_kind="speech")

    n "Эвейна почти не смотрела по сторонам." (show_side="none", show_kind="speech")
    n "Она добавила систему оценки: при каждом конфликте управление получала личность, чей вариант лучше соответствовал текущим условиям." (show_side="none", show_kind="speech")

    n "Модель наконец сдвинулась с места." (show_side="none", show_kind="speech")
    n "Одна личность получала управление чаще. Вторая раз за разом оставалась запертой внутри носителя — сохранённой, активной и совершенно бесполезной." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev_thought "Это не подавление. Она по-прежнему участвует в оценке." (show_side="left", show_kind="thought")
    hide eveina

    n "Формулировка звучала убедительно." (show_side="none", show_kind="speech")
    n "Особенно если не смотреть на то, что её выбор больше ни на что не влиял." (show_side="none", show_kind="speech")

    n "Эвейна изменила веса, позволив проигрывающей личности перехватывать управление при критическом расхождении." (show_side="none", show_kind="speech")
    n "Система выдержала несколько циклов, после чего оба центра одновременно признали ситуацию критической." (show_side="none", show_kind="speech")

    show eveina annoyed at eveina_left
    ev_thought "Тогда нужно снизить силу самого конфликта." (show_side="left", show_kind="thought")
    hide eveina

    n "Она ослабила конкурирующие импульсы. Конфликт уменьшился — вместе с активностью самого носителя." (show_side="none", show_kind="speech")

    show eveina upset thinking at eveina_left
    ev_thought "Нет. Это не решение." (show_side="left", show_kind="thought")
    hide eveina

    n "Эвейна вернула параметры и попробовала динамические приоритеты, временную изоляцию, новые пороги вмешательства." (show_side="none", show_kind="speech")
    n "Каждая конструкция выглядела убедительно ровно до того момента, когда система получала право её проверить." (show_side="none", show_kind="speech")

    show kael normal at kael_right
    ka "Все, кто признал очевидное, свободны." (show_side="right", show_kind="speech")
    hide kael

    n "Зашуршали вещи. Заскрипели кресла." (show_side="none", show_kind="speech")
    n "Через минуту в лаборатории осталось трое, потом двое, потом Эвейна одна." (show_side="none", show_kind="speech")

    n "Она снова открыла систему весов." (show_side="none", show_kind="speech")
    n "Если точнее настроить порог, слабая личность не будет полностью отстранена. Только временно. Только там, где мешает действовать." (show_side="none", show_kind="speech")

    show eveina annoyed at eveina_left
    ev_thought "Ещё немного." (show_side="left", show_kind="thought")
    hide eveina

    n "Эвейна снизила допустимую силу конфликтующего сигнала." (show_side="none", show_kind="speech")
    n "График стабилизировался." (show_side="none", show_kind="speech")
    n "Активность обеих личностей упала." (show_side="none", show_kind="speech")


    # --- Каэль диагностирует Эвейну ---

    n "Задача давно перестала быть учебной. Теперь она просто имела наглость не подчиняться." (show_side="none", show_kind="speech")

    show eveina annoyed at eveina_left
    ev_thought "Должен быть другой способ." (show_side="left", show_kind="thought")
    hide eveina

    n "Но вместо того чтобы искать его, Эвейна снова потянулась к настройке весов." (show_side="none", show_kind="speech")

    show eveina wrinkled at eveina_left
    ev_thought "Ещё раз." (show_side="left", show_kind="thought")
    hide eveina

    n "Она внесла очередную корректировку." (show_side="none", show_kind="speech")
    n "Тень легла на экран. Каэль стоял рядом и смотрел не на модель — на неё." (show_side="none", show_kind="speech")

    show kael normal at kael_right
    ka "Ты явно не знаешь, когда стоит остановиться." (show_side="right", show_kind="speech")
    hide kael

    show eveina annoyed at eveina_left
    ev "Я ещё не закончила." (show_side="left", show_kind="speech")
    hide eveina

    show kael eyebrow at kael_right
    ka "Верно. Ты даже не начала." (show_side="right", show_kind="speech")
    hide kael

    show eveina angry at eveina_left
    ev "Это вы так мотивируете студентов?" (show_side="left", show_kind="speech")
    hide eveina

    show kael intrigued at kael_right
    ka "Кажется, мы уже перешагнули ту стадию, когда ты обращалась ко мне на «вы», не считаешь?" (show_side="right", show_kind="speech")
    hide kael

    n "Эвейна поджала губы." (show_side="none", show_kind="speech")

    show eveina wrinkled at eveina_left
    ev_thought "Уже жалею, что вообще с тобой заговорила." (show_side="left", show_kind="thought")
    hide eveina
    show eveina annoyed at eveina_left
    ev "Я не сдамся." (show_side="left", show_kind="speech")
    hide eveina

    show kael normal at kael_right
    ka "Вот в этом и проблема." (show_side="right", show_kind="speech")
    hide kael

    n "Её пальцы продолжали двигаться по панели." (show_side="none", show_kind="speech")

    show kael thinking at kael_right
    ka "Услышав про единственную удачную попытку, ты сразу поставила себе цель повторить её сегодня." (show_side="right", show_kind="speech")
    hide kael

    show kael normal at kael_right
    ka "Но ты ни разу не пыталась понять природу конфликта." (show_side="right", show_kind="speech")
    hide kael

    show eveina angry at eveina_left
    ev "А чем, по-твоему, я занималась?" (show_side="left", show_kind="speech")
    hide eveina

    show kael thinking at kael_right
    ka "Пыталась сделать его послушным." (show_side="right", show_kind="speech")
    hide kael
    show kael normal at kael_right
    ka "Сначала развела личности по углам. Потом назначила, кому и когда позволено управлять." (show_side="right", show_kind="speech")
    ka "А когда они всё равно не подчинились — начала приглушать обеих." (show_side="right", show_kind="speech")
    hide kael
    show kael eyebrow at kael_right
    ka "Все твои попытки сводятся к одному: если система сопротивляется, нужно сильнее на неё надавить." (show_side="right", show_kind="speech")
    hide kael
    show kael eyebrow at kael_right
    ka "И до сих пор считаешь это достоинством." (show_side="right", show_kind="speech")
    hide kael

    n "Эвейна ещё немного снизила допустимую силу конфликтующего сигнала." (show_side="none", show_kind="speech")
    n "График выровнялся. Активность обеих личностей просела почти до минимума." (show_side="none", show_kind="speech")

    show kael normal at kael_right
    ka "Время." (show_side="right", show_kind="speech")
    hide kael

    show eveina wrinkled at eveina_left
    ev_thought "Ещё чуть-чуть..." (show_side="left", show_kind="thought")
    hide eveina

    n "Руки механически продолжали менять настройки, хотя голова уже понимала – это не поможет." (show_side="none", show_kind="speech")

    show kael eyebrow at kael_right
    ka "Хейла." (show_side="right", show_kind="speech")
    hide kael

    n "Очередное движение оборвалось на полпути. Пальцы решили послушаться Каэля. Сама Эвейна такой сговор не одобряла." (show_side="none", show_kind="speech")

    show eveina annoyed at eveina_left
    ev "Мне нужно ещё время." (show_side="left", show_kind="speech")
    hide eveina

    show kael normal at kael_right
    ka "Нет. Тебе нужно понять, что именно ты сейчас делаешь." (show_side="right", show_kind="speech")
    hide kael

    n "Эвейна посмотрела на модель." (show_side="none", show_kind="speech")
    n "Обе личности были сохранены. Обе ограничены. Обе почти лишены возможности влиять на носителя." (show_side="none", show_kind="speech")
    n "Она не устранила конфликт. Только затянула его потуже и назвала стабильностью." (show_side="none", show_kind="speech")

    show eveina upset thinking at eveina_left
    ev "Я не справилась." (show_side="left", show_kind="speech")
    hide eveina

    show kael eyebrow at kael_right
    ka "Это ты и так видишь." (show_side="right", show_kind="speech")
    ka "Но ты всё ещё уверена, что ещё одна попытка заставит систему уступить." (show_side="right", show_kind="speech")
    hide kael

    n "Словно признав поражение, пальцы нехотя соскользнули с терминала." (show_side="none", show_kind="speech")

    show kael normal at kael_right
    ka "Такие, как ты, опасны." (show_side="right", show_kind="speech")
    hide kael

    show eveina eyebrow at eveina_left
    ev "Потому что не сдаются?" (show_side="left", show_kind="speech")
    hide eveina

    show kael thinking at kael_right
    ka "Потому что продолжают давить, когда система уже трещит." (show_side="right", show_kind="speech")
    hide kael

    show kael normal at kael_right
    ka "Иногда это приводит к открытиям." (show_side="right", show_kind="speech")
    ka "Но чаще — ломает то, что ещё можно было сохранить." (show_side="right", show_kind="speech")
    hide kael

    n "Одно дело – нерешённая задача. Это можно было принять." (show_side="none", show_kind="speech")
    n "А вот с тем, что Каэль успел заодно вынести приговор ей, Эвейна мириться не собиралась." (show_side="none", show_kind="speech")

    $ kael_critique_response = renpy.call_screen(
        "choice",
        items=[
            ("Оспорить его вывод целиком", "resist"),
            ("Признать ошибку метода, не свою", "accept"),
        ],
        what="Я опасна? Ну-ну, как же..."
    )

    if kael_critique_response == "resist":
        show eveina annoyed at eveina_left
        ev "Я искала нужный порог. Ты говоришь так, будто я собиралась их сломать." (show_side="left", show_kind="speech")
        hide eveina

        show kael normal at kael_right
        ka "Ты видела, что их сигналы угасают. И продолжала менять параметры." (show_side="right", show_kind="speech")
        hide kael

        show eveina angry at eveina_left
        ev "Потому что прежние не работали. Я остановилась бы, если бы модель начала разрушаться." (show_side="left", show_kind="speech")
        hide eveina

        show kael normal at kael_right
        ka "Она уже перестала отвечать обеим личностям." (show_side="right", show_kind="speech")
        hide kael

        n "Эвейна опустила взгляд себе на колени. С этим спорить было трудно. Слишком трудно, чтобы признавать вслух." (show_side="none", show_kind="speech")

    else:
        show eveina upset thinking at eveina_left
        ev "Я видела, как падает активность. И всё равно сдвинула порог ещё раз." (show_side="left", show_kind="speech")
        hide eveina

        n "Каэль молчал, ожидая продолжения." (show_side="none", show_kind="speech")

        show eveina annoyed at eveina_left
        ev "Ты прав: я перестала искать решение и начала приглушать обеих. Но не надо по одной попытке решать, что я за человек." (show_side="left", show_kind="speech")
        hide eveina

        show kael normal at kael_right
        ka "Тогда в следующий раз остановись прежде, чем кому-либо придётся тебя останавливать." (show_side="right", show_kind="speech")
        hide kael

        n "Ей не понравился его тон. Ещё меньше — что на этот раз возразить было нечего." (show_side="none", show_kind="speech")

    show kael normal at kael_right
    ka "Свободна." (show_side="right", show_kind="speech")
    hide kael

    n "Он отключил терминал и ушёл." (show_side="none", show_kind="speech")

    if kael_critique_response == "resist":
        n "Она действительно видела, что сделала с моделью. Возможно, Каэль был прав насчёт этого порога." (show_side="none", show_kind="speech")
        n "Но один неверный порог ещё не доказывал, что сам подход бесполезен. В следующий раз она доведёт его до результата — и тогда посмотрит, что он скажет." (show_side="none", show_kind="speech")

    else:
        n "Упорство ей ещё понадобится. Только прежде чем снова менять параметры, стоило понять, почему любая попытка заставить личности замолчать приближает модель к провалу." (show_side="none", show_kind="speech")
        n "В следующий раз она начнёт с этого." (show_side="none", show_kind="speech")

    show eveina wrinkled at eveina_left
    ev_thought "К чёрту." (show_side="left", show_kind="thought")
    hide eveina
    show eveina normal at eveina_left
    ev_thought "Сначала архив. Я пришла сюда не ради его задач." (show_side="left", show_kind="thought")
    hide eveina

    n "Она направилась к выходу." (show_side="none", show_kind="speech")
    n "Задача увязалась за ней — незваная, упрямая и уже непозволительно личная." (show_side="none", show_kind="speech")

    jump scene_2_6
