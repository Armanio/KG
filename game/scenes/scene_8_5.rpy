label scene_8_5:
    $ previous_scene = "scene_8_4"
    $ next_scene = "scene_8_6"
    $ current_scene = "scene_8_5"
    call fade_to_black(1.2, 0.8)
    scene bg virt_cabinet at bg_fullscreen with dissolve

    n "Следующие несколько дней Эвейна возвращалась в привычный ритм, погрузившись в учёбу." (show_side="none", show_kind="speech")
    n "Внутри бурлило нетерпение, тревожное желание вернуться к поискам, но она терпеливо ждала. Ведь Аурелиан просил довериться ему. А Эриан вообще пропал с концами." (show_side="none", show_kind="speech")
    n "Она чуть не подпрыгнула от возбуждения, когда пришло короткое уведомление:" (show_side="none", show_kind="speech")

    n "📩 {i}Входящее сообщение{/i}\n{i}Отправитель: Аурелиан Вирт{/i}\n{i}Тема: Личный разговор{/i}\n\n{i}Мисс Хейла, Просьба в удобное для вас время подойти в мой кабинет. Хотел бы обсудить информацию, которой вы обладаете, и определить возможные шаги.\nС уважением, А. Вирт{/i}" (show_side="none", show_kind="speech")
    
    n "Кабинет декана, как всегда, пах древесным мхом и чаем. Профессор стоял у окна, повернувшись спиной." (show_side="none", show_kind="speech")

    show virt normal at virt_right
    vi "Рад, что ты восстановилась." (show_side="right", show_kind="speech")
    hide virt

    show virt thinking at virt_right
    vi "Надеюсь, теперь ты расскажешь мне, что тебе известно, и мы сможем поговорить открыто." (show_side="right", show_kind="speech")
    hide virt


    n "Эвейна не спешила отвечать. Она давно ждала этого разговора и сейчас, смотря на его напряжённые плечи, спросила о том, что давно крутилось в её голове:" (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev_thought "Ну раз мы на теперь на «ты»..." (show_side="left", show_kind="thought")
    hide eveina
    show eveina normal at eveina_left
    ev "Ты был знаком с моим отцом?" (show_side="left", show_kind="speech")
    hide eveina

    n "Аурелиан медленно повернул голову." (show_side="none", show_kind="speech")

    show virt normal at virt_right
    vi "Мы встречались на нескольких конференциях." (show_side="right", show_kind="speech")
    vi "Я знал его как сильного врача. Уважаемого. Мы не были близки, но крутились в одном сообществе… и я запомнил его." (show_side="right", show_kind="speech")
    hide virt

    n "Эвейна кивнула, мысленно собираясь с мыслями, чтобы задать следующий вопрос." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev_thought "Если не сейчас, то я никогда не решусь..." (show_side="left", show_kind="thought")
    hide eveina
    show eveina normal at eveina_left
    ev "Ты знаком с Кайром Далоном?" (show_side="left", show_kind="speech")
    hide eveina

    n "Аурелиан тяжело вздохнул, поняв, что разговор идёт не по плану. Сел в рабочее кресло, сцепив пальцы перед собой." (show_side="none", show_kind="speech")

    show virt thinking at virt_right
    vi "Когда-то мы были друзьями." (show_side="right", show_kind="speech")
    hide virt
    show virt serious at virt_right
    vi "Почему ты спрашиваешь?" (show_side="right", show_kind="speech")
    hide virt

    show eveina normal at eveina_left
    ev "Он — основоположник препарата NR-Δ3. Я думаю… если найду его — он поможет мне вылечить отца." (show_side="left", show_kind="speech")
    hide eveina

    n "Вирт отвёл взгляд, сжал пальцами переносицу. Казалось, следующие слова дались ему с трудом." (show_side="none", show_kind="speech")
    
    show virt upset at virt_right
    vi "Не думаю, что он тебе поможет, Эвейна." (show_side="right", show_kind="speech")
    hide virt
    show virt thinking at virt_right
    vi "Про него уже много лет никто ничего не слышал. Он даже себе помочь не смог." (show_side="right", show_kind="speech")
    hide virt

    n "Он сделал паузу, решая, говорить ли дальше." (show_side="none", show_kind="speech")

    show virt serious at virt_right
    vi "Он исчез вскоре после первых экспериментов. После... провала." (show_side="right", show_kind="speech")
    vi "С тех пор о нём никто не слышал." (show_side="right", show_kind="speech")
    hide virt

    n "Эвейна молчала, пытаясь переварить сказанное." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev_thought "Итак, Аурелиан ничего не знает." (show_side="left", show_kind="thought")
    ev_thought "Он не похож на человека, который может так запросто врать мне в глаза. И я... ему верю." (show_side="left", show_kind="thought")
    hide eveina
    show eveina eyebrow at eveina_left
    ev_thought "Но если так, то что делать дальше? Где искать этого призрака?" (show_side="left", show_kind="thought") 
    ev_thought "И нужно ли его искать? Вирт явно не верит в его помощь... И его эксперименты называет провалом." (show_side="left", show_kind="thought")
    ev_thought "Что же делать?" (show_side="left", show_kind="thought")
    hide eveina
    show eveina thinking at eveina_left
    ev_thought "Эриан... Никогда не признаюсь себе, что подумала об этом, но..." (show_side="left", show_kind="thought")
    hide eveina
    show eveina upset at eveina_left
    ev_thought "Если бы ты только был здесь..." (show_side="left", show_kind="thought")
    ev_thought "Ты бы точно что-нибудь придумал." (show_side="left", show_kind="thought")
    hide eveina
    show eveina thinking at eveina_left
    ev_thought "В своей дурацкой манере начал бы рассказывать, какой ты прекрасный и порекомендо..." (show_side="left", show_kind="thought")
    hide eveina
    show eveina wondered at eveina_left
    ev_thought "Рекомендации!" (show_side="left", show_kind="thought")
    hide eveina

    show eveina normal at eveina_left
    ev "Кто прислал мои рекомендации при поступлении? Ты ведь читал мои документы?" (show_side="left", show_kind="speech")
    hide eveina

    n "Аурелиан поднял на неё непонимающий взгляд и нахмурился. На секунду вопрос повис в тишине." (show_side="none", show_kind="speech")

    show virt serious at virt_right
    vi "Хм... не понимаю твоего вопроса." (show_side="right", show_kind="speech")
    hide virt

    show eveina annoyed at eveina_left
    ev "Мои рекомендации при поступлении. Ты сказал, что они были убедительны. Кто их прислал?" (show_side="left", show_kind="speech")
    hide eveina

    n "Аурелиан замер с маской непонимания на лице. Потом осторожно произнёс." (show_side="none", show_kind="speech")

    show virt serious at virt_right
    vi "Эвейна, рекомендации при поступлении присылает сам кандидат." (show_side="right", show_kind="speech")
    hide virt

    show eveina annoyed at eveina_left
    ev "Но я не присылала их!" (show_side="left", show_kind="speech")
    hide eveina

    show virt serious at virt_right
    vi "Ты в этом уверена?" (show_side="right", show_kind="speech")
    hide virt

    show eveina annoyed at eveina_left
    ev "Конечно уверена, Аурелиан!" (show_side="left", show_kind="speech")
    hide eveina

    show virt serious at virt_right
    vi "Дай мне минуту, я проверю. И... успокойся, пожалуйста." (show_side="right", show_kind="speech")
    hide virt
    show virt thinking at virt_right
    vi "Не то, чтобы этот кабинет никогда не слышал криков, но будет странно, если кто-то услышит, как студентка повышает голос на декана факультета." (show_side="right", show_kind="speech")
    hide virt

    show eveina upset at eveina_left
    ev "Простите, профе...прости." (show_side="left", show_kind="speech")
    hide eveina

    n "Аурелиан взял в руки планшет и начала там быстро что-то искать. Девушка глубоко вздохнула и продолжила свою мысль." (show_side="none", show_kind="speech")

    show eveina normal at eveina_left
    ev "Я абсолютно уверена, что не присылала никаких рекомендаций." (show_side="left", show_kind="speech")
    ev "И уж точно уверена, что до поступления сюда никогда не слышала имя Кайра Далона." (show_side="left", show_kind="speech")
    hide eveina

    n "Аурелиан, не отрываясь от экрана, спросил:" (show_side="none", show_kind="speech")

    show virt serious at virt_right
    vi "А он здесь при...?" (show_side="right", show_kind="speech")
    vi "Ах, вот оно что..." (show_side="right", show_kind="speech")
    hide virt

    n "Он поднял на неё непроницаемый взгляд." (show_side="none", show_kind="speech")

    show virt serious at virt_right
    vi "Рекомендации присланы с твоей почты." (show_side="right", show_kind="speech")
    vi "И да, твоим рекомендателем указан Кайр Далон." (show_side="right", show_kind="speech")
    hide virt

    show eveina annoyed at eveina_left
    ev "Это чушь полная! Я их не присылала." (show_side="left", show_kind="speech")
    hide eveina 

    n "Аурелиан отвёл взгляд и устало потёр переносицу." (show_side="none", show_kind="speech")

    show virt thinking at virt_right
    vi "Эвейна, пожалуйста..." (show_side="right", show_kind="speech")
    hide virt


    show eveina angry at eveina_left
    ev_thought "Чёрт, возьми себя в руки, пока это не сделал он и не вытолкал тебя из этого кабинета!" (show_side="left", show_kind="thought")
    hide eveina
    show eveina upset at eveina_left
    ev "Извини..." (show_side="left", show_kind="speech")
    hide eveina

    show virt thinking at virt_right
    vi "Ты действительно их не присылала?" (show_side="right", show_kind="speech")
    hide virt

    show eveina normal at eveina_left
    ev "Абсолютно точно нет." (show_side="left", show_kind="speech")
    hide eveina

    show virt thinking at virt_right
    vi "И... не подделывала?" (show_side="right", show_kind="speech")
    hide virt

    show eveina eyebrow at eveina_left
    ev "Серьезно?" (show_side="left", show_kind="speech")
    hide eveina

    show virt thinking at virt_right
    vi "Я просто спросил, Эвейна." (show_side="right", show_kind="speech")
    hide virt

    show eveina annoyed at eveina_left
    ev "Нет, я не подделывала свои документы, Аурелиан." (show_side="left", show_kind="speech")
    hide eveina

    show virt serious at virt_right
    vi "В таком случае... это и правда выглядит странно. И с этим стоит разобраться." (show_side="right", show_kind="speech")
    hide virt

    show eveina normal at eveina_left
    ev "Ты не мог бы переслать документ мне? Хочу поискать в нём подсказки." (show_side="left", show_kind="speech")
    hide eveina

    show virt serious at virt_right
    vi "Не думаю, что там есть что-то..." (show_side="right", show_kind="speech")
    hide virt

    n "Вирт не договорил, видя, как Эвейна вновь закипает. Он сделал несколько взмахов по планшету и устало произнёс:" (show_side="none", show_kind="speech")

    show virt serious at virt_right
    vi "Документ у тебя на почте." (show_side="right", show_kind="speech")
    hide virt

    n "Эвейна тут же потянулась к браслету, но её пригвоздил к полу следующий вопрос декана." (show_side="none", show_kind="speech")

    show virt thinking at virt_right
    vi "Если ты не отсылала документ... и никогда его не видела... Как ты вообще узнала, что его автор — Кайр Далон?" (show_side="right", show_kind="speech")
    hide virt

    show eveina angry at eveina_left
    ev_thought "Вот чёрт... доверие доверием, но в мои планы не входило сдавать Эриана." (show_side="left", show_kind="thought")
    hide eveina
    show eveina thinking at eveina_left
    ev_thought "Да и Вирт вряд ли будет в восторге от рассказа о ночных прогулках под ручку с Илейн." (show_side="left", show_kind="thought")
    hide eveina

    n "Девушка лихорадочно соображала, как выйти из этой ситуации, но, как назло, в голову ничего не приходило." (show_side="none", show_kind="speech")
    n "Она открыла рот, чтобы ответить хоть что-то — и в этот момент в кабинете раздался звук системного уведомления. На экране терминала появился сухой текст." (show_side="none", show_kind="speech")

    n "📩 {i}Уведомление: Срочное совещание.{/i}\n{i}Уровень доступа: Преподавательский.{/i}\n{i}Назначено немедленно.{/i}" (show_side="none", show_kind="speech")

    show ai at ai_right
    ai "Профессор Вирт, вас срочно вызывают в Сектор 6." (show_side="right", show_kind="speech")
    hide ai 
    
    n "Аурелиан сжал губы в тонкую линию. Кивнул." (show_side="none", show_kind="speech")

    show virt serious at virt_right
    vi "Мы продолжим этот разговор позже. Обязательно." (show_side="right", show_kind="speech")
    hide virt

    scene bg corridor at bg_fullscreen with dissolve

    n "Пропустив её вперед, Вирт вышел из кабинета и снова надел маску декана. Учтиво кивнул и уже почти сделал шаг прочь, но всё же обернулся и, не повышая голоса, добавил:" (show_side="none", show_kind="speech")

    show virt normal at virt_right
    vi "Будьте благоразумны, мисс Хейла. Воздержитесь от сомнительных инициатив, пока мы не завершили этот разговор." (show_side="right", show_kind="speech")
    hide virt

    show eveina eyebrow at eveina_left
    ev_thought "Сомнительные инициативы, да?" (show_side="left", show_kind="thought")
    hide eveina
    show eveina thinking at eveina_left
    ev_thought "Очевидно, он уже понял, с кем имеет дело." (show_side="left", show_kind="thought")
    ev_thought "Приятно, конечно, что всё ещё надеется на благоразумие — даже если это уже почти статистическая аномалия." (show_side="left", show_kind="thought")
    hide eveina

    n "Девушка закатила глаза, но кивнула в ответ, а затем поспешила в свою комнату." (show_side="none", show_kind="speech")

    jump scene_8_6
