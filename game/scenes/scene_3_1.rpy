label scene_3_1:
    $ previous_scene = "scene_2_9"
    $ next_scene = "scene_3_2"
    $ current_scene = "scene_3_1"

    # =========================================================
    # СЦЕНА 3_1 — «ПРАКТИКА / ЗАДАЧА ИДЕНТИКИ»
    # Структура: вход с намерением → игнорирует новое задание
    #            → перебирает методы → флэшбэк с отцом (х2)
    #            → воспоминания субъекта → тета-ритм → результат
    #            → Каэль молчит → «Выйди из лаборатории» → коридор
    # Близко к оригинальной scene_3_5 по монологу и реакции Каэля.
    # Отличие: Эвейна уже думала об этой задаче — приходит с намерением.
    # =========================================================

    call fade_to_black(1.2, 0.8)
    scene bg lab at bg_fullscreen with dissolve
    # play music "bgm/lab_pressure.ogg" fadein 2.0

    n "Она знала, что придёт сюда с намерением." (show_side="none", show_kind="speech")
    n "Не с тревогой первокурсницы — с намерением. Последние ночи дали ей несколько версий подхода. Теперь надо было проверить хотя бы одну." (show_side="none", show_kind="speech")
    n "Каэль стоял у консоли. По обыкновению, не поднял головы при её появлении." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev_thought "Что ж, посмотрим, кто кого." (show_side="left", show_kind="thought")
    hide eveina

    n "Студентов стало заметно меньше с прошлой практики. Эвейна окинула лабораторию взглядом и усмехнулась про себя." (show_side="none", show_kind="speech")

    show eveina eyeroll at eveina_left
    ev_thought "А Каэль, похоже, не соврал про каждого четвёртого." (show_side="left", show_kind="thought")
    hide eveina

    n "Каэль повернулся к оставшимся и без лишних предисловий сказал:" (show_side="none", show_kind="speech")

    show kael normal at kael_right
    ka "Ваша задача на экране терминала. Приступайте." (show_side="right", show_kind="speech")
    hide kael

    n "Эвейна посмотрела на экран." (show_side="none", show_kind="speech")

    n "{i}«Восстановите ассоциативную идентичность субъекта с утратой первичных автобиографических связей.{/i}" (show_side="none", show_kind="speech")
    n "{i}Перед вами симулированное сознание с частично разрушенными связями между памятью и личностной матрицей.{/i}" (show_side="none", show_kind="speech")
    n "{i}Оно «помнит», но не «осознаёт себя».{/i}" (show_side="none", show_kind="speech")
    n "{i}Ваша задача — активировать восстановление самоидентификации, не используя прямую загрузку исходных данных.»{/i}" (show_side="none", show_kind="speech")

    n "Та самая. Слово в слово." (show_side="none", show_kind="speech")

    show eveina eyebrow at eveina_left
    ev_thought "Ну что ж. Значит, сегодня." (show_side="left", show_kind="thought")
    hide eveina

    n "Рядом кто-то вздохнул с таким видом, будто только что приговорили к расстрелу." (show_side="none", show_kind="speech")

    show student annoyed at student_right
    st "Он реально сумасшедший. Это же невозможно." (show_side="right", show_kind="speech")
    hide student

    n "Каэль не отреагировал. Он уже ходил между терминалами — медленно, без спешки. Взгляд скользил по напряжённым спинам, по нервно дёргающимся плечам." (show_side="none", show_kind="speech")

    show kael serious at kael_right
    ka "Некоторые даже не пытаются. Страх — хорошее оправдание, если ты посредственность." (show_side="right", show_kind="speech")
    hide kael

    n "Эвейна уже тянулась к сенсорам." (show_side="none", show_kind="speech")
    n "Метод первый: попробовать напрямую восстановить связи через ассоциативные цепочки. Логично, структурно — и абсолютно предсказуемо." (show_side="none", show_kind="speech")
    n "Система не ответила." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev_thought "Ладно. Дальше." (show_side="left", show_kind="thought")
    hide eveina

    n "Метод второй: отключить конфликтующие блоки памяти, попробовать создать нейтральную основу для восстановления." (show_side="none", show_kind="speech")
    n "Система пискнула — и зависла." (show_side="none", show_kind="speech")

    show eveina annoyed at eveina_left
    ev_thought "Тоже нет." (show_side="left", show_kind="thought")
    hide eveina

    n "Метод третий — тот, что она придумала в три часа ночи и немедленно отвергла как слишком странный — она пока откладывала." (show_side="none", show_kind="speech")
    n "Рядом кто-то встал, собрал вещи и вышел молча. Потом ещё один." (show_side="none", show_kind="speech")
    n "Каэль шёл по рядам. Каждый раз, когда его шаги становились ближе, в груди что-то сжималось." (show_side="none", show_kind="speech")

    show kael normal at kael_right
    ka "Шаблон." (show_side="right", show_kind="speech")
    hide kael
    show kael serious at kael_right
    ka "Поверхностно." (show_side="right", show_kind="speech")
    hide kael
    show kael eyebrow at kael_right
    ka "Это даже не смешно." (show_side="right", show_kind="speech")
    hide kael

    n "Перед глазами — задача, но её скрытый смысл оставался закрытым. Буквы давили на глаза, въедаясь в сетчатку." (show_side="none", show_kind="speech")

    show eveina normal at eveina_left
    ev_thought "Ладно, логика не работает. Есть некий блок памяти. В нём — воспоминания." (show_side="left", show_kind="thought")
    hide eveina
    show eveina eyebrow at eveina_left
    ev_thought "Я могу отсмотреть каждое из них... но что мне это даст?" (show_side="left", show_kind="thought")
    hide eveina
    show eveina thinking at eveina_left
    ev_thought "Разве можно воткнуть в сознание флешку с данными и сказать ему: «Знакомься, дорогой, это твои воспоминания»?" (show_side="left", show_kind="thought")
    hide eveina
    show eveina eyebrow at eveina_left
    ev_thought "Разве станут данные от этого — воспоминаниями? Это так не работает." (show_side="left", show_kind="thought")
    hide eveina
    show eveina thinking at eveina_left
    ev_thought "И Каэль это тоже прекрасно понимает. Так чего он от нас хочет?" (show_side="left", show_kind="thought")
    hide eveina

    n "И вдруг — короткая вспышка памяти. Голос отца, как нить из далёкого прошлого." (show_side="none", show_kind="speech")

    call fade_to_black(0.8, 0.5)
    scene bg home_bedroom at bg_fullscreen with dissolve

    show rian normal at rian_right
    ri "Если кажется, что всё упирается в тупик — ты, возможно, смотришь слишком близко." (show_side="right", show_kind="speech")
    ri "Попробуй посмотреть на проблему с другой перспективы. Там всегда есть что-то, что ты упускаешь." (show_side="right", show_kind="speech")
    hide rian

    scene bg lab at bg_fullscreen with dissolve

    show eveina eyebrow at eveina_left
    ev_thought "О чём были эти слова? Что ты хотел этим сказать?" (show_side="left", show_kind="thought")
    hide eveina

    n "Она не вспомнила. Отмахнулась от непрошенных мыслей и попробовала снова." (show_side="none", show_kind="speech")
    n "За спиной послышались надменные шаги — они остановились прямо за ней." (show_side="none", show_kind="speech")

    show kael intrigued at kael_right
    ka "Смелая девушка с задачей и без идеи. Интересное сочетание." (show_side="right", show_kind="speech")
    hide kael

    n "Эвейна мысленно выругалась. Стиснула кулаки под столом. Закрыла глаза, сделала медленный вдох — и такой же медленный выдох." (show_side="none", show_kind="speech")
    n "И вспомнила." (show_side="none", show_kind="speech")

    call fade_to_black(0.8, 0.5)
    scene bg home_bedroom at bg_fullscreen with dissolve

    n "Голос отца. Просто разговор в её спальне." (show_side="none", show_kind="speech")

    show rian normal at rian_right
    ri "Если кажется, что всё упирается в тупик — ты, возможно, смотришь слишком близко." (show_side="right", show_kind="speech")
    ri "Попробуй посмотреть на проблему с другой перспективы. Там всегда есть что-то, что ты упускаешь." (show_side="right", show_kind="speech")
    hide rian

    n "Малышка со слезами на глазах передала ему головоломку." (show_side="none", show_kind="speech")

    show eveina little crying at eveina_little_right
    ev "У меня всё равно не получается её разгадать!" (show_side="left", show_kind="speech")
    hide eveina

    show rian normal at rian_right
    ri "Не всё объясняется логикой, Вейна." (show_side="right", show_kind="speech")
    ri "Некоторые решения нужно просто прочувствовать." (show_side="right", show_kind="speech")
    hide rian

    n "Он развернул головоломку под определённым углом, аккуратно надавил пальцем в почти невидимую глазу выемку — и детали сложились в идеальную форму." (show_side="none", show_kind="speech")

    scene bg lab at bg_fullscreen with dissolve

    n "Глаза Эвейны распахнулись." (show_side="none", show_kind="speech")
    n "Пальцы, будто найдя свою музыку, задвигались по интерфейсу — сначала медленно, потом быстрее." (show_side="none", show_kind="speech")
    n "Не умом — чутьём. Она перестроила интерфейс, отключила зону логики, включила зону аффекта. Сбоку вывела утерянные блоки исходных данных." (show_side="none", show_kind="speech")

    show eveina normal at eveina_left
    ev_thought "Так. Детское воспоминание: дождь, запах мокрой земли, плач на фоне... могила." (show_side="left", show_kind="thought")
    hide eveina
    show eveina thinking at eveina_left
    ev_thought "Чьи-то похороны." (show_side="left", show_kind="thought")
    hide eveina
    show eveina normal at eveina_left
    ev_thought "Второе тоже из детства. Запах сирени, тиканье часов, женские руки..." (show_side="left", show_kind="thought")
    hide eveina
    show eveina eyebrow at eveina_left
    ev_thought "Гладит по голове? Или делает причёску? Это мать?" (show_side="left", show_kind="thought")
    hide eveina
    show eveina normal at eveina_left
    ev_thought "Третье из более поздних. Парта. Пальцы отбивают ритм по выключенному экрану в столешнице." (show_side="left", show_kind="thought")
    hide eveina
    show eveina eyebrow at eveina_left
    ev_thought "Урок? Нет, что-то более волнительное. Какая-то проверка?" (show_side="left", show_kind="thought")
    hide eveina

    n "Каэль остановился за её спиной." (show_side="none", show_kind="speech")
    n "Молча. Его присутствие казалось теперь не угрозой — а частью задачи." (show_side="none", show_kind="speech")

    show kael eyebrow at kael_right
    ka "..." (show_side="right", show_kind="speech")
    hide kael

    n "Стараясь не отвлекаться на его взгляд, Эвейна прикрыла глаза на секунду и прислушалась к себе." (show_side="none", show_kind="speech")
    n "Она создала эмоционально-когнитивный импульс: скорбь от потери близкого, нежность от прикосновения матери, страх перед важным экзаменом. Передала их в модель." (show_side="none", show_kind="speech")
    n "Система обрабатывала. Замерла." (show_side="none", show_kind="speech")

    show eveina eyebrow at eveina_left
    ev_thought "Хм. Почему нет реакции?" (show_side="left", show_kind="thought")
    hide eveina
    show eveina upset thinking at eveina_left
    ev_thought "Слишком слабый импульс?" (show_side="left", show_kind="thought")
    hide eveina
    show eveina thinking at eveina_left
    ev_thought "Нет. Нужно что-то ещё — что спровоцировало бы консолидацию памяти..." (show_side="left", show_kind="thought")
    hide eveina
    show eveina eyebrow at eveina_left
    ev_thought "Мозговые ритмы. Что там отвечает за память — тета и гамма?" (show_side="left", show_kind="thought")
    hide eveina
    show eveina thinking at eveina_left
    ev_thought "Прости, парень, я не сильна в цифрах, поэтому выкручу на полную." (show_side="left", show_kind="thought")
    hide eveina
    show eveina normal at eveina_left
    ev_thought "Надеюсь, ты выдержишь." (show_side="left", show_kind="thought")
    hide eveina

    n "Несколько молниеносных движений — и система возмущённо пискнула на пороговые значения." (show_side="none", show_kind="speech")
    n "А затем отреагировала. Показатели начали расти." (show_side="none", show_kind="speech")

    n "Эвейна моргнула. Почти не верила, что это сработало." (show_side="none", show_kind="speech")
    n "Обернулась на Каэля — в ожидании его реакции." (show_side="none", show_kind="speech")
    n "Он не смотрел на неё. Он смотрел на экран." (show_side="none", show_kind="speech")

    show kael serious at kael_right
    ka "..." (show_side="right", show_kind="speech")
    hide kael

    n "Лицо не выражало ни одной эмоции. Долгое, тягучее молчание — почти целую минуту." (show_side="none", show_kind="speech")
    n "А потом:" (show_side="none", show_kind="speech")

    show kael serious at kael_right
    ka "Выйди из лаборатории." (show_side="right", show_kind="speech")
    hide kael

    n "Только и всего." (show_side="none", show_kind="speech")
    n "Эвейна сперва подумала, что ослышалась. Ни объяснений, ни намёка на одобрение." (show_side="none", show_kind="speech")
    n "Она медленно поднялась. Спина холодела. Дрожь прокатилась от поясницы к затылку." (show_side="none", show_kind="speech")
    n "Взгляды студентов прилипли к ней — но никто не сказал ни слова." (show_side="none", show_kind="speech")
    n "Каэль по-прежнему смотрел на экран." (show_side="none", show_kind="speech")
    n "И тогда она вышла — в полной тишине." (show_side="none", show_kind="speech")

    scene bg corridor at bg_fullscreen with dissolve

    show eveina eyebrow at eveina_left
    ev_thought "Что это было?" (show_side="left", show_kind="thought")
    hide eveina
    show eveina thinking at eveina_left
    ev_thought "Что я сделала не так?" (show_side="left", show_kind="thought")
    hide eveina
    show eveina annoyed at eveina_left
    ev_thought "Он же сам сказал — у меня есть потенциал. «Потенциал»." (show_side="left", show_kind="thought")
    hide eveina
    show eveina angry at eveina_left
    ev_thought "А теперь — просто выпроваживает?" (show_side="left", show_kind="thought")
    hide eveina

    n "Коридор был пуст. Эвейна шла, не зная куда — просто чтобы идти." (show_side="none", show_kind="speech")
    n "Ей нужен был воздух." (show_side="none", show_kind="speech")

    jump scene_3_2
