label scene_8_9:
    $ previous_scene = "scene_8_8"
    $ next_scene = "to_be_continued"
    $ current_scene = "scene_8_9"

    call fade_to_black(1.2, 0.8)
    scene bg lecture_hall at bg_fullscreen with dissolve

    n "Эвейна стояла перед Виртом, не поднимая глаз. Его голос ещё звенел в ушах, а руки дрожали." (show_side="none", show_kind="speech")
    n "Она уже почти смирилась с тем, что сейчас всё рухнет — отношения, доверие, её присутствие в Академии, надежда на спасение отца." (show_side="none", show_kind="speech")
    n "Буквально всё." (show_side="none", show_kind="speech")

    show virt serious at virt_right
    vi "Ты обманула моё доверие. И не один раз, Эвейна." (show_side="right", show_kind="speech")
    vi "Я пытался закрывать глаза. Пытался защищать тебя. Но ты снова перешла черту." (show_side="right", show_kind="speech")
    show virt angry at virt_right
    vi "Каждый раз, когда я очерчивал новую, ты стремилась тут же перепрыгнуть её." (show_side="right", show_kind="speech")
    hide virt

    n "Он в который раз нервно провёл руками по волосам и отвернулся на несколько долгих секунд, в течение которых Эвейны слышала только рваное биение своего сердца." (show_side="none", show_kind="speech")
    n "А потом Вирт медленно обернулся обратно, и голос его звучал уже почти умоляюще:" (show_side="none", show_kind="speech")

    show virt upset thinking at virt_right
    vi "Скажи, что это сделала не ты." (show_side="right", show_kind="speech")
    vi "Что это глупая случайность, и ты ни при чём..." (show_side="right", show_kind="speech")
    hide virt
    show virt upset at virt_right
    vi "Дай мне хоть одну причину не исключить тебя прямо здесь и сейчас, Эвейна." (show_side="right", show_kind="speech")
    hide virt

    show eveina thinking at eveina_left
    ev_thought "Ну, технически, это и правда не я…" (show_side="left", show_kind="thought")
    hide eveina
    show eveina annoyed at eveina_left
    ev_thought "Соври! Заставь его поверить!" (show_side="left", show_kind="thought")
    hide eveina
    show eveina thinking at eveina_left
    ev_thought "Он же сам этого хочет… сам об этом просит." (show_side="left", show_kind="thought")
    hide eveina

    n "Эвейна подняла на него глаза и тихим, но твёрдым голосом произнесла:" (show_side="none", show_kind="speech")

    show eveina normal at eveina_left
    ev "Это сделала я." (show_side="left", show_kind="speech")
    hide eveina
    show eveina thinking at eveina_left
    ev_thought "Одной фразой я и прокладываю путь к искренности, и закладываю фундамент новой стены между нами." (show_side="left", show_kind="thought")
    ev_thought "Великолепно. Кажется, пора признать, что стратегия — это не моё." (show_side="left", show_kind="thought")
    hide eveina

    show virt upset at virt_right
    vi "Эвейна, я..." (show_side="right", show_kind="speech")
    hide virt

    n "Аурелиан осёкся на полуслове, заставив девушку поднять глаза. Его взгляд вдруг стал непроницаемым, и направлен он был не на Эвейну, а за её спину." (show_side="none", show_kind="speech")
    n "Воздух вдруг изменился. Словно тень прошла по залу, заставив едва уловимо дрожать всё пространство. Вирт прищурился." (show_side="none", show_kind="speech")
    n "У входа в лекционный зал, в самой его тени, появился почти невесомый силуэт." (show_side="none", show_kind="speech")
    n "Он шёл медленно, но шаги эхом отдавались по залу. Ни один из них не был громким, но каждый — ощущался всем телом." (show_side="none", show_kind="speech")
    n "Эвейна почувствовала знакомых холодок, пробежавший по шее, но прежде, чем успела обернуться..." (show_side="none", show_kind="speech")

    show erian normal at erian_right
    er "Я бы не стал на вашем месте продолжать, профессор." (show_side="right", show_kind="speech")
    hide erian 

    n "Девушка резко развернулась вокруг своей оси, услышав знакомый голос. Секундная радость мгновенно сменилась страхом, когда она поняла, что Вирт тоже здесь — тоже его видит." (show_side="none", show_kind="speech")

    show eveina wondered at eveina_left
    ev "Что ты здесь...?" (show_side="left", show_kind="speech")
    hide eveina

    show erian intrigued at erian_right
    er "Пришёл тебя выручать, Каэ’нари." (show_side="right", show_kind="speech")
    hide eveina

    n "Он подошёл к ней вплотную и подмигнул, словно не явился на её казнь. Наклонившись к её уху, едва ощутимым движением пробежался пальцами по скуле и ласково прошептал:" (show_side="none", show_kind="speech")

    show erian intrigued at erian_right
    er "Ну что, сначала дадим ему отшлёпать тебя? Или сразу перейдём к делу?" (show_side="right", show_kind="speech")
    hide erian 

    show eveina angry at eveina_left
    ev_thought "Ты совсем охренел?" (show_side="left", show_kind="thought")
    hide eveina

    n "Эвейна бросила на него злобный взгляд, несмотря на возникшую вдруг дрожь по всему телу от его присутствия, которая ощущалась в разы сильнее, чем прежде." (show_side="none", show_kind="speech")
    n "Ответом ей была ленивая ухмылка, слишком явно говорящая, что ничего хорошего сейчас ждать не стоит. Собрав всю свою решительность в кулак, она тихо произнесла:" (show_side="none", show_kind="speech")

    show eveina annoyed at eveina_left
    ev "Уходи, Эриан. Я справлюсь сама." (show_side="left", show_kind="speech")
    hide eveina

    show erian intrigued at erian_right
    er "Приказываешь мне?" (show_side="right", show_kind="speech")
    hide erian
    show erian normal at erian_right
    er "Я никуда не уйду." (show_side="right", show_kind="speech")
    hide erian
    show erian thinking at erian_right
    er "Тут такое дело... Я действительно избавлю тебя от этого неловкого разговора, что бы ты там опять не натворила." (show_side="right", show_kind="speech")
    hide erian
    show erian intrigued at erian_right
    er "Но пришёл сюда не за этим." (show_side="right", show_kind="speech")
    hide erian

    show eveina annoyed at eveina_left
    ev "Чёрт... и что тебе здесь нужно?" (show_side="left", show_kind="speech")
    hide eveina
    show eveina angry at eveina_left
    ev "Либо объясни по-человечески, либо проваливай ко всем чертям, где тебя и носило!" (show_side="left", show_kind="speech")
    hide eveina

    show erian intrigued at erian_right
    er "Ух, какая грозная... совсем осмелела, пока меня не было?" (show_side="right", show_kind="speech")
    hide erian

    n "В глазах парня недобро сверкнуло, заставляя девушку сжаться под его выжигающим взглядом." (show_side="none", show_kind="speech")
    n "Стоять здесь, так близко к Эриану прямо на глазах у Вирта было… неловко." (show_side="none", show_kind="speech")
    n "Несмотря на продолжительную перепалку, профессор сохранял полное молчание, и девушка боялась даже обернуться в его сторону." (show_side="none", show_kind="speech")
    n "Что она увидит в его глазах? Злость? Разочарование? Признание её предательства? Эвейна застыла, остро ощущая, что находится между двух огней." (show_side="none", show_kind="speech") 
    n "Что-то во взгляде Эриана подсказывало, что он просто так не уйдёт. И выхода из этой ситуации она не видела." (show_side="none", show_kind="speech")

    show eveina sad at eveina_left
    ev_thought "Чёрт... Эриан, пожалуйста..." (show_side="left", show_kind="thought")
    hide eveina

    n "У Эриана, впрочем, были совсем другие планы." (show_side="none", show_kind="speech")

    show erian intrigued at erian_right
    er "Как там двигается наш план, Эвейна? Успела забраться нашему декану в голову и выяснить всё, что планировала?" (show_side="right", show_kind="speech")
    hide erian

    n "От этих тихих, но отчётливых слов, разнёсшихся по лекторию, глаза Эвейны невольно наполнились слезами. Она прикрыла их и закусила губу." (show_side="none", show_kind="speech")

    show eveina upset at eveina_left
    ev_thought "Что ты творишь..." (show_side="left", show_kind="thought")
    hide eveina

    n "Парень, казалось, не замечал её переживаний, продолжая лениво улыбаться." (show_side="none", show_kind="speech")

    show erian intrigued at erian_right
    er "Дай угадаю, он не сказал тебе ничего полезного, верно?" (show_side="right", show_kind="speech")
    hide erian  
    show erian wild smile at erian_right
    er "Только участливо похлопывал по плечу, наблюдая, как ты мечешься и совершаешь новые ошибки?" (show_side="right", show_kind="speech")
    hide erian 

    n "Эти слова больно ударили в грудь, заставляя одинокую слезу скатиться из полуприкрытых век." (show_side="none", show_kind="speech")
    n "Улыбка сползла с лица парня, на мгновение сменяясь сомнением. Он нежно коснулся пальцами её щеки, стирая мокрую дорожку и приподнимая её лицо за подбородок." (show_side="none", show_kind="speech")
    n "Склонившись к ней, он положил руку на её плечо, чуть сжимая. Словно прося прощения, которое никогда не будет произнесено вслух." (show_side="none", show_kind="speech")

    show erian normal at erian_right
    er "Эвейна, послушай... благодаря тебе я нашёл его." (show_side="right", show_kind="speech")
    er "Всё это время он был здесь, прямо перед моим носом." (show_side="right", show_kind="speech")
    hide erian 

    show eveina sad at eveina_left
    ev_thought "Что? О чём он говорит?" (show_side="left", show_kind="thought")
    ev_thought "Далон здесь? В Академии?" (show_side="left", show_kind="thought")
    hide eveina
    show eveina annoyed at eveina_left
    ev_thought "И это повод врываться сюда и ставить меня в такое положение?" (show_side="left", show_kind="thought")
    hide eveina
    show eveina angry at eveina_left
    ev_thought "Опять дурацкая ревность к Вирту? Или..." (show_side="left", show_kind="thought")
    hide eveina
    show eveina angry at eveina_left
    ev "Что ты пытаешься мне сказать? Объясни нормально!" (show_side="left", show_kind="speech")
    hide eveina

    show erian normal at erian_right
    er "Я же и объясняю..." (show_side="right", show_kind="speech")
    hide erian 

    n "Эриан выпрямился и, продолжая держать её за плечо одной рукой, другой осторожно развернул обратно к Вирту." (show_side="none", show_kind="speech")
    n "Девушка замерла, непонимающе смотря перед собой. Мир словно рассыпался на фрагменты, в которых она пыталась найти опору." (show_side="none", show_kind="speech")

    show eveina wondered at eveina_left
    ev_thought "Что... что здесь происходит?" (show_side="left", show_kind="thought")
    hide eveina
    
    n "Она непонимающе смотрела на Вирта, будто он что-то мог ей объяснить. Но взгляд профессора был прикован не к ней." (show_side="none", show_kind="speech")

    show virt serious at virt_right
    vi "Здравствуй, Эриан." (show_side="right", show_kind="speech")
    hide virt

    n "Он произнёс это ровно. В голосе не было ни удивления, ни страха, только какая-то бесконечная усталость." (show_side="none", show_kind="speech")
    n "Он смотрел на него как на давно забытую страницу, которую кто-то снова открыл. Потом медленно перевёл печальный взгляд на Эвейну." (show_side="none", show_kind="speech")

    show virt upset at virt_right
    vi "Это многое объясняет." (show_side="right", show_kind="speech")
    hide virt

    jump to_be_continued
