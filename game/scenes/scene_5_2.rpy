label scene_5_2:
    $ previous_scene = "scene_5_1"
    $ next_scene = "scene_5_3"
    $ current_scene = "scene_5_2"
    call fade_to_black(1.2, 0.8)
    scene bg eveina_room at bg_fullscreen with dissolve

    n "Утро наступило, как ни странно, мягко. Никаких липких снов, никакого проглатывающего внутренности тумана в груди." (show_side="none", show_kind="speech")
    n "В комнате было пусто — Лея ушла, оставив сообщение: «{i}Защита проекта по микрофлоре. На практике не жди.{/i}»" (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev_thought "Минус сосед. Ладно, посмотрим, кто сегодня попадётся в напарники. Только бы не кто-то из… этих." (show_side="left", show_kind="thought")
    hide eveina
    
    scene bg surgery_lab at bg_fullscreen with dissolve

    n "Лаборатория нейрохирургии встретила её стерильной прохладой и мягким белым светом. Органическая поверхность столов слегка пульсировала в такт ритму здания." (show_side="none", show_kind="speech")
    n "Студенты уже собирались — кто с нетерпением, кто с опасением. На кафедре — профессор Раукт, железная женщина с идеальной памятью и голосом, от которого учащались сердечные сокращения даже у самых уверенных студентов." (show_side="none", show_kind="speech")

    show serena normal at serena_right
    sr "Я распределила вас на пары. Возражения не принимаются." (show_side="right", show_kind="speech")
    sr "Материал у всех один. Вопросы — после работы. Если ваш желудок не вывернется на изнанку до этого момента." (show_side="right", show_kind="speech")
    hide serena 

    n "Она щёлкнула пальцами, и из-за кафедры к каждому столу выкатились контейнеры." (show_side="none", show_kind="speech")
    n "Внутри — светло-серые полушария с хрупкой пульсирующей сеткой по поверхности. Искусственно выращенный человеческий мозг." (show_side="none", show_kind="speech")

    show student smile at student_right
    st "Ну, наконец-то, настоящая Академия." (show_side="right", show_kind="speech")
    hide student

    show student pafos at student_right
    st "Держу пари, если его уронить, то в этом контейнере окажется твой мозг." (show_side="right", show_kind="speech")
    hide student

    n "Эвейна огляделась. Леи не было — и в паре с ней оказался Теро. Он кивнул ей с лёгкой улыбкой." (show_side="none", show_kind="speech")

    show tero smile at tero_right
    te "Похоже, ты теперь мой проводник в этот прекрасный мир серого вещества." (show_side="right", show_kind="speech")
    hide tero

    n "Они начали с осторожной пальпации, не притрагиваясь к хирургическим инструментам." (show_side="none", show_kind="speech")
    n "Теро оказался на удивление ловким, несмотря на его жалобы, что не понимает, как до этого докатился." (show_side="none", show_kind="speech")
    n "Он подставлял под сканнер в руках девушки очередной отдел мозга, Эвейна делала снимки и заносила их в отчёт." (show_side="none", show_kind="speech")
    n "Закончив с внешним осмотром, Теро вернул серую массу на стол и протянул напарнице скальпель." (show_side="none", show_kind="speech")

    show tero normal at tero_right
    te "Я слышал, ты решила Задачу Идентики. Это правда?" (show_side="right", show_kind="speech")
    hide tero

    n "Не отрывая взгляда от серой массы, девушка слегка улыбнулась." (show_side="none", show_kind="speech")

    show eveina normal at eveina_left
    ev "О полноценном решении рассуждать рано, но, говорят, что у моего подхода большой потенциал." (show_side="left", show_kind="speech")
    ev "Впрочем, думаю, мне повезло." (show_side="left", show_kind="speech")
    hide eveina
    show eveina thinking at eveina_left
    ev "Я ведь не знала, что она нерешаемая." (show_side="left", show_kind="speech")
    hide eveina

    n "Теро перевёл взгляд на неё с удивлением и настоящим уважением. А затем сделал аккуратный надрез вдоль полушарий." (show_side="none", show_kind="speech")

    show tero normal at tero_right
    te "Повезло?" (show_side="right", show_kind="speech")
    te "Ты решила задачу, над которой триста лет бьются." (show_side="right", show_kind="speech")
    hide tero
    show tero smile at tero_right
    te "Это не просто везение. Это… чертовски круто." (show_side="right", show_kind="speech")
    hide tero

    n "Эвейна чуть опустила глаза, в груди смешался клубок эмоций." (show_side="none", show_kind="speech")
    n "Радость от признания, смущение от столь искренней похвалы, осторожность по отношению к чужакам." (show_side="none", show_kind="speech")
    n "От своих сверстников ей куда привычнее было слышать насмешки и издёвки, поэтому Эвейна не сразу поняла, как ей реагировать." (show_side="none", show_kind="speech")

    show eveina normal at eveina_left
    ev "Спасибо. Но это всего лишь одна задача. Впереди — ещё тысячи." (show_side="left", show_kind="speech")
    hide eveina

    show tero normal at tero_right
    te "Мне бы твой взгляд на вещи. Может, тогда бы я не вскрывал мозги, а играл на каком-нибудь инструменте сейчас." (show_side="right", show_kind="speech")
    hide tero

    n "Он обвёл недовольным взглядом лабораторию." (show_side="none", show_kind="speech")

    show tero sad at tero_right
    te "Я ведь это не выбирал. Отец отправил меня сюда." (show_side="right", show_kind="speech")
    te "Сказал, что мне надо «научиться быть мужчиной», а не музыкой страдать." (show_side="right", show_kind="speech")
    hide tero

    n "Парень говорил легко, без трагичности. Но в глазах сквозила затаённая обида." (show_side="none", show_kind="speech")

    show eveina eyebrow at eveina_left
    ev "А если бы не отец? Что бы ты выбрал?" (show_side="left", show_kind="speech")
    hide eveina

    n "Теро задержал дыхание, будто на миг задумался, можно ли говорить это вслух. Потом медленно, почти шепотом произнес." (show_side="none", show_kind="speech")

    show tero smile at tero_right
    te "Я бы ушёл в звук." (show_side="right", show_kind="speech")
    te "Не в музыку — в сам звук." (show_side="right", show_kind="speech")
    te "Собирать шум, разбирать его на тоны. Искать в какофонии закономерности." (show_side="right", show_kind="speech")
    te "Делать это своим смыслом." (show_side="right", show_kind="speech")
    hide tero

    n "Он чуть улыбнулся — грустно, как будто эта мечта где-то рядом, но за стеклом." (show_side="none", show_kind="speech")

    show eveina eyebrow at eveina_left
    ev "Так иди. Кто тебе мешает?" (show_side="left", show_kind="speech")
    hide eveina

    n "Она не сказала это резко — наоборот, в голосе была почти осторожная поддержка." (show_side="none", show_kind="speech")
    n "Теро внимательно взглянул на неё." (show_side="none", show_kind="speech")

    show tero normal at tero_right
    te "Я. Я себе мешаю. Ну или точнее, мой страх." (show_side="right", show_kind="speech")
    te "Он универсален. Замечала, что у каждого он звучит по-своему?" (show_side="right", show_kind="speech")
    hide tero
    show tero sad at tero_right
    te "У меня — как голос отца, который говорит, что всё это чепуха." (show_side="right", show_kind="speech")
    te "Что я должен быть сильным. Рациональным. Как он." (show_side="right", show_kind="speech")
    hide tero

    n "Он замолчал. Пинцет в его руке чуть дрожал. Эвейна молча кивнула. Как будто его слова сказали ей что-то важное и о ней самой." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev_thought "Как странно — встретить человека, который боится не меньше, чем ты. Но не прячется." (show_side="left", show_kind="thought")
    hide eveina

    n "Некоторое время они усердно работали, кромсая мозги." (show_side="none", show_kind="speech")
    n "Но потом, почти не поднимая глаз, Эвейна осторожно бросила:" (show_side="none", show_kind="speech")

    show eveina eyebrow at eveina_left
    ev "Ты что-нибудь слышал о лекарстве… которое лечит дегенеративные заболевания мозга?" (show_side="left", show_kind="speech")
    hide eveina

    n "Рука парня слегка дрогнула от неожиданности. Он посмотрел на неё внимательнее." (show_side="none", show_kind="speech")

    show tero normal at tero_right
    te "Не знал, что о нём знают «не свои»." (show_side="right", show_kind="speech")
    te "Не то, чтобы я считал тебя чужой, но мой отец бы точно выразился именно так." (show_side="right", show_kind="speech")
    hide tero

    n "Эвейна выжидающе смотрела на него, пока он не продолжил." (show_side="none", show_kind="speech")

    show tero normal at tero_right
    te "Слышал, да. Отец говорил об этом. Вроде бы это не просто лекарство, что-то там было про терапию..." (show_side="right", show_kind="speech")
    te "Но тема закрытая. Лучше не суйся. Мало ли, кому-то могут не понравится твои вопросы." (show_side="right", show_kind="speech")
    hide tero

    n "Эвейна небрежно кивнула, словно речь шла не о самой ценной в мире информации." (show_side="none", show_kind="speech")

    show eveina normal at eveina_left
    ev "Поняла." (show_side="left", show_kind="speech")
    hide eveina

    show eveina thinking at eveina_left
    ev_thought "Его отец говорил об этом. Значит, лекарство реально существует и работает." (show_side="left", show_kind="thought")
    ev_thought "Его знают в кругу элиты — обсуждают, передают информацию друг другу." (show_side="left", show_kind="thought")
    ev_thought "Но за пределы этого круга оно не уходит." (show_side="left", show_kind="thought")
    hide eveina
    show eveina normal at eveina_left
    ev_thought "Они умышленно скрывают его. Даже от собственных детей." (show_side="left", show_kind="thought")
    ev_thought "Значит, оно либо опасно, либо не предназначено для всех." (show_side="left", show_kind="thought")
    ev_thought "Ограничения в производстве? Слишком высокая цена?" (show_side="left", show_kind="thought")
    hide eveina
    show eveina eyebrow at eveina_left
    ev_thought "Или... может, оно просто слишком эффективно для массового применения?" (show_side="left", show_kind="thought")
    ev_thought "Может, фармакомпаниям не выгодно его производить?" (show_side="left", show_kind="thought")
    hide eveina

    n "Они закончили работу молча. Когда всё было сделано, Эвейна аккуратно взяла контейнер с остатками серой массы, подошла к мусорному баку и высыпала их туда." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev_thought "Извините. Вы не виноваты, что стали частью этого курса." (show_side="left", show_kind="thought")
    hide eveina

    n "Она сняла перчатки, бросила их следом, повернулась и пошла прочь." (show_side="none", show_kind="speech")

    show eveina eyeroll at eveina_left
    ev_thought "Файл сам себя не расшифрует." (show_side="left", show_kind="thought")
    hide eveina

    n "Архив ждал." (show_side="none", show_kind="speech")

    jump scene_5_3
