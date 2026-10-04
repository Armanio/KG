label scene_6_8:
    $ previous_scene = "scene_6_7"
    $ next_scene = "scene_6_9"
    $ current_scene = "scene_6_8"
    call fade_to_black(1.2, 0.8)
    scene bg lab at bg_fullscreen with dissolve

    n "После лекций девушка направилась в лабораторию нейроанализа. Она не предупредила о своём приходе заранее и немного нервничала из-за этого." (show_side="none", show_kind="speech")
    n "Каэль сидел у одного из терминалов. Поднял взгляд, прищурился — как будто хотел что-то сказать. Но промолчал." (show_side="none", show_kind="speech")
    n "Только кивнул на кресло и сел на соседний терминал." (show_side="none", show_kind="speech")

    show eveina normal at eveina_left
    ev_thought "Вот это встречают. Ни «что тебе надо», ни «тебе тут не место», ни даже насмешки. Прогресс?" (show_side="left", show_kind="thought")
    hide eveina

    n "Они работали молча. Он наблюдал, как она вводит параметры, иногда кивая. Изредка тихо подсказывал." (show_side="none", show_kind="speech")

    show kael normal at kael_right
    ka "Подними порог здесь." (show_side="right", show_kind="speech")
    ka "Отрегулируй временную задержку." (show_side="right", show_kind="speech")
    ka "Попробуй более мягкую связку ритмов." (show_side="right", show_kind="speech")
    hide kael

    n "Браслет Эвейны — единственное, что нарушало тихий гул терминалов в лаборатории. Он без остановки вибрировал." (show_side="none", show_kind="speech")
    n "Сначала она игнорировала. Потом раздражённо выключила его." (show_side="none", show_kind="speech")
    n "Каэль, заметив это, тихо хмыкнул, но удержался от комментариев. После чего снова погрузился в наблюдение, и всё будто бы вернулось в рабочее русло." (show_side="none", show_kind="speech")
    n "До тех пор, пока в помещении не появился профессор Вирт." (show_side="none", show_kind="speech")
    n "Дверь открылась почти бесшумно. Аурелиан шагнул внутрь уверенно, с той мягкой настойчивостью, которую ни с чем не спутаешь." (show_side="none", show_kind="speech")
    n "Каэль, услышав шаги, не торопясь, встал со своего излюбленного места." (show_side="none", show_kind="speech")
    n "Как будто раздумывал, стоит ли вторжение кого бы то ни было того, чтобы менять позу. Но всё же сделал шаг в сторону от Эвейны. И замер." (show_side="none", show_kind="speech")

    show kael serious at kael_right
    ka "Аурелиан." (show_side="right", show_kind="speech")
    hide kael

    n "Вирт скользнул взглядом по ним обоим. Его глаза задержались на той самой точке, где только что Каэль сидел слишком близко к Эвейне." (show_side="none", show_kind="speech")
    n "Но он ничего не сказал. Вместо этого — повернулся к девушке." (show_side="none", show_kind="speech")

    show virt angry at virt_right
    vi "Мисс Хейла, почему вы не отвечаете на сообщения?" (show_side="right", show_kind="speech")
    hide virt

    n "Вопрос прозвучал резче, чем обычно. Профессор был если не зол, то точно раздражён. Эвейна вздрогнула от неожиданности." (show_side="none", show_kind="speech")

    show eveina normal at eveina_left
    ev "Я… Простите. Я отключила браслет. Думала, что ничего срочного." (show_side="left", show_kind="speech")
    hide eveina

    n "Аурелиан потёр переносицу пальцами. Медленно провёл ладонью по волосам, откидывая упавшую прядь." (show_side="none", show_kind="speech")

    show virt angry at virt_right
    vi "Что произошло между вами с Кайстром?" (show_side="right", show_kind="speech")
    hide virt

    n "Имя прозвучало как выстрел. Каэль нахмурился и инстинктивно сделал шаг ближе к Эвейне." (show_side="none", show_kind="speech")
    n "Вирт метнул на него холодный взгляд. Оба замерли, глядя друг на друга. Мгновение — и тишина стала гуще воздуха." (show_side="none", show_kind="speech")
    n "Эвейна недоуменно переводила глаза с одного на другого, гадая, что стало причиной этого напряжения." (show_side="none", show_kind="speech")
    n "Наконец, Аурелиан медленно отвернулся от Каэля и посмотрел на неё." (show_side="none", show_kind="speech")

    show virt normal at virt_right
    vi "Он подал запрос на дисциплинарное слушание. В отношении вас." (show_side="right", show_kind="speech")
    hide virt

    n "Эвейна открыла рот — и сразу захлопнула. Две пары выжидающих глаз были устремлены к ней." (show_side="none", show_kind="speech")

    show eveina normal at eveina_left
    ev "Я… На лекции. Он… сказал... что женщинам в науке не место." (show_side="left", show_kind="speech")
    ev "Я просто ответила. Я не думала, что… это повод." (show_side="left", show_kind="speech")
    hide eveina

    n "Вирт нахмурился больше прежнего. Скользнул тяжёлым взглядом по ней, затем перевёл его на Каэля. Каэль ответил ему тем же." (show_side="none", show_kind="speech")
    n "Между ними будто происходил немой диалог, в котором Эвейну не позвали участвовать." (show_side="none", show_kind="speech")
    n "Девушка поёжилась, заметив побелевшие костяшки пальцев на руке Каэля, что опиралась о край терминала." (show_side="none", show_kind="speech")

    show eveina eyebrow at eveina_left
    ev_thought "Ой... Что бы тут ни происходило — я точно в эпицентре." (show_side="left", show_kind="thought")
    hide eveina

    show virt serious at virt_right
    vi "Мисс Хейла, впредь прошу вас воздерживаться от вмешательств в лекции подобного рода." (show_side="right", show_kind="speech")
    vi "Особенно, если это касается профессора Кайстра." (show_side="right", show_kind="speech")
    vi "Он не тот человек, с которым нужно вести открытые споры…" (show_side="right", show_kind="speech")
    vi "…и уж тем более не та цель, которую стоит выбирать себе в противники." (show_side="right", show_kind="speech")
    hide virt

    show eveina normal at eveina_left
    ev "Поняла." (show_side="left", show_kind="speech")
    hide eveina

    n "Аурелиан снова нервно провёл рукой по волосам. Сделал глубокий вдох, как будто собирался продолжить, но замер — на миг, слишком долгий для простого молчания." (show_side="none", show_kind="speech")
    n "Он смотрел на Эвейну, как будто хотел что-то сказать. Предупредить. Объяснить. Убедить." (show_side="none", show_kind="speech")
    n "Но не позволил себе. И, отведя взгляд, сухо произнёс:" (show_side="none", show_kind="speech")

    show virt thinking at virt_right
    vi "Я разберусь. А вам, мисс Хейла… удачи с задачей Идентики." (show_side="right", show_kind="speech")
    hide virt

    n "Он повернулся к двери, но перед уходом снова задумчиво посмотрел на Каэля. Каэль не остался в долгу." (show_side="none", show_kind="speech")
    n "Слегка приподнял бровь, с тем самым привычным, почти высокомерным видом, который ничего не выражал, но говорил слишком много." (show_side="none", show_kind="speech")
    n "Дверь за профессором закрылась." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev_thought "Окей… это был Вирт в режиме «ты почти вывела меня из себя»." (show_side="left", show_kind="thought")
    ev_thought "Отлично. Просто идеально." (show_side="left", show_kind="thought")
    ev_thought "Надеюсь, следующий режим мне видеть не придётся." (show_side="left", show_kind="thought")
    hide eveina

    show eveina eyebrow at eveina_left
    ev "У меня проблемы, да?" (show_side="left", show_kind="speech")
    hide eveina

    n "Каэль оторвал взгляд от двери и медленно повернулся к ней с таким видом, будто напрочь забыл, что она здесь." (show_side="none", show_kind="speech")

    show kael thinking at kael_right
    ka "Кажется, не только у тебя..." (show_side="right", show_kind="speech")
    hide kael
    show kael serious at kael_right
    ka "В любом случае, если Вирт сказал, что разберётся — он разберётся. Он человек слова." (show_side="right", show_kind="speech")
    hide kael

    n "Она кивнула, неосознанно подметив, что в голосе Каэля прозвучало искреннее уважение." (show_side="none", show_kind="speech")

    show eveina normal at eveina_left
    ev_thought "Если даже Каэль так о нём говорит… Возможно, не стоит испытывать судьбу." (show_side="left", show_kind="thought")
    hide eveina

    n "Они вернулись к работе. В этот вечер — медленно, но сдвигаясь вперёд — они довели процент синхронизации до сорока семи." (show_side="none", show_kind="speech")
    n "Прогресс, стоящих вложенных усилий." (show_side="none", show_kind="speech")
    n "Выходя из лаборатории, она на автомате бросила:" (show_side="none", show_kind="speech")

    show eveina normal at eveina_left
    ev "Доброй ночи." (show_side="left", show_kind="speech")
    hide eveina

    n "Дверь уже закрывалась за Эвейной, когда до неё донесся ответ." (show_side="none", show_kind="speech")

    show kael normal at kael_right
    ka "Доброй ночи, Хейла." (show_side="right", show_kind="speech")
    hide kael

    show eveina eyebrow at eveina_left
    ev_thought "Ого… попрощался. Каэль попрощался." (show_side="left", show_kind="thought")
    ev_thought "Вот это — действительно достижение." (show_side="left", show_kind="thought")
    hide eveina
    show eveina thinking at eveina_left
    ev_thought "Может, в следующий раз ещё и «привет» скажет. И тогда точно пора бить тревогу." (show_side="left", show_kind="thought")
    hide eveina

    jump scene_6_9

