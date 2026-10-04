label scene_3_3:
    $ previous_scene = "scene_3_2"
    $ next_scene = "scene_3_4"
    $ current_scene = "scene_3_3"

    # =========================================================
    # СЦЕНА 3_3 — «КОМПАНИЯ / ИСТОРИЯ ТРЁХ ЛЕТ»
    # Структура: Лея зовёт → мох → лабораторный алкоголь → Ноа/Каэль-дьявол
    #            → три года назад (через несколько голосов)
    #            → Лея — тихое сомнение → расходятся
    # Тональность: живая, с юмором, с нарастающей тревогой к концу.
    # Ноа несёт байку про Каэля — его реплики из оригинала.
    # История трёх лет — через несколько голосов, версии чуть расходятся.
    # =========================================================

    call fade_to_black(1.2, 0.8)
    scene bg common_room at bg_fullscreen with dissolve
    # play music "bgm/evening_lounge.ogg" fadein 2.0

    n "Когда Лея сказала «посидим немного», Эвейна не сразу поняла, что это означает «Ноа уже принёс что-то в непрозрачной фляжке и Теро не знает, как тактично отказаться»." (show_side="none", show_kind="speech")

    show leya smile at leya_right
    le "Ви, не смотри так. Это местное. Ботаники и биохимики гонят после занятий — говорят, абсолютно безвредно." (show_side="right", show_kind="speech")
    hide leya

    show eveina eyebrow at eveina_left
    ev "«Говорят»." (show_side="left", show_kind="speech")
    hide eveina

    show noa intrigued at noa_right
    no "Я лично проверил. Трижды. Исключительно в научных целях." (show_side="right", show_kind="speech")
    hide noa

    show tero normal at tero_right
    te "В каждый из трёх раз ты проснулся в саду." (show_side="right", show_kind="speech")
    hide tero

    show noa intrigued at noa_right
    no "Это называется «единение с природой», Теро. Расширь горизонты." (show_side="right", show_kind="speech")
    hide noa

    n "Эвейна взяла кружку. Понюхала. Сделала маленький глоток." (show_side="none", show_kind="speech")

    show eveina eyebrow at eveina_left
    ev_thought "Терпимо. Даже... почти приятно." (show_side="left", show_kind="thought")
    hide eveina

    n "Лея между делом достала с подоконника горшок с мхом — принесла с собой, как обычно." (show_side="none", show_kind="speech")

    show leya normal at leya_right
    le "Кстати. Помните, я рассказывала про серебристый налёт?" (show_side="right", show_kind="speech")
    hide leya

    show noa intrigued at noa_right
    no "Гриб-имитатор, да. Помним." (show_side="right", show_kind="speech")
    hide noa

    show leya eyebrow at leya_right
    le "Он изменился. Вот, смотрите — по цвету и текстуре стал напоминать... мою кожу." (show_side="right", show_kind="speech")
    hide leya

    n "Все немного подались вперёд. Это действительно выглядело странно." (show_side="none", show_kind="speech")

    show leya thinking at leya_right
    le "Я попробовала дотронуться — и он мгновенно осыпался. Весь. И начался сначала." (show_side="right", show_kind="speech")
    hide leya

    show noa intrigued at noa_right
    no "То есть гриб буквально хочет быть тобой." (show_side="right", show_kind="speech")
    hide noa

    show leya normal at leya_right
    le "Он адаптируется. Это не то же самое." (show_side="right", show_kind="speech")
    hide leya

    show noa smile at noa_right
    no "Лея. Это именно то же самое." (show_side="right", show_kind="speech")
    hide noa

    show tero normal at tero_right
    te "..." (show_side="right", show_kind="speech")
    hide tero

    n "Теро смотрел на горшок с выражением человека, которому неловко за незнакомый организм." (show_side="none", show_kind="speech")

    show eveina eyeroll at eveina_left
    ev_thought "Интересно, что будет, если этот мох окажется рядом с кем-то... менее человеческим." (show_side="left", show_kind="thought")
    hide eveina

    n "Мысль мелькнула и ушла. Ноа уже разливал по второму кругу." (show_side="none", show_kind="speech")

    show noa intrigued at noa_right
    no "Ладно, у меня есть история. Про Каэля." (show_side="right", show_kind="speech")
    hide noa

    show eveina eyebrow at eveina_left
    ev_thought "О, отлично. Именно то, что мне сейчас нужно." (show_side="left", show_kind="thought")
    hide eveina

    show leya eyebrow at leya_right
    le "Ноа, не надо..." (show_side="right", show_kind="speech")
    hide leya

    show noa intrigued at noa_right
    no "Один студент с третьего курса. Перед зачётом тихо ляпнул, что готов отдать душу за этот чёртов экзамен." (show_side="right", show_kind="speech")
    hide noa
    show noa smile at noa_right
    no "А Каэль — тут как тут за спиной. И говорит, что он оскорбляет саму суть взяток такими смешными ценами." (show_side="right", show_kind="speech")
    hide noa

    show eveina thinking at eveina_left
    ev_thought "Звучит правдоподобно." (show_side="left", show_kind="thought")
    hide eveina

    show noa intrigued at noa_right
    no "И что его душа, похоже, вообще ничего не стоит, раз он готов отдать её за такую мелочь." (show_side="right", show_kind="speech")
    no "И добавил, что совсем другое — если бы у него было доказательство её существования. Вот тогда бы нам было о чём побеседовать." (show_side="right", show_kind="speech")
    hide noa

    show tero normal at tero_right
    te "Это правда?" (show_side="right", show_kind="speech")
    hide tero

    show noa smile at noa_right
    no "Я тебе говорю — он чёртов дьявол. История ещё не придумала преподавателя хуже." (show_side="right", show_kind="speech")
    hide noa

    show eveina eyeroll at eveina_left
    ev_thought "Мдаа, Каэль, до чего ты довёл людей. Дьявол и андроид в одном лице." (show_side="left", show_kind="thought")
    hide eveina

    show leya eyebrow at leya_right
    le "Ви, ты же с ним работаешь. Он правда такой?" (show_side="right", show_kind="speech")
    hide leya

    show eveina thinking at eveina_left
    ev "Он, конечно, парень с особенностями." (show_side="left", show_kind="speech")
    hide eveina
    show eveina normal at eveina_left
    ev "Следит за каждой реакцией, за каждым движением. Говорит — будто ты уже виноват. Смотрит — будто сканирует." (show_side="left", show_kind="speech")
    hide eveina
    show eveina eyeroll at eveina_left
    ev "А паузы у него такие, что думаешь: не ответишь — и он сейчас же вскроет тебе мозг, чтобы достать оттуда ответ." (show_side="left", show_kind="speech")
    hide eveina

    show noa intrigued at noa_right
    no "Видишь? Андроид." (show_side="right", show_kind="speech")
    hide noa

    show eveina smile at eveina_left
    ev "Ага, а ночами он ищет способ обрести человечность. Это же сюжет «Искусственного разума»." (show_side="left", show_kind="speech")
    hide eveina
    show eveina normal at eveina_left
    ev "Но робот, андроид или перепрограммированный мозг — нет." (show_side="left", show_kind="speech")
    hide eveina
    show eveina annoyed at eveina_left
    ev "Если бы задача была создать робота-лаборанта, они справились бы паршиво. Он своих студентов на дух не переносит." (show_side="left", show_kind="speech")
    hide eveina

    show leya smile at leya_right
    le "Значит, точно человек. Только человек может быть таким раздражающим." (show_side="right", show_kind="speech")
    hide leya

    n "Ноа поднял кружку в знак согласия." (show_side="none", show_kind="speech")
    n "Помолчали — тепло, без неловкости. За окном темнело." (show_side="none", show_kind="speech")

    show tero normal at tero_right
    te "Кстати, вы слышали, что на этой неделе опять нашли старые файлы в архиве? Те, что относятся к инциденту." (show_side="right", show_kind="speech")
    hide tero

    show eveina eyebrow at eveina_left
    ev_thought "Вот оно." (show_side="left", show_kind="thought")
    hide eveina

    show eveina normal at eveina_left
    ev "Какому инциденту?" (show_side="left", show_kind="speech")
    hide eveina

    show noa intrigued at noa_right
    no "О, ты не знаешь?" (show_side="right", show_kind="speech")
    hide noa

    show tero normal at tero_right
    te "Три года назад. До купола и браслетов." (show_side="right", show_kind="speech")
    hide tero

    show eveina eyebrow at eveina_left
    ev "Расскажете?" (show_side="left", show_kind="speech")
    hide eveina

    n "Ноа, Теро и Лея переглянулись — каждый знал свою часть." (show_side="none", show_kind="speech")

    show tero normal at tero_right
    te "Тогда всё было иначе. Не было ни купола, ни этих браслетов. Отношения с илейн — не то чтобы тёплые, но терпимые." (show_side="right", show_kind="speech")
    hide tero
    show tero thinking at tero_right
    te "Ходили слухи, что кто-то похищал илейн для экспериментов с биополем. Но никто не воспринимал всерьёз." (show_side="right", show_kind="speech")
    hide tero

    show noa intrigued at noa_right
    no "Пока в один день у всех, кто был в Академии, не пропала память о целых сутках." (show_side="right", show_kind="speech")
    hide noa

    show eveina wondered at eveina_left
    ev "Что — у всех сразу?" (show_side="left", show_kind="speech")
    hide eveina

    show noa intrigued at noa_right
    no "У всех. Разом. Как будто день просто... вырезали." (show_side="right", show_kind="speech")
    hide noa

    show leya thinking at leya_right
    le "Академия начала расследование. По записям восстановили почти всё. Осталось несколько пробелов." (show_side="right", show_kind="speech")
    hide leya

    show eveina eyebrow at eveina_left
    ev "И что выяснили?" (show_side="left", show_kind="speech")
    hide eveina

    show leya sad at leya_right
    le "Что в тот день Академию посещал представитель народа илейн." (show_side="right", show_kind="speech")
    hide leya

    show eveina normal at eveina_left
    ev "И решили, что это они?" (show_side="left", show_kind="speech")
    hide eveina

    show tero normal at tero_right
    te "Вроде того. Но была ещё одна деталь." (show_side="right", show_kind="speech")
    hide tero

    n "Он сделал паузу. Ноа не спешил перебивать — первый раз за вечер." (show_side="none", show_kind="speech")

    show tero thinking at tero_right
    te "По документам в Академии числилось 849 студентов. По ранним отчётам того дня — 850." (show_side="right", show_kind="speech")
    hide tero

    show eveina eyebrow at eveina_left
    ev "И?" (show_side="left", show_kind="speech")
    hide eveina

    show tero normal at tero_right
    te "И в женском блоке нашли одну лишнюю незаправленную кровать." (show_side="right", show_kind="speech")
    hide tero

    n "Тишина. Даже Ноа не нашёлся с шуткой сразу." (show_side="none", show_kind="speech")

    show noa intrigued at noa_right
    no "Звучит как дешёвый детектив, я понимаю." (show_side="right", show_kind="speech")
    hide noa

    n "Но пауза после «незаправленная кровать» была чуть длиннее, чем нужна для шутки." (show_side="none", show_kind="speech")

    show leya sad at leya_right
    le "В тот день пропала студентка. Но ни люди, ни система не помнили — кто она и откуда." (show_side="right", show_kind="speech")
    le "Её никто не искал. Ни родители, ни родственники." (show_side="right", show_kind="speech")
    hide leya

    show eveina thinking at eveina_left
    ev_thought "Господи, Эриан, во что ты пытаешься меня втянуть?" (show_side="left", show_kind="thought")
    hide eveina

    show tero thinking at tero_right
    te "Потом прилетела сама глава Вайскорп. Её муж на тот момент занимал пост ректора." (show_side="right", show_kind="speech")
    te "После инцидента он его покинул." (show_side="right", show_kind="speech")
    hide tero

    show noa intrigued at noa_right
    no "А Вайскорп опубликовала отчёт — илейн похитили девушку и стёрли память всем в отместку за то, что похищали их самих." (show_side="right", show_kind="speech")
    hide noa
    show noa thinking at noa_right
    no "И вот тебе купол. И браслеты. И всё прочее." (show_side="right", show_kind="speech")
    hide noa

    show leya eyebrow at leya_right
    le "Моя сестра как раз заканчивала последний курс. Говорила, что до этого Академия держалась особняком — не давала Вайскорп слишком много влияния." (show_side="right", show_kind="speech")
    hide leya
    show leya thinking at leya_right
    le "Это была заслуга ректора. После его смещения Вайскорп взяла всё под контроль. Нового ректора так и не назначили." (show_side="right", show_kind="speech")
    hide leya

    show eveina thinking at eveina_left
    ev "Странно." (show_side="left", show_kind="speech")
    hide eveina
    show eveina eyebrow at eveina_left
    ev "Лея, ты как-то не выглядишь убеждённой своим же рассказом." (show_side="left", show_kind="speech")
    hide eveina

    show leya smile at leya_right
    le "Кто я такая, чтобы спорить с Вайскорп." (show_side="right", show_kind="speech")
    hide leya

    n "Она покрутила кружку в руках." (show_side="none", show_kind="speech")

    show leya thinking at leya_right
    le "Просто... если бы ты хотела отомстить за похищение своих людей..." (show_side="right", show_kind="speech")
    hide leya
    show leya eyebrow at leya_right
    le "Разве ты бы стала стирать память об этой мести?" (show_side="right", show_kind="speech")
    hide leya

    n "Никто не ответил." (show_side="none", show_kind="speech")
    n "Вопрос повис в воздухе — тихий, неудобный." (show_side="none", show_kind="speech")

    show leya normal at leya_right
    le "Не говоря уже о том, что Академия и Вайскорп сами подтвердили: похищения илейн всё же имели место быть." (show_side="right", show_kind="speech")
    hide leya

    show eveina eyebrow at eveina_left
    ev "Да. Звучит нелогично." (show_side="left", show_kind="speech")
    hide eveina

    show eveina thinking at eveina_left
    ev_thought "«Этика стала переменной»." (show_side="left", show_kind="thought")
    hide eveina
    show eveina eyebrow at eveina_left
    ev_thought "Вот что он имел в виду." (show_side="left", show_kind="thought")
    hide eveina

    n "Она сделала ещё глоток. Лабораторный самогон был уже почти привычным." (show_side="none", show_kind="speech")
    n "Теро пересел чуть ближе к Лее — когда рассказывал страшную часть. Лея этого не заметила." (show_side="none", show_kind="speech")

    show noa intrigued at noa_right
    no "Ладно. Хватит на сегодня детективов. Кто будет ещё?" (show_side="right", show_kind="speech")
    hide noa

    show leya eyebrow at leya_right
    le "Только если Теро потом дотащит нас до комнаты." (show_side="right", show_kind="speech")
    hide leya

    show tero normal at tero_right
    te "Я всегда дотаскиваю." (show_side="right", show_kind="speech")
    hide tero

    show noa smile at noa_right
    no "Это потому что ты единственный, кто не пьёт." (show_side="right", show_kind="speech")
    hide noa

    show tero normal at tero_right
    te "Именно." (show_side="right", show_kind="speech")
    hide tero

    n "Ноа разлил по третьему кругу." (show_side="none", show_kind="speech")
    n "За окном было совсем темно. Эвейна смотрела в кружку." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev_thought "Три года назад. Массовое стирание. Пропавшая студентка. Вайскорп забрала Академию." (show_side="left", show_kind="thought")
    hide eveina
    show eveina eyebrow at eveina_left
    ev_thought "Вот что ты хочешь знать, Эриан." (show_side="left", show_kind="thought")
    hide eveina
    show eveina thinking at eveina_left
    ev_thought "Но почему ты сам не можешь это найти?" (show_side="left", show_kind="thought")
    hide eveina

    n "Ответа у неё не было. Зато теперь было кое-что другое — козырь, которого раньше не было." (show_side="none", show_kind="speech")
    n "Вечер продолжался ещё какое-то время — тёплый, немного смазанный по краям. Хороший." (show_side="none", show_kind="speech")

    jump scene_3_4
