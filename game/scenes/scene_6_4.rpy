label scene_6_4:
    $ previous_scene = "scene_6_3"
    $ next_scene = "scene_6_5"
    $ current_scene = "scene_6_4"
    call fade_to_black(1.2, 0.8)
    scene bg lab at bg_fullscreen with dissolve

    n "Подготовка к тестам стала для Эвейны не просто рутиной — ритуалом." (show_side="none", show_kind="speech")
    n "Лея приносила кофе, садилась рядом, мурлыкала себе под нос что-то на несуществующем языке, пока Эвейна грызла текстовые ряды и графики, словно они были ключом к тому, от чего зависела жизнь. Так, в общем-то, и было." (show_side="none", show_kind="speech")
    n "Эриан не появлялся уже несколько дней. И всё же — иногда, в коротких провалах внимания, Эвейна вспоминала: как сияла каждая травинка на поляне, вторя отблеску его глаз, как вертикальные зрачки читали её душу." (show_side="none", show_kind="speech")
    n "Миг, невозможный и прекрасный." (show_side="none", show_kind="speech")
    n "А потом наступил этот день." (show_side="none", show_kind="speech")

    show eveina normal at eveina_left
    ev_thought "Конечно, именно сегодня он возвращается. Каэль." (show_side="left", show_kind="thought")
    hide eveina
    show eveina thinking at eveina_left
    ev_thought "И, конечно, именно сегодня я решила захватить в лабораторию стакан кофе." (show_side="left", show_kind="thought")
    hide eveina
    show eveina normal at eveina_left
    ev_thought "Действительно, зачем оставлять себе хоть каплю надежды на спокойное начало?" (show_side="left", show_kind="thought")
    hide eveina

    show kael eyebrow at kael_right
    ka "Ты не ошиблась дверью?" (show_side="right", show_kind="speech")
    hide kael

    n "Эвейна удивленно вскинула на него взгляд, отвлекаясь от своих мыслей и понимая, что она уже пересекла порог лаборатории." (show_side="none", show_kind="speech")
    n "Каэль медленно перевёл недовольный взгляд с её лица на стакан в руке." (show_side="none", show_kind="speech")

    show kael serious at kael_right
    ka "Этому здесь не место." (show_side="right", show_kind="speech")
    hide kael

    show eveina eyeroll at eveina_left
    ev_thought "И на что я вообще рассчитывала?" (show_side="left", show_kind="thought")
    hide eveina
    show eveina thinking at eveina_left
    ev_thought "Придется вернуться в столовую и сдать остатки надежды на человеческое отношение." (show_side="left", show_kind="thought")
    hide eveina

    n "Пока она, ругая себя за беспечность, относила стакан, он уже раздал задание остальным. К её возвращению — только одно незанятое место." (show_side="none", show_kind="speech")

    show eveina eyebrow at eveina_left
    ev "Эм… Каэль?" (show_side="left", show_kind="speech")
    hide eveina

    n "Парень не удосужился поднять на неё взгляд. Она обвела аудиторию растерянным взглядом и столкнулась глазами с Сайласом." (show_side="none", show_kind="speech")

    show silas normal at silas_right
    si "..." (show_side="right", show_kind="speech")
    hide silas

    n "Он улыбнулся ей в немом привествии и кивнул в сторону Каэля, пожав плечами." (show_side="none", show_kind="speech")

    show eveina eyeroll at eveina_left
    ev_thought "Ожидаемо. Ладно, попробуем снова." (show_side="left", show_kind="thought")
    hide eveina
    show eveina eyebrow at eveina_left
    ev "Каэль, я не знаю, чем мне заняться. Выдай мне задачу." (show_side="left", show_kind="speech")
    hide eveina

    n "Пальца Каэля, летающие по интерфейсу, на секунду зависли в воздухе. Всем телом Эвейна почувствовала, как температура воздуха вокруг снизилась на несколько градусов." (show_side="none", show_kind="speech")
    n "Она уже была готова отбиваться от очередной колкости." (show_side="none", show_kind="speech")
    n "Но вместо этого Каэль молча встал, подошёл к ней, нетерпеливо постучал пальцами по креслу, ожидая, когда она сядет, а потом открыл на экране последние наработки по задаче Идентики." (show_side="none", show_kind="speech")

    show kael normal at kael_right
    ka "Доведи процент синхронизации до шестидесяти." (show_side="right", show_kind="speech")
    hide kael

    n "Она вскинула на него взгляд, ища подвох." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev_thought "В прошлые попытки он еле-еле перевалил за тридцать пять. И это только с его помощью. Но шестьдесят?" (show_side="left", show_kind="thought")
    hide eveina
    show eveina eyebrow at eveina_left
    ev "Это вообще реально?" (show_side="left", show_kind="speech")
    hide eveina

    n "Она не собиралась говорить это вслух, шепот просто сорвался с её губ. Каэль услышал. Конечно, услышал." (show_side="none", show_kind="speech")
    n "Успев сделать пару шагов в сторону, он снова вернулся к ней за спину. Наклонился и только ей слышным шепотом произнёс:" (show_side="none", show_kind="speech")

    show kael serious at kael_right
    ka "Реально то, что мы делаем реальностью, Хейла." (show_side="right", show_kind="speech")
    hide kael   
    show kael thinking at kael_right
    ka "Может, ты действительно так умна, как себе кажешься." (show_side="right", show_kind="speech")
    hide kael   
    show kael serious at kael_right
    ka "А может, все твои успехи — лишь статистический выброс." (show_side="right", show_kind="speech")
    hide kael

    show eveina thinking at eveina_left
    ev_thought "Ну спасибо, Каэль. Вот бы ещё диаграмму отклонения моего существования приложил — для наглядности." (show_side="left", show_kind="thought")
    ev_thought "А то вдруг кто-то не понял, насколько я здесь лишняя." (show_side="left", show_kind="thought")
    hide eveina
    show eveina annoyed at eveina_left
    ev "Да, я уже поняла, что ты считаешь ошибкой и меня, и всё, что со мной связано." (show_side="left", show_kind="speech")
    hide eveina

    n "Он резко отстранился, не сказав ни слова. И больше к ней не подходил. Только бродил по лаборатории, холодно комментируя работу других студентов." (show_side="none", show_kind="speech")
    n "Эвейна взялась за работу." (show_side="none", show_kind="speech")

    call fade_to_black(1.2, 0.8)
    scene bg lab at bg_fullscreen with dissolve

    show eveina eyeroll at eveina_left
    ev_thought "Три часа ада. И кое-как тридцать восемь процентов." (show_side="left", show_kind="thought")
    hide eveina

    n "Последний час настройками она буквально двигала доли процентов вперёд и назад, словно капли в иссохшем колодце. Сотая доля вперёд — три назад. И снова. И снова." (show_side="none", show_kind="speech")

    show eveina upset at eveina_left
    ev_thought "А что, если он прав? Что, если это и правда была просто удача?" (show_side="left", show_kind="thought")
    hide eveina
    show eveina eyebrow at eveina_left
    ev_thought "Или он снова ставит передо мной невыполнимую цель, а потом с интересом наблюдает за моей реакцией?" (show_side="left", show_kind="thought")
    hide eveina
    
    n "Взгляд девушки метнулся в сторону Каэля, но тот не выдавал ни малейших признаков интереса. И уж точно на неё не смотрел." (show_side="none", show_kind="speech")  
    n "Она сидела перед терминалом, направив взгляд куда-то сквозь цифры, будто что-то за ними могло дать ответ." (show_side="none", show_kind="speech")
    n "Но ответ был внутри. И он был пугающим." (show_side="none", show_kind="speech")

    show eveina sad at eveina_left
    ev_thought "Я — ошибка. Маленькая, наивная ошибка в большом эксперименте жизни." (show_side="left", show_kind="thought")
    hide eveina

    n "Эвейна медленно встала, привлекая к себе внимание остальных студентов." (show_side="none", show_kind="speech")

    show eveina sad at eveina_left
    ev_thought "Ну и плевать... смотрите, как это местро ломает людей. Потому что вы — следующие." (show_side="left", show_kind="thought")
    hide eveina
    
    n "Она собрала вещи и двинулась к выходу, произнеся сухое «до свидания», будто в горле был песок. Каэль не поднял головы, не двинулся, будто её и не существовало." (show_side="none", show_kind="speech")

    show eveina angry at eveina_left
    ev_thought "Вежлив, как всегда. Ну и чёрт с тобой." (show_side="left", show_kind="thought")
    hide eveina

    n "Она вышла. А в груди остался гул — не от поражения, нет. От того, что внутри снова что-то надломилось. И на этот раз она не понимала, как это склеить." (show_side="none", show_kind="speech")

    jump scene_6_5
