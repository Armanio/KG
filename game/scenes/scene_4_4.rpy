label scene_4_4:
    $ previous_scene = "scene_4_3"
    $ next_scene = "scene_4_5"
    $ current_scene = "scene_4_4"

    # =========================================================
    # СЦЕНА 4_4 — «ПРАКТИКА / ОТРАБОТКА / ПОЦЕЛУЙ»
    # Структура: временная прокладка → ожидание в лаборатории
    #            → флэшбэк с практики (включая первый сбой имплантов)
    #            → приход Каэля, он напряжён
    #            → отработка → диалог → вспышка → поцелуй
    # =========================================================

    call fade_to_black(1.2, 0.8)
    scene bg lab at bg_fullscreen with dissolve

    # --- Временная прокладка ---

    n "Со вчерашнего утра прошли почти сутки." (show_side="none", show_kind="speech")
    n "Слова ИИ крутились в голове сами собой: «запретные секции архива», «данные изолированы», «доступны только внутри помещения»." (show_side="none", show_kind="speech")
    n "Эвейна твёрдо решила, что разберётся с этим сегодня — нужно было только пережить практику у Каэля." (show_side="none", show_kind="speech")

    # --- Ожидание в лаборатории ---

    n "Но сначала нужно было его дождаться." (show_side="none", show_kind="speech")
    n "Она сидела в пустой лаборатории. Терминал светился. Каэль опаздывал." (show_side="none", show_kind="speech")

    show eveina annoyed at eveina_left
    ev_thought "Опаздывает. Каэль опаздывает." (show_side="left", show_kind="thought")
    hide eveina
    show eveina eyebrow at eveina_left
    ev_thought "Это на него совсем не похоже." (show_side="left", show_kind="thought")
    hide eveina
    show eveina annoyed at eveina_left
    ev_thought "Хотя, откровенно говоря, меня это злит ещё больше. Мало того, что оставил меня на отработку — так ещё и заставляет ждать." (show_side="left", show_kind="thought")
    hide eveina

    n "Она барабанила пальцами по панели, смотрела в пустой экран. Тишина лаборатории давила." (show_side="none", show_kind="speech")
    n "Против воли мысли потянулись назад — к тому, что было несколько часов назад." (show_side="none", show_kind="speech")

    # --- Флэшбэк с практики ---

    call fade_to_black(0.8, 0.5)
    scene bg lab at bg_fullscreen with dissolve

    n "Лаборатория встречала запахом озона, словно гроза уже виднелась на горизонте. Эвейна шагнула внутрь и тут же ощутила себя, как на поле боя." (show_side="none", show_kind="speech")
    n "Игнорируя это чувство, она до последнего надеялась, что сегодня не придётся бороться и с ним, и со своей усталостью одновременно." (show_side="none", show_kind="speech")
    n "Каэль, кажется, был настроен на противоположное." (show_side="none", show_kind="speech")

    show kael normal at kael_right
    ka "Хейла. Ты снова опоздала." (show_side="right", show_kind="speech")
    hide kael
    show kael thinking at kael_right
    ka "Хотя, кажется, у тебя это входит в привычку." (show_side="right", show_kind="speech")
    hide kael

    n "Он даже не посмотрел на неё, только скользнул взглядом по лаборатории. В голосе чувствовалась ледяная, обидно колющая сталь." (show_side="none", show_kind="speech")
    n "Эвейна прошла на своё место, пробурчав сквозь стиснутые зубы:" (show_side="none", show_kind="speech")

    show eveina annoyed at eveina_left
    ev "Не выспался? Или ещё не успел съесть ни одну жертву на завтрак?" (show_side="left", show_kind="speech")
    hide eveina

    n "Она села к интерфейсу, заметив, как дрожат от усталости кончики пальцев. Корректировка нейросигналов — задача вроде бы простая, но сейчас всё валилось из рук." (show_side="none", show_kind="speech")
    n "Она смахнула один из параметров чуть не туда, сдвинула коэффициент, нажала «Применить». Терминал выдал предупреждение." (show_side="none", show_kind="speech")
    n "Эвейна отвела взгляд, зевнула — и нажала подтверждение. Через секунду поле отклика заполнилось рябью, а лаборатория — неприятным писком." (show_side="none", show_kind="speech")

    show eveina wondered at eveina_left
    ev_thought "Что за..." (show_side="left", show_kind="thought")
    hide eveina

    n "Каэль мгновенно оказался рядом. Его рука скользнула по панели, откатив действия. Вся система замерла." (show_side="none", show_kind="speech")
    n "Он опёрся ладонью на терминал, нависнув над ней и наклонившись так близко, что почти касался её волос." (show_side="none", show_kind="speech")

    show kael eyebrow at kael_right
    ka "Интересно. Новая стратегия?" (show_side="right", show_kind="speech")
    ka "Создавать нестабильность, чтобы списать ошибку на сбой оборудования?" (show_side="right", show_kind="speech")
    hide kael

    n "Эти слова были бы смешными, если бы не хлёсткая нота в голосе, от которой по позвоночнику побежали иглы." (show_side="none", show_kind="speech")
    n "Она едва удержалась, чтобы не оттолкнуть его руку, не вспыхнуть. Внутри бурлило раздражение от собственной ошибки, от усталости и того, что он снова смотрит на неё вот так — сверху вниз." (show_side="none", show_kind="speech")
    n "Эвейна сжала зубы и процедила:" (show_side="none", show_kind="speech")

    show eveina annoyed at eveina_left
    ev "Просто... не заметила." (show_side="left", show_kind="speech")
    hide eveina

    show kael normal at kael_right
    ka "Ошибки входят в привычку. Я уже почти начинаю считать её твоим научным методом." (show_side="right", show_kind="speech")
    hide kael
    show kael intrigued at kael_right
    ka "После занятий — у тебя отработка. Сама напросилась." (show_side="right", show_kind="speech")
    hide kael

    n "Он развернулся и отошёл к своему терминалу, бросив напоследок:" (show_side="none", show_kind="speech")

    show kael serious at kael_right
    ka "Надеюсь, в следующий раз ты хотя бы поймешь, в чём именно ошиблась." (show_side="right", show_kind="speech")
    ka "Это было бы... освежающе." (show_side="right", show_kind="speech")
    hide kael

    n "Подавленным взглядом Эвейна обвела лабораторию, замечая, что на неё смотрят многие студенты." (show_side="none", show_kind="speech")

    show eveina upset at eveina_left
    ev_thought "Отработка. И я снова не доберусь до закрытых секций. Не сегодня." (show_side="left", show_kind="thought")
    ev_thought "«Данные изолированы и доступны только внутри помещения»... Как вообще туда попасть?" (show_side="left", show_kind="thought")
    hide eveina
    show eveina thinking at eveina_left
    ev_thought "Как будто всё, что действительно важно, всегда отодвигается на потом." (show_side="left", show_kind="thought")
    hide eveina
    show eveina upset at eveina_left
    ev_thought "Только вот у меня может не быть этого «потом»." (show_side="left", show_kind="thought")
    hide eveina

    n "Эвейна опустила глаза, делая вид, что снова сосредоточилась на параметрах. Но что-то в выражении её лица — не раздражение, не обида, а тень настоящего… утомления — заставило Каэля задержать взгляд." (show_side="none", show_kind="speech")
    n "Эвейна не видела, как парень долго изучающе на неё смотрел." (show_side="none", show_kind="speech")
    n "Не как преподаватель, чья студентка снова сплоховала. Как человек, который пытался понять, что именно с ней сейчас происходит." (show_side="none", show_kind="speech")

    # --- Первый сбой имплантов — тихий ---

    n "Взгляд задержался слишком долго. Каэль, кажется, сам не заметил этого сразу." (show_side="none", show_kind="speech")
    n "А потом — быстрое, почти механическое движение: пальцы коснулись виска. Секунда. Он отвернулся к консоли." (show_side="none", show_kind="speech")
    n "Эвейна смотрела в экран. Ничего не видела." (show_side="none", show_kind="speech")

    # --- Конец флэшбэка ---

    call fade_to_black(0.8, 0.5)
    scene bg lab at bg_fullscreen with dissolve

    n "Лаборатория всё так же была пуста." (show_side="none", show_kind="speech")

    show eveina annoyed at eveina_left
    ev_thought "Где его вообще носит?" (show_side="left", show_kind="thought")
    hide eveina

    n "Дверь открылась." (show_side="none", show_kind="speech")
    n "Каэль вошёл — и что-то в нём было не так. Не обычная сухость. Что-то другое, более плотное." (show_side="none", show_kind="speech")
    n "Напряжение, которое носят внутри, а не снаружи." (show_side="none", show_kind="speech")

    show eveina eyebrow at eveina_left
    ev_thought "Что с ним?" (show_side="left", show_kind="thought")
    hide eveina

    n "Он не объяснился. Просто сел за соседний терминал." (show_side="none", show_kind="speech")

    show kael normal at kael_right
    ka "Приступим." (show_side="right", show_kind="speech")
    hide kael

    jump scene_4_5
