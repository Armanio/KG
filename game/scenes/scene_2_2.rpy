label scene_2_2:
    $ previous_scene = "scene_2_1"
    $ next_scene = "scene_2_3"
    $ current_scene = "scene_2_2"
    $ kg_prepare_scene("scene_2_2")

    # =========================================================
    # СЦЕНА 2 — «ЗАВТРАК / ПРИЗНАНИЕ»
    # Структура: столовая → Эвейна рассказывает об отце
    #            → принимает помощь Леи → прозвище «Ви»
    #            → Ноа и Теро → уходит на лекцию
    # =========================================================

    call fade_to_black(1.2, 0.8)
    
    scene bg dinning room at bg_fullscreen with dissolve
    # play music "bgm/cafeteria.ogg" fadein 2.0

    n "Столовая была пропитана запахом специй и бодрым настроем. Эвейна сразу почувствовала себя не в своей тарелке." (show_side="none", show_kind="speech")
    #n "Эвейна шагнула внутрь — и почти сразу поймала чужой взгляд."
    #n "У стены, чуть в тени, стоял парень. Облокотившись, с видом человека, которому совершенно незачем здесь находиться, — и смотрел прямо на неё."
    n "Задумалась на секунду, а стоит ли завтрак того, чтобы находиться в этой обители оптимизма, но всё же шагнула внутрь." (show_side="none", show_kind="speech")

    show eveina annoyed at eveina_left
    ev_thought "Где-то здесь должна быть... а, вот и она." (show_side="left", show_kind="thought")
    hide eveina

    #n "Лея сидевшая за одним из столов, помахала рукой."

    n "Найдя соседку за одним из столов, Эвейна направилась прямо к нему." (show_side="none", show_kind="speech")

    scene bg scene 2_2 leya normal at bg_fullscreen with dissolve

    #show leya smile at leya_right
    le "Таким взглядом можно убивать, ты в курсе?" (show_side="right", show_kind="speech")
    #hide leya

    n "Ответом ей послужил лишь тихий стон." (show_side="none", show_kind="speech")

    scene bg scene 2_2 leya eyebrow

    #show leya eyebrow at leya_right
    le "Тяжёлое утро?" (show_side="right", show_kind="speech")
    #hide leya

    scene bg scene 2_2 eveina facepalm at bg_fullscreen with dissolve

    #show eveina eyeroll at eveina_left
    ev "Довольно точное описание." (show_side="left", show_kind="speech")
    #hide eveina

    n "Лея внимательно посмотрела на неё — но больше ничего не сказала. Просто подвинула тарелку." (show_side="none", show_kind="speech")
    n "Тишина держалась минуту. Может, две. Потом Лея неуверенно заговорила." (show_side="none", show_kind="speech")

    scene bg scene 2_2 dinning room 1 at bg_fullscreen with dissolve

    #show leya eyebrow at leya_right
    le "Я слышала сообщение утром..." (show_side="right", show_kind="speech")
    le "Это был твой отец?" (show_side="right", show_kind="speech")
    #hide leya

    #show eveina upset at eveina_left
    ev_thought "Ох... Это точно не то, что я хотела бы обсуждать." (show_side="left", show_kind="thought")
    #hide eveina

    #show leya eyebrow at leya_right
    le "Извини. Я не хотела подслушивать." (show_side="right", show_kind="speech")
    #hide leya

    scene bg scene 2_2 dinning room 2 at bg_fullscreen with dissolve

    #show eveina upset thinking at eveina_left
    ev "Это сохранённая запись." (show_side="left", show_kind="speech")
    ev "Мой отец болен. Дегенеративное расстройство памяти." (show_side="left", show_kind="speech")
    #hide eveina

    scene bg scene 2_2 dinning room 3 at bg_fullscreen with dissolve

    n "Лея не ответила. Только опустила взгляд в тарелку." (show_side="none", show_kind="speech")

    ev_thought "Сколько раз я ещё увижу подобную реакцию?" (show_side="left", show_kind="thought")
    ev_thought "Каждому в современном мире знаком этот диагноз. Каждый знает, что это приговор." (show_side="left", show_kind="thought")

    n "Эвейна задумчиво повертела в руке вилку, так и не притронувшись к салату." (show_side="none", show_kind="speech")
    n "Можно было остановиться. Сослаться на тяжёлое утро, сменить тему и больше к ней не возвращаться." (show_side="none", show_kind="speech")
    n "Но Лея не стала её утешать или обещать, что всё обязательно наладится. Просто ждала." (show_side="none", show_kind="speech")
    n "И Эвейне вдруг стало невыносимо, что для ещё одного человека отец уже успел превратиться в диагноз." (show_side="none", show_kind="speech")

    scene bg scene 2_2 eveina upset thinking at bg_fullscreen with dissolve

    ev "Он шестнадцать лет работал хирургом." (show_side="right", show_kind="speech")
    ev "Провёл тысячи операций. Многие его пациенты остались живы только благодаря ему." (show_side="right", show_kind="speech")

    n "Вилка замерла между её пальцами." (show_side="none", show_kind="speech")

    scene bg scene 2_2 dinning room 1 at bg_fullscreen with dissolve

    ev "После диагноза я написала всем, кого нашла в его рабочих контактах." (show_side="left", show_kind="speech")
    ev "Коллегам. Бывшим пациентам. Людям, которых он вытаскивал с операционного стола." (show_side="left", show_kind="speech")

    le "И никто не помог?" (show_side="right", show_kind="speech")

    scene bg scene 2_2 dinning room 2 at bg_fullscreen with dissolve

    ev "Помогли." (show_side="left", show_kind="speech")
    ev "Прислали номер городской клиники и пожелали держаться." (show_side="left", show_kind="speech")
    ev "Оказалось, у благодарности довольно короткий срок годности." (show_side="left", show_kind="speech")


    scene bg scene 2_2 dinning room 3 at bg_fullscreen with dissolve

    le "Он спасал этих людей, а когда помощь понадобилась ему, они просто..." (show_side="right", show_kind="speech")

    ev "Да." (show_side="left", show_kind="speech")

    scene bg scene 2_2 eveina upset thinking at bg_fullscreen with dissolve

    #show eveina upset thinking at eveina_left
    ev "Теперь он почти не выходит на связь. Разговоры даются ему слишком тяжело." (show_side="right", show_kind="speech")
    ev "А я продолжила искать. В конце концов всё привело меня в Академию." (show_side="right", show_kind="speech")
    ev "Вот только доступ к большей части исследований оказался закрыт для простых смертных." (show_side="right", show_kind="speech")
    ev "Поэтому я подала заявку на поступление." (show_side="right", show_kind="speech")

    scene bg scene 2_2 leya eyebrow at bg_fullscreen with dissolve

    le "То есть ты прошла несколько этапов экзаменов, собеседований и эссе — только чтобы получить доступ к базе исследований?" (show_side="right", show_kind="speech")
    le "Ви, у меня нет слов..." (show_side="right", show_kind="speech")


    scene bg scene 2_2 leya normal

    #show leya smile at leya_right
    le "Это что-то на грани отчаяния и гениальности." (show_side="right", show_kind="speech")
    #hide leya

    scene bg dinning room at bg_fullscreen with dissolve

    n "Эвейна взглянула на время и встала из-за стола. Лея последовала за ней." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev_thought "Ви. Вроде не раздражает. Пусть так." (show_side="left", show_kind="thought")
    hide eveina

    show eveina normal at eveina_left
    ev "Сегодня проверю, что открывает студенческий профиль." (show_side="left", show_kind="speech")
    ev "Нужно понять, насколько внутренняя база отличается от публичной." (show_side="left", show_kind="speech")
    hide eveina

    show leya normal at leya_right
    le "Я помогу." (show_side="right", show_kind="speech")
    hide leya
    show leya thinking at leya_right
    le "У сестры остались конспекты и знакомые в Академии. Спрошу у неё, где обычно ищут внутренние материалы." (show_side="right", show_kind="speech")
    hide leya

    show eveina thinking at eveina_left
    ev "Поспрашивай. Только без подробностей про отца." (show_side="left", show_kind="speech")
    hide eveina

    show leya normal at leya_right
    le "Конечно." (show_side="right", show_kind="speech")
    hide leya
    show leya thinking at leya_right
    le "И у студентов узнаю. Кто-то точно..." (show_side="right", show_kind="speech")
    hide leya

    n "Прежде чем она успела договорить, рядом материализовались двое." (show_side="none", show_kind="speech")

    show noa eyebrow at noa_right
    no "Кто-то точно что?" (show_side="right", show_kind="speech")
    hide noa

    show tero smile at tero_right
    unknown "Ноа, мы же делаем вид, что не подслушиваем!" (show_side="right", show_kind="speech")
    hide tero

    show noa intrigued at noa_right
    no "Ну а вдруг этот кто-то – я? Нельзя упускать такой шанс." (show_side="right", show_kind="speech")
    hide noa

    show leya eyeroll at leya_right
    le "Кто-то точно суёт свой нос не в своё дело." (show_side="right", show_kind="speech")
    hide leya

    show eveina thinking at eveina_left
    ev_thought "Это же те, которые собирались «сожрать меня живьём»?" (show_side="left", show_kind="thought")
    hide eveina
    show eveina intrigued at eveina_left
    ev_thought "Буду звать их пожирателями." (show_side="left", show_kind="thought")
    hide eveina

    show noa intrigued at noa_right
    no "Лея, познакомишь со своей подругой?" (show_side="right", show_kind="speech")
    hide noa

    show leya thinking at leya_right
    le "Эм... Эвейна, это Теро и Ноа..." (show_side="right", show_kind="speech")
    hide leya

    n "Эвейна, не дослушав, махнула рукой на прощанье." (show_side="none", show_kind="speech")

    show eveina normal at eveina_left
    ev "Мне пора." (show_side="left", show_kind="speech")
    hide eveina

    show noa intrigued at noa_right
    no "Мм, какая дружелюбная." (show_side="right", show_kind="speech")
    hide noa

    show leya annoyed at leya_right
    le "Кто ж виноват, что вы вчера произвели на неё впечатление своры гиен?" (show_side="right", show_kind="speech")
    hide leya

    show tero thinking at tero_right
    unknown "Справедливо." (show_side="right", show_kind="speech")
    hide tero

    show noa intrigued at noa_right
    no "Но мы готовы исправиться!" (show_side="right", show_kind="speech")
    no "Эвейна, зуб даю, я ещё стану твоим лучшим другом!" (show_side="right", show_kind="speech")
    hide noa

    show eveina wrinkled at eveina_left
    ev "Это угроза?" (show_side="left", show_kind="speech")
    hide eveina

    show noa intrigued at noa_right
    no "Это обещание!" (show_side="right", show_kind="speech")
    hide noa

    show eveina eyeroll at eveina_left
    ev "Зубы побереги, парень..." (show_side="left", show_kind="speech")
    hide eveina

    n "Закатив глаза, Эвейна вышла в коридор, не оглядываясь." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev_thought "Что за муха дружелюбия покусала этих двоих?" (show_side="left", show_kind="thought")
    hide eveina

    jump scene_2_3
