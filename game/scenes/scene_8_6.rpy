label scene_8_6:
    $ previous_scene = "scene_8_5"
    $ next_scene = "scene_8_7"
    $ current_scene = "scene_8_6"
    call fade_to_black(1.2, 0.8)
    scene bg eveina_room at bg_fullscreen with dissolve

    n "Лея сидела у окна с планшетом и наушниками, полностью погружённая в учебные материалы." (show_side="none", show_kind="speech")
    n "Эвейна села за стол, активировала терминал и открыла документ с рекомендацией." (show_side="none", show_kind="speech")

    scene bg recomendation_list1 at bg_fullscreen with dissolve
    pause
    scene bg recomendation_list2 at bg_fullscreen with dissolve
    pause

    scene bg eveina_room at bg_fullscreen with dissolve

    n "Она несколько раз перечитала письмо, прежде чем откинуться в кресле и сжать виски руками." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev_thought "Ну... Если быть честной, с такой рекомендацией я бы сама себя куда угодно приняла." (show_side="left", show_kind="thought")
    ev_thought "Но вот это...«за долгие годы я редко встречал»..." (show_side="left", show_kind="thought")
    hide eveina
    show eveina eyebrow at eveina_left
    ev_thought "Значит ли это, что мы с ним встречались? Или просто оборот речи такой?" (show_side="left", show_kind="thought")
    hide eveina
    show eveina normal at eveina_left
    ev_thought "Я абсолютно точно никогда не слышала этого имени раньше." (show_side="left", show_kind="thought")
    hide eveina
    show eveina thinking at eveina_left
    ev_thought "И это его «прошу дать ей шанс»..." (show_side="left", show_kind="thought")
    hide eveina
    show eveina normal at eveina_left
    ev_thought "Я никогда всерьез не задумывалась об этом, но..." (show_side="left", show_kind="thought")
    hide eveina
    show eveina eyebrow at eveina_left
    ev_thought "Зачем вообще он написал рекомендации мне?" (show_side="left", show_kind="thought")
    hide eveina
    show eveina annoyed at eveina_left
    ev_thought "Чёрт, что здесь вообще происходит? Чушь какая-то!" (show_side="left", show_kind="thought")
    hide eveina
    show eveina upset at eveina_left
    ev_thought "Голова разболелась от всего этого бреда..." (show_side="left", show_kind="thought")
    hide eveina
    show eveina thinking at eveina_left
    ev_thought "Мне нужно что-то понятное, что-то, за что можно зацепиться." (show_side="left", show_kind="thought")
    hide eveina

    n "Эвейна устало поднялась, молча прошла к кровати, и рухнула на неё лицом вниз. А потом, чуть подумав, перевернулась и активировала Сайфа." (show_side="none", show_kind="speech")

    show sf at ai_right
    sf "О, честь, наконец, оказана." (show_side="right", show_kind="speech")
    sf "Приятно знать, что моё существование всё ещё входит в твою систему экстренных вызовов. Как приятно быть нужным — иногда." (show_side="right", show_kind="speech")
    hide sf 

    show eveina smile at eveina_left
    ev "И тебе вечер добрый, обиженное облако данных." (show_side="left", show_kind="speech")
    hide eveina

    show sf at ai_right
    sf "Надеюсь, взлом планшета Вирта прошёл успешно?" (show_side="right", show_kind="speech")
    sf "Хотя, судя по тому, что ты всё ещё в Академии — ты наконец-то сделала правильный выбор?" (show_side="right", show_kind="speech")
    hide sf 

    show eveina thinking at eveina_left
    ev "Не совсем. План самоуничтожения с треском провалился." (show_side="left", show_kind="speech")
    hide eveina

    show sf at ai_right
    sf "Ты в порядке? Или сейчас снова будет душераздирающая пауза перед ответом?" (show_side="right", show_kind="speech")
    hide sf 

    show eveina eyeroll at eveina_left
    ev "Я не знаю." (show_side="left", show_kind="speech")
    hide eveina
    show eveina normal at eveina_left
    ev "Но если ты опять собираешься подключиться к эмоциональному анализу — предупреди. Я подберу драматичную позу." (show_side="left", show_kind="speech")
    hide eveina

    show sf at ai_right
    sf "Судя по уровню сарказма — с тобой всё в порядке." (show_side="right", show_kind="speech")
    hide sf 

    show eveina thinking at eveina_left
    ev "Ладно, хватит душевных откровений." (show_side="left", show_kind="speech")
    hide eveina
    show eveina eyebrow at eveina_left
    ev "Что у нас по подозрительным профессорам с гладкими речами и странными мотивами?" (show_side="left", show_kind="speech")
    ev "Что там с Кайстром?" (show_side="left", show_kind="speech")
    hide eveina

    n "Проекция несколько секунд мерцала, вторя ударам сердца в груди девушки. Потом Сайф заговорил:" (show_side="none", show_kind="speech")

    show sf at ai_right
    sf "Я… нашёл нечто. Но не уверен, что правильно это понимаю." (show_side="right", show_kind="speech")
    sf "И не уверен, что хочу в этом участвовать." (show_side="right", show_kind="speech")
    hide sf 

    show eveina annoyed at eveina_left
    ev "Ты уже по уши в этом. Так что давай, удиви меня." (show_side="left", show_kind="speech")
    ev "Или хотя бы не испорти вечер своим молчанием. Он и так выдался непростым." (show_side="left", show_kind="speech")
    hide eveina

    n "На экране браслета всплыл фрагмент письма. Без отправителя. Только строчка:" (show_side="none", show_kind="speech")
    n "{i}«...кажется, эти запросы делали просто любопытные студенты. Ничего серьёзного. Да и кому придёт в голову искать Далона в Академии?»{/i}" (show_side="none", show_kind="speech")

    show eveina eyebrow at eveina_left
    ev_thought "...кому придёт в голову искать Далона в Академии?" (show_side="left", show_kind="thought")
    hide eveina

    n "Строчка пульсировала, вторя нарастающему пульсу в висках. Эвейна хрипло выдавила из себя:" (show_side="none", show_kind="speech")

    show eveina wondered at eveina_left
    ev_thought "Это значит… он был здесь? Всё это время?" (show_side="left", show_kind="thought")
    hide eveina

    n "Она не могла ни говорить, ни дышать. Мысли рвались в разные стороны." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev_thought "Если Кайр Далон действительно находился в Академии всё это время…" (show_side="left", show_kind="thought")
    hide eveina
    show eveina wondered at eveina_left
    ev_thought "Кто ещё об этом знает? Кто-то прикрывает его?" (show_side="left", show_kind="thought")
    ev_thought "Мог ли он знать о том, что я ищу его? Мог ли он следить за моими поисками?" (show_side="left", show_kind="thought")
    hide eveina

    n "Внезапное осознание ударило под дых. Она резко села, взглянула на проекцию Сайфа и спросила:" (show_side="none", show_kind="speech")

    show eveina eyebrow at eveina_left
    ev "Сайф… кто тебя создал?" (show_side="left", show_kind="speech")
    hide eveina

    n "Наступила долгая пауза, а потом — ожидаемый ответ:" (show_side="none", show_kind="speech")

    show sf at ai_right
    sf "У тебя нет доступа к этой информации." (show_side="right", show_kind="speech")
    hide sf 

    show eveina annoyed at eveina_left
    ev_thought "Ну уж нет, набор ноликов и единичек, так легко ты не отделаешься..." (show_side="left", show_kind="thought")
    hide eveina
    show eveina angry at eveina_left
    ev_thought "Не в этот раз." (show_side="left", show_kind="thought")
    hide eveina

    show eveina annoyed at eveina_left
    ev "Это был Кайр Далон?" (show_side="left", show_kind="speech")
    hide eveina

    show sf at ai_right
    sf "Нет. К счастью — нет." (show_side="right", show_kind="speech")
    sf "Спасибо, конечно, за столь лестное предположение, но я предпочитаю не быть детищем трусливых неудачников. Даже если это модно." (show_side="right", show_kind="speech")
    hide sf 

    show eveina thinking at eveina_left
    ev_thought "Вряд ли он мне соврал так прямолинейно." (show_side="left", show_kind="thought")
    hide eveina
    show eveina eyebrow at eveina_left
    ev_thought "ИИ вообще умеют лгать?" (show_side="left", show_kind="thought")
    hide eveina
    show eveina annoyed at eveina_left
    ev_thought "Пфф, чушь какая, конечно, умеют. Чему их научат, то и умеют." (show_side="left", show_kind="thought")
    hide eveina
    show eveina thinking at eveina_left
    ev_thought "Но всё же..." (show_side="left", show_kind="thought")
    hide eveina

    n "Бестелесный голос вырвал её из раздумий до того, как она успела решить, говорит ли он правду." (show_side="none", show_kind="speech")

    show sf at ai_right
    sf "Мне нужно отключиться. Я оставил следы в системе Кайстра. Мне стоило бы... исчезнуть на время." (show_side="right", show_kind="speech")
    hide sf 

    n "Проекция погасла. Эвейна осталась в тишине, нарушаемой только тихим мурлыканьем напевающей себе что-то Леи." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev_thought "Итак, Кайр Далон… здесь?" (show_side="left", show_kind="thought")
    hide eveina

    n "Нет. Она не могла утверждать это наверняка. Это было всего лишь предположение, гипотеза, зацепка — но она билась в голове, как истина." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev_thought "Если он действительно в Академии… то где он?" (show_side="left", show_kind="thought")
    hide eveina
    show eveina eyebrow at eveina_left
    ev_thought "Как прячется? Почему никто ничего не знает?" (show_side="left", show_kind="thought")
    ev_thought "Как Эриан мог не знать? Как Вирт не смог ничего заподозрить?" (show_side="left", show_kind="thought")
    hide eveina
    show eveina annoyed at eveina_left
    ev_thought "Если Кайр Далон действительно здесь — как они могли этого не заметить? Или всё-таки заметили?" (show_side="left", show_kind="thought")
    hide eveina
    show eveina angry at eveina_left
    ev_thought "И просто… решили не говорить ей?" (show_side="left", show_kind="thought")
    hide eveina

    n "Мысль была неприятной, больно врезавшейся в самое нутро. Как будто кто-то вкрутил иглу прямо под рёбра." (show_side="none", show_kind="speech")

    show eveina angry at eveina_left
    ev_thought "Может, даже Сайф знал. Может, знал с самого начала." (show_side="left", show_kind="thought")
    ev_thought "А я? Просто удобная дура, которой подкидывают по крошке — то строчку в письме, то размазанную подпись в книге." (show_side="left", show_kind="thought") 
    ev_thought "Чтобы не убежала. Чтобы продолжала копать." (show_side="left", show_kind="thought") 
    ev_thought "Идеальная искательница в лабиринте, которую все трое ведут, держа на коротком поводке и уверяя, что вот-вот — за следующим углом — правда." (show_side="left", show_kind="thought") 
    hide eveina

    n "Эвейна села, опёршись локтями на колени. Всё, что казалось стабильным, снова шатнулось. Доверие — хрупкая вещь. А сейчас оно трещало — ко всем сразу." (show_side="none", show_kind="speech")
    n "Комната казалась тесной. Потолок — слишком низким. Сердце билось слишком громко." (show_side="none", show_kind="speech")
    n "Все слова, сказанные за день, теперь казались намёками. И каждое — значило больше, чем тогда." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev_thought "Или… я снова перегибаю?" (show_side="left", show_kind="thought")
    hide eveina
    show eveina eyebrow at eveina_left
    ev_thought "С чего я вообще взяла, что Кайр Далон здесь? Одна строчка в письме? Возможно, я её неправильно поняла…" (show_side="left", show_kind="thought")
    hide eveina
    show eveina thinking at eveina_left
    ev_thought "Возможно, он давно мёртв. Или исчез. Или никогда и не приближался к Академии." (show_side="left", show_kind="thought")
    ev_thought "А эта чёртова рекомендация — чья-то недобрая шутка." (show_side="left", show_kind="thought")
    hide eveina

    n "Она провела ладонью по лицу, пытаясь собрать в кучу остатки самообладания." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev_thought "Вирт уже сделал для меня больше, чем сделал бы кто угодно." (show_side="left", show_kind="thought")
    ev_thought "Уж точно больше, чем друзья моего отца, которые наблюдали, как я росла." (show_side="left", show_kind="thought")
    ev_thought "А Эриан… он искал Далона ещё до меня. У него не было причин молчать об этом, так ведь?" (show_side="left", show_kind="thought")
    hide eveina

    n "Эти мысли немного остудили воображение. Не уничтожили сомнения, но вернули равновесие. Ровно настолько, чтобы не сорваться." (show_side="none", show_kind="speech")
    n "Она ещё не знала, во что верить, но знала что нужно делать." (show_side="none", show_kind="speech")

    jump scene_8_7
