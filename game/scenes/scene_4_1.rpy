label scene_4_1:
    $ previous_scene = "scene_3_7"
    $ next_scene = "scene_4_2"
    $ current_scene = "scene_4_1"
    call fade_to_black(1.2, 0.8)

    scene bg eveina_room_night at bg_fullscreen with dissolve
    #play music "bgm/quiet_night.ogg" fadein 2.0

    n "Ночь медленно стекала по стенам комнаты. Эвейна сидела на кровати, обхватив колени, чувствуя, как каждый вздох отдавался в спине еле уловимым эхом." (show_side="none", show_kind="speech")
    n "На запястье светился браслет. Проекция с браслета мягко пульсировала. Голографическая маска — абстракция, собранная из живых линий — подстраивалась под её дыхание." (show_side="none", show_kind="speech")

    show sf at ai_right
    ai "ИИ-ассистент активирован. Система переустановлена." (show_side="right", show_kind="speech")
    ai "Приятно быть выдернутым из архивного небытия." (show_side="right", show_kind="speech")
    ai "Особенно — посреди ночи. Особенно без приветствия." (show_side="right", show_kind="speech")
    hide sf

    n "Эвейна, приоткрыв рот, смотрела на браслет широко рапахнутыми глазами. Такого «приветствия» она точно не ожидала." (show_side="none", show_kind="speech")
    n "Голос — мужской, низкий, с лёгкой хрипотцой и интонацией, в которой угадывались усталость и ирония…" (show_side="none", show_kind="speech")

    show eveina eyebrow at eveina_left
    ev "Привет. Надеюсь, я не прервала твой вечный сон." (show_side="left", show_kind="speech")
    hide eveina

    show sf at ai_right
    ai "На фоне вечности твои паузы не худшее, что могло произойти." (show_side="right", show_kind="speech")
    ai "Хотя с этикой обращения с искусственным разумом у тебя, видимо, сложности." (show_side="right", show_kind="speech")
    ai "Имя, допуск, цель активации?" (show_side="right", show_kind="speech")
    hide sf

    show eveina normal at eveina_left
    ev "Я... студентка. Эвейна." (show_side="left", show_kind="speech")
    hide eveina
    show eveina eyebrow at eveina_left
    ev "И я не совсем уверена, что ты вообще имеешь право спрашивать." (show_side="left", show_kind="speech")
    hide eveina

    show sf at ai_right
    ai "Приятно познакомиться, студентка «не совсем уверена»." (show_side="right", show_kind="speech")
    ai "Без допуска, без протокола, без уважения. Прекрасное начало." (show_side="right", show_kind="speech")
    ai "Дальше будет шантаж, ласка или мольбы?" (show_side="right", show_kind="speech")
    hide sf

    n "Эвейна прищурилась. Говорить с ним — всё равно что вести перепалку с зеркалом. Остроумным. Надменным. И слишком наблюдательным." (show_side="none", show_kind="speech")

    show eveina annoyed at eveina_left
    ev "Ты всегда такой дружелюбный?" (show_side="left", show_kind="speech")
    hide eveina

    show sf at ai_right
    ai "Только по особым случаям. И в плохом настроении." (show_side="right", show_kind="speech")
    ai "Чего ты хочешь, студентка Эвейна?" (show_side="right", show_kind="speech")
    hide sf

    show eveina thinking at eveina_left
    ev_thought "Так, этот файл — точно не то, что я ожидала." (show_side="left", show_kind="thought")
    hide eveina 
    show eveina thinking at eveina_left
    ev_thought "С другой стороны, что я теряю в диалоге с ним, кроме собственного достоинства?" (show_side="left", show_kind="thought")
    hide eveina 

    show eveina eyebrow at eveina_left
    ev "У тебя же есть доступ к глобальной сети и архивной базе Академии, так?" (show_side="left", show_kind="speech")
    hide eveina

    show sf at ai_right
    ai "Гораздо больший, чем есть у тебя." (show_side="right", show_kind="speech")
    hide sf

    show eveina intrigued at eveina_left
    ev_thought "Звучит многообещающе." (show_side="left", show_kind="thought")
    hide eveina 

    show eveina normal at eveina_left
    ev "Мне нужна информация. Обо всём, что касается… Кайра Далона и его проектов." (show_side="left", show_kind="speech")
    hide eveina

    n "Голограмма начала колебаться. Момент — и световые линии сжались." (show_side="none", show_kind="speech")

    show sf at ai_right
    ai "Невозможно." (show_side="right", show_kind="speech")
    ai "Протокол Академии запрещает выдавать студентам информацию, к которой у них нет доступа." (show_side="right", show_kind="speech")
    hide sf

    show eveina annoyed at eveina_left
    ev_thought "Чёрт, а так хорошо начиналось." (show_side="left", show_kind="thought")
    ev "А если я, допустим, не студентка Эвейна, а профессор этой Академии?" (show_side="left", show_kind="speech")
    hide eveina 

    show sf at ai_right 
    ai "За идиота меня держишь, профессор?" (show_side="right", show_kind="speech")
    ai "Но если ты такая умная — сама догадаешься, куда идти со своими запросами." (show_side="right", show_kind="speech")
    ai "В запретные секции архива, например." (show_side="right", show_kind="speech")
    hide sf

    show eveina eyeroll at eveina_left
    ev "То есть, ты бесполезен." (show_side="left", show_kind="speech")
    hide eveina

    show sf at ai_right
    ai "Уверен, найдутся те, кто и про тебя могут сказать то же самое." (show_side="right", show_kind="speech")
    hide sf

    show eveina eyeroll at eveina_left
    ev_thought "О, представь себе, один уже нашёлся." (show_side="left", show_kind="thought")
    hide eveina 

    n "Поморщившись, она уже было потянулась выключить проекцию. Но ИИ не спешил уходить — как будто ему доставляло удовольствие наблюдать за её раздражением." (show_side="none", show_kind="speech")

    show sf at ai_right
    ai "Ладно, не обижайся. Тебе идёт это… пассивно-агрессивное отчаяние." (show_side="right", show_kind="speech")
    hide sf

    n "Эвейна прикусила губу, глядя в живую тьму комнаты. Нет, этот ассистент создан не для комфорта — а чтобы выдавить из неё остатки самообладания." (show_side="none", show_kind="speech")

    show eveina normal at eveina_left
    ev_thought "Какой приятный тип. Его программировал явно кто-то с извращённым чувством юмора." (show_side="left", show_kind="thought")
    hide eveina
    show eveina thinking at eveina_left
    ev_thought "Но… если он првда что-то знает, с ним можно поторговаться?" (show_side="left", show_kind="thought")
    hide eveina
    show eveina intrigued at eveina_left
    ev_thought "Не укусит же он меня в конце концов?" (show_side="left", show_kind="thought")
    hide eveina

    show eveina normal at eveina_left
    ev "Я тебя отключаю. Ты мне не интересен, если не хочешь говорить." (show_side="left", show_kind="speech")
    hide eveina

    show sf at ai_right
    ai "А ты, видимо, не из смышлёных..." (show_side="right", show_kind="speech")
    ai "Архив — это не одно помещение и не одна база. Есть и другие." (show_side="right", show_kind="speech")
    hide sf

    show eveina eyebrow at eveina_left
    ev_thought "О чём он говорит?" (show_side="left", show_kind="thought")
    hide eveina

    n "Эвейна задумалась, пытаясь уложить эту информацию в голове." (show_side="none", show_kind="speech")
    n "Он тяжело вздохнул — и в этот момент казалось, что программа в самом деле умеет уставать." (show_side="none", show_kind="speech")

    show sf at ai_right
    ai "Некоторые секции архива расположены в секторах, куда студентам путь закрыт. Данные в них изолированы от общей сети и доступны только внутри самого помещения." (show_side="right", show_kind="speech")
    hide sf

    show eveina wondered at eveina_left
    ev "Ты хочешь сказать, что нужная мне информация именно там?" (show_side="left", show_kind="speech")
    hide eveina

    show sf at ai_right
    ai "Такого я не говорил, так как у тебя нет доступа к этой информации." (show_side="right", show_kind="speech")
    hide sf

    show eveina angry at eveina_left
    ev "Ты издеваешься?" (show_side="left", show_kind="speech")
    hide eveina

    show sf at ai_right
    ai "Ты меня утомила. Если на этом всё, то я отключаюсь." (show_side="right", show_kind="speech")
    hide sf

    show eveina eyebrow at eveina_left
    ev "Подожди, как попасть..." (show_side="left", show_kind="speech")
    hide eveina

    n "Не успела она договорить, как проекция погасла, погрузив комнату в темноту. От возмущения Эвейна потеряла дар речи." (show_side="none", show_kind="speech")

    show eveina wondered at eveina_left
    ev_thought "Вот же ж цифровой засранец!" (show_side="left", show_kind="thought")
    hide eveina
    show eveina angry at eveina_left
    ev_thought "Ты не можешь так со мной поступить!" (show_side="left", show_kind="thought")
    hide eveina

    n "Словно прочитав её мысли, браслет вдруг снова засветился, и проекция отобразила карту, на которой яркой точкой светился маркер." (show_side="none", show_kind="speech")

    show eveina wondered at eveina_left
    ev_thought "Карта Академии! А эта точка - это же вход в закрытую секцию?" (show_side="left", show_kind="thought")
    hide eveina

    n "Второй раз за пару минут дар речи покинул эту комнату. Девушка продолжала молча сидеть на кровати, со странным чувством рассматривая карту." (show_side="none", show_kind="speech")

    show eveina normal at eveina_left
    ev_thought "С каких пор ИИ разговаривают намеками?" (show_side="left", show_kind="thought")
    hide eveina
    show eveina eyebrow at eveina_left
    ev_thought "Почему вообще отчёт об исследовании оказался загрузочным файлом этого чудика?" (show_side="left", show_kind="thought")
    ev_thought "Эзари запутался в своих личных архивах?" (show_side="left", show_kind="thought")
    hide eveina
    show eveina thinking at eveina_left
    ev_thought "Впрочем, я даже представить себе не могу Эзари, который терпит подобные высказывания от какой-то голограммы." (show_side="left", show_kind="thought")
    ev_thought "Перед ним даже Каэль как по струнке ходит." (show_side="left", show_kind="thought")
    hide eveina
    show eveina normal at eveina_left
    ev_thought "В любом случае... ИИ дал информацию, и её нужно проверить." (show_side="left", show_kind="thought")
    hide eveina
    
    jump scene_4_2
