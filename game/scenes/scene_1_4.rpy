label scene_1_4:

    $ previous_scene = "scene_1_3"
    $ next_scene = "scene_1_5"
    $ current_scene = "scene_1_4"
    $ kg_prepare_scene("scene_1_4")

    call fade_to_black(1.2, 0.8)
    scene bg scene 1_4 garden 1 at bg_fullscreen with dissolve
    pause (1.0)
    # play music "bgm/garden_evening.ogg" fadein 2.0

    n "Оставшийся день прошёл в череде вводных лекций и экскурсионных блоков." (show_side="none", show_kind="speech")
    n "Когда официальная часть была окончена, голова гудела от лиц, голосов и нескончаемого потока сведений." (show_side="none", show_kind="speech")
    n "ИИ-ассистент настойчиво рекомендовал отдых." (show_side="none", show_kind="speech")

    #show eveina eyeroll at eveina_left
    ev_thought "Отдых. Конечно." (show_side="left", show_kind="thought")
    #hide eveina

    n "Вместо того чтобы строить маршрут до общежития, Эвейна нашла на карте дорогу в сад — место, где, по словам ИИ, «рекомендуется рекреация»." (show_side="none", show_kind="speech")

    scene bg garden evening  at bg_fullscreen with dissolve

    n "Из окна шаттла сад выглядел самым обычным. Но сейчас, в закатном солнце на листьях и траве поблёскивали биолюминесцентные прожилки, а вода дробила их отражения мелкой рябью." (show_side="none", show_kind="speech")
    n "Здесь наконец можно было думать, не пытаясь одновременно слушать, отвечать и запоминать очередное имя." (show_side="none", show_kind="speech")
    n "Девушка остановилась неподалёку от раскидистого дерева у кромки озера. По карте граница купола проходила через его корни." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left, sprite_warm_light
    ev_thought "Вирт сказал, что без контроля поле планеты повреждает нейронные связи." (show_side="left", show_kind="thought")
    ev_thought "Парень из холла — что какой-то инцидент произошёл из-за инналу." (show_side="left", show_kind="thought")
    ev_thought "А после инцидента Академия активировала купол и запретила контакты." (show_side="left", show_kind="thought")
    hide eveina
    show eveina eyebrow at eveina_left, sprite_warm_light
    ev_thought "Так от чего именно нас защищают?" (show_side="left", show_kind="thought")
    hide eveina
    show eveina normal at eveina_left, sprite_warm_light
    ev "ИИ, какова функция защитного купола?" (show_side="left", show_kind="speech")
    hide eveina

    show ai at ai_right
    ai "Купол экранирует территорию Академии от неконтролируемого воздействия поля Иннаки и ограничивает перемещение через установленную границу." (show_side="right", show_kind="speech")
    hide ai

    show eveina eyebrow at eveina_left, sprite_warm_light
    ev "Почему раньше его держали выключенным?" (show_side="left", show_kind="speech")
    hide eveina

    show ai at ai_right
    ai "В штатном режиме полная изоляция территории Академии не требуется." (show_side="right", show_kind="speech")
    hide ai

    show eveina eyebrow at eveina_left, sprite_warm_light  
    ev "Что изменилось?" (show_side="left", show_kind="speech")
    hide eveina

    show ai at ai_right
    ai "После недавнего технического сбоя введён усиленный режим безопасности." (show_side="right", show_kind="speech")
    hide ai

    show eveina normal at eveina_left, sprite_warm_light
    ev "Сбой был связан с полем?" (show_side="left", show_kind="speech")
    hide eveina

    show ai at ai_right
    ai "Причина технического сбоя не установлена." (show_side="right", show_kind="speech")
    hide ai

    show eveina eyebrow at eveina_left, sprite_warm_light 
    ev "А инналу имеют к нему отношение?" (show_side="left", show_kind="speech")
    hide eveina

    show ai at ai_right
    ai "Подтверждённые сведения о причастности инналу отсутствуют." (show_side="right", show_kind="speech")
    hide ai

    show eveina annoyed at eveina_left, sprite_warm_light  
    ev "Тогда почему контакты с ними запрещены?" (show_side="left", show_kind="speech")
    hide eveina

    show ai at ai_right
    ai "Самовольные контакты запрещены уставом Академии. Временный режим предусматривает дополнительные ограничения." (show_side="right", show_kind="speech")
    hide ai

    show eveina thinking at eveina_left, sprite_warm_light 
    ev_thought "Допустим, от негативного влияния поля защищает купол. От инналу — правила. И оба ограничения Академия ввела после инцидента." (show_side="left", show_kind="thought")
    hide eveina
    show eveina eyeroll at eveina_left, sprite_warm_light 
    ev_thought "Но что произошло месяц назад, никто объяснять не собирается." (show_side="left", show_kind="thought")
    hide eveina

    n "На той стороне озера виднелась территория за куполом. Инналу проводили там всю жизнь — без лабораторий и экранирующего контура." (show_side="none", show_kind="speech")

    show eveina eyebrow at eveina_left, sprite_warm_light
    ev_thought "Если нам нужна защита от поля, почему оно не вредит им?" (show_side="left", show_kind="thought")
    hide eveina
    show eveina normal at eveina_left, sprite_warm_light
    ev "ИИ, как поле Иннаки воздействует на инналу?" (show_side="left", show_kind="speech")
    hide eveina

    show ai at ai_right
    ai "Негативное воздействие поля на организм инналу не зафиксировано." (show_side="right", show_kind="speech")
    hide ai

    show eveina eyebrow at eveina_left, sprite_warm_light
    ev "А что у них с нейродегенеративными заболеваниями?" (show_side="left", show_kind="speech")
    hide eveina

    show ai at ai_right
    ai "Подтверждённые случаи среди представителей народа инналу отсутствуют." (show_side="right", show_kind="speech")
    hide ai

    n "Эвейна провела ладонью по нагретой солнцем коре, пытаясь соединить разрозненные факты." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left, sprite_warm_light
    ev_thought "Значит, дело не только в поле. Важно понять, почему оно не вредит им." (show_side="left", show_kind="thought")
    hide eveina
    show eveina normal at eveina_left, sprite_warm_light
    ev "Покажи исследования их нервной системы." (show_side="left", show_kind="speech")
    hide eveina

    show ai at ai_right
    ai "Материалы, связанные с физиологией инналу, требуют отдельного допуска." (show_side="right", show_kind="speech")
    hide ai

    show eveina annoyed at eveina_left, sprite_warm_light
    ev "У меня есть студенческий доступ к внутренней базе." (show_side="left", show_kind="speech")
    hide eveina

    show ai at ai_right
    ai "Студенческий доступ не распространяется на исследования с участием инналу." (show_side="right", show_kind="speech")
    hide ai

    show eveina eyeroll at eveina_left, sprite_warm_light
    ev_thought "Ну конечно. Самое интересное начинается ровно там, где заканчивается доступ." (show_side="left", show_kind="thought")
    hide eveina

    n "Эвейна создала на браслете новый пункт в заметке." (show_side="none", show_kind="speech")

    n "{i}Проверить внутреннюю базу:\n— поле Иннаки;\n— нейродегенеративные заболевания;\n— физиология инналу.{/i}" (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left, sprite_warm_light
    ev_thought "Ладно. Утром посмотрим, что они всё-таки разрешили мне увидеть." (show_side="left", show_kind="thought")
    hide eveina

    n "Она сделала ещё несколько шагов к дереву." (show_side="none", show_kind="speech")

    scene bg scene 1_4 garden 2 at bg_fullscreen with dissolve
    pause (1.0)

    n "Браслет завибрировал." (show_side="none", show_kind="speech")

    ev "Да-да, я поняла — не пересекать границу." (show_side="left", show_kind="speech")

    n "Купол выдавало лишь лёгкое дрожание воздуха над корнями дерева." (show_side="none", show_kind="speech")
    n "Эвейна остановилась у самой границы." (show_side="none", show_kind="speech")


    ev_thought "Если их нервная система устойчива и к полю, и к дегенеративным заболеваниям, эти исследования могут оказаться ближе всего к тому, зачем я сюда прилетела." (show_side="left", show_kind="thought")
    ev_thought "Но тут в игру вступает третье ограничение – уровни допуска." (show_side="left", show_kind="thought")
    
    n "За спиной еле слышно хрустнула ветка." (show_side="none", show_kind="speech")

    scene bg scene 1_4 garden 3 at bg_fullscreen with dissolve
    pause (1.0)

    ev "Здесь кто-то есть?" (show_side="left", show_kind="speech")

    n "Ответа не последовало. Только ветви у дальней дорожки ещё немного покачивались." (show_side="none", show_kind="speech")
    n "Она снова повернулась к озеру." (show_side="none", show_kind="speech")

    scene bg scene 1_4 garden 2 at bg_fullscreen with dissolve
    pause (1.0)

    ev "Ну, как хочешь." (show_side="left", show_kind="speech")

    n "Девушка провела ладонью по тёплому стволу и прикрыла глаза. Пахло водой и нагретой травой. Уходить не хотелось." (show_side="none", show_kind="speech")
    n "Но после второго напоминания об отдыхе она всё же решила прислушаться." (show_side="none", show_kind="speech")

    scene bg scene 1_4 garden 4 at bg_fullscreen with dissolve
    pause (1.0)

    n "И направилась в сторону Академии." (show_side="none", show_kind="speech")
    n "На обратном пути пришлось признать: ИИ в кои-то веки посоветовал что-то полезное." (show_side="none", show_kind="speech")

    jump scene_1_5  # Переход к следующей сцене
