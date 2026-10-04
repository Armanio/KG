label scene_1_3:
    $ previous_scene = "scene_1_2"
    $ next_scene = "scene_1_4"
    $ current_scene = "scene_1_3"
    $ kg_prepare_scene("scene_1_3")
 
    call fade_to_black(0.8, 0.5)
    scene bg scene 1_3 hall 1 at bg_fullscreen with dissolve

    n "Холл гудел голосами. Повсюду звучали приветствия, короткие объятия, перекатывающийся смех." (show_side="none", show_kind="speech")
    n "Многие здесь были детьми тех, кто управлял галактикой. И почти все они — уже знакомы между собой." (show_side="none", show_kind="speech")
    n "Эвейна обвела взглядом всех новоприбывших и быстро поняла: если в этом зале кто-то и был чужим элементом, то, скорее всего, именно она." (show_side="none", show_kind="speech")

    # --- Знакомство со второстепенными персонажами ---

    show noa intrigued at noa_right, sprite_warm_light
    unknown "Сайрен, дорогая, чего такое недовольное лицо?" (show_side="right", show_kind="speech")
    hide noa
    show noa eyebrow at noa_right, sprite_warm_light
    unknown "Уже ищешь себе жертву?" (show_side="right", show_kind="speech")
    hide noa

    show sairen normal at sairen_right, sprite_warm_light
    sa "Какого чёрта они заставляют нас стоять здесь столько времени?" (show_side="right", show_kind="speech")
    hide sairen

    show noa smile at noa_right, sprite_warm_light
    unknown "Я всегда готов подставить тебе своё плечо." (show_side="right", show_kind="speech")
    hide noa
    show noa thinking at noa_right, sprite_warm_light
    unknown "Только давай в этот раз без ядовитых укусов." (show_side="right", show_kind="speech")
    hide noa

    show sairen angry at sairen_right, sprite_warm_light
    sa "Ой, отвали. Между нами ничего больше не будет." (show_side="right", show_kind="speech")
    hide sairen

    show noa eyebrow at noa_right, sprite_warm_light
    unknown "Да мне больше и не надо. В прошлый раз и так был исчерпывающий образовательный опыт..." (show_side="right", show_kind="speech")
    hide noa

    show sairen angry at sairen_right, sprite_warm_light
    sa "Ноа. Ещё слово — и я устрою тебе второй. Посмертный." (show_side="right", show_kind="speech")
    hide sairen

    show silas smile at silas_right, sprite_warm_light
    unknown "Принцесса сегодня не в духе?" (show_side="right", show_kind="speech")
    hide silas

    show m03 smile at student_right, sprite_warm_light
    unknown "Я бы тоже был не в духе, если бы узнал, что учиться мне придётся с вами." (show_side="right", show_kind="speech")
    hide m03
    show m03 normal at student_right, sprite_warm_light
    unknown "Хотя погодите..." (show_side="right", show_kind="speech")
    hide m03

    scene bg hall wall at bg_fullscreen with dissolve

    n "Эвейна уже успела подойти к стойке регистрации, но ИИ велел ждать общего инструктажа. Без нового браслета доступ к базе не активировался." (show_side="none", show_kind="speech")
    n "Теперь она стояла немного в стороне, облокотившись на мягкую стену из сот, и наблюдала за будущими однокурсниками." (show_side="none", show_kind="speech")

    show eveina normal at eveina_left,sprite_warm_light
    ev_thought "Элита галактики. Будущее человечества." (show_side="left", show_kind="thought")
    hide eveina
    show eveina eyeroll at eveina_left, sprite_warm_light
    ev_thought "Стоит признать, шансов на выживание у нас маловато..." (show_side="left", show_kind="thought")
    hide eveina

    # --- Инструктаж ИИ ---

    scene bg scene 1_3 hall 1 at bg_fullscreen with dissolve
    pause (0.5)
    scene bg scene 1_3 hall 2 at bg_fullscreen with dissolve

    n "Свечение в центре зала изменилось — сигнал к началу вводного инструктажа." (show_side="none", show_kind="speech")
    n "Гул в холле мгновенно стих." (show_side="none", show_kind="speech")

    #show ai at ai_right
    ai_offscreen "Внимание, первокурсники. Добро пожаловать в Академию Мемория на планете Иннаки." (show_side="none", show_kind="speech")
    ai_offscreen "В связи с недавним техническим сбоем Академия временно переведена в усиленный режим безопасности." (show_side="none", show_kind="speech")
    ai_offscreen "Самовольные контакты с представителями народа инналу запрещены. Все взаимодействия – строго регламентированы." (show_side="none", show_kind="speech")

    ai_offscreen "Аварийный защитный купол активирован и работает в режиме изоляции." (show_side="none", show_kind="speech")
    ai_offscreen "Проникновение за пределы разрешённой зоны, ограниченной куполом — нарушение первого уровня." (show_side="none", show_kind="speech")
    ai_offscreen "Попытки исследовать территорию инналу без официального допуска приведут к немедленному отчислению и депортации." (show_side="none", show_kind="speech")

    ai_offscreen "Каждому из вас будет выдан браслет со всеми необходимыми доступами, мессенджером, навигацией и ИИ-ассистентом." (show_side="none", show_kind="speech")
    ai_offscreen "Нахождение на территории Академии без браслета — нарушение второго уровня." (show_side="none", show_kind="speech")
    ai_offscreen "Личные устройства связи подлежат сдаче." (show_side="none", show_kind="speech")

    ai_offscreen "Доступ к глобальной сети сохраняется через академический браслет, стационарные терминалы в жилом и учебном секторах." (show_side="none", show_kind="speech")
    ai_offscreen "Использование других внешних устройств и средств связи — нарушение второго уровня." (show_side="none", show_kind="speech")
    ai_offscreen "В ближайшее время каждого из вас вызовут для прохождения ознакомительных экскурсий в небольших группах. До этого момента, пожалуйста, находитесь в этом холле." (show_side="none", show_kind="speech")
    #hide ai


    n "Наступила тишина. А потом, как по команде, вспыхнули шёпоты." (show_side="none", show_kind="speech")

    # --- Реакции студентов ---

    scene bg scene 1_3 hall 1 at bg_fullscreen with dissolve

    show noa angry at noa_right, sprite_warm_light
    no "Это Академия или тюрьма? А поссать без их браслета я могу сходить?" (show_side="right", show_kind="speech")
    hide noa

    show m03 smile at student_right, sprite_warm_light
    unknown "На этот случай у них есть ещё нарушения третьего уровня." (show_side="right", show_kind="speech")
    hide m03

    show tero thinking at tero_right, sprite_warm_light
    unknown "Раньше такого не было." (show_side="right", show_kind="speech")
    hide tero
    show tero normal at tero_right, sprite_warm_light
    unknown "Сестра выпустилась этой весной — никаких академических браслетов, купол вообще держали выключенным." (show_side="right", show_kind="speech")
    hide tero
    show tero upset thinking at tero_right, sprite_warm_light
    unknown "После того случая месяц назад всё закрутили. Говорят, всё из-за инналу." (show_side="right", show_kind="speech")
    hide tero

    show m03 annoyed at student_right, sprite_warm_light
    unknown "Старшекурсники рассказывали, что после него несколько человек не могли вспомнить, что происходило в Академии." (show_side="right", show_kind="speech")
    hide m03

    show sairen angry at sairen_right, sprite_warm_light
    sa "Старшекурсники много чего рассказывают. Никто толком не знает, что тогда произошло." (show_side="right", show_kind="speech")
    hide sairen

    scene bg hall wall at bg_fullscreen with dissolve

    show eveina thinking at eveina_left, sprite_warm_light
    ev_thought "Провал памяти после «технического сбоя»?" (show_side="left", show_kind="thought")
    hide eveina

    scene bg scene 1_3 hall 1 at bg_fullscreen with dissolve

    show noa eyebrow at noa_right, sprite_warm_light
    no "Да к чёрту инналу, это не они нас тут заперли без связи с внешним миром..." (show_side="right", show_kind="speech")
    hide noa

    show m03 normal at student_right, sprite_warm_light
    unknown "Не скажи... Мне рассказывали, что инналу враждебно настроены к людям." (show_side="right", show_kind="speech")
    hide m03

    show sairen thinking at sairen_right, sprite_warm_light
    sa "Да это всё слухи. Никто ничего о них не знает — вот и додумывают ужасы. Обычные аборигены." (show_side="right", show_kind="speech")
    hide sairen

    n "Игнорируя витающие в воздухе настроения, ИИ-ассистент бодрым голосом начал называть чьи-то имена и выдавать инструкции." (show_side="none", show_kind="speech")
    n "Разговоры сразу стали тише, но не прекратились." (show_side="none", show_kind="speech")

    scene bg hall wall at bg_fullscreen with dissolve

    show eveina normal at eveina_left, sprite_warm_light
    ev_thought "Общаться с инналу нельзя.\nВидеть их — небезопасно." (show_side="left", show_kind="thought")
    hide eveina
    show eveina eyebrow at eveina_left, sprite_warm_light
    ev_thought "И даже думать о них дольше пары секунд — вроде как дурной тон." (show_side="left", show_kind="thought")
    hide eveina
    show eveina eyeroll at eveina_left, sprite_warm_light
    ev_thought "Ах да, и добро пожаловать под купол. Вот тебе и Академия." (show_side="left", show_kind="thought")
    hide eveina

    n "Эвейна задумчиво провела пальцем по внутреннему краю стены, где светился живой узор." (show_side="none", show_kind="speech")

    # --- ИИ вызывает Эвейну ---

    scene bg scene 1_3 hall 1 at bg_fullscreen with dissolve

    #show ai at ai_right
    ai_offscreen "Мисс Хейла, сдайте личное устройство связи и возьмите академический браслет. Вам назначена комната 4B в жилом секторе." (show_side="none", show_kind="speech")
    ai_offscreen "После получения браслета пройдите на вводную экскурсию в лабораторию нейросетевого анализа. Начало через 15 минут." (show_side="none", show_kind="speech")
    #hide ai

    n "Несколько студентов обернулись, услышав её имя. Эвейна медленно двинулась к стойке регистрации, ловя на себе заинтересованные взгляды." (show_side="none", show_kind="speech")

    show sairen intrigued at sairen_right, sprite_warm_light
    sa "Это она? Та, что с периферии… но с чьей-то рекомендацией." (show_side="right", show_kind="speech")
    hide sairen
    show sairen angry at sairen_right, sprite_warm_light
    sa "Интересно, чьей?" (show_side="right", show_kind="speech")
    hide sairen

    show eveina annoyed at eveina_left, sprite_warm_light
    ev_thought "Блондиночка, мне и самой интересно, с чьей!" (show_side="left", show_kind="thought")
    hide eveina

    show noa eyebrow at noa_right, sprite_warm_light
    no "Залетела в последний вагон, и сразу в нейротерапию. Смелость или безумие?" (show_side="right", show_kind="speech")
    hide noa

    n "Эвейна недовольно фыркнула, закатив глаза." (show_side="none", show_kind="speech")

    show eveina eyeroll at eveina_left, sprite_warm_light
    ev_thought "Слабоумие и отвага?" (show_side="left", show_kind="thought")
    hide eveina

    show tero eyebrow at tero_right, sprite_warm_light
    unknown "Понимает ли она, что оказалась заперта здесь с вами?" (show_side="right", show_kind="speech")
    hide tero
    show tero thinking at tero_right, sprite_warm_light
    unknown "Вы ж её живьём сожрёте..." (show_side="right", show_kind="speech")
    hide tero

    show silas thinking at silas_right, sprite_warm_light
    unknown "Да ладно вам. Может, в ней действительно что-то есть." (show_side="right", show_kind="speech")
    hide silas
    show silas intrigued at silas_right, sprite_warm_light
    unknown "Общество любит истории про безликих героев. В них спрятан блестящий исход. Или блестящее падение." (show_side="right", show_kind="speech")
    hide silas

    show eveina angry at eveina_left, sprite_warm_light
    ev_thought "Ну всё, блондинчик, тебе я точно сейчас вта…" (show_side="left", show_kind="thought")
    hide eveina

    # --- Первая встреча с Леей ---

    n "В тот же момент перед Эвейной возникла незнакомка, сбив ту с опрометчивой мысли. Она протянула ей маленький плод, похожий на свернутый лист, и улыбнулась." (show_side="none", show_kind="speech")

    show leya normal at leya_right, sprite_warm_light
    unknown "Держи. Снимает ком в горле." (show_side="right", show_kind="speech")
    hide leya
    show leya eyebrow at leya_right, sprite_warm_light
    unknown "Ну, или можно швырнуть в какого-нибудь недоумка, испортившего тебе день." (show_side="right", show_kind="speech")
    hide leya

    n "Не понимая, как реагировать на это приветствие, Эвейна молча взяла в руки плод и на автомате двинулась дальше." (show_side="none", show_kind="speech")

    show leya smile at leya_right, sprite_warm_light
    unknown "Ох, Сайлас, прости, совсем тебя не заметила!" (show_side="right", show_kind="speech")
    hide leya

    show silas intrigued at silas_right, sprite_warm_light
    si "Я запомню." (show_side="right", show_kind="speech")
    hide silas

    n "Дойдя до стойки, девушка ещё раз мысленно повторила правила Академии: закрытый контур, отслеживающие браслеты, никаких контактов с инналу." (show_side="none", show_kind="speech")
    n "Формально новый браслет сохранял связь с внешним миром. Приватность в комплект не входила: перемещения, обращения к системе и даже записи в личном дневнике теперь могли стать достоянием Академии." (show_side="none", show_kind="speech")
    n "Эвейне это не нравилось. Но без регистрации доступ оставался бесполезной надписью на экране." (show_side="none", show_kind="speech")
    n "Она расстегнула личный браслет и положила его в предназначенный для этого отсек." (show_side="none", show_kind="speech")

    n "Отсек закрылся и тут же открылся снова. Внутри лежал академический браслет. Эвейна застегнула его на запястье." (show_side="none", show_kind="speech")

    n "{i}Профиль зарегистрирован.\nСтуденческий доступ к внутренней базе активирован.{/i}" (show_side="none", show_kind="speech")

    scene bg hall corridor at bg_fullscreen with dissolve

    n "Лишь покинув холл, девушка поняла, что не поблагодарила студентку, внезапно вставшую на её сторону. От мысли об этом стало совсем неловко." (show_side="none", show_kind="speech")

    show eveina eyeroll at eveina_left
    ev_thought "Мои социальные навыки на уровне пещерного человека." (show_side="left", show_kind="thought")
    hide eveina
    show eveina eyebrow at eveina_left
    ev_thought "Что дальше — откусить руку, если кто-то поздоровается?" (show_side="left", show_kind="thought")
    hide eveina

    n "Чужим рукам в тот день повезло. Эвейна вонзила зубы в плод — и от терпкого вкуса сразу свело скулы." (show_side="none", show_kind="speech")

    jump scene_1_4  # Переход к следующей сцене
