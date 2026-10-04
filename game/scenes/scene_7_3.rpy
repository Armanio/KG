label scene_7_3:
    $ previous_scene = "scene_7_2"
    $ next_scene = "scene_7_4"
    $ current_scene = "scene_7_3"
    call fade_to_black(1.2, 0.8)
    scene bg dining_room at bg_fullscreen with dissolve

    n "Утро началось с кофе — обжигающе горького, почти как мысли о предстоящем эксперименте." (show_side="none", show_kind="speech")
    n "Эвейна сидела в столовой с Леей, Теро и Ноа. Ребята смеялись, обменивались подколками, кивали на кого-то у входа." (show_side="none", show_kind="speech")
    n "Но беспокойные мысли девушки блуждали где-то далеко отсюда. Её пальцы были сцеплены в замок вокруг чашки, как будто кофе был якорем, а всё остальное — штормом." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev_thought "Дыши. Пей. Не смотри на часы. Не думай. Не волнуйся." (show_side="left", show_kind="thought")
    hide eveina 
    show eveina annoyed at eveina_left
    ev_thought "В каком смысле - не волнуйся? Как тут вообще можно оставаться спокойной?" (show_side="left", show_kind="thought")
    hide eveina 

    n "Сцепленные пальцы не выдавали легкую дрожь, но она чувствовала её в легкой вибрации чайной ложки, и злилась на себя на неумение сдерживать свои эмоции." (show_side="none", show_kind="speech")
    n "Видя её хмурый взгляд, Лея ободряюще ей улыбалась, но заговорить не решалась." (show_side="none", show_kind="speech")

    show noa intrigued at noa_right
    no "Кстати, кто-нибудь заметил, что у Раукт феноменальная память?" (show_side="right", show_kind="speech")
    hide noa
    show noa normal at noa_right
    no "На экзамене она припомнила мне, как я чихнул, перебив её монолог на первой лекции." (show_side="right", show_kind="speech")
    no "Мне кажется, над своими мозгами она тоже поэкспериментировала в лаборатории." (show_side="right", show_kind="speech")
    hide noa

    show leya smile at leya_right
    le "Нет, она просто не ест углеводы." (show_side="right", show_kind="speech")
    le "Мозг очищен от булочек, и вот тебе — абсолютная концентрация зла." (show_side="right", show_kind="speech")
    hide leya

    show tero normal at tero_right
    te "А как вам манера Кайстра постоянно задавать вопросы и самому на них отвечать?" (show_side="right", show_kind="speech")
    te "Интересно, он так делает перед зеркалом?" (show_side="right", show_kind="speech")
    hide tero
    show tero smile at tero_right
    te "{i}«Кто ты такой, профессор Кайстр?» — «Я — угроза академической морали!»{/i}" (show_side="right", show_kind="speech")
    hide tero

    show noa intrigued at noa_right
    no "И зеркало такое: {i}«Уберите меня, я не хочу видеть этот стыд!»{/i}" (show_side="right", show_kind="speech")
    hide noa

    show eveina eyeroll at eveina_left
    ev_thought "Выдохни. Это просто эксперимент. Просто демонстрация. Просто…" (show_side="left", show_kind="thought")
    hide eveina 

    n "Ребята захохотали, о чём-то споря и перебивая друг друга. Лея кивнула на кого-то в зале, одергивая Теро, который изображал Раукт с указкой в зубах." (show_side="none", show_kind="speech")
    n "И вдруг резко наступила тишина, будто кто-то нажал кнопку «Стоп». Эвейна оторвала взгляд от чашки и посмотрела на ребят." (show_side="none", show_kind="speech")
    n "Но взгляды напротив были устремлены куда-то за её спину. Не успела она обернуться, как прохладная рука аккуратно коснулась её плеча." (show_side="none", show_kind="speech")

    show kael normal at kael_right
    ka "Нам пора." (show_side="right", show_kind="speech")
    hide kael

    scene bg capsule at bg_fullscreen with dissolve

    n "Её ждала тестовая капсула — изолированное пространство с приглушённым светом биолюминесцентное свечение." (show_side="none", show_kind="speech")
    n "Когда они вошли внутрь, у неё чуть не подкосились ноги от страха." (show_side="none", show_kind="speech")

    show eveina wondered at eveina_left
    ev_thought "На что я подписалась? Каэль же буквально залезет ко мне в голову." (show_side="left", show_kind="thought")
    hide eveina
    show eveina eyebrow at eveina_left
    ev_thought "А вдруг он там что-то испортит?" (show_side="left", show_kind="thought")
    hide eveina
    show eveina thinking at eveina_left
    ev_thought "Хотя... там и без этого не всё в порядке." (show_side="left", show_kind="thought")
    ev_thought "Хуже не сделает." (show_side="left", show_kind="thought")
    hide eveina
    show eveina wondered at eveina_left
    ev_thought "Не сделает же?" (show_side="left", show_kind="thought")
    hide eveina

    n "За стеклом собрались наблюдающие: преподаватели, ассистенты, несколько незнакомых ей людей." (show_side="none", show_kind="speech")
    n "Каэль молча помог ей забраться в капсулу. Осторожно зафиксировал ремни, настроил датчики, проверил показатели." (show_side="none", show_kind="speech")
    n "Действовал быстро, чётко. Почти отстранённо." (show_side="none", show_kind="speech")
    n "Но в какой-то момент — используя ракурс, с которого никто не видел, он опустил руку и ободряюще сжал её ладонь, взглянув в глаза." (show_side="none", show_kind="speech")
    n "Он был спокоен и абсолютно уверен в себе. Что-то незримое в этом спокойствии передалось и ей. Как будто через этот простой жест он сказал: {i}«Я здесь. Всё под контролем.»{/i}" (show_side="none", show_kind="speech")

    show kael normal at kael_right
    ka "Готова?" (show_side="right", show_kind="speech")
    hide kael

    show eveina eyebrow at eveina_left
    ev_thought "Готова? Нет, конечно." (show_side="left", show_kind="thought")
    ev_thought "К такому вообще можно быть готовой?" (show_side="left", show_kind="thought")
    hide eveina


    n "Эвейна молча кивнула, боясь, что если откроет рот, дрожь в голосе её выдаст." (show_side="none", show_kind="speech")
    n "Каэль прошёл за внешний терминал. Сделал несколько точных, спокойных движений по панели и поднял на неё глаза." (show_side="none", show_kind="speech")

    show kael normal at kael_right
    ka "Подумай о воспоминании, которое мы будем стирать." (show_side="right", show_kind="speech")
    hide kael
    show kael intrigued at kael_right
    ka "Позволь ему стать ярким." (show_side="right", show_kind="speech")
    hide kael

    n "Уголки его губ дрогнули вверх, едва заметно, как будто он на секунду и сам вспомнил, что именно собирался стереть." (show_side="none", show_kind="speech")
    n "Эвейна уловила это, и вопреки тревоге внутри — ей стало тепло. Она закрыла глаза. И позволила себе уйти туда, в то самое воспоминание." (show_side="none", show_kind="speech")

    call fade_to_black(1.2, 0.8)
    scene bg lab at bg_fullscreen with dissolve
    n "Он был совсем близко, смотрел на неё своим пронзительным изучающим взглядом." (show_side="none", show_kind="speech")

    show kael normal at kael_right
    ka "Эвейна, я собираюсь тебя поцеловать." (show_side="right", show_kind="speech")
    ka "И у тебя есть шанс меня остановить." (show_side="right", show_kind="speech")
    hide kael

    n "Она пыталась что-то возразить, но в этот момент его губы накрыли её, не дав ей договорить. В голове словно взорвался фейерверк эмоций." (show_side="none", show_kind="speech")
    n "И прежде чем она смогла что-то осознать, он притянул её ближе, а поцелуй стал глубже, увереннее, жарче." (show_side="none", show_kind="speech")
    n "Ощущения были настолько яркими, что у Эвейны запорхали бабочки в животе. Но прошло мгновение, и теперь всё это исчезало." (show_side="none", show_kind="speech")
    n "Она чувствовала, как воспоминание начинает блекнуть." (show_side="none", show_kind="speech")
    n "Краски — уходили. Слова — стирались. Контуры — расплывались." (show_side="none", show_kind="speech")
    n "И оставалась только пустота. Как будто сердце всё ещё помнило, а мозг — уже нет." (show_side="none", show_kind="speech")

    call fade_to_black(1.2, 0.8)
    scene bg capsule at bg_fullscreen with dissolve

    n "Она знала: Каэль видел в интерфейсе, как светятся нити нейросвязей, и по одной методично обрезал их, словно хирургическим скальпелем." (show_side="none", show_kind="speech")
    n "Теперь она знала, что у неё было это воспоминание, этот момент, но само воспоминание — исчезло." (show_side="none", show_kind="speech")
    n "На его месте осталась обжигающая дыра. Как будто внутри теперь не хватало кусочка пазла, затерянного где-то под диваном." (show_side="none", show_kind="speech")

    show kael normal at kael_right
    ka "Воспоминание удалено. Стабилизация — в норме." (show_side="right", show_kind="speech")
    hide kael

    n "Он бросил на Эвейну быстрый взгляд и убедился, что та в порядке." (show_side="none", show_kind="speech")

    show kael normal at kael_right
    ka "Запускаю." (show_side="right", show_kind="speech")
    hide kael

    n "Сперва Эвейна ничего не почувствовала и прикрыла глаза в беспокойном ожидании." (show_side="none", show_kind="speech")
    n "Следом ощутила легкую дрожь во всём теле, а за этим — слепящую вспышку. И снова погрузилась в воспоминание." (show_side="none", show_kind="speech")

    call fade_to_black(1.2, 0.8)
    scene bg night_garden at bg_fullscreen with dissolve

    n "Эвейна неторопливо шла по ночному саду, осматривая странные светящиеся деревья, переливающиеся биолюминисцентыми оттенками, и пытаясь успокоить беспокойное сердце, переживающее за отца." (show_side="none", show_kind="speech")
    n "В самом дальнем краю, у озера, под знакомым раскидистым деревом она заметила лежащую фигуру. Холодок пробежал по шее, намекая, что там её не ждёт ничего хорошего." (show_side="none", show_kind="speech")
    n "Но любопытство упорно вело вперёд." (show_side="none", show_kind="speech")

    show eveina eyebrow tshirt at eveina_left
    ev_thought "Там что, кто-то уснул?" (show_side="left", show_kind="thought")
    hide eveina

    n "Но чем ближе она приближалась, тем страннее казалась разворачивающаяся картина." (show_side="none", show_kind="speech")
    n "Под деревом кто-то лежал. Девушка. А над ней склонился силуэт мужчины." (show_side="none", show_kind="speech")
    n "От ствола дерева и травы вокруг тянулись волны света, похожие на круги в воде от брошенного в неё камня, но движущиеся внутрь воронки, а не наружу." (show_side="none", show_kind="speech")
    n "И эти волны, касаясь тела девушки, заставляли её кожу светиться изнутри. Эвейна в шоке прижала ко рту ладонь и замерла в нерешительности." (show_side="none", show_kind="speech")

    show eveina wondered tshirt at eveina_left
    ev_thought "Господи, что за чёртовщина..." (show_side="left", show_kind="thought")
    hide eveina   

    n "Машинально сделав шаг назад, она наступила на сухую ветку, будто специально брошенную под её ноги, и тишину в саду нарушил легкий, но так отчётливо слышный хруст." (show_side="none", show_kind="speech") 
    n "Волны света внезапно потухли, оставив лишь крошечные искроки в воздухе, напоминающие светлячков в ночном поле." (show_side="none", show_kind="speech")
    n "Мужчина медленно поднялся и обернулся на шум. Эвейна чуть не вскрикнула от ужаса. В неё уперлись горящие золотом радужки с вертикальными зрачками." (show_side="none", show_kind="speech")

    show eveina wondered tshirt at eveina_left
    ev_thought "Эриан... Боже, это Эриан!" (show_side="left", show_kind="thought")
    hide eveina 

    n "Не оставляя себе время на размышление, она резко развернулась и бросилась бежать." (show_side="none", show_kind="speech")

    show eveina wondered tshirt at eveina_left
    ev_thought "Он меня видел! Он не..." (show_side="left", show_kind="thought")
    hide eveina  

    show erian annoyed at erian_right
    er "Стоять." (show_side="right", show_kind="speech")
    hide erian

    n "Эвейна будто на ходу врезалась в стену. Ноги внезапно вросли в землю, не давая возможности сдвинуться с места. Девушка в ужасе обернулась и увидела, как огромная фигура с ленивой грацией, совершенно не торопясь, приближается к ней." (show_side="none", show_kind="speech")

    show eveina wondered tshirt at eveina_left
    ev "Не приближайся, Эриан! Иначе я закричу!" (show_side="left", show_kind="speech")
    hide eveina

    show erian normal at erian_right
    er "Кричи." (show_side="right", show_kind="speech")
    hide erian

    show eveina sad tshirt at eveina_left
    ev "Не подходи... Пожалуйста. Просто дай мне уйти." (show_side="left", show_kind="speech")
    hide eveina

    show erian intrigued at erian_right
    er "О, теперь ты решила умолять. Как вовремя..." (show_side="right", show_kind="speech")
    hide erian
    show erian normal at erian_right
    er "Сядь." (show_side="right", show_kind="speech")
    hide erian

    n "Тело Эвейны, следуя приказу и не в силах сопротивляться, послушно опустилось на траву. Эриан присел на корточки рядом с ней, с сомнением вглядываясь в испуганные глаза, подернутые солёной плёнкой." (show_side="none", show_kind="speech")

    show eveina wondered tshirt at eveina_left
    ev "Кто ты такой?" (show_side="left", show_kind="speech")
    hide eveina

    show erian thinking at erian_right
    er "Тот, кого тебе лучше не злить." (show_side="right", show_kind="speech")
    hide erian

    n "Взгляд девушки устремился за его плечо, на тело, продолжившее лежать под деревом без единого движения." (show_side="none", show_kind="speech")

    show eveina upset thinking tshirt at eveina_left
    ev "Кто это?" (show_side="left", show_kind="speech")
    ev "Она... она жива?" (show_side="left", show_kind="speech")
    hide eveina

    n "Парень поморщился от её вопроса." (show_side="none", show_kind="speech")

    show erian annoyed at erian_right
    er "Побудешь хорошей девочкой? Посиди молча, пока я подумаю." (show_side="right", show_kind="speech")
    hide erian

    n "Губы Эвейны задрожали, когда Эриан отвернулся от неё и уставился на гладь озера." (show_side="none", show_kind="speech")
    n "Ноги начали неметь от неудобной позы, и она сосредоточила всё своё внимание на том, чтобы заставить их двигаться." (show_side="none", show_kind="speech")

    show eveina upset tshirt at eveina_left
    ev_thought "Давайте же... пожалуйста..." (show_side="left", show_kind="thought")
    ev_thought "Мне нужно убраться отсюда. Сбежать. Спрятаться." (show_side="left", show_kind="thought")
    hide eveina 

    n "Словно усшылав её немую молитву, невидимая сила, держащая её ноги в неподвижности, ослабла и она осторожно ими подвигала, убеждаясь, что они в порядке." (show_side="none", show_kind="speech")

    show erian thinking at erian_right
    er "Проклятье, Эвейна, ну и что с тобой делать прика..." (show_side="right", show_kind="speech")
    hide erian

    n "Поворачиваясь к Эвейне, Эриан задумчиво начал фразу, которой не суждено было закончиться. В следующую секунду ему в скулу прилетело колено." (show_side="none", show_kind="speech")
    n "Эвейна подпрыгнула на месте и снова бросилась бежать, лишь мельком разглядев искреннее удивление на лице Эриана." (show_side="none", show_kind="speech")

    show erian annoyed at erian_right
    er "Как ты..? Ты совсем выжила из ума?" (show_side="right", show_kind="speech")
    hide erian

    n "Отойдя от шока, Эриан в несколько прыжков настиг её, схватил за запястье и дёрнул на себя, обхватывая в сковывающие объятия." (show_side="none", show_kind="speech")

    show erian annoyed at erian_right
    er "Ты что тут устроила?" (show_side="right", show_kind="speech")
    hide erian

    if  bite_reaction == "slap":
        show erian annoyed at erian_right
        er "Ударить меня один раз было смело. Но ударить дважды — уже глупо." (show_side="right", show_kind="speech")
        hide erian

    show eveina wondered tshirt at eveina_left
    ev "Отпусти меня, чёртово чудовище!" (show_side="left", show_kind="speech")
    hide eveina

    show erian upset at erian_right
    er "Чудовище? Вот каким ты меня видишь, Эвейна?" (show_side="right", show_kind="speech")
    hide erian
    show erian annoyed at erian_right
    er "Что ж могу побыть и им для тебя..." (show_side="right", show_kind="speech")
    hide erian

    n "Он с такой силой сжал её запястье, что Эвейна взвизгнула и дернулась так сильно, что из глаз вылетели слёзы. Хватка тут же стала слабее." (show_side="none", show_kind="speech")

    show erian annoyed at erian_right
    er "Проклятье... умеешь же ты выводить из себя..." (show_side="right", show_kind="speech")
    er "Не на такой диалог я рассчитывал. Но с тобой всё катится к чертям!" (show_side="right", show_kind="speech")
    show erian thinking at erian_right
    er "Поэтому даю тебе один последний шанс избавиться от меня раз и навсегда." (show_side="right", show_kind="speech")
    hide erian

    n "Услышав это, Эвейна замерла и перестала вырываться. На раздраженное лицо парня уставились серые глаза, полные слёз." (show_side="none", show_kind="speech")

    show erian normal at erian_right
    er "Ответь мне на один вопрос. И можешь быть свободна." (show_side="right", show_kind="speech")
    hide erian

    n "Эвейна всхлипнула и кивнула, чувствуя, как по щеке скатилась слеза. Эриан проследил за тем, как она медленно опустилась вниз по щеке, оставляя за собой влажную дорожку, и замерла в уголке губ." (show_side="none", show_kind="speech")

    show erian normal at erian_right
    er "Кто такой Кайр Далон, Эвейна?" (show_side="right", show_kind="speech")
    er "Кто он... для тебя?" (show_side="right", show_kind="speech")
    hide erian

    n "Вопрос будто выжгли ей клеймом на груди, потому что услышав его, она поняла — он её не отпустит. Что бы его больной мозг не придумал — она не найдёт для него подходящего ответа." (show_side="none", show_kind="speech")

    show eveina upset tshirt at eveina_left
    ev "Я не знаю..." (show_side="left", show_kind="speech")
    hide eveina

    n "Эриан медленно поднял глаза к небу, и Эвейна могла поклясться, что в сейчас её не станет. Только вот жить отчего-то очень хотелось." (show_side="none", show_kind="speech")

    show erian normal at erian_right
    er "Решила поиграть, значит..." (show_side="right", show_kind="speech")
    er "Хорошо. Будь по-твоему, поиграем." (show_side="right", show_kind="speech")
    hide erian

    n "В следующую секунду он нагнулся к ней, касаясь её лба своим. Эвейна замерла, и в глазах потемнело. Лишь боль в запястье осталась с ней даже в кромешной тьме, как проводник в реальность." (show_side="none", show_kind="speech")

    call fade_to_black(1.2, 0.8)
    scene bg capsule at bg_fullscreen with dissolve

    n "Эвейна вздрогнула. Это точно не было тем воспоминанием, которое только что стёр Каэль. Она вообще такого не помнила. {i}Не помнила.{/i}" (show_side="none", show_kind="speech")

    show eveina wondered at eveina_left
    ev "Каэль, что-то не..." (show_side="left", show_kind="speech")
    hide eveina

    n "Внезапная боль пронзила запястье как игла. Сердце начало стремительно набирать темп, пытаясь угнаться за хаосом в мыслях." (show_side="none", show_kind="speech")
    n "Паника и страх накрыли с головой. Разум судорогой бился в голове, как зверь, которого поймали в капкан." (show_side="none", show_kind="speech")

    show eveina wondered at eveina_left
    ev "Что это? Что ты сделал?!" (show_side="left", show_kind="speech")
    hide eveina

    n "По всему её телу прошла дрожь. Грудная клетка сжалась в судороге." (show_side="none", show_kind="speech")
    n "Она закричала. То ли от боли, то ли от раздирающего душу панического приступа, которого она никогда ранее не испытывала." (show_side="none", show_kind="speech")
    n "Гул капсулы нарастал набатом в ушах, пока не стал невыносимым. Свет заморгал. А потом резко всё закончилось." (show_side="none", show_kind="speech")

    call fade_to_black(1.2, 0.8)

    n "Будто кто-то выключил свет, и она провалилась в темноту." (show_side="none", show_kind="speech")

    call fade_to_black(1.2, 0.8)
    scene bg capsule at bg_fullscreen with dissolve

    n "Эвейна пришла в себя всего несколько мгновений спустя — в той же капсуле, в той же позе." (show_side="none", show_kind="speech")
    n "Над ней нависал силуэт, в котором, привыкнув к свету, она узнала Каэля. Глаза широко раскрыты, лицо бледнее обычного, а на виске — капля пота." (show_side="none", show_kind="speech")
    n "За ним стоял Вирт, сжимая руки в кулаки. Его стальной голос разрезал тишину." (show_side="none", show_kind="speech")

    show virt angry at virt_right
    vi "Вы своим экспериментом решили угробить мою студентку?" (show_side="right", show_kind="speech")
    hide virt

    n "Каэль не отвечал, помогая Эвейне приподняться. Во рту она ощутила солоноватый привкус крови и сморщилась." (show_side="none", show_kind="speech")

    show kael sad at kael_right
    ka "Как ты?" (show_side="right", show_kind="speech")
    hide kael

    show eveina normal at eveina_left
    ev "Жива. Только… голова раскалывается. И, кажется, я прикусила язык." (show_side="left", show_kind="speech")
    hide eveina

    n "Он, не глядя, кивнул Вирту." (show_side="none", show_kind="speech")

    show kael thinking at kael_right
    ka "Воды." (show_side="right", show_kind="speech")
    hide kael

    n "Вирт развернулся и вышел. Каэль обернулся к оставшимся." (show_side="none", show_kind="speech")

    show kael serious at kael_right
    ka "Эксперимент окончен. Программа требует калибровки." (show_side="right", show_kind="speech")
    hide kael

    n "Люди за стеклом начали медленно расходиться." (show_side="none", show_kind="speech")
    n "Каэль опустился рядом с Эвейной и коснулся её плеча. Эвейна подняла на него усталый взгляд и впервые увидела на его лице настоящую тревогу." (show_side="none", show_kind="speech")
    n "Медленно, будто сомневаясь в своих выводах, Каэль произнёс:" (show_side="none", show_kind="speech")

    show kael sad at kael_right
    ka "Эвейна... ты ведь что-то вспомнила? Что-то другое?" (show_side="right", show_kind="speech")
    hide kael

    show eveina upset at eveina_left
    ev "Да." (show_side="left", show_kind="speech")
    hide eveina

    show kael thinking at kael_right
    ka "Такое могло произойти только если в твоём сознании уже были поврежденные воспоминания." (show_side="right", show_kind="speech")
    hide kael
    show kael serious at kael_right
    ka "Ты понимаешь… откуда они?" (show_side="right", show_kind="speech")
    hide kael

    n "Эвейна отвела взгляд, с помощью Каэля осторожно выбралась из капсулы и прижалась к ней спиной." (show_side="none", show_kind="speech")
    n "Подняла к глазам ноющее запястье, убеждаясь, что следа не осталось — а значит, боль была фантомной, просто воспоминанием." (show_side="none", show_kind="speech")
    n "Каэль встал сбоку, поддерживая за локоть. Наконец, тяжело вздохнув, девушка кивнула." (show_side="none", show_kind="speech")

    show eveina upset at eveina_left
    ev "Да. Думаю, да. Понимаю." (show_side="left", show_kind="speech")
    hide eveina

    show kael eyebrow at kael_right
    ka "Ты встречала кого-то из Илейн?" (show_side="right", show_kind="speech")
    hide kael

    show eveina upset at eveina_left
    ev "Да." (show_side="left", show_kind="speech")
    hide eveina

    n "Он не ругал, не обвинял, не угрожал. Только прикрыл на мгновение глаза, а потом поднял на неё тяжелый взгляд, покачав головой." (show_side="none", show_kind="speech")

    show kael serious at kael_right
    ka "Если бы ты сказала сразу, я бы исключил этот вариант." (show_side="right", show_kind="speech")
    hide kael
    show kael sad at kael_right
    ka "Мы могли бы избежать этого." (show_side="right", show_kind="speech")
    hide kael

    show eveina annoyed at eveina_left
    ev_thought "И как ты себе это представляешь?" (show_side="left", show_kind="thought")
    hide eveina
    show eveina thinking at eveina_left
    ev_thought "Привет, Каэль, помнишь, я у тебя на глазах сперла файл из документов Эзари?" (show_side="left", show_kind="thought")
    ev_thought "Так вот, это мелочи — слушай полный список моих нарушений!" (show_side="left", show_kind="thought")
    hide eveina

    n "Не дождавшись ответа, Каэль грустно усмехнулся. Кажется, он и сам понимал, почему она не могла сказать." (show_side="none", show_kind="speech")
    n "Вот только это было слабым оправданием для него самого. Он обязан был её предупредить. Даже о теоретическом риске." (show_side="none", show_kind="speech")
    n "Но не предупредил. Отвлёкся, заигрался в чувства. И навредил той, кому никогда не хотел навредить." (show_side="none", show_kind="speech")
    n "Кажется, все эмоции, которые он так умело держал в себе, сейчас прорвались наружу и отразились на его лице." (show_side="none", show_kind="speech")
    n "Иначе он не мог объяснить, почему Эвейна вдруг посмотрела на него испуганным взглядом и протянула руку, беря его ладонь в свою." (show_side="none", show_kind="speech")

    show eveina upset at eveina_left
    ev "Каэль... прости меня. Я всё испортила." (show_side="left", show_kind="speech")
    hide eveina

    n "Парень, сжав крепче её ладошку, хотел что-то ответить, но этот момент вернулся Вирт со стаканом воды." (show_side="none", show_kind="speech")

    show virt sad at virt_right
    vi "Вы в порядке?" (show_side="right", show_kind="speech")
    hide virt

    show eveina normal at eveina_left
    ev "Да." (show_side="left", show_kind="speech")
    hide eveina

    n "Будто пытаясь убедить его в искренности своих слов, она чересчур уверенно кивнула и сделала несколько глотков из стакана." (show_side="none", show_kind="speech")

    show virt sad at virt_right
    vi "Тогда вы освобождены от занятий. Я провожу вас до комнаты." (show_side="right", show_kind="speech")
    hide virt

    n "Каэль не спорил, просто сделал шаг назад и наблюдал, как Вирт обхватил её за талию и вывел из комнаты." (show_side="none", show_kind="speech")
    n "Он остался один посреди пустой лаборатории, бросил взгляд на пустую капсулу." (show_side="none", show_kind="speech")
    n "И — впервые за долгое время — позволил себе опустить голову." (show_side="none", show_kind="speech")

    jump scene_7_4