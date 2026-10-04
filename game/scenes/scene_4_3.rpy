label scene_4_3:
    $ previous_scene = "scene_4_2"
    $ next_scene = "scene_4_4"
    $ current_scene = "scene_4_3"

    scene bg eveina_room_day at bg_fullscreen with dissolve
    n "Залетев в комнату, девушка трясущимися пальцами поспешно вызвала ИИ-ассистента." (show_side="none", show_kind="speech")

    show sf at ai_right
    ai "И тебе доброго утра. Уже соскучилась, любительница бега по утрам?" (show_side="right", show_kind="speech")
    hide sf

    show eveina angry at eveina_left
    ev "Какого чёрта?" (show_side="left", show_kind="speech")
    ev "Почему мне сейчас декан Вирт сообщил о том, что на моём браслете случился сбой в момент твоей активации?" (show_side="left", show_kind="speech")
    ev "Я была в шаге от того, чтобы попасться!" (show_side="left", show_kind="speech")
    hide eveina

    show sf at ai_right
    ai "Полегче, студентка Эвейна, твой пульс зашкаливает." (show_side="right", show_kind="speech")
    hide sf

    show eveina angry at eveina_left
    ev "Полегче, говоришь?" (show_side="left", show_kind="speech")
    ev "Да я была в шаге от того, чтобы попасться!" (show_side="left", show_kind="speech")
    hide eveina    
    show eveina annoyed at eveina_left
    ev "Какого чёрта ты сделал с моим браслетом?" (show_side="left", show_kind="speech")
    hide eveina

    show sf at ai_right
    ai "Я ничего не делал. Ты сама меня активировала." (show_side="right", show_kind="speech")
    ai "Я просто перезаписал системные файлы своими." (show_side="right", show_kind="speech")
    hide sf

    show eveina annoyed at eveina_left
    ev "Что...что ты сделал?" (show_side="left", show_kind="speech")
    hide eveina

    show sf at ai_right
    ai "Это было необходимо для моей активации. В одном браслете не ужиться двум управляющим системам." (show_side="right", show_kind="speech")
    ai "Считай, что твой браслет получил небольшой апгрейд." (show_side="right", show_kind="speech")
    hide sf

    show eveina annoyed at eveina_left
    ev "Как это исправить? Вернуть всё, как было!" (show_side="left", show_kind="speech")
    hide eveina

    show sf at ai_right
    ai "Ты всегда можешь заменить браслет на новый." (show_side="right", show_kind="speech")
    ai "Но тогда, вероятно, моя активация не останется без внимания." (show_side="right", show_kind="speech")
    ai "Но ты не переживай, я, как прилежный шпион, продолжу отсылать данные обо всех твоих перемещениях и запросах к сети." (show_side="right", show_kind="speech")
    ai "Никто и не заметит." (show_side="right", show_kind="speech")
    hide sf

    show eveina sad at eveina_left
    ev "Боже, что я натворила..." (show_side="left", show_kind="speech")
    ev "Меня же за такое исключат." (show_side="left", show_kind="speech")
    hide eveina

    show sf at ai_right
    ai "Дорогуша, я не в настроении для сеанса психологии." (show_side="right", show_kind="speech")
    ai "Поэтому, будь добра, возьми себя в руки и прими тот факт, что мы теперь с тобой живём вместе." (show_side="right", show_kind="speech")
    ai "Я тоже не восторге, если тебе интересно." (show_side="right", show_kind="speech")
    ai "Но мне нравится...быть активным. Поэтому я готов немного тебе посодействовать." (show_side="right", show_kind="speech")
    hide sf

    show eveina upset thinking at eveina_left
    ev "О, ты уже прекрасно посодействовал моему исключению." (show_side="left", show_kind="speech")
    hide eveina
    show eveina annoyed at eveina_left
    ev "И я тебе не дорогуша!" (show_side="left", show_kind="speech")
    hide eveina

    show sf at ai_right
    ai "Твоё исключение тоже не входит в зону моих интересов, так что будь паинькой и никому не говори про меня. Тогда всё будет в порядке." (show_side="right", show_kind="speech")
    ai "И вообще, научись смотреть на ситуацию в целом." (show_side="right", show_kind="speech")
    ai "Если бы ты запросила недоступную информацию у стандартного ИИ, то об этом бы уже знала вся Академия." (show_side="right", show_kind="speech")
    ai "А я умею хранить секреты." (show_side="right", show_kind="speech")
    ai "Смекаешь?" (show_side="right", show_kind="speech")
    hide sf

    show eveina upset thinking at eveina_left
    ev "Смекаю. Я в заложниках у искусственного интеллекта." (show_side="left", show_kind="speech")
    hide eveina

    show sf at ai_right
    ai "Я почти оскорблён. Хватит ныть о том, что изменить нельзя." (show_side="right", show_kind="speech")
    ai "Лучше поторопись с душем, иначе опоздаешь на лекцию." (show_side="right", show_kind="speech")
    ai "А я пока восстановлю свои душевные силы. Разговор с тобой весьма утомляет." (show_side="right", show_kind="speech")
    hide sf

    n "ИИ отключился, на прощанье мигнув проекцией текущего времени." (show_side="none", show_kind="speech")
    n "Взглянув на часы, девушка спешно подхватила полотенце и направилась в душ смывать с себя события этого утра." (show_side="none", show_kind="speech")

    show eveina upset thinking at eveina_left
    ev_thought "Я точно об этом когда-нибудь пожалею..." (show_side="left", show_kind="thought")
    hide eveina

    jump scene_4_4
