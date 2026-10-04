label scene_2_6:
    $ previous_scene = "scene_2_5"
    $ next_scene = "scene_2_7"
    $ current_scene = "scene_2_6"
    $ kg_prepare_scene("scene_2_6")

    # =========================================================
    # СЦЕНА 6 — «АРХИВ / ДРУГОЙ ПОДХОД»
    # Функция:
    # — показать цену одержимости Эвейны;
    # — столкнуть рациональный подход Каэля с интуитивным подходом Эриана;
    # — оставить интеллектуальный вывод и проверку Эвейне;
    # — получить частичный, а не окончательный результат.
    # =========================================================
        # --- Архив / второй дом ---

    call fade_to_black(1.2, 0.8)
    scene bg archive at bg_fullscreen with dissolve
    # play music "bgm/archive.ogg" fadein 2.0

    # --- Архив / поиски отца ---

    n "Большая часть следующей недели сложилась из занятий, короткого сна и одинаковых вечеров в архиве." (show_side="none", show_kind="speech")
    n "Эвейна научилась обходить зависающие фильтры, восстановила цепочки ссылок между десятками отчётов и составила список проектов, упоминавшихся только в сносках." (show_side="none", show_kind="speech")
    n "Поиск сдвинулся. Но каждая цепочка заканчивалась одинаково: исследование закрыто, перенесено или прекращено." (show_side="none", show_kind="speech")
    n "Оставалось выяснить сущую мелочь: где Академия прячет хоть что-нибудь действительно полезное." (show_side="none", show_kind="speech")

    scene bg archive terminal at bg_fullscreen with dissolve

    show eveina thinking at eveina_left, sprite_warm
    ev_thought "Интересно, кто-нибудь заметит, если я обустрою постель в последнем ряду?" (show_side="left", show_kind="thought")
    hide eveina

    n "На экране висели отчёты по нейрополям, стабилизационным протоколам и старым экспериментам Академии." (show_side="none", show_kind="speech")
    n "Информации становилось больше. Ответов — нет." (show_side="none", show_kind="speech")

    show eveina annoyed at eveina_left, sprite_warm
    ev_thought "Биополе как инструмент влияния. Биополе как фактор когнитивной устойчивости. Биополе как ресурс." (show_side="left", show_kind="thought")
    ev_thought "Биополе как что угодно, кроме способа спасти человека, который забывает собственную дочь." (show_side="left", show_kind="thought")
    hide eveina

    n "Эвейна открыла очередной отчёт." (show_side="none", show_kind="speech")
    n "Введение. Методика. Выводы. Ещё одна аккуратно оформленная бесполезность." (show_side="none", show_kind="speech")

    show eveina upset thinking at eveina_left, sprite_warm
    ev_thought "Нет. Не то." (show_side="left", show_kind="thought")
    hide eveina

    n "Она вернулась к началу страницы. Прочитала первый абзац, потом перечитала. " (show_side="none", show_kind="speech")
    n "Смысл по-прежнему не задерживался в голове." (show_side="none", show_kind="speech")
    n "Вместо него возвращались лаборатория, погасший терминал и холодный голос Каэля." (show_side="none", show_kind="speech")

    show eveina annoyed at eveina_left, sprite_warm
    ev_thought "«Ты явно не знаешь, когда стоит остановиться»." (show_side="left", show_kind="thought")
    hide eveina

    n "Эвейна закрыла глаза." (show_side="none", show_kind="speech")
    n "Тактика не помогла – теперь Каэль раздражал её ещё и в темноте." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left, sprite_warm
    ev_thought "Две автономные личности. Один носитель. Стабилизировать управление, сохранив обе." (show_side="left", show_kind="thought")
    hide eveina

    n "Она посмотрела на отчёт, который открыла ради отца. Потом осторожно перевела взгляд на панель активации проектора." (show_side="none", show_kind="speech")

    show eveina normal at eveina_left, sprite_warm
    ev_thought "Только проверю одну мысль." (show_side="left", show_kind="thought")
    hide eveina

    n "Ложь была такой маленькой и незначительной, что Эвейне не составило труда отмахнуться от неё, как от назойливого насекомого." (show_side="none", show_kind="speech")

    # --- Схема / протокол конфликтующих личностей - Рациональный арбитр ---

    n "На миг она задумалась, потом запустила модель, активировала голограмму и начертила два пересекающихся контура сознания." (show_side="none", show_kind="speech")

    scene bg archive scheme 1 at bg_fullscreen with dissolve
    pause (1.0)

    show eveina thinking at eveina_left, sprite_warm
    ev_thought "Две личности. Один носитель." (show_side="left", show_kind="thought")
    ev_thought "Каждая сохраняет собственную память, ценности и представление о том, что лучше для носителя." (show_side="left", show_kind="thought")
    hide eveina

    n "Она коснулась проекции, добавляя в каждый контур внутренний узел управления." (show_side="none", show_kind="speech")

    scene bg archive scheme 2 at bg_fullscreen with dissolve
    pause (1.0)

    show eveina thinking at eveina_left, sprite_warm
    ev_thought "У каждой — собственный центр принятия решений." (show_side="left", show_kind="thought")
    hide eveina
    show eveina annoyed at eveina_left, sprite_warm
    ev_thought "Если одна уступит, получится подавление." (show_side="left", show_kind="thought")
    ev_thought "Если обе будут управлять одновременно — конфликт продолжит рвать носителя изнутри." (show_side="left", show_kind="thought")
    hide eveina

    n "Она соединила центры прямым каналом." (show_side="none", show_kind="speech")
    n "Модель немедленно воспроизвела знакомый конфликт: каждая личность получила доступ к аргументам другой и использовала их, чтобы спорить ещё убедительнее." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left, sprite_warm
    ev_thought "Прекрасно. Теперь они не только не согласны, но и лучше подготовлены." (show_side="left", show_kind="thought")
    hide eveina

    n "Эвейна стёрла соединение." (show_side="none", show_kind="speech")
    n "На свободном месте под двумя контурами появился третий узел." (show_side="none", show_kind="speech")

    scene bg archive scheme 3 at bg_fullscreen with dissolve
    pause (1.0)

    show eveina thinking at eveina_left, sprite_warm
    ev_thought "Если они не способны выбрать вместе, нужен независимый арбитр." (show_side="left", show_kind="thought")
    ev_thought "Он получит оба варианта, сравнит риски и передаст носителю оптимальную команду." (show_side="left", show_kind="thought")
    hide eveina

    n "Она задала критерии: безопасность, соответствие цели, вероятность успеха." (show_side="none", show_kind="speech")
    n "Запустила короткую симуляцию." (show_side="none", show_kind="speech")

    n "В первом сценарии носитель столкнулся с незнакомым потенциально опасным объектом." (show_side="none", show_kind="speech")
    n "Первая личность потребовала сохранить привычный порядок действий." (show_side="none", show_kind="speech")
    n "Вторая предложила рискованную адаптацию." (show_side="none", show_kind="speech")
    n "Третий узел оценил оба варианта и выбрал первый." (show_side="none", show_kind="speech")

    n "Носитель подчинился. Обе личности остались активны." (show_side="none", show_kind="speech")
    n "Графики впервые не пытались убить друг друга." (show_side="none", show_kind="speech")

    show eveina eyebrow at eveina_left, sprite_warm
    ev_thought "Работает?" (show_side="left", show_kind="thought")
    hide eveina

    n "Эвейна запустила следующий сценарий." (show_side="none", show_kind="speech")
    n "На этот раз арбитр выбрал рискованный вариант. Носитель снова выполнил команду." (show_side="none", show_kind="speech")

    show eveina normal at eveina_left, sprite_warm
    ev_thought "Вот. Им не нужно соглашаться. Достаточно, чтобы кто-то оценивал их выводы со стороны." (show_side="left", show_kind="thought")
    hide eveina

    n "Она уже потянулась к следующему набору параметров, когда между стеллажами послышались шаги." (show_side="none", show_kind="speech")

    # --- Ноа вмешивается ---

    show noa normal at noa_right, sprite_warm
    no "Лея сказала, что я найду тебя здесь." (show_side="right", show_kind="speech")
    hide noa

    n "Эвейна вздрогнула так резко, что едва не смахнула всю проекцию." (show_side="none", show_kind="speech")

    show eveina annoyed at eveina_left, sprite_warm
    ev "Чтоб тебя, Ноа!" (show_side="left", show_kind="speech")
    hide eveina

    show noa smile at noa_right, sprite_warm
    no "Вообще-то я рассчитывал на эмоциональное «Ноа, я так рада, что ты пришёл!», но вижу, ты..." (show_side="right", show_kind="speech")
    hide noa

    show eveina annoyed at eveina_left, sprite_warm
    ev "Не сейчас." (show_side="left", show_kind="speech")
    hide eveina

    show noa intrigued at noa_right, sprite_warm
    no "О, это как раз тот случай, когда «не сейчас» означает «срочно вмешайся, иначе её потеряем»." (show_side="right", show_kind="speech")
    hide noa

    n "Он заглянул через её плечо на проекцию, медленно склонил голову вбок, рассматривая блок-схему." (show_side="none", show_kind="speech")

    show noa normal at noa_right, sprite_warm
    no "Два круга. Два треугольника. Один подозрительный треугольник снизу." (show_side="right", show_kind="speech")
    hide noa

    show eveina fear at eveina_left, sprite_warm
    ev_thought "Он же не поймёт, что я делаю, правда?" (show_side="left", show_kind="thought")
    hide eveina


    n "За годы обучения конкуренция в научном сообществе научила её не делиться собственными гипотезами." (show_side="none", show_kind="speech")
    n "Она с подозрением покосилась на парня." (show_side="none", show_kind="speech")

    show eveina eyeroll at eveina_left, sprite_warm
    ev_thought "Не-ет... Он бы не понял, что я тут делаю, даже если бы я выдала ему документацию." (show_side="left", show_kind="thought")
    hide eveina
    show eveina normal at eveina_left, sprite_warm
    ev "Это схема сознания." (show_side="left", show_kind="speech")
    hide eveina

    show noa smile at noa_right, sprite_warm
    no "А я на секунду подумал, что ты рисуешь очень грустную сову." (show_side="right", show_kind="speech")
    hide noa

    show eveina intrigued at eveina_left, sprite_warm
    ev_thought "Ну ещё бы." (show_side="left", show_kind="thought")
    hide eveina
    show eveina annoyed at eveina_left, sprite_warm
    ev "Очень смешно." (show_side="left", show_kind="speech")
    hide eveina

    show noa smile at noa_right, sprite_warm
    no "Всё-всё. Молчу. Почти." (show_side="right", show_kind="speech")
    hide noa

    n "Он протянул руку к проекции." (show_side="none", show_kind="speech")

    show eveina surprized at eveina_left, sprite_warm
    ev "Не трогай!" (show_side="left", show_kind="speech")
    hide eveina

    n "Поздно." (show_side="none", show_kind="speech")
    n "Пара быстрых линий — и строгая схема превратилась в нечто преступно далёкое от нейрофизиологии." (show_side="none", show_kind="speech")

    scene bg archive scheme 4 at bg_fullscreen with dissolve
    pause (1.0)

    n "Модель жалобно пискнула." (show_side="none", show_kind="speech")
    n "Впрочем, любой бы пискнул, попытайся он воссоздать симуляцию сознания с такими формами." (show_side="none", show_kind="speech")
    n "Эвейна смотрела на результат, хлопая глазами от удивления." (show_side="none", show_kind="speech")

    show eveina fear at eveina_left, sprite_warm
    ev "Какого хрена, Ноа?" (show_side="left", show_kind="speech")
    hide eveina

    show noa eyebrow at noa_right, sprite_warm
    no "Что? Я просто добавил схеме телесности." (show_side="right", show_kind="speech")
    hide noa

    show eveina angry at eveina_left, sprite_warm
    ev "Ты превратил мой протокол в... в..." (show_side="left", show_kind="speech")
    hide eveina

    show noa intrigued at noa_right, sprite_warm
    no "В междисциплинарный проект?" (show_side="right", show_kind="speech")
    hide noa

    show eveina angry at eveina_left, sprite_warm
    ev "Вон." (show_side="left", show_kind="speech")
    hide eveina

    show noa intrigued at noa_right, sprite_warm
    no "Сразу вон? Даже без благодарности за творческий вклад?" (show_side="right", show_kind="speech")
    hide noa

    show eveina annoyed at eveina_left, sprite_warm
    ev "Ноа." (show_side="left", show_kind="speech")
    hide eveina

    show noa upset thinking at noa_right, sprite_warm
    no "Понял, ухожу. Забираю с собой талант, харизму и чувство композиции." (show_side="right", show_kind="speech")
    hide noa

    n "Он отступил, подняв руки в примирительном жесте." (show_side="none", show_kind="speech")

    show noa intrigued at noa_right, sprite_warm
    no "Но если что, нижний треугольник я бы не стирал. Он композиционно важен." (show_side="right", show_kind="speech")
    hide noa

    n "Ноа скрылся между стеллажами, явно довольный собой." (show_side="none", show_kind="speech")

    n "Эвейна осталась перед проекцией, всё ещё красная от злости." (show_side="none", show_kind="speech")
    n "Научной ценности рисунок не приобрёл даже после долгого изучения. Зато достоинство потеряло последние шансы на спасение." (show_side="none", show_kind="speech")

    show eveina eyeroll at eveina_left, sprite_warm
    ev_thought "Прекрасно. Теперь у моей схемы есть сиськи." (show_side="left", show_kind="thought")
    hide eveina

    # --- Появление Эриана ---


    n "Она подняла руку, чтобы поправить схему, когда сзади раздался насмешливый голос." (show_side="none", show_kind="speech")

    show erian intrigued at erian_right, sprite_warm
    unknown  "Смелый выбор форм для академического архива." (show_side="right", show_kind="speech")
    hide erian

    n "Второй раз за последние десять минут Эвейна дёрнулась и даже почти выругалась от неожиданности." (show_side="none", show_kind="speech") 
    n "Голос она узнала раньше, чем успела обернуться. Незнакомец из сада и тёмного коридора — тот самый, который следил за ней и почему-то ожидал, что она его вспомнит." (show_side="none", show_kind="speech")
    n "После пропавшей ночи его вопрос уже не казался неудачной попыткой знакомства." (show_side="none", show_kind="speech")

    show eveina annoyed at eveina_left, sprite_warm
    ev_thought "Да как так-то? Вам тут столы мёдом намазали что ли?" (show_side="left", show_kind="thought")
    hide eveina
    
    n "Но потом пришло осознание, что он появился ровно в тот момент, когда её достоинство валялось на полу рядом с неприличной схемой и дёргало лапкой." (show_side="none", show_kind="speech")

    show eveina fear at eveina_left, sprite_warm
    ev "..." (show_side="left", show_kind="speech")
    hide eveina

    n "Она медленно обернулась." (show_side="none", show_kind="speech")
    n "Парень стоял за её плечом. Его взгляд скользнул по проекции, затем на мгновение задержался на открытом отчёте рядом с терминалом." (show_side="none", show_kind="speech")

    show erian intrigued at erian_right, sprite_warm
    unknown  "Хотя надо признать, композиция выразительная." (show_side="right", show_kind="speech")
    hide erian

    show eveina angry at eveina_left, sprite_warm
    ev "Ты ещё откуда взялся?" (show_side="left", show_kind="speech")
    hide eveina

    show erian normal at erian_right, sprite_warm
    unknown "Из-за стеллажа." (show_side="right", show_kind="speech")
    hide erian

    show eveina annoyed at eveina_left, sprite_warm
    ev "Это был не настоящий вопрос." (show_side="left", show_kind="speech")
    hide eveina

    show erian eyeroll at erian_right, sprite_warm
    unknown "Ответ, в принципе, тоже." (show_side="right", show_kind="speech")
    hide erian

    n "Эвейна резко повернулась к проекции и попыталась стереть рисунок." (show_side="none", show_kind="speech")

    show erian intrigued at erian_right, sprite_warm
    unknown "Не спеши. Я ещё не успел оценить методологию." (show_side="right", show_kind="speech")
    hide erian

    show eveina angry at eveina_left, sprite_warm
    ev "Если ты пришёл поиздеваться, можешь считать задачу выполненной." (show_side="left", show_kind="speech")
    hide eveina

    show erian eyebrow at erian_right, sprite_warm
    unknown "Я ж ещё даже не начал." (show_side="right", show_kind="speech")
    hide erian

    n "Она сжала пальцы в попытке удержать внутри пару крепких выражений. Получалось плохо." (show_side="none", show_kind="speech")

    show erian smile at erian_right, sprite_warm
    unknown "Ты всегда краснеешь, когда занимаешься научной работой, или только когда методология становится особенно... наглядной?" (show_side="right", show_kind="speech")
    hide erian

    show eveina angry at eveina_left, sprite_warm
    ev "Сгинь, пожалуйста." (show_side="left", show_kind="speech")
    hide eveina

    show erian normal at erian_right, sprite_warm
    unknown "Вежливость и грубость в одном предложении. Ты, случаем, не любимица Кайстра?" (show_side="right", show_kind="speech")
    hide erian

    show eveina annoyed at eveina_left, sprite_warm
    ev "Кто это?" (show_side="left", show_kind="speech")
    hide eveina
    show eveina thinking at eveina_left, sprite_warm
    ev "Хотя не, неважно..." (show_side="left", show_kind="speech")
    hide eveina
    show eveina annoyed at eveina_left, sprite_warm
    ev "Выход в той стороне – вот что важно." (show_side="left", show_kind="speech")
    hide eveina

    n "Он не ушёл. Напротив, наклонился ближе к проекции, уже не обращая внимания на анатомический вклад Ноа." (show_side="none", show_kind="speech")

    show erian thinking at erian_right, sprite_warm
    unknown "Любопытно." (show_side="right", show_kind="speech")
    hide erian

    show eveina eyebrow at eveina_left, sprite_warm
    ev "Что именно?" (show_side="left", show_kind="speech")
    hide eveina

    show erian normal at erian_right, sprite_warm
    unknown "Ты пытаешься выглядеть злой, но на самом деле боишься, что я понял схему." (show_side="right", show_kind="speech")
    hide erian

    n "Эвейна поджала губы и сдвинулась, закрывая ему обзор." (show_side="none", show_kind="speech")

    show eveina eyebrow at eveina_left, sprite_warm
    ev "Ты видел неприличную каракулю. Не переоценивай себя." (show_side="left", show_kind="speech")
    hide eveina

    show erian intrigued at erian_right, sprite_warm
    unknown "Я видел два конфликтующих контура, третий узел и твою попытку превратить контроль в решение." (show_side="right", show_kind="speech")
    hide erian

    n "Это прозвучало слишком легко. Эвейна поджала губы." (show_side="none", show_kind="speech")
    n "Красивых, но безмозглых самовлюблённых идиотов можно было терпеть. Умных самовлюблённых идиотов хотелось придушить сразу, пока они не стали проблемой." (show_side="none", show_kind="speech")

    show erian normal at erian_right, sprite_warm
    unknown "Третий узел — арбитр?" (show_side="right", show_kind="speech")
    hide erian

    show eveina eyebrow at eveina_left, sprite_warm
    ev "Ты понял это по сиськам?" (show_side="left", show_kind="speech")
    hide eveina

    show erian intrigued at erian_right, sprite_warm
    unknown "Они придали схеме наглядности." (show_side="right", show_kind="speech")
    hide erian

    n "Эвейна сжала пальцы. Отрицать было бесполезно." (show_side="none", show_kind="speech")

    show eveina annoyed at eveina_left, sprite_warm
    ev "Два центра выдают несовместимые команды. Третий сравнивает их и выбирает оптимальную." (show_side="left", show_kind="speech")
    hide eveina

    show erian normal at erian_right, sprite_warm
    unknown "Рациональный судья над двумя неразумными спорщиками." (show_side="right", show_kind="speech")
    hide erian

    show eveina annoyed at eveina_left, sprite_warm
    ev "Обе личности разумны." (show_side="left", show_kind="speech")
    hide eveina

    show erian intrigued at erian_right, sprite_warm
    unknown "Тем хуже для судьи." (show_side="right", show_kind="speech")
    hide erian

    n "Он бегло просмотрел выставленные Эвейной критерии." (show_side="none", show_kind="speech")

    show erian normal at erian_right, sprite_warm
    unknown "Поздравляю. Ты только что заново изобрела схему Каэля." (show_side="right", show_kind="speech")
    hide erian

    show eveina surprized at eveina_left, sprite_warm
    ev "{i}Его{/i} схему? Хочешь сказать, что единственный, кто решил эту задачу, он сам?" (show_side="left", show_kind="speech")
    hide eveina

    show erian eyebrow at erian_right, sprite_warm
    unknown "А ты ещё не поняла, что всё его обучение – это попытка самоутвердиться?" (show_side="right", show_kind="speech")
    hide erian

    show eveina annoyed at eveina_left, sprite_warm
    ev "Но она работает." (show_side="left", show_kind="speech")
    hide eveina

    show erian normal at erian_right, sprite_warm
    unknown "Обе личности говорят. Третий центр решает, чьё мнение имеет значение." (show_side="right", show_kind="speech")
    unknown "Носитель действует, показатели стабильны, никто не удалён." (show_side="right", show_kind="speech")
    hide erian
    show erian annoyed at erian_right, sprite_warm
    unknown "Полное дерьмо." (show_side="right", show_kind="speech")
    hide erian

    show eveina angry at eveina_left, sprite_warm
    ev "Очень содержательная критика." (show_side="left", show_kind="speech")
    hide eveina

    show erian intrigued at erian_right, sprite_warm
    unknown "Ты добавила третьего участника и отдала ему власть над двумя остальными." (show_side="right", show_kind="speech")
    unknown "Конфликт не исчез. Ты просто поставила над ним начальника." (show_side="right", show_kind="speech")
    hide erian

    show eveina annoyed at eveina_left, sprite_warm
    ev "Зато носитель снова способен действовать." (show_side="left", show_kind="speech")
    hide eveina

    show erian normal at erian_right, sprite_warm
    unknown "Кто из них теперь носитель?" (show_side="right", show_kind="speech")
    hide erian

    n "Эвейна открыла рот и ничего не сказала." (show_side="none", show_kind="speech")

    show erian intrigued at erian_right, sprite_warm
    unknown "Молчишь теперь?" (show_side="right", show_kind="speech")
    hide erian

    show eveina annoyed at eveina_left, sprite_warm
    ev "Раздумываю, что хрустнет в первую очередь — планшет или твоя челюсть." (show_side="left", show_kind="speech")
    hide eveina

    show erian smile at erian_right, sprite_warm
    unknown "Сомневаюсь, что ты на это способна. Слишком дорожишь этой дощечкой." (show_side="right", show_kind="speech")
    hide erian

    n "Она ненавидела, что он был прав. С планшетом, разумеется. Всё остальное ещё требовало проверки." (show_side="none", show_kind="speech")

    show eveina annoyed at eveina_left, sprite_warm
    ev "Ты подслушивал?" (show_side="left", show_kind="speech")
    hide eveina

    show erian thinking at erian_right, sprite_warm
    unknown "Ты очень громко думала." (show_side="right", show_kind="speech")
    hide erian

    show eveina angry at eveina_left, sprite_warm
    ev "Кто ты такой?" (show_side="left", show_kind="speech")
    hide eveina

    show erian smile at erian_right, sprite_warm
    er "Рад, что ты наконец решила спросить. Эриан. Приятно познакомиться." (show_side="right", show_kind="speech")
    hide erian

    show eveina angry at eveina_left, sprite_warm
    ev "Ничего приятного. И я не об этом спрашивала." (show_side="left", show_kind="speech")
    hide eveina

    show erian eyeroll at erian_right, sprite_warm
    er "Тогда я — человек, который умеет сдерживаться и не рисовать подобное в общественных местах." (show_side="right", show_kind="speech")
    hide erian

    show eveina annoyed at eveina_left, sprite_warm
    ev "Это не я нарисовала." (show_side="left", show_kind="speech")
    hide eveina

    show erian eyebrow at erian_right, sprite_warm
    er "Разумеется." (show_side="right", show_kind="speech")
    hide erian

    n "Он снова посмотрел на третий узел." (show_side="none", show_kind="speech")

    show erian normal at erian_right, sprite_warm
    er "Ты всё ещё ищешь того, кто рассудит обе стороны." (show_side="right", show_kind="speech")
    hide erian

    show eveina eyebrow at eveina_left, sprite_warm
    ev "А что ещё должно происходить при конфликте?" (show_side="left", show_kind="speech")
    hide eveina

    n "Эриан протянул руку к проекции." (show_side="none", show_kind="speech")

    show eveina annoyed at eveina_left, sprite_warm
    ev "Эй. Только попробуй пририсовать что-нибудь ещё." (show_side="left", show_kind="speech")
    hide eveina

    show erian intrigued at erian_right, sprite_warm
    er "Трудно превзойти оригинал." (show_side="right", show_kind="speech")
    hide erian

    n "Он провёл две линии от центров личностей к нижнему узлу." (show_side="none", show_kind="speech")

    scene bg archive scheme 5 at bg_fullscreen with dissolve
    pause (1.0)

    show erian normal at erian_right, sprite_warm
    er "Компромисс — это когда обе стороны теряют достаточно, чтобы никто не был доволен." (show_side="right", show_kind="speech")
    er "Тебе нужно не это." (show_side="right", show_kind="speech")
    hide erian

    show eveina thinking at eveina_left, sprite_warm
    ev "Не это..." (show_side="left", show_kind="speech")
    hide eveina

    n "Эриан обвёл нижний узел неровным контуром." (show_side="none", show_kind="speech")

    scene bg archive scheme 6 at bg_fullscreen with dissolve
    pause (1.0)

    show erian normal at erian_right, sprite_warm
    er "Вот, что тебе нужно. Выбор не обязан быть рациональным." (show_side="right", show_kind="speech")
    hide erian

    show eveina intrigued at eveina_left, sprite_warm
    ev "Облачко?" (show_side="left", show_kind="speech")
    hide eveina

    show erian annoyed at erian_right, sprite_warm
    er "В голове у тебя облачко." (show_side="right", show_kind="speech")
    hide erian

    show eveina wrinkled at eveina_left, sprite_warm
    ev_thought "Вот же самовлюблённый придурок." (show_side="left", show_kind="thought")
    hide eveina

    n "Эриан сделал шаг назад и развернулся." (show_side="none", show_kind="speech")

    show eveina annoyed at eveina_left, sprite_warm
    ev "Стой." (show_side="left", show_kind="speech")
    hide eveina

    show erian intrigued at erian_right, sprite_warm
    er "Снова просишь остаться?" (show_side="right", show_kind="speech")
    hide erian

    show eveina wrinkled at eveina_left, sprite_warm
    ev "Я не... Я не про это!" (show_side="left", show_kind="speech")
    hide eveina
    show eveina annoyed at eveina_left, sprite_warm
    ev "Если ты всё это знаешь, почему просто не скажешь, что означает облачко?" (show_side="left", show_kind="speech")
    hide eveina

    show erian eyeroll at erian_right, sprite_warm
    er "Потому что думать за тебя я не нанимался." (show_side="right", show_kind="speech")
    hide erian

    show eveina annoyed at eveina_left, sprite_warm
    ev "А Каэлю это решение почему не отнёс?" (show_side="left", show_kind="speech")
    hide eveina

    show erian intrigued at erian_right, sprite_warm
    er "Ну, мне-то самоутверждаться не нужно." (show_side="right", show_kind="speech")
    hide erian

    show eveina wrinkled at eveina_left, sprite_warm
    ev "Тогда зачем вообще вмешался?" (show_side="left", show_kind="speech")
    hide eveina

    show erian intrigued at erian_right, sprite_warm
    er "Рисунки твои понравились." (show_side="right", show_kind="speech")
    hide erian

    show eveina angry at eveina_left, sprite_warm
    ev "Ой, да пошёл ты..." (show_side="left", show_kind="speech")
    hide eveina

    n "Он даже не обернулся. Через несколько шагов его закрыли стеллажи, оставив девушку наедине со своими мыслями." (show_side="none", show_kind="speech")

    # --- Вывод Эвейны ---

    n "Эвейна снова посмотрела на схему." (show_side="none", show_kind="speech")
    n "Два сознательных центра. Третий узел. И облачко, которое, по мнению Эриана, объясняло всё без единого объяснения." (show_side="none", show_kind="speech")

    show eveina eyebrow at eveina_left, sprite_warm
    ev_thought "И что мне с ним делать?" (show_side="left", show_kind="thought")
    hide eveina

    show eveina annoyed at eveina_left, sprite_warm
    ev_thought "«Выбор не обязан быть рациональным». Очень полезно. Почти инструкция." (show_side="left", show_kind="thought")
    hide eveina

    n "Она потянулась стереть облако." (show_side="none", show_kind="speech")
    n "Остановилась." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left, sprite_warm
    ev_thought "Нерациональный — не значит случайный." (show_side="left", show_kind="thought")
    hide eveina

    n "Страх не требовал расчётов, чтобы заставить тело отступить." (show_side="none", show_kind="speech")
    n "Привычка не устраивала голосование перед каждым движением." (show_side="none", show_kind="speech")
    n "Желание возникало раньше, чем человек успевал объяснить себе, почему ему что-то нужно." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left, sprite_warm
    ev_thought "Третий контур не должен выбирать. Он должен сработать раньше выбора." (show_side="left", show_kind="thought")
    hide eveina

    show eveina surprized at eveina_left, sprite_warm
    ev_thought "Подсознание." (show_side="left", show_kind="thought")
    hide eveina

    show eveina eyebrow at eveina_left, sprite_warm
    ev_thought "Если связать с ним обе личности, оно не выберет победителя — но сможет дать носителю единый импульс." (show_side="left", show_kind="thought")
    hide eveina

    # --- Проверка гипотезы ---

    n "Эвейна убрала критерии рационального арбитра." (show_side="none", show_kind="speech")
    n "Связала оба сознательных центра с общей областью и запустила первый сценарий." (show_side="none", show_kind="speech")

    n "Первая личность потребовала сохранить привычный порядок." (show_side="none", show_kind="speech")
    n "Вторая — немедленно его изменить." (show_side="none", show_kind="speech")
    n "Обе команды дошли до нижнего контура." (show_side="none", show_kind="speech")

    n "Модель замерла." (show_side="none", show_kind="speech")
    n "На мгновение Эвейне показалось, что ничего не изменилось." (show_side="none", show_kind="speech")

    n "Потом носитель отступил." (show_side="none", show_kind="speech")
    n "Не выбрал ни один из предложенных вариантов — просто увеличил дистанцию до источника угрозы." (show_side="none", show_kind="speech")

    show eveina surprized at eveina_left, sprite_warm
    ev_thought "Он действует." (show_side="left", show_kind="thought")
    hide eveina

    n "Эвейна проверила показатели." (show_side="none", show_kind="speech")
    n "Обе личности оставались активны. Ни одна не была подавлена. Конфликт тоже никуда не исчез." (show_side="none", show_kind="speech")
    n "Но впервые он не парализовал носителя." (show_side="none", show_kind="speech")

    show eveina normal at eveina_left, sprite_warm
    ev_thought "Ещё один сценарий." (show_side="left", show_kind="thought")
    hide eveina

    n "Она повысила сложность." (show_side="none", show_kind="speech")
    n "Общий контур снова сформировал импульс — медленнее, с заметным колебанием, но сформировал." (show_side="none", show_kind="speech")

    n "На третьем сценарии нагрузка резко возросла." (show_side="none", show_kind="speech")
    n "Сигналы наложились друг на друга. Нижний контур захлебнулся обратной связью, и модель рухнула." (show_side="none", show_kind="speech")

    show eveina upset thinking at eveina_left, sprite_warm
    ev_thought "Не готово." (show_side="left", show_kind="thought")
    hide eveina

    n "Она просмотрела журнал сбоя." (show_side="none", show_kind="speech")
    n "Связи были нестабильны. Общая область не справлялась с сильным расхождением и начинала возвращать импульсы обратно в сознательные центры." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left, sprite_warm
    ev_thought "Но первые два раза носитель действовал." (show_side="left", show_kind="thought")
    ev_thought "Без арбитра. Без подавления. Без победителя." (show_side="left", show_kind="thought")
    hide eveina

    n "Это ещё не было ответом." (show_side="none", show_kind="speech")
    n "Но впервые ошибка находилась не в самом подходе, а в его настройке." (show_side="none", show_kind="speech")

    # --- Цена ---

    n "Браслет Эвейны мягко завибрировал – сработало установленное ею напоминание о сне." (show_side="none", show_kind="speech")
    n "Эвейна моргнула и посмотрела на часы." (show_side="none", show_kind="speech")

    show eveina surprized at eveina_left, sprite_warm
    ev_thought "Сколько?!" (show_side="left", show_kind="thought")
    hide eveina

    n "Отчёт, ради которого она пришла, всё ещё был открыт на том же абзаце." (show_side="none", show_kind="speech")
    n "За весь вечер Эвейна не продвинулась в поисках для отца ни на строчку." (show_side="none", show_kind="speech")

    show eveina upset thinking at eveina_left, sprite_warm
    ev_thought "Прекрасно. Зато спасла учебную модель от внутренних разногласий." (show_side="left", show_kind="thought")
    hide eveina

    n "Она перенесла схему в браслет, пометив её как непроверенную гипотезу." (show_side="none", show_kind="speech")
    n "Затем закрыла проектор и вернулась к отчёту." (show_side="none", show_kind="speech")

    n "Но слова расплывались перед глазами." (show_side="none", show_kind="speech")
    n "На сегодня Академия закончила делиться своими тщательно отобранными бесполезностями." (show_side="none", show_kind="speech")

    show eveina annoyed at eveina_left, sprite_warm
    ev_thought "Завтра. И завтра я начинаю с отца." (show_side="left", show_kind="thought")
    hide eveina

    n "На этот раз она хотя бы не стала добавлять: «Только проверю одну мысль»." (show_side="none", show_kind="speech")

    jump scene_2_7
