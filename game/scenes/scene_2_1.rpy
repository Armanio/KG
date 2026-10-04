label scene_2_1:
    $ previous_scene = "scene_1_6"
    $ next_scene = "scene_2_2"
    $ current_scene = "scene_2_1"
    $ kg_prepare_scene("scene_2_1")

    # =========================================================
    # ОТКРЫТИЕ ГЛАВЫ 2
    # После провала памяти Эвейна пересматривает сохранённую
    # запись отца и решает начать поиск внутренних исследований.
    # =========================================================

    scene bg room day at bg_fullscreen with dissolve
    # play music "bgm/morning_mist.ogg" fadein 2.0

    n "Рассвет пришёл не как облегчение. Как приговор. Наступило утро, но ничего не изменилось." (show_side="none", show_kind="speech")
    n "За остаток ночи Эвейна так и не сомкнула глаз. Стоило начать засыпать, как кровать исчезала из-под спины, а тело дёргалось, спасаясь от падения, которого не было." (show_side="none", show_kind="speech")
    n "Если бы кто-то спросил, чего она ожидала от первого дня в Академии..." (show_side="none", show_kind="speech")

    show eveina upset thinking tshirt at eveina_left
    ev_thought "Получить доступы к внутренним исследованиям?" (show_side="left", show_kind="thought")
    hide eveina
    show eveina thinking tshirt at eveina_left
    ev_thought "Логично." (show_side="left", show_kind="thought")
    hide eveina

    show eveina eyebrow tshirt at eveina_left
    ev_thought "Познакомиться с интересными людьми?" (show_side="left", show_kind="thought")
    hide eveina
    show eveina eyeroll tshirt at eveina_left
    ev_thought "Допустим." (show_side="left", show_kind="thought")
    hide eveina

    show eveina upset thinking tshirt at eveina_left
    ev_thought "Проснуться в мокрой траве с синяком на запястье?" (show_side="left", show_kind="thought")
    hide eveina

    n "Она снова сжала запястье. Под пальцами отозвалась тупая боль." (show_side="none", show_kind="speech")

    show eveina annoyed tshirt at eveina_left
    ev_thought "Несколько часов не могут просто исчезнуть." (show_side="left", show_kind="thought")
    hide eveina

    n "Могли." (show_side="none", show_kind="speech")
    n "Эвейна слишком хорошо знала, что память не обязана спрашивать разрешения." (show_side="none", show_kind="speech")
    n "На соседней кровати уже сидела Лея. В ушах у неё были наушники, взгляд был прикован к планшету." (show_side="none", show_kind="speech")
    n "Эвейна открыла меню браслета. После этой ночи хотелось услышать отца." (show_side="none", show_kind="speech")
    n "Не объяснять ему про сад. Просто услышать, как он назовёт её малышом." (show_side="none", show_kind="speech")
    n "Она перешла к сохранённым записям. Нужное видео было закреплено наверху." (show_side="none", show_kind="speech")

    show eveina upset thinking tshirt at eveina_left
    ev_thought "Только один раз." (show_side="left", show_kind="thought")
    hide eveina

    n "Девушка повторяла это как отговорку каждый раз." (show_side="none", show_kind="speech")
    n "А потом неизменно нажимала кнопку Старт." (show_side="none", show_kind="speech")

    scene bg room hospital room at bg_fullscreen with dissolve

    n "Отец сидел слишком близко к камере. Первые несколько секунд он молча смотрел в экран, словно ждал, что она заговорит первой." (show_side="none", show_kind="speech")

    show rian normal at rian_right
    ri "Привет, малыш." (show_side="right", show_kind="speech")
    hide rian

    n "Он замолчал, потом вдруг широко улыбнулся." (show_side="none", show_kind="speech")

    show rian smile at rian_right
    ri "Так давно тебя не видел. Очень соскучился." (show_side="right", show_kind="speech")
    hide rian

    show eveina upset thinking at eveina_left
    ev_thought "Мы ж тогда разговаривали накануне, пап." (show_side="left", show_kind="thought")
    hide eveina

    show rian normal at rian_right
    ri "Мари принесла грибы в сырном соусе." (show_side="right", show_kind="speech")
    ri "Твои любимые." (show_side="right", show_kind="speech")
    hide rian

    show eveina upset thinking at eveina_left
    ev_thought "Не мои, пап. Твои." (show_side="left", show_kind="thought")
    hide eveina

    show rian smile at rian_right
    ri "Я оставил тебе половину на кухне." (show_side="right", show_kind="speech")
    hide rian

    n "Отец уверенно кивнул, будто действительно видел перед собой знакомую кухню, а не больничную палату." (show_side="none", show_kind="speech")
    n "Потом его взгляд ушёл куда-то в сторону." (show_side="none", show_kind="speech")

    show rian thinking at rian_right
    ri "Что-то я забыл, что ещё хотел..." (show_side="right", show_kind="speech")
    hide rian

    n "Он нахмурился и потёр ладонью висок." (show_side="none", show_kind="speech")

    show rian worried at rian_right
    ri "Подожди секунду." (show_side="right", show_kind="speech")
    hide rian

    n "Мужчина поднялся и вышел из кадра. Запись продолжалась. Эвейна смотрела на пустое кресло, край незаправленной постели и полоску света на стене." (show_side="none", show_kind="speech")
    n "Отец не вернулся." (show_side="none", show_kind="speech")
    n "Через минуту видео оборвалось." (show_side="none", show_kind="speech")

    scene bg room day at bg_fullscreen with dissolve

    n "Девушка провела пальцем по браслету и вернула запись в список сохранённых." (show_side="none", show_kind="speech")

    show eveina worried tshirt at eveina_left
    ev_thought "Когда-то ты хотя бы присылал сообщения." (show_side="left", show_kind="thought")
    hide eveina

    n "После госпитализации разговоры становились всё короче. Отец путался, раздражался и всё чаще отключался раньше, чем она успевала понять, узнал ли он её." (show_side="none", show_kind="speech")
    n "Записи давались ему легче. Он отправлял их, когда хотел поговорить, но не мог выдержать её ответ." (show_side="none", show_kind="speech")
    n "Потом они стали приходить реже." (show_side="none", show_kind="speech")
    n "А затем перестали совсем." (show_side="none", show_kind="speech")

    show eveina upset tshirt at eveina_left
    ev_thought "Он всегда выглядел таким уязвимым и виноватым, когда терялся. Наверное, общение со мной давалось ему нелегко." (show_side="left", show_kind="thought")
    hide eveina

    n "За эту версию Эвейна держалась особенно крепко. Другие ей не нравились." (show_side="none", show_kind="speech")

    n "Палец снова лёг на значок воспроизведения." (show_side="none", show_kind="speech")
    n "Эвейна почти дотронулась, но вовремя остановила себя. Она уже знала, когда отец улыбнётся, что скажет и на какой секунде выйдет из кадра." (show_side="none", show_kind="speech")

    show eveina upset thinking tshirt at eveina_left
    ev_thought "Я бы сейчас всё тебе рассказала, пап." (show_side="left", show_kind="thought")
    hide eveina

    n "Девушка погасила проекцию." (show_side="none", show_kind="speech")

    show eveina thinking tshirt at eveina_left
    ev_thought "Ладно. Ты просил подождать." (show_side="left", show_kind="thought")
    ev_thought "Только сидеть и ждать я не умею." (show_side="left", show_kind="thought")
    hide eveina

    n "Эвейна поднялась с кровати и потянулась за одеждой." (show_side="none", show_kind="speech")


    jump scene_2_2
