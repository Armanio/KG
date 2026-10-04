label scene_2_4:
    $ previous_scene = "scene_2_3_after_lecture"
    $ next_scene = "scene_2_5"
    $ current_scene = "scene_2_4"
    $ kg_prepare_scene("scene_2_4")

    # =========================================================
    # СЦЕНА 4 — «ДОРОГА В АРХИВ»
    # Функция: Эвейна находит Архив, но сознательно откладывает
    # поиск, чтобы заранее прийти на первую практику.
    # =========================================================

    call fade_to_black(1.2, 0.8)
    scene bg corridor at bg_fullscreen with dissolve

    n "На карте Академии Архив выглядел почти доступным." (show_side="none", show_kind="speech")
    n "Нужно было пройти два коридора, спуститься на один уровень и повернуть у лабораторного блока." (show_side="none", show_kind="speech")
    n "В действительности первый же указатель отправил Эвейну в противоположную сторону." (show_side="none", show_kind="speech")

    show eveina annoyed at eveina_left
    ev_thought "Либо карту составлял садист, либо она обновлялась последний раз до моего рождения." (show_side="left", show_kind="thought")
    hide eveina

    scene bg corridor_3 at bg_fullscreen with dissolve

    n "Правильный переход оказался перекрыт прозрачной перегородкой." (show_side="none", show_kind="speech")
    n "За ней ремонтные платформы снимали со стены повреждённые панели, а над блокировкой мерцала сухая надпись." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev_thought "Технический сбой." (show_side="left", show_kind="thought")
    hide eveina
    show eveina eyeroll at eveina_left
    ev_thought "Скоро глаз начнёт дергаться от этой фразы." (show_side="left", show_kind="thought")
    hide eveina

    n "Рядом двое старшекурсников спорили с сотрудником безопасности, требуя открыть короткий проход." (show_side="none", show_kind="speech")
    n "Тот молча указывал на временный маршрут в обход." (show_side="none", show_kind="speech")

    show eveina eyeroll at eveina_left
    ev_thought "Ещё три коридора и небольшая экскурсия по административному аду." (show_side="left", show_kind="thought")
    hide eveina

    scene bg corridor_2 at bg_fullscreen with dissolve

    n "Эвейна сверилась с расписанием, запомнила направление и пошла в обход." (show_side="none", show_kind="speech")
    n "Новые указатели закончились через два поворота." (show_side="none", show_kind="speech")
    n "Пришлось возвращаться, сравнивать номера секций и искать проход по служебной схеме на браслете." (show_side="none", show_kind="speech")

    show eveina annoyed at eveina_left
    ev_thought "Формально Архив открыт для студентов." (show_side="left", show_kind="thought")
    ev_thought "Неформально Академия очень надеется, что они сдадутся по дороге." (show_side="left", show_kind="thought")
    hide eveina

    scene bg archive corridor day at bg_fullscreen with dissolve

    n "Дверь нашлась в конце узкого коридора без единого указателя." (show_side="none", show_kind="speech")
    n "Над ней было выбито одно слово: «Архив»." (show_side="none", show_kind="speech")

    show eveina eyebrow at eveina_left
    ev_thought "Вот ты где." (show_side="left", show_kind="thought")
    hide eveina

    n "Эвейна приложила браслет к панели." (show_side="none", show_kind="speech")
    n "Индикатор сменил цвет." (show_side="none", show_kind="speech")

    n "{i}«Студенческий доступ подтверждён»{/i}" (show_side="none", show_kind="speech")

    n "Дверь приоткрылась, выпуская полоску холодного света и запах старой бумаги." (show_side="none", show_kind="speech")
    n "Эвейна уже шагнула вперёд, но браслет напомнил о расписании." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev_thought "До практики тридцать две минуты." (show_side="left", show_kind="thought")
    hide eveina

    n "Лаборатория находилась в другом блоке." (show_side="none", show_kind="speech")
    n "Времени хватало, чтобы прийти заранее." (show_side="none", show_kind="speech")
    n "И совершенно не хватало, чтобы открыть первый отчёт и убедить себя закрыть его через пять минут." (show_side="none", show_kind="speech")

    show eveina annoyed at eveina_left
    ev_thought "Нет. Сначала практика." (show_side="left", show_kind="thought")
    hide eveina

    n "Она сохранила расположение Архива в браслете и отступила." (show_side="none", show_kind="speech")
    n "Дверь закрылась." (show_side="none", show_kind="speech")

    show eveina normal at eveina_left
    ev_thought "Теперь я хотя бы знаю, куда вернуться." (show_side="left", show_kind="thought")
    hide eveina

    jump scene_2_5
