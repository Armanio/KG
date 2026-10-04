label scene_1_2:
    $ previous_scene = "scene_1_1"
    $ next_scene = "scene_1_3"
    $ current_scene = "scene_1_2"
    $ kg_prepare_scene("scene_1_2")
    
    call fade_to_black(1.2, 0.8)
    scene bg scene 1_2 virt cabinet 1 at bg_fullscreen with dissolve
    #play music "bgm/interview_theme.ogg" fadein 1.5

    n "Новоиспечённая студентка стояла перед массивным столом." (show_side="none", show_kind="speech")
    n "За ним — профессор Вирт листал её досье, не предлагая сесть." (show_side="none", show_kind="speech")
    #n "За ним — декан кафедры. Он казался человеком, который давно перестал показывать, что чувствует. Не холоден — скорее сдержан."
    
    ev_thought "Учёный. Декан. Человек, которого до сегодняшнего дня я знала только по фамилии под научными статьями." (show_side="left", show_kind="thought")
    ev_thought "И, судя по тому, как выглядит его кабинет – последний выживший герой викторианского романа." (show_side="left", show_kind="thought")

    n "Эвейна поймала себя на том, что рассматривает его губы, и поспешно перевела взгляд." (show_side="none", show_kind="speech")

    ev_thought "Прекрасно. Именно этого мне не хватало перед собеседованием." (show_side="left", show_kind="thought")
    ev_thought "Хотя нельзя отрицать: выглядит так, будто его специально вывели в лаборатории для проверки концентрации первокурсниц." (show_side="left", show_kind="thought")

    n "Концентрация уже размахивала белым флагом за его спиной." (show_side="none", show_kind="speech")

    n "Вирт поднял голову и задержал хмурый взгляд на студентке. Потом снова посмотрел в досье, словно хотел что-то проверить." (show_side="none", show_kind="speech")

    scene bg scene 1_2 virt cabinet 2 at bg_fullscreen with dissolve

    vi "Вы выбрали специализацию по нейропротокольной терапии. Почему?" (show_side="right", show_kind="speech")

    ev "Я окончила медицинский институт. Последние месяцы изучала работы по нейродегенеративным заболеваниям." (show_side="left", show_kind="speech")

    ev "В открытом доступе есть результаты, обзоры и обещания. Но почти нет протоколов, исходных данных и неудачных исследований." (show_side="left", show_kind="speech")

    ev "У Академии такие материалы есть." (show_side="left", show_kind="speech")

    vi "То есть вас интересует не обучение, а чужие исследования?" (show_side="right", show_kind="speech")

    ev "Одно мешает другому?" (show_side="left", show_kind="speech")

    vi "Иногда." (show_side="right", show_kind="speech")

    n "Его взгляд снова вернулся к досье." (show_side="none", show_kind="speech")

    scene bg scene 1_2 virt cabinet 1 at bg_fullscreen with dissolve

    vi "Приглашение в Академию не гарантирует место на выбранной кафедре." (show_side="right", show_kind="speech")
    vi "В этом году на нейропротокольную терапию претендовали восемьдесят человек." (show_side="right", show_kind="speech")

    ev "На одно место. Я читала условия." (show_side="left", show_kind="speech")

    vi "И вас это не смутило?" (show_side="right", show_kind="speech")

    ev "Я не боюсь конкуренции." (show_side="left", show_kind="speech")
    ev "И уже изучила всё, до чего могла добраться без Академии. Восемьдесят человек — не причина останавливаться." (show_side="left", show_kind="speech")

    n "Вирт ещё несколько секунд изучал планшет, потом погасил экран и поднялся." (show_side="none", show_kind="speech")
    n "Рука привычным движением откинула пряди со лба." (show_side="none", show_kind="speech")

    scene bg virt cabinet day at bg_fullscreen with dissolve

    show virt normal at virt_right, sprite_warm
    vi "Вступительные испытания вы прошли хорошо." (show_side="right", show_kind="speech")
    hide virt

    show virt thinking at virt_right, sprite_warm
    vi "Рекомендация тоже оказалась убедительной." (show_side="right", show_kind="speech")
    hide virt

    show eveina surprized at eveina_left, sprite_warm
    ev_thought "Что? Какая ещё рекомендация?" (show_side="left", show_kind="thought")
    hide eveina

    n "Эвейна могла бы спросить об этом, но в голове крутился куда более важный вопрос." (show_side="none", show_kind="speech")

    show eveina normal at eveina_left, sprite_warm
    ev "Так каково ваше решение?" (show_side="left", show_kind="speech")
    hide eveina

    show virt normal at virt_right, sprite_warm
    vi "Я не возражаю против вашей специализации." (show_side="right", show_kind="speech")
    hide virt

    show eveina eyebrow at eveina_left, sprite_warm
    ev "Это означает «да»?" (show_side="left", show_kind="speech")
    hide eveina

    show virt eyebrow at virt_right, sprite_warm
    vi "Это означает, что вы приняты на кафедру." (show_side="right", show_kind="speech")
    hide virt
    show virt smile at virt_right, sprite_warm
    vi "Добро пожаловать в Академию, мисс Хейла." (show_side="right", show_kind="speech")
    hide virt

    show eveina intrigued at eveina_left, sprite_warm
    ev_thought "Вот 2теперь — готово." (show_side="left", show_kind="thought")
    hide eveina

    n "Эвейна уже собиралась спросить о рекомендации, когда третий участник собеседования счёл паузу своим выходом." (show_side="none", show_kind="speech")

    show ai at ai_right
    ai "Запись собеседования сохранена. Доступ к материалам ограничен." (show_side="right", show_kind="speech")
    hide ai

    show eveina surprized at eveina_left, sprite_warm
    ev_thought "Фу-ух, зачем так пугать?" (show_side="left", show_kind="thought")
    hide eveina
    show eveina thinking at eveina_left, sprite_warm
    ev_thought "О чём я там? А, рекомен..." (show_side="left", show_kind="thought")
    hide eveina

    show virt normal at virt_right, sprite_warm
    vi "Мисс Хейла." (show_side="right", show_kind="speech")
    hide virt

    n "Девушка поспешно подняла глаза на профессора." (show_side="none", show_kind="speech")

    show virt normal at virt_right, sprite_warm
    vi "Вы ознакомлены с системой наставничества в Академии?" (show_side="right", show_kind="speech")
    hide virt

    show eveina normal at eveina_left, sprite_warm
    ev "В общих чертах." (show_side="left", show_kind="speech")
    hide eveina

    show virt normal at virt_right, sprite_warm
    vi "На первый семестр Академия назначает каждому студенту наставника." (show_side="right", show_kind="speech")
    hide virt
    show virt upset thinking at virt_right, sprite_warm
    vi "Он подтверждает доступ к внутренним данным, а также помогает в проектной работе и исследованиях." (show_side="right", show_kind="speech")
    hide virt

    show eveina eyebrow at eveina_left, sprite_warm
    ev "Кто назначен мне?" (show_side="left", show_kind="speech")
    hide eveina

    show virt normal at virt_right, sprite_warm
    vi "Я." (show_side="right", show_kind="speech")
    hide virt

    n "Эвейна не сразу нашлась с ответом." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left, sprite_warm
    ev_thought "Наставник — сам Вирт, второе лицо Академии." (show_side="left", show_kind="thought")
    hide eveina
    show eveina eyeroll at eveina_left, sprite_warm
    ev_thought "Либо мне невероятно повезло." (show_side="left", show_kind="thought")
    hide eveina
    show eveina upset thinking at eveina_left, sprite_warm
    ev_thought "Либо я в полной з..." (show_side="left", show_kind="thought")
    hide eveina

    # --- Приглашение на прогулку ---

    n "Эвейна сжала полы пиджака пальцами, собираясь с мыслями. От ответа Вирта зависел следующий пункт её плана." (show_side="none", show_kind="speech")

    show eveina normal at eveina_left, sprite_warm
    ev "Тогда мне понадобится ваше согласие." (show_side="left", show_kind="speech")
    hide eveina

    show virt eyebrow at virt_right, sprite_warm
    vi "На что именно?" (show_side="right", show_kind="speech")
    hide virt

    show eveina normal at eveina_left, sprite_warm
    ev "На доступ к внутренней базе исследований." (show_side="left", show_kind="speech")
    hide eveina

    show virt serious at virt_right, sprite_warm
    vi "Вы ещё не покинули мой кабинет." (show_side="right", show_kind="speech")
    hide virt

    show eveina eyebrow at eveina_left, sprite_warm
    ev "Зато уже принята на кафедру." (show_side="left", show_kind="speech")
    hide eveina

    show virt normal at virt_right, sprite_warm
    vi "Уверен, вы понимаете: внутренний доступ существует не для удовлетворения любопытства." (show_side="right", show_kind="speech")
    hide virt

    show eveina normal at eveina_left, sprite_warm
    ev "Мне нужны завершённые исследования по нейродегенеративным заболеваниям: методики, отрицательные результаты, исходные данные." (show_side="left", show_kind="speech")
    hide eveina

    show virt eyebrow at virt_right, sprite_warm
    vi "Зачем?" (show_side="right", show_kind="speech")
    hide virt

    n "Правдивый ответ сделал бы просьбу слишком похожей на мольбу. Эвейна предпочитала переговоры." (show_side="none", show_kind="speech")

    show eveina normal at eveina_left, sprite_warm
    ev "Хочу продолжить свою карьеру в этой специализации." (show_side="left", show_kind="speech")
    hide eveina

    n "Вирт взглянул на часы." (show_side="none", show_kind="speech")

    show virt thinking at virt_right, sprite_warm
    vi "До общего сбора ещё есть время." (show_side="right", show_kind="speech")
    hide virt
    show virt normal at virt_right, sprite_warm
    vi "Пройдёмтесь." (show_side="right", show_kind="speech")
    hide virt

    n "Профессор сделал шаг к двери и замер под удивлённым взглядом студентки." (show_side="none", show_kind="speech")

    show virt eyebrow at virt_right, sprite_warm
    vi "Идёте? Или у вас есть другие планы?" (show_side="right", show_kind="speech")
    hide virt

    show eveina normal at eveina_left, sprite_warm
    ev "Нет... то есть, да, конечно." (show_side="left", show_kind="speech")
    hide eveina

    # =========================================================
    # ПРОГУЛКА
    # Вирт проверяет её мотивы и знания.
    # Эвейна добивается ограниченного доступа.
    # =========================================================

    call fade_to_black(0.8, 0.5)
    scene bg garden inner at bg_fullscreen with dissolve

    n "Вирт вывел её во внутренний сад. Он не уточнил, было ли это просто прогулкой или продолжением собеседования." (show_side="none", show_kind="speech")

    show eveina eyeroll at eveina_left
    ev_thought "Продолжением. Разумеется." (show_side="left", show_kind="thought")
    hide eveina

    n "Некоторое время они шли молча." (show_side="none", show_kind="speech")

    show virt eyebrow at virt_right
    vi "Что вы знаете об Иннаки, мисс Хейла?" (show_side="right", show_kind="speech")
    hide virt

    show eveina eyebrow at eveina_left
    ev "Это имеет отношение к моему запросу?" (show_side="left", show_kind="speech")
    hide eveina

    n "Не торопясь с ответом, декан сделал несколько шагов в сторону и опёрся спиной на стену. Эвейна последовала его примеру." (show_side="none", show_kind="speech")

    scene bg virt normal eveina normal garden at bg_fullscreen

    vi "Самое непосредственное." (show_side="right", show_kind="speech")

    ev "Знаю то, что прислали при поступлении." (show_side="left", show_kind="speech")

    n "Девушка сделала паузу, но, не получив ответа, продолжила." (show_side="none", show_kind="speech")

    scene bg virt normal eveina thinking garden at bg_fullscreen

    ev "Планета почти полностью покрыта водой. На единственном континенте живут инналу — потомки древних исследователей или колонистов." (show_side="left", show_kind="speech")
    ev "Городов нет, так как местные предпочитают небольшие поселения." (show_side="left", show_kind="speech")
    ev "Академию построили после открытия... около семидесяти лет назад. Для изучения местного поля." (show_side="left", show_kind="speech")

    scene bg virt normal eveina normal garden at bg_fullscreen

    vi "Продолжайте." (show_side="right", show_kind="speech")

    ev "На этом содержательная часть открытых материалов заканчивается." (show_side="left", show_kind="speech")
    ev "Структуру поля описывают поверхностно. Результаты его изучения — почти никак." (show_side="left", show_kind="speech")

    scene bg virt smile eveina normal garden at bg_fullscreen

    vi "Вы действительно внимательно читали буклет." (show_side="right", show_kind="speech")

    scene bg virt normal eveina eyebrow garden at bg_fullscreen

    ev "Я всё ещё не понимаю, какое отношение поле имеет к нейропротокольной терапии." (show_side="left", show_kind="speech")

    n "Профессор на секунду задумался." (show_side="none", show_kind="speech")

    scene bg virt normal eveina normal garden at bg_fullscreen

    vi "Поле Иннаки уникально тем, что представляет собой сочетание тепловых, электромагнитных и биохимических излучений." (show_side="right", show_kind="speech")
    vi "Оно больше похоже на биополе, излучаемое живым существом, нежели космическим объектом." (show_side="right", show_kind="speech")
    vi "Но наибольший интерес для науки представляет то, как поле влияет на местную экосистему и на нейронную активность живых организмов." (show_side="right", show_kind="speech")

    scene bg virt normal eveina eyebrow garden at bg_fullscreen

    ev_thought "Нейронную активность живых организмов?" (show_side="left", show_kind="thought")
    ev "Включая людей?" (show_side="left", show_kind="speech")

    vi "Включая людей." (show_side="right", show_kind="speech")

    ev "И как же оно на нас влияет?" (show_side="left", show_kind="speech")   

    scene bg virt normal eveina thinking garden at bg_fullscreen

    vi "В контролируемых условиях воздействие поля способно восстанавливать и усиливать когнитивные функции." (show_side="right", show_kind="speech")
    vi "Без контроля результат может быть обратным: повреждение нейронных связей, провалы памяти, расстройства восприятия." (show_side="right", show_kind="speech")

    ev_thought "Об этом в буклете упомянуть забыли." (show_side="left", show_kind="thought")

    scene bg virt normal eveina eyebrow garden at bg_fullscreen

    ev "Эти эффекты легли в основу исследований кафедры?" (show_side="left", show_kind="speech")

    vi "Некоторых." (show_side="right", show_kind="speech")

    ev "И отчёты есть во внутренней базе?" (show_side="left", show_kind="speech")

    scene bg virt normal eveina normal garden at bg_fullscreen

    vi "В ней хранятся завершённые исследования, учебные материалы и часть исторических отчётов." (show_side="right", show_kind="speech")
    vi "Действующие проекты и необработанные данные имеют другой уровень допуска." (show_side="right", show_kind="speech")

    ev "Для начала мне хватит студенческого." (show_side="left", show_kind="speech")

    scene bg virt normal eveina eyebrow garden at bg_fullscreen

    vi "Вы говорите так, будто он уже у вас в кармане." (show_side="right", show_kind="speech")

    ev "Потому что не вижу причин для вашего отказа." (show_side="left", show_kind="speech")

    n "Уголок его рта едва заметно дёрнулся." (show_side="none", show_kind="speech")

    scene bg virt smile eveina normal garden at bg_fullscreen

    vi "Разумно." (show_side="right", show_kind="speech")

    scene bg virt normal eveina normal garden at bg_fullscreen

    vi "Я дам согласие на студенческий уровень. Доступ появится после регистрации браслета." (show_side="right", show_kind="speech")

    scene bg virt normal eveina eyebrow garden at bg_fullscreen

    ev "И никаких дополнительных условий?" (show_side="left", show_kind="speech")

    vi "Соблюдать правила Академии. Не пытаться открыть материалы выше своего уровня. Иначе доступ будет аннулирован." (show_side="right", show_kind="speech")

    scene bg virt normal eveina thinking garden at bg_fullscreen

    ev_thought "То есть одно условие и сразу одна угроза." (show_side="left", show_kind="thought")

    ev "Поняла." (show_side="left", show_kind="speech")

    n "На браслете появилось уведомление." (show_side="none", show_kind="speech")

    n "{i}Запрос на доступ к внутренней базе одобрен.\nАктивация после регистрации профиля.{/i}" (show_side="none", show_kind="speech")

    ev_thought "Получилось." (show_side="left", show_kind="thought")

    n "Эвейна закрыла уведомление, пока Вирт не заметил её улыбку, и оттолкнулась от стены." (show_side="none", show_kind="speech")

    scene bg garden inner at bg_fullscreen with dissolve

    show virt intrigued at virt_right
    vi "Есть ещё вопросы?" (show_side="right", show_kind="speech")
    hide virt

    show eveina normal at eveina_left
    ev "Есть." (show_side="left", show_kind="speech")
    hide eveina
    show eveina eyebrow at eveina_left
    ev "Но для первого знакомства, пожалуй, достаточно." (show_side="left", show_kind="speech")
    hide eveina

    show virt eyebrow at virt_right
    vi "Удивительно рассудительно." (show_side="right", show_kind="speech")
    hide virt
    show virt normal at virt_right
    vi "Вам пора в холл на общий сбор." (show_side="right", show_kind="speech")
    hide virt

    show eveina normal at eveina_left
    ev "Спасибо, профессор." (show_side="left", show_kind="speech")
    hide eveina

    n "Вирт оставил её у входа в центральный холл Академии, а Эвейна снова открыла свой список." (show_side="none", show_kind="speech")

    n "{i}{s}Закрепиться на кафедре нейропротокольной терапии – готово.{/s}\n{s}Получить согласие наставника – получено.{/s}\nПолучить доступ к внутренней базе Академии — ожидается активация.{/i}" (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev_thought "Пока всё идёт по плану." (show_side="left", show_kind="thought")
    hide eveina
    show eveina eyeroll at eveina_left
    ev_thought "Даже как-то слишком гладко." (show_side="left", show_kind="thought")
    hide eveina

    n "Она погасила проекцию и направилась в здание." (show_side="none", show_kind="speech")



    jump scene_1_3  # Переход к следующей сцене
