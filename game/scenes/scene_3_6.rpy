label scene_3_6:
    $ previous_scene = "scene_3_5"
    $ next_scene = "scene_3_7"
    $ current_scene = "scene_3_6"

    # =========================================================
    # СЦЕНА 3_6 — «ПРАКТИКА ЭЗАРИ / ФЛЕШКА»
    # Структура: флэшбэк с признанием Каэля (полный диалог из 3_6)
    #            → из-за рассеянности ошибка → дыра в потолке
    #            → Эзари задерживает → Каэль появляется
    #            → флешка К.Д./NR-Δ → Каэль замечает, молчит
    # Флэшбэк — почти дословно из оригинальной scene_3_6.
    # Остальное — из оригинальной scene_3_9.
    # =========================================================

    call fade_to_black(1.2, 0.8)
    scene bg lab_botany at bg_fullscreen with dissolve
    # play music "bgm/lab_peaceful.ogg" fadein 2.0

    n "Профессор Эзари — пожилой мужчина с благоговейным тоном и походкой задумчивого гриба — медленно расхаживал вдоль живых проекционных конструкций, рассказывая о том, как местные растения адаптируются под нейрокоманды и формируют архитектуру." (show_side="none", show_kind="speech")

    show ezari normal at ezari_right
    ez "..." (show_side="right", show_kind="speech")
    hide ezari

    n "Эвейна сидела у терминала и почти не слушала." (show_side="none", show_kind="speech")
    n "Прямо перед практикой — в коридоре, у двери в лабораторию — её ждал Каэль." (show_side="none", show_kind="speech")

    # --- Флэшбэк ---

    call fade_to_black(0.8, 0.5)
    scene bg corridor_3 at bg_fullscreen with dissolve

    n "Он стоял, прислонившись к стене и скрестив руки. Холодные глаза смотрели прямо на неё." (show_side="none", show_kind="speech")
    n "И всё же… в его лице что-то изменилось. Никакого высокомерия. Только внимание. Только анализ." (show_side="none", show_kind="speech")

    show kael normal at kael_right
    ka "Ты действительно решила её." (show_side="right", show_kind="speech")
    hide kael
    show kael thinking at kael_right
    ka "Я проверил данные. Провёл сравнительный анализ с историческими моделями." (show_side="right", show_kind="speech")
    hide kael
    show kael serious at kael_right
    ka "За последние триста лет разработано одиннадцать подходов к задаче Идентики." (show_side="right", show_kind="speech")
    ka "Ни один не достиг стабильного восстановления выше двенадцати процентов. Твой дал двадцать девять. С первой попытки." (show_side="right", show_kind="speech")
    hide kael

    n "Его голос звучал ровно, почти отстранённо. Словно он зачитывал доклад." (show_side="none", show_kind="speech")
    n "Но глаза внимательно изучали её — будто пытались разглядеть что-то, чего в ней никогда не видели." (show_side="none", show_kind="speech")

    show kael eyebrow at kael_right
    ka "Как ты это сделала?" (show_side="right", show_kind="speech")
    hide kael

    show eveina thinking at eveina_left
    ev "Я подумала, что блоки памяти — это просто данные. От воспоминаний их отличают эмоции, которые они вызывали." (show_side="left", show_kind="speech")
    hide eveina
    show eveina normal at eveina_left
    ev "И я просмотрела все воспоминания, чтобы подобрать к ним соответствующие эмоции." (show_side="left", show_kind="speech")
    hide eveina
    show eveina upset thinking at eveina_left
    ev "Но это не сработало." (show_side="left", show_kind="speech")
    hide eveina
    show eveina thinking at eveina_left
    ev "Поэтому я ввела мозг в состояние быстрого сна с помощью тета-ритмов и прокрутила эти воспо..." (show_side="left", show_kind="speech")
    hide eveina

    show kael eyebrow at kael_right
    ka "Ты... что сделала?" (show_side="right", show_kind="speech")
    hide kael

    show eveina thinking at eveina_left
    ev "Подобрала к ним соответствующие эмоции." (show_side="left", show_kind="speech")
    hide eveina

    show kael normal at kael_right
    ka "Я не об этом. Ты отсмотрела все блоки памяти? Зачем?" (show_side="right", show_kind="speech")
    hide kael

    show eveina eyebrow at eveina_left
    ev "А как я ещё пойму, какие эмоциональные импульсы к ним подобрать?" (show_side="left", show_kind="speech")
    hide eveina

    show kael eyebrow at kael_right
    ka "И как ты поняла, какие будут правильными?" (show_side="right", show_kind="speech")
    hide kael

    show eveina normal at eveina_left
    ev "Ну... я представила, что чувствовала бы, будь это моими воспоминаниями." (show_side="left", show_kind="speech")
    hide eveina

    show kael eyebrow at kael_right
    ka "А усыплять его зачем?" (show_side="right", show_kind="speech")
    hide kael

    show eveina normal at eveina_left
    ev "В бодрствующем состоянии мозг просто поглотил импульс. И я подумала, что в состоянии быстрого сна он сможет создать новые связи..." (show_side="left", show_kind="speech")
    hide eveina

    n "Напряжённое молчание повисло между ними. Сомнение на лице Каэля сменилось сначала недоверием, а потом осознанием." (show_side="none", show_kind="speech")

    show kael eyebrow at kael_right
    ka "Этот тест не предназначался для решения. Он был проверкой. На адаптацию. На сопротивление." (show_side="right", show_kind="speech")
    ka "На способность мыслить вне схем." (show_side="right", show_kind="speech")
    hide kael
    show kael serious at kael_right
    ka "Я не ожидал результата." (show_side="right", show_kind="speech")
    hide kael

    show eveina eyebrow at eveina_left
    ev "То есть... ты удивлён?" (show_side="left", show_kind="speech")
    hide eveina

    n "Каэль сделал долгую паузу." (show_side="none", show_kind="speech")

    show kael thinking at kael_right
    ka "Скажем так: ты не соответствуешь своей модели поведения. И это вызывает необходимость пересмотра параметров." (show_side="right", show_kind="speech")
    hide kael

    show eveina eyebrow at eveina_left
    ev "Это комплимент такой? Или ты снова собираешься выставить меня за дверь?" (show_side="left", show_kind="speech")
    hide eveina

    show kael serious at kael_right
    ka "Пока что — наблюдаю. Ты нестабильна. Но обучаема." (show_side="right", show_kind="speech")
    hide kael

    n "В голосе Каэля — абсолютная убеждённость. Ни намёка на издёвку, лишь холодная диагностика." (show_side="none", show_kind="speech")
    n "И этого хватило, чтобы Эвейна вспыхнула." (show_side="none", show_kind="speech")

    show eveina angry at eveina_left
    ev "Ты всегда раздаёшь ярлыки вместо похвалы?" (show_side="left", show_kind="speech")
    ev "Или только тем, кто выбивается из твоих прогнозов?" (show_side="left", show_kind="speech")
    hide eveina

    n "Каэль не отвечал. Просто смотрел на неё — секунду, две, три." (show_side="none", show_kind="speech")
    n "Оба не отводили взгляда. Между ними висела такая тишина, что казалось: если заговорить, что-то хрупкое лопнет." (show_side="none", show_kind="speech")
    n "Потом он повернулся к двери — и голос его прозвучал уже со спины:" (show_side="none", show_kind="speech")

    show kael thinking at kael_right
    ka "Прогнозам ты действительно не поддаёшься." (show_side="right", show_kind="speech")
    hide kael

    n "Он скрылся в лаборатории, не оборачиваясь." (show_side="none", show_kind="speech")

    # --- Конец флэшбэка ---

    call fade_to_black(0.8, 0.5)
    scene bg lab_botany at bg_fullscreen with dissolve

    show eveina normal at eveina_left
    ev_thought "Практику с утра пораньше придумали для очистки кармы студентов, не иначе..." (show_side="left", show_kind="thought")
    hide eveina

    n "Лея, заручившись поддержкой своего наставника, сбежала после первой же симуляции, оставив её одну на боевом посту." (show_side="none", show_kind="speech")
    n "Остальные студенты вяло вводили команды, искажающие стены и потолки тестового полигона лаборатории." (show_side="none", show_kind="speech")
    n "Эвейна попробовала задать собственную последовательность." (show_side="none", show_kind="speech")
    n "Через секунду в потолке лаборатории образовалась дыра, из которой начала литься вязкая, мерцающая жидкость." (show_side="none", show_kind="speech")
    n "Сзади послышался усталый вздох." (show_side="none", show_kind="speech")

    show ezari normal at ezari_right
    ez "Мисс Хейла, мы тут не портал в иное измерение открываем." (show_side="right", show_kind="speech")
    hide ezari
    show ezari smile at ezari_right
    ez "Хотя… это интересная интерпретация задачи." (show_side="right", show_kind="speech")
    hide ezari

    show eveina sad at eveina_left
    ev "Извините, профессор." (show_side="left", show_kind="speech")
    hide eveina

    show ezari normal at ezari_right
    ez "После окончания практики задержитесь, пожалуйста, чтобы убрать за собой." (show_side="right", show_kind="speech")
    hide ezari

    show eveina eyeroll at eveina_left
    ev_thought "Отлично. Ещё один триумф инженерной мысли." (show_side="left", show_kind="thought")
    hide eveina
    show eveina normal at eveina_left
    ev_thought "Если бы в Академии вручали премии за нестандартный провал, я бы уже стояла в Зале славы с венком из лиан на голове." (show_side="left", show_kind="thought")
    hide eveina

    n "Эта мысль почему-то вызвала в ней улыбку." (show_side="none", show_kind="speech")
    n "Когда остальные студенты разошлись, профессор вручил Эвейне пульт управления роботом-полотёром — и попросил восстановить порядок." (show_side="none", show_kind="speech")
    n "Пока она счищала следы своего «катастрофического полёта мысли», он копался в старых носителях и бормотал себе под нос." (show_side="none", show_kind="speech")

    show ezari normal at ezari_right
    ez "Моя база данных всё ещё не интегрирована с основным архивом." (show_side="right", show_kind="speech")
    ez "Эти носители — память эпохи, мисс Хейла. Поможете с оцифровкой?" (show_side="right", show_kind="speech")
    ez "Каэль вот... где-то здесь... должен был подключить консоль." (show_side="right", show_kind="speech")
    hide ezari

    n "В этот момент действительно появился Каэль — внезапно, будто материализовался из воздуха." (show_side="none", show_kind="speech")

    show kael normal at kael_right
    ka "..." (show_side="right", show_kind="speech")
    hide kael

    n "Он коротко кивнул, подключил носитель, ввёл пару команд и исчез обратно вглубь лаборатории, погружённый в собственную работу." (show_side="none", show_kind="speech")
    n "Эвейна закинула на рабочий стол внушительных размеров коробку и достала одну из архивных шкатулок — вытянутую флешку с переливающимся кончиком." (show_side="none", show_kind="speech")
    n "Каждый носитель надо было ввести вручную, просканировать и дать ему категорию: ботаника, архитектура, питательные свойства, токсичность." (show_side="none", show_kind="speech")
    n "Минут через двадцать одно из названий на экране заставило её сердце стукнуть сильнее:" (show_side="none", show_kind="speech")
    n "{i}«К.Д. — NR-Δ Секв. Нейрон-3 / Модиф. нейроинтеграция / Исследование окончено.»{/i}" (show_side="none", show_kind="speech")

    show eveina wondered at eveina_left
    ev_thought "К.Д. — Кайр Далон? Или просто совпадение?" (show_side="left", show_kind="thought")
    ev_thought "А вот это «NR-Δ Секв. Нейрон-3» — это то, что я думаю?" (show_side="left", show_kind="thought")
    hide eveina

    n "Она незаметно вставила носитель в свой браслет-интерфейс, быстро копируя данные на внутренний модуль памяти." (show_side="none", show_kind="speech")
    n "Делала это вслепую — пальцы двигались, как будто сами." (show_side="none", show_kind="speech")
    n "И в этот момент она почувствовала на себе чей-то взгляд. Каэль, стоящий в паре метров, повернул голову." (show_side="none", show_kind="speech")

    show kael thinking at kael_right
    ka "..." (show_side="right", show_kind="speech")
    hide kael

    n "Его взгляд скользнул по ней, по рукам, по браслету. Он ничего не говорил, просто смотрел секунду… две… и отвернулся." (show_side="none", show_kind="speech")
    n "Возвратился к терминалу, как будто ничего не видел." (show_side="none", show_kind="speech")

    show eveina eyebrow at eveina_left
    ev_thought "Он ведь заметил? Но промолчал? О, молчаливый Каэль — худшая версия Каэля." (show_side="left", show_kind="thought")
    hide eveina
    show eveina normal at eveina_left
    ev_thought "Возможно, он ничего не заметил." (show_side="left", show_kind="thought")
    hide eveina
    show eveina thinking at eveina_left
    ev_thought "Но, вероятнее всего, уже планирует, куда отправить меня, когда всё вскроется." (show_side="left", show_kind="thought")
    hide eveina

    n "Профессор Эзари тем временем ворчал себе под нос что-то о несовершенстве интерфейсов и подсовывал Эвейне новую порцию флешек." (show_side="none", show_kind="speech")
    n "Она кивала, но всё внимание уже было в другом месте. Внутри неё всё сгорало от нетерпения. Она держала в руках крупицу информации." (show_side="none", show_kind="speech")
    n "Ответ? Подсказку? Или очередной тупик?" (show_side="none", show_kind="speech")

    jump scene_3_7
