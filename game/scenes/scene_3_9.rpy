label scene_3_9:
    $ previous_scene = "scene_3_8"
    $ next_scene = "scene_3_10"
    $ current_scene = "scene_3_9"
    call fade_to_black(1.2, 0.8)

    scene bg lab_botany at bg_fullscreen with dissolve
    # play music "bgm/lab_peaceful.ogg" fadein 2.0

    n "Профессор Эзари — пожилой мужчина с благоговейным тоном и походкой задумчивого гриба — медленно расхаживал вдоль живых проекционных конструкций, рассказывая о том, как местные растения адаптируются под нейрокоманды и формируют архитектуру." (show_side="none", show_kind="speech")
    
    show ezari normal at ezari_right
    ez "..." (show_side="right", show_kind="speech")
    hide ezari 

    n "Эвейна сидела у терминала, разглядывая свои пальцы и отчаянно сдерживая зевоту." (show_side="none", show_kind="speech")

    show eveina normal at eveina_left
    ev_thought "Практику с утра пораньше придумали для очистки кармы студентов, не иначе..." (show_side="left", show_kind="thought")
    hide eveina

    n "Лея, заручившись поддержкой своего наставника, сбежала после первой же симуляции, оставив её одну на боевом посту." (show_side="none", show_kind="speech")
    n "Остальные студенты вяло вводили команды, искажающие стены и потолки тестового полигона лаборатории. У кого-то получалось странно, у кого-то — совсем никак." (show_side="none", show_kind="speech")
    n "Эвейна попробовала задать собственную последовательность. Через секунду в потолке лаборатории образовалась дыра, из которой начала литься вязкая, мерцающая жидкость." (show_side="none", show_kind="speech")
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
    n "Когда остальные студенты разошлись, профессор вручил Эвейне пульт управления роботом-полотёром, скромно стоящим в углу — и попросил восстановить порядок." (show_side="none", show_kind="speech")
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
    n "Эвейна закинула на рабочий стол внушительных размеров коробку и достала оттуда одну из архивных шкатулок — вытянутую флешку с переливающимся кончиком." (show_side="none", show_kind="speech")
    n "Каждый носитель надо было ввести вручную, просканировать и дать ему категорию: ботаника, архитектура, питательные свойства, токсичность, и так далее." (show_side="none", show_kind="speech")
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

    jump scene_3_10
