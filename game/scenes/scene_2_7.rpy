label scene_2_7:
    $ previous_scene = "scene_2_6"
    $ next_scene = "scene_2_8"
    $ current_scene = "scene_2_7"
    $ kg_prepare_scene("scene_2_7")


    # --- Следующий вечер / Архив ---

    call fade_to_black(1.2, 0.8)
    scene bg archive at bg_fullscreen with dissolve
    # play music "bgm/archive.ogg" fadein 2.0

    # --- Лея ---

    n "Десятый вечер в Академии Эвейна снова встретила в архиве. Только на этот раз у неё появилась компания." (show_side="none", show_kind="speech")
    n "Аккуратно поставив тарелку с десертом на стол, Лея плюхнулась за соседний терминал." (show_side="none", show_kind="speech")

    show leya normal at leya_right, sprite_warm
    le "Мы с этими милыми пироженками решили, что тебе нужно подкрепление." (show_side="right", show_kind="speech")
    hide leya 

    n "Эвейна с подозрением покосилась на тарелку." (show_side="none", show_kind="speech")

    show eveina eyebrow at eveina_left, sprite_warm
    ev "А они точно пришли сюда по своей воле?" (show_side="left", show_kind="speech")
    hide eveina

    show leya smile at leya_right, sprite_warm
    le "На самом деле эти милашки были кем-то вероломно украдены из столовой... Но мы об этом никому не расскажем, верно?" (show_side="right", show_kind="speech")
    hide leya
    show leya eyebrow at leya_right, sprite_warm
    le "Что ж, приступим." (show_side="right", show_kind="speech")
    hide leya 

    scene bg archive terminal at bg_fullscreen with dissolve

    n "Она открыла каталог и подтянула к себе часть запросов, лишь выразительным взглядом оценив беспорядок в списках." (show_side="none", show_kind="speech")
    n "Эвейна с улыбкой покосилась на соседку. Зная её любовь к порядку, можно было без труда предположить, что сейчас творится у неё в голове." (show_side="none", show_kind="speech")
    n "Задача Каэля больше не занимала её голову – она ждала своего часа." (show_side="none", show_kind="speech")
    n "А вот поиски исследования по нейротерапии так легко сдаваться не собирались. Прочитанных отчётов становилось больше. Ответов — нет." (show_side="none", show_kind="speech")
    n "Весь её план по выведыванию тайных разработок Академии ломался о простую мысль, которую она с упорством бегущего носорога отказывалась признавать." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left, sprite_warm
    ev_thought "Что, если здесь действительно ничего нет и я проделала весь этот путь зря?" (show_side="left", show_kind="thought")
    hide eveina

    n "Закрыв очередную вкладку, девушка устало провела ладонью по лицу. Глаза жгло. В висках ныло от слишком долгого чтения мелкого текста." (show_side="none", show_kind="speech")
    n "Эвейна откинулась на спинку кресла и машинально оглядела зал." (show_side="none", show_kind="speech")
    n "В дальнем конце архива кто-то сидел за отдельным столом." (show_side="none", show_kind="speech")
    n "Сначала она заметила не человека, а стопки бумажных книг рядом с ним — настоящих, тяжёлых, с плотными корешками и неровными закладками между страницами." (show_side="none", show_kind="speech")
    n "Потом узнала профиль." (show_side="none", show_kind="speech")

    scene bg archive erian books 1 at bg_fullscreen with dissolve
    pause

    scene bg archive terminal at bg_fullscreen with dissolve
    show eveina eyebrow at eveina_left, sprite_warm
    ev_thought "Эриан?" (show_side="left", show_kind="thought")
    hide eveina

    scene bg archive erian books 1 at bg_fullscreen with dissolve
    n "Он сидел, склонившись над раскрытым томом, и неторопливо перелистывал страницу." (show_side="none", show_kind="speech")
    n "На столе перед ним лежали ещё десятки книг, некоторые из них были открыты, словно он читал их все разом." (show_side="none", show_kind="speech")

    scene bg archive terminal at bg_fullscreen with dissolve

    show eveina thinking at eveina_left, sprite_warm
    ev_thought "Надо же. А я думала, эти книги здесь для красоты. Чтобы первокурсники проникались уважением к истокам, так сказать." (show_side="left", show_kind="thought")
    hide eveina

    scene bg archive erian books 1 at bg_fullscreen with dissolve

    n "Эриан не смотрел в её сторону. И это дало возможность Эвейне впервые рассмотреть его как следует." (show_side="none", show_kind="speech")
    n "Она невольно задержала взгляд на тонких пальцах, перелистывающих страницы, на идеальном профиле, которому позавидовали бы античные статуи." (show_side="none", show_kind="speech")

    scene bg archive terminal at bg_fullscreen with dissolve

    show eveina eyebrow at eveina_left, sprite_warm
    ev_thought "Интересно, нарциссические повадки всегда идут в довесок к такой внешности?" (show_side="left", show_kind="thought")
    hide eveina
    show eveina thinking at eveina_left, sprite_warm
    ev_thought "Издалека как приличный человек выглядит. Книжки вон читает." (show_side="left", show_kind="thought")
    hide eveina

    n "Она смотрела на него чуть дольше, чем собиралась. И это было ошибкой." (show_side="none", show_kind="speech")

    scene bg archive erian books 2 at bg_fullscreen with dissolve
    pause

    n "Словно почувствовав её взгляд, Эриан вдруг оторвался от страницы и столкнулся с ней взглядом. Эвейна тут же опустила глаза." (show_side="none", show_kind="speech")

    scene bg archive terminal at bg_fullscreen with dissolve

    show eveina upset thinking at eveina_left, sprite_warm
    ev_thought "Упс..." (show_side="left", show_kind="thought")
    hide eveina
    show eveina annoyed at eveina_left, sprite_warm
    ev_thought "Ещё не хватало, чтобы он подумал, что я на него пялюсь. Вот ещё..." (show_side="left", show_kind="thought")
    hide eveina

    n "Вновь сосредоточившись на задаче, девушка ввела новый запрос. Терминал послушно выдал десятки совпадений." (show_side="none", show_kind="speech")
    n "Первые пять оказались бесполезными. Следующие семь — почти издевательски близкими и всё равно пустыми." (show_side="none", show_kind="speech")
    n "Какое-то время они работали молча, нырнув с головой в болото архивных записей." (show_side="none", show_kind="speech")

    show eveina annoyed at eveina_left, sprite_warm
    ev_thought "Не то." (show_side="left", show_kind="thought")
    ev_thought "Нет." (show_side="left", show_kind="thought")
    ev_thought "И снова нет." (show_side="left", show_kind="thought")
    hide eveina

    n "Пирожное осталось нетронутым. Крем чуть осел по краям, ягоды потемнели от тепла, а Эвейна всё глубже проваливалась в сухие строки чужих исследований." (show_side="none", show_kind="speech")

    show leya normal at leya_right, sprite_warm
    le "Вот это посмотри." (show_side="right", show_kind="speech")
    hide leya

    n "Она отправила ссылку на соседний экран. Эвейна открыла отчёт, пробежала глазами вводную, методику, заключение." (show_side="none", show_kind="speech")

    show eveina angry at eveina_left, sprite_warm
    ev "Снова не то. Блять." (show_side="left", show_kind="speech")
    hide eveina

    n "Слово вышло тихим. Не злым плевком в терминал, а скорее уставшим стоном." (show_side="none", show_kind="speech")
    n "Эвейна закрыла отчёт и уткнулась лицом в ладони." (show_side="none", show_kind="speech")

    show leya sad at leya_right, sprite_warm
    le "Эй." (show_side="right", show_kind="speech")
    hide leya

    n "Она не ответила. Пальцы давили на веки, перед глазами плыли мутные пятна от света терминала." (show_side="none", show_kind="speech")

    show eveina upset thinking at eveina_left, sprite_warm
    ev_thought "Я здесь ничего не найду." (show_side="left", show_kind="thought")
    hide eveina

    n "Мысль больше не была паникой. Именно это пугало сильнее всего." (show_side="none", show_kind="speech")
    n "Она становилась реальностью — спокойной, тяжёлой и почти неоспоримой." (show_side="none", show_kind="speech")

    show eveina upset at eveina_left, sprite_warm
    ev_thought "Не потому что я плохо ищу." (show_side="left", show_kind="thought")
    ev_thought "Не потому что не знаю правильный запрос." (show_side="left", show_kind="thought")
    ev_thought "А потому что нужного ответа здесь просто нет. Или он спрятан так глубоко, что мне до него не добраться." (show_side="left", show_kind="thought")
    hide eveina
    show eveina upset thinking at eveina_left, sprite_warm
    ev_thought "Двести двадцать два дня, пап. Десять дней в Академии – впустую." (show_side="left", show_kind="thought")
    ev_thought "Не говоря уже о том, что сама идея поступления сюда, вероятно, была большой ошибкой." (show_side="left", show_kind="thought")
    hide eveina

    n "Лея молчала. Наверное, поняла, что сейчас любое утешение прозвучит как плохо подобранная ложь." (show_side="none", show_kind="speech")

    # --- Эриан ---

    n "Внезапно на край стола легла книга. Увесистый том — Эвейна почувствовала это даже по глухому звуку, с которым тот опустился на столешницу." (show_side="none", show_kind="speech")
    n "Девушка медленно подняла голову." (show_side="none", show_kind="speech")

    show erian normal at erian_right, sprite_warm
    er "Выглядит мрачно." (show_side="right", show_kind="speech")
    hide erian

    show eveina annoyed at eveina_left, sprite_warm
    ev "Что именно?" (show_side="left", show_kind="speech")
    hide eveina

    show erian eyebrow at erian_right, sprite_warm
    er "Всё. Ты, экран, твои тщетные попытки." (show_side="right", show_kind="speech")
    hide erian
    show erian intrigued at erian_right, sprite_warm
    er "Я мог бы помочь." (show_side="right", show_kind="speech")
    er "Но, признаться, наблюдать за твоим отчаянием — куда интереснее." (show_side="right", show_kind="speech")
    hide erian

    n "Он наклонился чуть ближе, бросил взгляд на открытый терминал и недовольно хмыкнул." (show_side="none", show_kind="speech")

    show erian eyebrow at erian_right, sprite_warm
    er "Твои поисковые запросы будто писала пятилетка. Ты правда считаешь, что так сможешь найти хоть что-то полезное?" (show_side="right", show_kind="speech")
    hide erian

    show eveina angry at eveina_left, sprite_warm
    ev "А ты всегда суёшь свой длинный нос в чужие дела или это просто побочный эффект безразмерного эго?" (show_side="left", show_kind="speech")
    hide eveina

    show erian intrigued at erian_right, sprite_warm
    er "Скорее, побочный эффект врождённого превосходства." (show_side="right", show_kind="speech")
    hide erian
    show erian smile wild at erian_right, sprite_warm
    er "Неприятно, знаю. Но ты же тоже это чувствуешь, правда?" (show_side="right", show_kind="speech")
    hide erian

    n "Её глаза закатились сами. Да так, что чуть шею не свело." (show_side="none", show_kind="speech")

    show eveina eyeroll at eveina_left, sprite_warm
    ev_thought "Нет, ну он это серьёзно?" (show_side="left", show_kind="thought")
    hide eveina
    show eveina annoyed at eveina_left, sprite_warm
    ev_thought "Чувствую... чувствую я неудержимое желание тебя чем-то треснуть." (show_side="left", show_kind="thought")
    hide eveina

    n "Проблема была в том, что это не отменяло второго ощущения: он попадал. Не в сердце, не в душу. Господи, какая пошлость. В раздражение. Точно под кожу." (show_side="none", show_kind="speech")
    n "Эвейна выпрямилась. Усталость не ушла, но под ней резко вспыхнула злость." (show_side="none", show_kind="speech")

    show eveina annoyed at eveina_left, sprite_warm
    ev "Если у тебя есть что сказать — говори. Если нет, можешь вернуться туда, откуда вылез." (show_side="left", show_kind="speech")
    hide eveina

    show erian intrigued at erian_right, sprite_warm
    er "Какая у тебя трогательная вера в то, что нужные ответы лежат на верхушке этой выгребной ямы." (show_side="right", show_kind="speech")
    hide erian

    show eveina eyebrow at eveina_left, sprite_warm
    ev "А где они должны лежать?" (show_side="left", show_kind="speech")
    hide eveina

    show erian normal at erian_right, sprite_warm
    er "У её истоков." (show_side="right", show_kind="speech")
    hide erian

    n "Он коротко кивнул на книгу." (show_side="none", show_kind="speech")

    show erian normal at erian_right, sprite_warm
    er "Если хочешь докопаться до истины, всегда начинай с основ." (show_side="right", show_kind="speech")
    er "С того времени, когда ещё не успели всё причесать, переименовать и убрать в закрытые разделы." (show_side="right", show_kind="speech")
    hide erian

    show eveina thinking at eveina_left, sprite_warm
    ev "И что это?" (show_side="left", show_kind="speech")
    hide eveina

    show erian normal at erian_right, sprite_warm
    er "Книга." (show_side="right", show_kind="speech")
    hide erian

    show eveina eyeroll at eveina_left, sprite_warm
    ev "Я восхищена глубиной твоего ответа." (show_side="left", show_kind="speech")
    hide eveina

    show erian intrigued at erian_right, sprite_warm
    er "Привыкай. Восхищение – обычная реакция в моём присутствии." (show_side="right", show_kind="speech")
    hide erian

    n "Эвейна недовольно поморщила нос, но всё же посмотрела на обложку." (show_side="none", show_kind="speech")
    n "Плотная тёмная ткань, потёртые углы, выцветшее тиснение. Название было выбито мелкими строгими буквами." (show_side="none", show_kind="speech")
    n "{i}«История исследований планеты Иннаки. Первые пятьдесят лет Академии Мемории.»{/i}" (show_side="none", show_kind="speech")

    show eveina surprized at eveina_left, sprite_warm
    ev "Да ты издеваешься." (show_side="left", show_kind="speech")
    hide eveina

    show erian eyebrow at erian_right, sprite_warm
    er "Надо же как-то развлекаться." (show_side="right", show_kind="speech")
    hide erian

    show eveina annoyed at eveina_left, sprite_warm
    ev "Мне нужны не исторические экскурсии." (show_side="left", show_kind="speech")
    hide eveina

    show erian normal at erian_right, sprite_warm
    er "Тогда можешь продолжать ковыряться в этом мусоре." (show_side="right", show_kind="speech")
    hide erian

    n "Он лениво кивнул на терминал и нахально улыбнулся. Почему-то захотелось швырнуть в него книгой." (show_side="none", show_kind="speech")

    show eveina angry at eveina_left, sprite_warm
    ev "Ты даже понятия не имеешь, что я ищу." (show_side="left", show_kind="speech")
    hide eveina

    show erian intrigued at erian_right, sprite_warm
    er "А ты – что можешь найти." (show_side="right", show_kind="speech")
    hide erian

    n "Ответ ударил неприятнее, чем должен был. Эвейна опустила глаза, размышляя." (show_side="none", show_kind="speech")

    show eveina upset thinking at eveina_left, sprite_warm
    ev_thought "А что, если он прав?" (show_side="left", show_kind="thought")
    hide eveina
    
    n "Девушка искоса взглянула на соседку. Та усердно игнорировала диалог, продолжая копаться в отчётах. Поддержки ждать было неоткуда." (show_side="none", show_kind="speech")
    n "Эвейна снова взглянула на парня, внезапно поняв, что он склонился ещё ближе к терминалу, из-за чего они чуть не столкнулись лбами." (show_side="none", show_kind="speech")
    n "Вроде и не коснулся, и даже не смотрел на неё, но это почему-то взбесило ещё больше. Он вторгался в её личное пространство так, будто формально ничего не нарушал." (show_side="none", show_kind="speech")

    show eveina annoyed at eveina_left, sprite_warm
    ev "Может, мне мебель подвинуть, чтобы ты разместился чуть подальше от меня?" (show_side="left", show_kind="speech")
    hide eveina

    n "Эриан хмыкнул и отстранился. Его рука напоследок, как бы между прочим, закрыла несколько окон в терминале." (show_side="none", show_kind="speech")

    show eveina angry at eveina_left, sprite_warm
    ev "Эй! А ну руки прочь!" (show_side="left", show_kind="speech")
    hide eveina

    show erian smile at erian_right, sprite_warm
    er "Там всё равно ничего нет. Всего лишь экономлю тебе время." (show_side="right", show_kind="speech")
    hide erian

    n "Эвейна открыла рот, чтобы красноречиво рассказать ему всё, что она думает о его помощи. Но Эриан уже развернулся и двинулся к своему столу." (show_side="none", show_kind="speech")
    n "Книга осталась лежать на столе — чужая, тяжёлая и до невозможности подозрительная." (show_side="none", show_kind="speech")

    show eveina eyeroll at eveina_left, sprite_warm
    ev_thought "Ну да, ну да... Пыльный кирпич сейчас спасёт ситуацию." (show_side="left", show_kind="thought")
    hide eveina

    n "Она несколько секунд смотрела на том, не прикасаясь. Потом всё-таки подтянула его ближе." (show_side="none", show_kind="speech")

    # --- Книга ---

    n "Книга оказалась тяжелее, чем выглядела." (show_side="none", show_kind="speech")
    n "Девушка пролистала первые страницы. Открытие планеты Иннаки, первые экспедиции, строительство Академии Мемории." (show_side="none", show_kind="speech")
    n "Политические соглашения, финансирование, первые лабораторные корпуса, споры о статусе местных биоформ." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left, sprite_warm
    ev_thought "Эриан, если это шутка такая, то у тебя отвратительное чувство юмора." (show_side="left", show_kind="thought")
    hide eveina

    n "Но любопытство взяло своё. Эвейна лениво перевернула ещё несколько страниц. Читать это внимательно сил не было." (show_side="none", show_kind="speech")
    n "Она скользила взглядом по заголовкам, цепляясь только за знакомые слова." (show_side="none", show_kind="speech")

    show eveina wrinkled at eveina_left, sprite_warm
    ev_thought "Если ничего в ней не найду, точно приложу её о его голову." (show_side="left", show_kind="thought")
    hide eveina

    n "Ближе к концу книги страницы стали плотнее, словно редкий читатель дочитывал её до конца." (show_side="none", show_kind="speech")
    n "Меньше общей истории, больше списков проектов: номера, краткие описания, инициаторы, даты, пометки о переносе в отдельные архивы." (show_side="none", show_kind="speech")
    n "Эвейна почти не глядя пролистывала страницы одну за другой, пока не остановилась." (show_side="none", show_kind="speech")

    show eveina surprized at eveina_left, sprite_warm
    ev "Эм..." (show_side="left", show_kind="speech")
    hide eveina

    n "Уставший взгляд зацепился за странную сноску, небрежно обведённую чьей-то рукой." (show_side="none", show_kind="speech")
    n "{i}«NR-D3: Проект нейрогенеративной терапии. Первичный контур восстановления когнитивных связей при прогрессирующем распаде памяти. Инициатор: @KAIRDALON.»{/i}" (show_side="none", show_kind="speech")
    n "Эвейна перечитала сноску. Потом ещё раз. Буквы не изменились." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left, sprite_warm
    ev_thought "Нейрогенеративная терапия..." (show_side="left", show_kind="thought")
    ev_thought "Кайр Далон?" (show_side="left", show_kind="thought")
    hide eveina

    n "За эти дни, проведённые в архиве, она встречала одни и те же имена десятки раз, но ни разу не видела упоминаний о Кайре Далоне." (show_side="none", show_kind="speech")
    n "Да и в классификаторе проекта с таким номером не находила." (show_side="none", show_kind="speech")

    show eveina annoyed at eveina_left, sprite_warm
    ev_thought "Нет. Так не бывает." (show_side="left", show_kind="thought")
    ev_thought "Если это было реальное исследование, оно должно быть в базе." (show_side="left", show_kind="thought")
    hide eveina

    n "Эвейна резко развернулась к терминалу. Пальцы застучали по панели чуть с большим усилием, чем требовалось." (show_side="none", show_kind="speech")

    show eveina normal at eveina_left, sprite_warm
    ev_thought "NR-D3." (show_side="left", show_kind="thought")
    hide eveina

    n "Запрос ушёл в архивную систему. Терминал бодро мигнул, выдав ответ слишком быстро." (show_side="none", show_kind="speech")
    n "{i}«Совпадений не найдено.»{/i}" (show_side="none", show_kind="speech")

    show eveina eyebrow at eveina_left, sprite_warm
    ev_thought "Чушь." (show_side="left", show_kind="thought")
    hide eveina

    n "Она ввела полное название. Потом часть названия. Потом «нейрогенеративная терапия». Потом «прогрессирующий распад памяти»." (show_side="none", show_kind="speech")
    n "Потом только одно слово." (show_side="none", show_kind="speech")

    show eveina annoyed at eveina_left, sprite_warm
    ev_thought "KAIRDALON" (show_side="left", show_kind="thought")
    hide eveina

    n "{i}«Совпадений не найдено.»{/i}" (show_side="none", show_kind="speech")

    n "Эвейна замерла." (show_side="none", show_kind="speech")
    n "Потом медленно посмотрела обратно на страницу книги." (show_side="none", show_kind="speech")

    show eveina annoyed at eveina_left, sprite_warm
    ev_thought "Кто ты такой, Кайр Далон?" (show_side="left", show_kind="thought")
    ev_thought "И почему тебя вырезали так аккуратно, что даже шрама не осталось?" (show_side="left", show_kind="thought")
    hide eveina

    n "Она снова подняла взгляд, машинально ища Эриана в дальнем конце зала." (show_side="none", show_kind="speech")
    n "Стол, за которым он сидел, был пуст." (show_side="none", show_kind="speech")

    # --- Лея ---

    show eveina eyebrow at eveina_left, sprite_warm
    ev "Лея, ты не видела, куда он ушёл?" (show_side="left", show_kind="speech")
    hide eveina

    show leya eyebrow at leya_right, sprite_warm
    le "Кто?" (show_side="right", show_kind="speech")
    hide leya

    n "Эвейна с удивлением посмотрела на подругу. Потом скосила взгляд на терминал Леи: три открытых отчёта, заметки на полях, перечень ссылок, в котором нормальный человек утонул бы с первой строки." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left, sprite_warm
    ev_thought "Конечно. Она всё это время сидела носом в отчётах." (show_side="left", show_kind="thought")
    hide eveina

    show eveina normal at eveina_left, sprite_warm
    ev "Неважно. Один... парень тут был." (show_side="left", show_kind="speech")
    hide eveina

    show leya normal at leya_right, sprite_warm
    le "Не видела, извини." (show_side="right", show_kind="speech")
    hide leya

    show eveina eyeroll at eveina_left, sprite_warm
    ev "Забудь." (show_side="left", show_kind="speech")
    hide eveina

    n "Лея устало кивнула и снова повернулась к экрану." (show_side="none", show_kind="speech")
    n "Опустив взгляд на страницу, Эвейна провела пальцем по чернилам, что обвели такую нужную ей сноску." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left, sprite_warm
    ev_thought "Это Эриан сделал?" (show_side="left", show_kind="thought")
    hide eveina
    show eveina normal at eveina_left, sprite_warm
    ev_thought "Странно, они не выглядят свежими." (show_side="left", show_kind="thought")
    hide eveina
    show eveina annoyed at eveina_left, sprite_warm
    ev_thought "Кому вообще в голову пришло портить бумажный экземпляр?" (show_side="left", show_kind="thought")
    hide eveina

    n "Но в глубине души она была благодарна этому неизвестному хулигану." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left, sprite_warm
    ev_thought "Вдруг в ней есть что-то ещё полезное?" (show_side="left", show_kind="thought")
    hide eveina
    show eveina upset thinking at eveina_left, sprite_warm
    ev_thought "Проект удалили из базы. Имя тоже." (show_side="left", show_kind="thought")
    ev_thought "Если кто-то узнает, что я нашла этот экземпляр, книга может исчезнуть следом." (show_side="left", show_kind="thought")
    hide eveina
    show eveina normal at eveina_left, sprite_warm
    ev_thought "Я не могу оставить её здесь." (show_side="left", show_kind="thought")
    hide eveina

    n "Мысль прозвучала слишком спокойно." (show_side="none", show_kind="speech")
    n "Даже не как решение. Как факт, который просто дождался своей очереди, игнорируя один из строжайших запретов архива – не выносить данные наружу." (show_side="none", show_kind="speech")
    n "Эвейна закрыла книгу и подтянула к себе сумку. Планшет скользнул внутрь первым. Следом, уже осторожнее, она убрала тяжёлый том." (show_side="none", show_kind="speech")
    n "Рука застегнула сумку чуть быстрее, чем следовало. Девушка поднялась." (show_side="none", show_kind="speech")

    show leya eyebrow at leya_right, sprite_warm
    le "Ты чего?" (show_side="right", show_kind="speech")
    hide leya

    show eveina normal at eveina_left, sprite_warm
    ev "Хватит на сегодня." (show_side="left", show_kind="speech")
    hide eveina

    show leya thinking at leya_right, sprite_warm
    le "Серьёзно?" (show_side="right", show_kind="speech")
    hide leya

    show eveina upset thinking at eveina_left, sprite_warm
    ev "Если я сейчас открою ещё один отчёт, я либо усну лицом в терминал, либо начну кусаться." (show_side="left", show_kind="speech")
    hide eveina

    show leya smile at leya_right, sprite_warm
    le "Кусаться ты начала с момента своего прибытия." (show_side="right", show_kind="speech")
    hide leya

    show eveina eyeroll at eveina_left, sprite_warm
    ev "Справедливо." (show_side="left", show_kind="speech")
    hide eveina

    n "Лея закрыла свои окна, собрала заметки и забрала контейнер с пирожными." (show_side="none", show_kind="speech")
    n "Эвейна подняла сумку. Плечо сразу отозвалось тяжестью." (show_side="none", show_kind="speech")

    show eveina annoyed at eveina_left, sprite_warm
    ev_thought "Невероятно незаметно, Хейла. Просто образец преступного мастерства." (show_side="left", show_kind="thought")
    hide eveina

    call fade_to_black(1.2, 0.8)
    scene bg archive corridor night at bg_fullscreen with dissolve

    n "Но до комнаты она не дошла. На полпути браслет мягко завибрировал." (show_side="none", show_kind="speech")
    n "{i}«Мисс Хейла, прошу вас зайти ко мне в кабинет, как только сможете. Аурелиан Вирт.»{/i}" (show_side="none", show_kind="speech")
    n "Эвейна остановилась посреди коридора. Сумка на плече вдруг стала вдвое тяжелее." (show_side="none", show_kind="speech")

    show eveina fear at eveina_left, sprite_night_mixed
    ev_thought "Он знает." (show_side="left", show_kind="thought")
    hide eveina

    n "Мысль была глупой, поспешной, и почти наверняка параноидальной. Но пальцы всё равно начали предательски дрожать." (show_side="none", show_kind="speech")
    n "Лея не сразу заметила, что Эвейна отстала." (show_side="none", show_kind="speech")

    show leya normal at leya_right, sprite_night_mixed
    le "Эй, ты идёшь?" (show_side="right", show_kind="speech")
    hide leya

    show eveina thinking at eveina_left, sprite_night_mixed
    ev "Позже. Вирт вызвал к себе." (show_side="left", show_kind="speech")
    hide eveina

    show leya annoyed at leya_right, sprite_night_mixed
    le "В такое позднее время? Отчёт ему задолжала, что ли?" (show_side="right", show_kind="speech")
    hide leya

    show eveina upset thinking at eveina_left, sprite_night_mixed
    ev_thought "Ага, отчёт и хорошее оправдание." (show_side="left", show_kind="thought")
    hide eveina

    n "Эвейна пожала плечами, устало выдохнула и свернула в сторону преподавательского крыла." (show_side="none", show_kind="speech")

    jump scene_2_8
