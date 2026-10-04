label scene_3_5:
    $ previous_scene = "scene_3_4"
    $ next_scene = "scene_3_6"
    $ current_scene = "scene_3_5"

    # =========================================================
    # СЦЕНА 3_5 — «КОРИДОР / КОМНАТА / ЭРИАН ВХОДИТ»
    # Структура: коридор — диалог об «выступлении» (из оригинала 3_8)
    #            → дверь комнаты → он входит без приглашения
    #            → принц/дракон → приход Леи → знакомство
    #            → мох осыпался
    # Диалог в коридоре — близко к оригинальной scene_3_8.
    # =========================================================

    call fade_to_black(1.2, 0.8)
    scene bg corridor_2 at bg_fullscreen with dissolve
    # play music "bgm/corridor_evening.ogg" fadein 2.0

    n "Выйдя из лекционного зала, Эвейна сделала пару шагов в сторону лестницы — и тут же вздрогнула, уловив знакомое движение сбоку." (show_side="none", show_kind="speech")

    show erian normal at erian_right
    er "Признаться, я рассчитывал на более эпичное столкновение." (show_side="right", show_kind="speech")
    er "Словесные удары, взгляд Вирта, обращённого в пепел…" (show_side="right", show_kind="speech")
    hide erian
    show erian eyebrow at erian_right
    er "А ты бросила пару фраз — и ушла." (show_side="right", show_kind="speech")
    hide erian
    show erian annoyed at erian_right
    er "Я разочарован, Эвейна. Я даже не успел поаплодировать." (show_side="right", show_kind="speech")
    hide erian

    show eveina thinking at eveina_left
    ev "Хочешь аплодисментов — поищи их в зеркале." (show_side="left", show_kind="speech")
    hide eveina
    show eveina eyebrow at eveina_left
    ev "Ты ведь и сам мог поучаствовать." (show_side="left", show_kind="speech")
    hide eveina

    show erian eyebrow at erian_right
    er "И испортить себе удовольствие наблюдать, как ты нервно рвёшь академические швы?" (show_side="right", show_kind="speech")
    hide erian
    show erian intrigued at erian_right
    er "Нет уж. У тебя хорошо получается без меня." (show_side="right", show_kind="speech")
    hide erian

    n "Эвейна продолжила идти, не ускоряясь. Он шагал вровень, но не слишком близко — как будто давал ей пространство только для того, чтобы напомнить, что может его забрать." (show_side="none", show_kind="speech")

    show erian normal at erian_right
    er "Думал, Вирт начнёт заикаться или испарится прямо на месте." (show_side="right", show_kind="speech")
    er "Думал, в тебе больше упорства." (show_side="right", show_kind="speech")
    hide erian

    show eveina normal at eveina_left
    ev "Я хотела задать вопрос, а не организовать казнь." (show_side="left", show_kind="speech")
    hide eveina
    show eveina thinking at eveina_left
    ev "Хотя… по лицу Вирта можно было подумать, что я украла его любимую пижаму." (show_side="left", show_kind="speech")
    hide eveina

    show erian intrigued at erian_right
    er "Или его веру в студенческую наивность." (show_side="right", show_kind="speech")
    hide erian
    show erian normal at erian_right
    er "Осторожней, так можно быстро нажить себе проблем. И врагов." (show_side="right", show_kind="speech")
    hide erian

    show eveina eyebrow at eveina_left
    ev "Считаешь, я была слишком резка?" (show_side="left", show_kind="speech")
    hide eveina

    n "Эриан небрежно смахнул пылинку с одежды." (show_side="none", show_kind="speech")

    show erian normal at erian_right
    er "Наоборот. Слишком мягкая." (show_side="right", show_kind="speech")
    hide erian
    show erian intrigued at erian_right
    er "Начала философствовать — и тут же пожалела, что задела чужие чувства. С тобой не соскучишься." (show_side="right", show_kind="speech")
    hide erian

    show eveina eyebrow at eveina_left
    ev "Что ты вообще делал на этой лекции? Она же для первокурсников." (show_side="left", show_kind="speech")
    hide eveina

    show erian smile at erian_right
    er "Это не я пришёл на лекцию — это вы пришли туда, где я спал." (show_side="right", show_kind="speech")
    hide erian

    show eveina eyeroll at eveina_left
    ev "Боже, зачем я вообще с тобой разговариваю..." (show_side="left", show_kind="speech")
    hide eveina

    show erian intrigued at erian_right
    er "Вероятно, потому что не можешь устоять перед обаятельной улыбкой?" (show_side="right", show_kind="speech")
    hide erian

    show eveina intrigued at eveina_left
    ev "За этим я хожу на лекции к Вирту." (show_side="left", show_kind="speech")
    hide eveina

    n "Эриан бросил на неё быстрый, острый взгляд — почти как укол иглой. Она заметила, как уголок его губы чуть дёрнулся вниз. И расплылась в ехидной улыбке." (show_side="none", show_kind="speech")

    show eveina intrigued at eveina_left
    ev "Неужели ты там тоже за этим, Эриан?" (show_side="left", show_kind="speech")
    hide eveina

    show erian annoyed at erian_right
    er "Если тебе больше нечего сказать — я отказываюсь участвовать в этом диалоге." (show_side="right", show_kind="speech")
    hide erian

    # --- Дверь комнаты ---

    n "Они дошли до её коридора. Эвейна остановилась у двери, обернулась." (show_side="none", show_kind="speech")

    show eveina normal at eveina_left
    ev "Там беспорядок." (show_side="left", show_kind="speech")
    hide eveina

    n "Эриан уже открывал дверь." (show_side="none", show_kind="speech")

    show eveina annoyed at eveina_left
    ev "Я не приглашала." (show_side="left", show_kind="speech")
    hide eveina

    n "Он прошёл внутрь." (show_side="none", show_kind="speech")

    scene bg eveina_room_day at bg_fullscreen with dissolve

    n "Огляделся без особого интереса. Лёг на её кровать, закинул руки за голову." (show_side="none", show_kind="speech")
    n "С видом человека, который сделал это сто раз." (show_side="none", show_kind="speech")

    show eveina annoyed at eveina_left
    ev_thought "Вот наглость." (show_side="left", show_kind="thought")
    hide eveina

    n "Она осталась стоять у двери. Злилась. Но он был здесь — и никуда не уходил." (show_side="none", show_kind="speech")
    n "И ей нужны были ответы." (show_side="none", show_kind="speech")

    show eveina normal at eveina_left
    ev "Подожди. Думаю, я поняла, что ты делаешь." (show_side="left", show_kind="speech")
    hide eveina

    show erian eyebrow at erian_right
    er "Ну же, удиви меня." (show_side="right", show_kind="speech")
    hide erian

    show eveina thinking at eveina_left
    ev "Ты ищешь ту пропавшую три года назад студентку." (show_side="left", show_kind="speech")
    ev "Три года назад. Это из-за неё ты читал старые книги. Всё складывается." (show_side="left", show_kind="speech")
    hide eveina
    show eveina eyebrow at eveina_left
    ev "Я угадала?" (show_side="left", show_kind="speech")
    hide eveina

    n "Эриан приподнял голову с подушки и уставился на неё так, словно она сморозила самую большую глупость в своей жизни." (show_side="none", show_kind="speech")

    show erian eyebrow at erian_right
    er "Ты ведь это несерьёзно сейчас?" (show_side="right", show_kind="speech")
    hide erian

    show eveina eyebrow at eveina_left
    ev "Эм, а что не так?" (show_side="left", show_kind="speech")
    ev "Так кто она? Вы были близки? Ты её помнишь?" (show_side="left", show_kind="speech")
    hide eveina

    n "Изумлённое лицо парня медленно расплылось в нахальном оскале." (show_side="none", show_kind="speech")

    show erian intrigued at erian_right
    er "Даа, Эвейна, ты меня раскусила. Я как принц лечу за своей сбежавшей принцессой..." (show_side="right", show_kind="speech")
    hide erian

    show eveina normal at eveina_left
    ev "Похищенной." (show_side="left", show_kind="speech")
    hide eveina

    show erian intrigued at erian_right
    er "Похищенной принцессой, чтобы спасти её из лап коварного дракона." (show_side="right", show_kind="speech")
    hide erian

    show eveina thinking at eveina_left
    ev "Честно говоря, ты больше тянешь на роль коварного дракона." (show_side="left", show_kind="speech")
    hide eveina

    show erian eyebrow at erian_right
    er "Что ты сказала?" (show_side="right", show_kind="speech")
    hide erian

    show eveina wondered at eveina_left
    ev "Что я сказала?" (show_side="left", show_kind="speech")
    hide eveina

    n "Пауза. Что-то изменилось в его взгляде — не злость, что-то другое. Он смотрел на неё чуть дольше, чем нужно." (show_side="none", show_kind="speech")

    show erian normal at erian_right
    er "Заканчивай с этим. Тебе не десять лет, чтобы верить в сказки." (show_side="right", show_kind="speech")
    hide erian

    show eveina eyeroll at eveina_left
    ev "Мне нравятся сказки." (show_side="left", show_kind="speech")
    hide eveina

    # --- Приход Леи ---

    n "Дверь открылась." (show_side="none", show_kind="speech")
    n "Эриан мгновенно изменил позу — сел на край кровати, как будто так и сидел. Бросил на Эвейну быстрый взгляд." (show_side="none", show_kind="speech")

    show erian eyebrow at erian_right
    er "..." (show_side="right", show_kind="speech")
    hide erian

    show eveina eyeroll at eveina_left
    ev_thought "Могла бы предупредить, да. Могла бы." (show_side="left", show_kind="thought")
    hide eveina

    show leya normal at leya_right
    le "Эвейна, идём! Я стащила немного сладких батончиков из столовой. Ещё тёплые!" (show_side="right", show_kind="speech")
    hide leya

    n "Лея увидела гостя и остановилась." (show_side="none", show_kind="speech")

    show leya eyebrow at leya_right
    le "О. Привет." (show_side="right", show_kind="speech")
    hide leya

    show eveina normal at eveina_left
    ev "Лея, это Эриан. Он… периодически появляется и разрушает мой покой. С грацией и сарказмом." (show_side="left", show_kind="speech")
    ev "Эриан, это Лея. Моя соседка." (show_side="left", show_kind="speech")
    hide eveina

    n "Лея смотрела на него с лёгким удивлением. Эриан поднялся с кровати — неторопливо — и чуть склонил голову." (show_side="none", show_kind="speech")

    show erian smile at erian_right
    er "Рад знакомству, Лея." (show_side="right", show_kind="speech")
    hide erian

    n "Его лицо стало почти безэмоциональным. Никакой иронии. Никакой маски. Только спокойная вежливость. Совершенно не похоже на того Эриана, которого она знала." (show_side="none", show_kind="speech")

    show eveina eyebrow at eveina_left
    ev_thought "О, так тебе не чужды манеры, Эриан?" (show_side="left", show_kind="thought")
    hide eveina

    show leya eyebrow at leya_right
    le "Приятно… эм… познакомиться." (show_side="right", show_kind="speech")
    hide leya

    n "Что-то в её взгляде было странным. Не испуг — что-то другое. Как будто она пыталась зацепиться взглядом за его лицо — и не могла." (show_side="none", show_kind="speech")

    show erian normal at erian_right
    er "Удачного вечера. Берегите сладкое. Оно склонно к исчезновению." (show_side="right", show_kind="speech")
    hide erian

    n "Он вышел, не обернувшись." (show_side="none", show_kind="speech")
    n "Лея смотрела на закрытую дверь. Потом — на Эвейну." (show_side="none", show_kind="speech")

    show leya eyebrow at leya_right
    le "Кто это?" (show_side="right", show_kind="speech")
    hide leya

    show eveina normal at eveina_left
    ev "Он... периодически появляется." (show_side="left", show_kind="speech")
    hide eveina

    show leya thinking at leya_right
    le "Я как будто... не могу понять, как он выглядит. Нормально, да?" (show_side="right", show_kind="speech")
    hide leya

    show eveina eyeroll at eveina_left
    ev "Он просто... незаметный." (show_side="left", show_kind="speech")
    hide eveina

    n "Лея посмотрела на неё." (show_side="none", show_kind="speech")

    show leya normal at leya_right
    le "Незаметный — последнее слово, которое я бы о нём сказала." (show_side="right", show_kind="speech")
    hide leya

    n "Она вернулась к своим делам. Больше не говорила об этом." (show_side="none", show_kind="speech")
    n "Эвейна смотрела на кровать, где только что лежал Эриан. На подушке осталась вмятина." (show_side="none", show_kind="speech")

    # --- Мох ---

    n "Прошла минута. Может, две." (show_side="none", show_kind="speech")
    n "Лея подняла взгляд от экрана — на подоконник." (show_side="none", show_kind="speech")

    show leya eyebrow at leya_right
    le "Ви, ты опять трогала мох?" (show_side="right", show_kind="speech")
    hide leya

    show eveina wondered at eveina_left
    ev "Нет." (show_side="left", show_kind="speech")
    hide eveina

    show leya eyebrow at leya_right
    le "Налёт осыпался." (show_side="right", show_kind="speech")
    hide leya

    show eveina eyebrow at eveina_left
    ev "Я не трогала." (show_side="left", show_kind="speech")
    hide eveina

    n "Лея посмотрела на неё с лёгким недоверием — не злым, просто привычным." (show_side="none", show_kind="speech")
    n "Потом вернулась к экрану." (show_side="none", show_kind="speech")

    show leya thinking at leya_right
    le "Ладно. Начнём сначала." (show_side="right", show_kind="speech")
    hide leya

    jump scene_3_6
