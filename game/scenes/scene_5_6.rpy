label scene_5_6:
    $ previous_scene = "scene_5_5"
    $ next_scene = "scene_5_7"
    $ current_scene = "scene_5_6"
    call fade_to_black(1.2, 0.8)
    scene bg lecture_hall at bg_fullscreen with dissolve

    n "Следующим утром лекционный зал гудел, как улей. Студенты переговаривались, оживлённо жестикулировали, спорили о чём-то, пересказывали слухи." (show_side="none", show_kind="speech")
    n "Сегодня была тема, к которой никто не был равнодушен: нейроимпланты." (show_side="none", show_kind="speech")
    n "Все слышали — почти никто не видел их в деле. А те, кто имел доступ — хранили молчание, как будто речь шла не о технологии, а о тайном оружии." (show_side="none", show_kind="speech")
    n "Эвейна, по привычке, села на последний ряд, пропустив перед собой Лею, которая буквально заставила взять её с собой на эту лекцию." (show_side="none", show_kind="speech")

    show leya eyebrow at leya_right
    le "Не помню такого оживления на лекциях Эзари..." (show_side="right", show_kind="speech")
    hide leya

    show eveina normal at eveina_left
    ev "Просто в воздухе чувствуется запах чего-то особенного." (show_side="left", show_kind="speech")
    hide eveina
    show eveina intrigued at eveina_left
    ev "Или это запах дорогостоящего безумия, встроенного прямо в мозг?" (show_side="left", show_kind="speech")
    hide eveina

    show leya normal at leya_right
    le "Безумие - это если бы нейроимпланты продавались со скидкой на маркетплейсах." (show_side="right", show_kind="speech")
    hide leya

    n "Профессор Эзари начал без прелюдий — его тон, как всегда, был размеренным, даже немного усыпляющим, но в этом сонном тембре таилось знание, которому стоило прислушаться." (show_side="none", show_kind="speech")

    show ezari normal at ezari_right
    ez "Нейроимпланты — это не просто технологическое расширение мозга. Это его перепрошивка." (show_side="right", show_kind="speech")
    ez "Их типы разнообразны: от простейшей фиксации событий — до полной сенсорной модификации." (show_side="right", show_kind="speech")
    ez "Импланты памяти." (show_side="right", show_kind="speech")
    ez "Импланты зрения." (show_side="right", show_kind="speech")
    ez "Эмоциональные фильтры." (show_side="right", show_kind="speech")
    ez "Блокираторы панических реакций." (show_side="right", show_kind="speech")
    ez "Модуляторы сна." (show_side="right", show_kind="speech")
    hide ezari

    n "Лекция оказалась неожиданно захватывающей. Эзари шаг за шагом раскрывал сложные темы — от истории имплантации до спорных клинических случаев." (show_side="none", show_kind="speech")
    n "Он рассказывал о пациентах, чья жизнь изменилась благодаря нейромодуляции, показывал видеозаписи экспериментов, диаграммы, графики активности мозга." (show_side="none", show_kind="speech")
    n "Всё было подано спокойно, с тем самым академическим флёром, за которым прятались истории о страхе, выборе и попытке контролировать собственное сознание." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev_thought "Рассказывает так, будто нейроимплант — это не просто техника, а целая философия." (show_side="left", show_kind="thought")
    hide eveina
    show eveina smile at eveina_left
    ev "Интересно, а можно вставить себе в голову чип, который будет генерировать остроумные ответы в любой ситуации?" (show_side="left", show_kind="speech")
    ev "Если нет, то изобрету его сама и разбогатею!" (show_side="left", show_kind="speech")
    hide eveina

    show leya normal at leya_right
    le "О, я в деле! Сколько же всего можно было бы сказать сестре..." (show_side="right", show_kind="speech")
    hide leya  

    n "Но в один момент у Эвейны сжалось сердце. Профессор Эзари демонстрировал один сложный кейс — женщину, у которой после гибели ребёнка имплант отключил аффективные реакции." (show_side="none", show_kind="speech")
    n "На проекционном экране сменялись кадры видеохроники, а потом крупным планом замерла фотография. Лицо женщины, получившей имплант, стало гладким, как стекло. С ничего не выражающим взглядом." (show_side="none", show_kind="speech")
    n "Затем снова видеоряд. Она снова пошла работать — «функционировать», как выразился профессор." (show_side="none", show_kind="speech")
    n "Но Эвейна, глядя на кадры, не видела «здоровья». Она видела пустоту." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev_thought "Если отключить боль — мы перестаём быть собой?" (show_side="left", show_kind="thought")
    ev_thought "Или становимся собой, наконец, очищенными?" (show_side="left", show_kind="thought")
    hide eveina

    n "Впрочем, казалось, другие не разделяли точку зрения девушки. Некоторые студенты, включая Лею, смотрели на экран, затаив дыхание. Кто-то вслух шепнул:" (show_side="none", show_kind="speech")

    show student confused at student_right
    st "И кто всё это реально использует?" (show_side="right", show_kind="speech")
    hide student

    show ezari normal at ezari_right
    ez "Отличный вопрос! Давайте посмотрим." (show_side="right", show_kind="speech")
    ez "Один из немногих, кто не просто использует, а сам проектировал себе импланты." (show_side="right", show_kind="speech")
    hide ezari

    n "Профессор перевёл взгляд на дверь и она, как по команде, беззвучно открылась." (show_side="none", show_kind="speech")
    n "Высокий темноволосый парень вошёл, не оглянувшись на аудиторию и не смотря на студентов." (show_side="none", show_kind="speech")
    n "Он прошёл уверенным, резким шагом вперёд и остановился в центре зала. Ровный, замкнутый, невозмутимый." (show_side="none", show_kind="speech")

    show kael thinking at kael_right
    ka "..." (show_side="right", show_kind="speech")
    hide kael

    n "Увидев его, Лея внезапно подскочила в кресле." (show_side="none", show_kind="speech")

    show leya normal at leya_right
    le "О, я видела этого парня в столовой, это один из студентов!" (show_side="right", show_kind="speech")
    hide leya     

    show eveina thinking at eveina_left
    ev "Не совсем. Знакомься, Каэль." (show_side="left", show_kind="speech")
    hide eveina

    show leya eyebrow at leya_right
    le "Это твой Каэль? Я думала, он выглядит... несколько старше." (show_side="right", show_kind="speech")
    hide leya 

    show eveina annoyed at eveina_left
    ev "Он не мой. Достояние общественности." (show_side="left", show_kind="speech")
    hide eveina

    show ezari normal at ezari_right
    ez "Каэль — носитель нескольких функциональных прототипов." (show_side="right", show_kind="speech")
    ez "У него два импланта: первый — подавление активности центров, отвечающих за эмоциональные реакции." (show_side="right", show_kind="speech")
    ez "Второй — усиление нейросвязей в областях логики, концентрации и памяти." (show_side="right", show_kind="speech")
    ez "Благодаря им он способен выполнять вычисления, которые не под силу другим. Он работает эффективнее, спит меньше, ошибается реже." (show_side="right", show_kind="speech")
    hide ezari

    n "Эзари повернулся к нему и лёгким, почти отеческим, жестом положил руку на плечо парня." (show_side="none", show_kind="speech")

    show ezari normal at ezari_right
    ez "Мальчик мой…" (show_side="right", show_kind="speech")
    ez "Покажи им. Отключи их." (show_side="right", show_kind="speech")
    hide ezari

    show kael sad at kael_right
    ka "..." (show_side="right", show_kind="speech")
    hide kael

    n "Каэль не двинулся. Эта задержка была едва заметной — но она была. Затем его пальцы медленно поднялись к лицу и чуть коснулись виска. Импланты отключились." (show_side="none", show_kind="speech")
    n "Мир вокруг не изменился. Но он — изменился." (show_side="none", show_kind="speech")
    n "Взгляд, прежде стеклянно-прямой, встрепенулся. Он на секунду прикрыл глаза, хмурясь. А потом открыл." (show_side="none", show_kind="speech")
    n "И... сразу нашёл взглядом её." (show_side="none", show_kind="speech")

    show kael serious at kael_right
    ka "..." (show_side="right", show_kind="speech")
    hide kael

    show eveina normal at eveina_left
    ev_thought "Ну... привет." (show_side="left", show_kind="thought")
    hide eveina

    show leya eyebrow at leya_right
    le "Он точно не твой? Потому что, кажется, что смотрит он именно на тебя." (show_side="right", show_kind="speech")
    hide leya 

    n "Эвейна не ответила, и Лее не оставалось ничего, кроме как переводить непонимающий взгляд с Каэля на соседку и обратно." (show_side="none", show_kind="speech")
    n "Профессор Эзари продолжал рассказ, о том, как отключение импланта влияет на донора и как важно периодически его отключать, чтобы давать мозгу справляться без поддержки." (show_side="none", show_kind="speech")
    n "Каэль всё это время безотрывно смотрел ей в глаза. Между его бровей пролегла складка, а взгляд, хоть и не выражал никаких особых эмоций, но нёс в себе что-то, из-за чего её сердце сжалось." (show_side="none", show_kind="speech")
    n "Что-то хрупкое и почти личное, что обычно тщательно скрывалось действием имплантов." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev_thought "Так вот как выглядишь ты. Настоящий. Живой." (show_side="left", show_kind="thought")
    hide eveina

    show ezari normal at ezari_right
    ez "Спасибо, Каэль." (show_side="right", show_kind="speech")
    ez "На этом всё." (show_side="right", show_kind="speech")
    hide ezari

    n "Каэль перевёл взгляд на профессора. Пальцы снова коснулись виска." (show_side="none", show_kind="speech")
    n "Складка исчезла. Взгляд мгновенно потерял глубину скрытых внутри эмоций и снова стал пронизывающим, резким и слишком спокойным." (show_side="none", show_kind="speech")
    n "Парень коротко кивнул, развернулся и ушёл, всё также ни на кого не смотря." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev_thought "Ну конечно.\nВыключил чувства — и жизнь снова по расписанию." (show_side="left", show_kind="thought")
    ev_thought "Удобно. Особенно если кто-то мешает твоей безупречной производительности. Например… я?" (show_side="left", show_kind="thought")
    hide eveina

    n "Сбоку Эвейна почувствовала робкий толчок." (show_side="none", show_kind="speech")

    show leya eyebrow at leya_right
    le "Всё в порядке?" (show_side="right", show_kind="speech")
    hide leya  

    show eveina normal at eveina_left
    ev "Что? А, да, всё нормально." (show_side="left", show_kind="speech")
    hide eveina 

    show leya normal at leya_right
    le "Это было... увлекательно. Пропущенная лекция от Кайстра точно того стоила." (show_side="right", show_kind="speech")
    hide leya 

    show eveina thinking at eveina_left
    ev "Рада, что она пришлась тебе по вкусу." (show_side="left", show_kind="speech")
    hide eveina 

    show leya eyebrow at leya_right
    le "С тобой точно всё в порядке? Ты как будто не здесь." (show_side="right", show_kind="speech")
    hide leya 

    show eveina thinking at eveina_left
    ev "Да, просто задумалась." (show_side="left", show_kind="speech")
    hide eveina

    n "Подумать и правда было о чём. Взгляд Каэля не выходил из головы. Он видел её. Смотрел именно на неё." (show_side="none", show_kind="speech")
    n "И в этом взгляде была слишком настоящая тоска, чтобы не почувствовать что-то в собственной груди в ответ." (show_side="none", show_kind="speech")

    jump scene_5_7