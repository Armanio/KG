label scene_1_1:

    $ previous_scene = "prolog"
    $ next_scene = "scene_1_2"
    $ current_scene = "scene_1_1"
    $ kg_prepare_scene("scene_1_1")

    # =========================================================
    # СЦЕНА 1 — «ШАТТЛ»
    # Функция: установить дедлайн, показать план Эвейны
    # и привести её к первой цели — закрепиться на кафедре.
    # =========================================================

    scene bg scene 1_1 shuttle 1 at bg_fullscreen with dissolve

    n "Эвейна взглянула на часы и выпрямилась в кресле, разминая затёкшие плечи." (show_side="none", show_kind="speech")

    ev_thought "Двести тридцать один день." (show_side="left", show_kind="thought")

    n "Именно столько оставалось до точки невозврата по расчётам доктора Нэла." (show_side="none", show_kind="speech")

    ev_thought "Если он не ошибся." (show_side="left", show_kind="thought")
    ev_thought "А если ошибся, лучше мне об этом пока не знать." (show_side="left", show_kind="thought")

    n "Шаттл качнуло и прозрачная панель едва заметно завибрировала." (show_side="none", show_kind="speech")

    scene bg scene 1_1 shuttle 2 at bg_fullscreen with dissolve
    pause (1.0)

    n "За окном простиралась планета Иннаки: вода до самого горизонта и один клочок суши посреди неё." (show_side="none", show_kind="speech")

    ev_thought "Одна из лучших академий галактики — на островке, который с орбиты можно принять за грязь на стекле." (show_side="left", show_kind="thought")
    ev_thought "Обнадёживает." (show_side="left", show_kind="thought")

    scene bg scene 1_1 shuttle 3 at bg_fullscreen with dissolve

    n "Шаттл шёл на снижение. На острове проступили здания Академии, сады и узкая тёмная полоса леса." (show_side="none", show_kind="speech")
    n "Эвейна отвела взгляд от окна и подняла руку." (show_side="none", show_kind="speech")

    scene bg scene 1_1 shuttle 6 at bg_fullscreen with dissolve
    pause (0.5)

    n "Над браслетом развернулся список, который она дополняла последние несколько месяцев." (show_side="none", show_kind="speech")

    n "{i}{s}Открытые медицинские базы — проверены.{/s}\n{s}Запросы в исследовательские центры — отклонены.{/s}\n{s}Доступные фармацевтические программы — подходящих нет.{/s}{/i}" (show_side="none", show_kind="speech")

    n "Ниже оставалась незакрытая строка." (show_side="none", show_kind="speech")

    n "{i}Получить приглашение Академии Мемории.{/i}" (show_side="none", show_kind="speech")

    n "Эвейна коснулась её. Рядом загорелась отметка о выполнении." (show_side="none", show_kind="speech")

    ev_thought "Готово." (show_side="left", show_kind="thought")

    n "Следующий пункт тут же поднялся выше." (show_side="none", show_kind="speech")

    n "{i}Получить доступ к внутренней базе исследований Академии.{/i}" (show_side="none", show_kind="speech")

    n "Эвейна нажала на строку. Проекция показала два условия доступа: внутренняя специализация и согласие наставника." (show_side="none", show_kind="speech")

    ev_thought "Разумеется, просто постучать в дверь недостаточно." (show_side="left", show_kind="thought")
    ev_thought "Нужно ещё убедить их, что меня можно пустить внутрь." (show_side="left", show_kind="thought")

    n "Она добавила промежуточный пункт." (show_side="none", show_kind="speech")

    n "{i}Закрепиться на кафедре нейропротокольной терапии.{/i}" (show_side="none", show_kind="speech")

    ev_thought "С этого и начнём." (show_side="left", show_kind="thought")

    n "План выглядел вполне выполнимым. Реальность пока не успела высказать возражения." (show_side="none", show_kind="speech")

    n "Эвейна погасила проекцию. Под ней лежала потрёпанная обложка «Дневников Эдварда Пирса»." (show_side="none", show_kind="speech")

    scene bg scene 1_1 shuttle 5 at bg_fullscreen with dissolve
    pause(1.0)

    n "Книгу подарил отец — единственную бумажную книгу, которую она когда-либо держала в руках." (show_side="none", show_kind="speech")
    n "За годы страницы потемнели на сгибах, а несколько уголков так и остались загнутыми, несмотря на все попытки их расправить." (show_side="none", show_kind="speech")

    ev_thought "Ну что, капитан? Открытые маршруты закончились." (show_side="left", show_kind="thought")

    n "Пальцы сами раскрыли книгу на знакомой странице." (show_side="none", show_kind="speech")

    scene bg scene 1_1 shuttle 7 at bg_fullscreen with dissolve
    pause(1.0)

    n "Между страницами лежала фотография, которую Эвейна использовала вместо закладки." (show_side="none", show_kind="speech")
    n "Снимку было около года. Они с отцом стояли рядом, но оба смотрели мимо камеры: Риан — на неё, она — вообще куда-то в сторону." (show_side="none", show_kind="speech")

    ev_thought "Семейные фотографии нам определённо не давались." (show_side="left", show_kind="thought")

    n "Она задержала взгляд на фото ещё на несколько секунд, затем вернула его на место и пробежала глазами по странице." (show_side="none", show_kind="speech")

    ev_thought "«Даже самые великие открытия часто выглядят разочаровывающе с орбиты»." (show_side="left", show_kind="thought")

    ev_thought "Твои слова, капитан. И весьма подходящие для описания этого пейзажа." (show_side="left", show_kind="thought")
    ev_thought "Что ж, надеюсь, внутри я найду то, зачем прилетела." (show_side="left", show_kind="thought")

    n "В своих дневниках капитан Эдвард Пирс упорно продолжал путь после того, как остальные уже принимались подсчитывать потери. Возможно, поэтому в девять лет Эвейна решила, что влюблена в него." (show_side="none", show_kind="speech")

    ev_thought "Прекрасный выбор для первой любви: взрослый мужик без царя в голове и с хронической неспособностью вовремя остановиться." (show_side="left", show_kind="thought")
    ev_thought "Пап, ты сам сформировал мои предпочтения. Теперь не жалуйся." (show_side="left", show_kind="thought")

    n "Палец задержался на потертом уголке страницы, когда Эвейна задумалась об отце." (show_side="none", show_kind="speech")

    # =========================================================
    # ФЛЕШБЭК — РАЗГОВОР С ОТЦОМ
    # =========================================================

    call fade_to_black(0.8, 0.5)
    scene bg home_dining_room at bg_fullscreen with dissolve

    n "Они завтракали вместе, как каждую субботу." (show_side="none", show_kind="speech")

    show rian normal at rian_right
    ri "Есть планы на выходные?" (show_side="right", show_kind="speech")
    hide rian

    show eveina smile tshirt at eveina_left
    ev "Конечно. Напиться, станцевать на стойке и залететь от незнакомца с красивой улыбкой." (show_side="left", show_kind="speech")
    hide eveina

    show eveina thinking tshirt at eveina_left
    ev "Или как там принято проводить выходные?" (show_side="left", show_kind="speech")
    hide eveina

    show rian smile at rian_right
    ri "Весьма продуктивно." (show_side="right", show_kind="speech")
    hide rian

    show rian normal at rian_right
    ri "А внука оставишь мне? Возможно, со второй попытки получится воспитать приличного человека." (show_side="right", show_kind="speech")
    hide rian

    show eveina annoyed tshirt at eveina_left
    ev "Эй!" (show_side="left", show_kind="speech")
    hide eveina

    n "Браслет завибрировал, отвлекая её от перебранки. Над столом раскрылось входящее сообщение." (show_side="none", show_kind="speech")

    scene bg scene 1_1 dinning_room 1 at bg_fullscreen with dissolve

    ev "Пап, кажется, внук откладывается." (show_side="left", show_kind="speech")

    n "Улыбка Риана медленно сползла с лица." (show_side="none", show_kind="speech")

    scene bg home_dining_room  at bg_fullscreen with dissolve

    show rian sad at rian_right
    ri "Ты всё-таки отправила заявку." (show_side="right", show_kind="speech")
    hide rian

    show eveina eyebrow tshirt at eveina_left
    ev "Я предупреждала." (show_side="left", show_kind="speech")
    hide eveina

    show rian sad at rian_right
    ri "А я надеялся, что ты передумаешь." (show_side="right", show_kind="speech")
    hide rian

    show eveina annoyed tshirt at eveina_left
    ev "Почему?" (show_side="left", show_kind="speech")
    hide eveina

    show rian thinking at rian_right
    ri "Иннаки далеко. Связь с внешним миром ограничена. Мы почти ничего не знаем о том, что происходит в этой Академии." (show_side="right", show_kind="speech")
    hide rian

    show eveina normal tshirt at eveina_left
    ev "Зато я знаю, чем собираюсь там заниматься." (show_side="left", show_kind="speech")
    hide eveina

    show rian worried at rian_right
    ri "Эвейна..." (show_side="right", show_kind="speech")
    hide rian

    show eveina annoyed tshirt at eveina_left
    ev "Я не прошу разрешения." (show_side="left", show_kind="speech")
    hide eveina

    show rian sad at rian_right
    ri "Знаю." (show_side="right", show_kind="speech")
    hide rian

    n "Он потянулся к чашке, но пальцы дрогнули. Риан убрал руку под стол." (show_side="none", show_kind="speech")

    show rian sad at rian_right
    ri "Лишь спрашиваю, действительно ли ты этого хочешь?" (show_side="right", show_kind="speech")
    hide rian

    show eveina normal tshirt at eveina_left
    ev "Да, хочу." (show_side="left", show_kind="speech")
    hide eveina

    n "Ответ прозвучал слишком поспешно, будто был заучен наизусть. Внимательный взгляд отца скользнул по ней. Но спорить он не стал." (show_side="none", show_kind="speech")

    # =========================================================
    # ВОЗВРАЩЕНИЕ В ШАТТЛ
    # =========================================================

    call fade_to_black(0.8, 0.5)
    scene bg scene 1_1 shuttle 5 at bg_fullscreen with dissolve

    n "Эвейна закрыла книгу." (show_side="none", show_kind="speech")

    ev_thought "Не хочу." (show_side="left", show_kind="thought")
    ev_thought "Так нужно." (show_side="left", show_kind="thought")

    scene bg scene 1_1 shuttle 4 at bg_fullscreen with dissolve
    pause (0.5)

    n "Шаттл заложил плавный поворот вокруг главного здания." (show_side="none", show_kind="speech")
    n "За мгновение до того, как белая стена ушла в сторону, Эвейна почему-то зажмурилась." (show_side="none", show_kind="speech")
    n "Через мгновение солнечный отблеск от озера ударил в стеклянную панель." (show_side="none", show_kind="speech")
    n "Она медленно открыла глаза. За белой стеной Академии показались дикий сад и вода." (show_side="none", show_kind="speech")

    ev_thought "Я знала, что это произойдёт. Видела в буклете?" (show_side="left", show_kind="thought")

    n "Эвейна посмотрела на отражение в стекле." (show_side="none", show_kind="speech")

    ev_thought "Вряд ли. Скорее, в рекламном ролике." (show_side="left", show_kind="thought")

    scene bg shuttle at bg_fullscreen with dissolve

    n "Безликий женский голос бесцеремонно оборвал эту мысль." (show_side="none", show_kind="speech")

    show ai at ai_right
    ai "Посадка через четыре минуты. Все жизненные параметры — в пределах нормы." (show_side="right", show_kind="speech")
    hide ai

    show eveina eyeroll at eveina_left, sprite_warm
    ev_thought "А вот эмоциональные, дорогая моя, в пределы уже не вписываются." (show_side="left", show_kind="thought")
    hide eveina

    n "Эвейна снова открыла список и выделила ближайшую задачу." (show_side="none", show_kind="speech")
    n "{i}Закрепиться на кафедре нейропротокольной терапии.{/i}" (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left, sprite_warm
    ev_thought "Сначала собеседование и разговор с наставником." (show_side="left", show_kind="thought")
    hide eveina
    show eveina normal at eveina_left, sprite_warm
    ev_thought "Потом база." (show_side="left", show_kind="thought")
    hide eveina

    n "Она погасила проекцию и убрала книгу в сумку." (show_side="none", show_kind="speech")
    n "Шаттл коснулся посадочной площадки." (show_side="none", show_kind="speech")

    show eveina normal at eveina_left, sprite_warm
    ev_thought "Что ж... Здравствуй, планета Иннаки." (show_side="left", show_kind="thought")
    hide eveina
    show eveina intrigued at eveina_left, sprite_warm
    ev_thought "Давай не разочаруем друг друга?" (show_side="left", show_kind="thought")
    hide eveina

    jump scene_1_2 
