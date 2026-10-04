label scene_6_3:
    $ previous_scene = "scene_6_2"
    $ next_scene = "scene_6_4"
    $ current_scene = "scene_6_3"
    call fade_to_black(1.2, 0.8) 
    scene bg virt_cabinet at bg_fullscreen with dissolve

    n "Ноги не слушались. Кажется, она шла автоматически, не чувствуя, как проходила по холлу, поднималась по лестнице, встала перед дверью." (show_side="none", show_kind="speech")
    n "Дрожащая рука потянулась к панели, заявляя о своём присутствии, и дверь открылась бесшумно." (show_side="none", show_kind="speech")
    n "Аурелиан Вирт стоял у окна, спиной к ней. Его силуэт был напряжённым. Молчание повисло в воздухе, как перед грозой." (show_side="none", show_kind="speech")

    show virt serious at virt_right
    vi "Закройте за собой дверь." (show_side="right", show_kind="speech")
    hide virt

    n "Эвейна послушно сделала шаг внутрь, дверь за ней закрылась, отрезая путь к побегу. Её дыхание сбилось." (show_side="none", show_kind="speech")

    show virt serious at virt_right
    vi "Я просматривал архивные журналы." (show_side="right", show_kind="speech")
    hide virt
    show virt thinking at virt_right
    vi "Обнаружил нестандартную активность…" (show_side="right", show_kind="speech")
    hide virt
    show virt serious at virt_right
    vi "И заметил отсутствие одной книги." (show_side="right", show_kind="speech")
    hide virt

    n "Профессор развернулся. Его лицо было мрачным, губы — сжаты в тонкую линию. Он подошёл к терминалу, активировал голограмму с логами." (show_side="none", show_kind="speech")

    show virt angry at virt_right
    vi "Вы украли материал из закрытого фонда, где хранились бесценные печатные издания. Нарушили протокол доступа." (show_side="right", show_kind="speech")
    vi "И, что хуже всего, обманули моё доверие." (show_side="right", show_kind="speech")
    hide virt

    n "Голос — спокойный, без эмоций. Но от этого — вдвойне страшнее. За этой сдержанностью, словно за тонким стеклом, бушевал настоящий шторм." (show_side="none", show_kind="speech")

    show virt thinking at virt_right
    vi "Я дал вам свободу. Верил в вашу искренность." (show_side="right", show_kind="speech")
    hide virt
    show virt serious at virt_right
    vi "А вы воспользовались этим, чтобы действовать за моей спиной." (show_side="right", show_kind="speech")
    hide virt

    n "Эвейна опустила глаза. Слова резали сильнее, чем крик." (show_side="none", show_kind="speech")

    show eveina upset at eveina_left
    ev "Я… я просто…" (show_side="left", show_kind="speech")
    ev "Я хотела вернуть её..." (show_side="left", show_kind="speech")
    hide eveina

    n "Он кивнул — один раз, коротко, словно ставил точку." (show_side="none", show_kind="speech")

    show virt angry at virt_right
    vi "Вы и вернёте. Немедленно." (show_side="right", show_kind="speech")
    hide virt
    show virt serious at virt_right
    vi "Знаете, мисс Хейла… доверие — это не академическая единица. Оно не восстанавливается после пересдачи." (show_side="right", show_kind="speech")
    vi "Его можно обмануть лишь однажды." (show_side="right", show_kind="speech")
    hide virt

    n "Эвейна почувствовала, как у неё подкашиваются ноги. Горло сжалось, а голос в голове кричал:" (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev_thought "Скажи что-то. Защити себя. Извинись. Сделай что-нибудь! Не стой как школьница после прокола." (show_side="left", show_kind="thought")
    hide eveina
    show eveina upset at eveina_left   
    ev "Простите… Я не хотела…" (show_side="left", show_kind="speech")
    ev "Я просто…" (show_side="left", show_kind="speech")
    hide eveina

    n "Вирт поднял на неё тяжелый взгляд. Его глаза потускнели. На мгновение в них появился не холод, а разочарование. И, быть может, след боли?" (show_side="none", show_kind="speech")

    show virt serious at virt_right
    vi "Я не могу закрывать на это глаза." (show_side="right", show_kind="speech")
    hide virt
    show virt angry at virt_right
    vi "Вы должны понимать, что Академия — не место для детских выходок. Это первое и последнее предупреждение." (show_side="right", show_kind="speech")
    hide virt

    n "Он снова отвернулся, делая шаг к окну и давая понять, что разговор окончен." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev_thought "Прекрасный момент, чтобы попросить об одолжении. Правда, Эвейна?" (show_side="left", show_kind="thought")
    hide eveina

    n "Девушка молча стояла посреди кабинета и боролась сама с собой. Услышать сейчас отказ было подобно смерти. Но и расчитывать на положительный ответ - чистое безумие." (show_side="none", show_kind="speech")
    n "Когда она решилась, то смогла выдавить из себя лишь шёпот, будто в надежде, что профессор его не услышит:" (show_side="none", show_kind="speech")

    show eveina normal at eveina_left
    ev "Я бы хотела... увидеть отца. Он... ему стало хуже." (show_side="left", show_kind="speech")
    hide eveina

    n "Некоторое время Вирт хмурился, продолжая глядеть в окно. Затем потер переносицу пальцами, подошёл к терминалу, набрал команду." (show_side="none", show_kind="speech")
    n "Голограмма расписания транспортных узлов отобразилась в воздухе." (show_side="none", show_kind="speech")

    show virt serious at virt_right
    vi "Ближайший шаттл, следующий к вашему сектору, прибудет через две недели." (show_side="right", show_kind="speech")
    vi "Я подал заявку. Места для вас забронированы." (show_side="right", show_kind="speech")
    hide virt
    show virt thinking at virt_right
    vi "Но до этого момента… вы должны закончить работу над проектом по задаче Идентики. И сдать все тесты. Они начнутся через неделю." (show_side="right", show_kind="speech")
    hide virt

    n "Он обернулся. Его взгляд снова стал строгим." (show_side="none", show_kind="speech")

    show virt normal at virt_right
    vi "Не делайте больше ничего безрассудного. И тем более — опасного." (show_side="right", show_kind="speech")
    hide virt
    show virt serious at virt_right
    vi "Ещё одна подобная выходка и, боюсь, я смогу защитить вас от отчисления." (show_side="right", show_kind="speech")
    hide virt

    n "Невольно вздрогнув от тона его просьбы, Эвейна кивнула." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev_thought "Систематическое мелкое воровство, проникновение на закрытую территорию, взлом защищённых архивных файлов…" (show_side="left", show_kind="thought")
    ev_thought "Ах да, ещё регулярное общение с существом, к которому по уставу Академии вообще нельзя приближаться ближе, чем на 40 километров." (show_side="left", show_kind="thought")
    hide eveina
    show eveina upset at eveina_left
    ev_thought "Да куда уже безрассуднее, ага." (show_side="left", show_kind="thought")
    hide eveina

    n "Она направилась к выходу, но, почувствовав на себе его взгляд, на мгновение задержалась у двери." (show_side="none", show_kind="speech")

    show virt serious at virt_right
    vi "Вы хотели что-то ещё?" (show_side="right", show_kind="speech")
    hide virt

    show eveina thinking at eveina_left
    ev_thought "Я — нет. А вы, профессор?" (show_side="left", show_kind="thought")
    hide eveina

    n "Она покачала головой и вышла. За её спиной дверь сомкнулась с глухим шипением." (show_side="none", show_kind="speech")
    n "Вирт остался в кабинете один. Его лицо было всё тем же — спокойным, собранным. Но пальцы на краю стола медленно сжались в кулак." (show_side="none", show_kind="speech")

    jump scene_6_4
