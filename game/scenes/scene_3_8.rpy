label scene_3_8:
    $ previous_scene = "scene_3_7"
    $ next_scene = "scene_3_9"
    $ current_scene = "scene_3_8"
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
    er "Думал, Вирт начнёт заикаться или испарится прямо на месте. А ты… удивила меня. Думал, в тебе больше упорства." (show_side="right", show_kind="speech")
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
    er "Это не я пришёл на лекцию, это вы пришли туда, где я спал." (show_side="right", show_kind="speech")
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

    n "Эриан бросил на неё быстрый, острый взгляд — почти как укол иглой. Она заметила, как уголок его губы чуть дёрнулся вниз. И раплылась в ехидной улыбке." (show_side="none", show_kind="speech")

    show eveina intrigued at eveina_left
    ev "Неужели ты там тоже за этим, Эриан?" (show_side="left", show_kind="speech")
    hide eveina

    show erian annoyed at erian_right
    er "Если тебе больше нечего сказать, то я отказываюсь участвовать в этом диалоге." (show_side="right", show_kind="speech")
    hide erian

    show eveina normal at eveina_left
    ev "Подожди. Думаю, я поняла, что ты делаешь." (show_side="left", show_kind="speech")
    hide eveina

    show erian eyebrow at erian_right 
    er "Ну же, удиви меня." (show_side="right", show_kind="speech")
    hide erian

    show eveina thinking at eveina_left
    ev "Ты ведь ищешь ту пропавшую три года назад студентку?" (show_side="left", show_kind="speech")
    hide eveina

    show erian eyebrow at erian_right 
    er "Что, прости?.." (show_side="right", show_kind="speech")
    hide erian

    show eveina eyebrow at eveina_left
    ev "Я про твои поиски." (show_side="left", show_kind="speech")
    hide eveina
    show eveina normal at eveina_left
    ev "Три года назад пропала студентка. А ты пытаешься понять, что тогда произошло. Все складывается." (show_side="left", show_kind="speech")
    hide eveina
    show eveina eyebrow at eveina_left
    ev "Я угадала?" (show_side="left", show_kind="speech")
    hide eveina

    n "Эриан внезапно перегородил ей дорогу, уставившись на неё, словно она сморозила самую большую глупость в своей жизни." (show_side="none", show_kind="speech")

    show erian eyebrow at erian_right 
    er "Ты ведь это несерьезно сейчас?" (show_side="right", show_kind="speech")
    hide erian

    show eveina eyebrow at eveina_left
    ev "Эм, а что не так?" (show_side="left", show_kind="speech")
    ev "Так кто она? Вы были близки? Ты её помнишь?" (show_side="left", show_kind="speech")
    hide eveina

    n "Изумленное лицо парня медленно расплылось в нахальном оскале." (show_side="none", show_kind="speech")

    show erian intrigued at erian_right 
    er "Даа, Эвейна, ты меня раскусила, я как принц лечу за своей сбежавшей принцессой..." (show_side="right", show_kind="speech")
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

    show erian normal at erian_right 
    er "Заканчивай с этим. Тебе не 10 лет, чтобы верить в сказки." (show_side="right", show_kind="speech")
    hide erian

    show eveina eyeroll at eveina_left
    ev "Мне нравятся сказки." (show_side="left", show_kind="speech")
    hide eveina
    show eveina upset thinking at eveina_left
    ev "Но судя по твоей реакции, я не угадала..." (show_side="left", show_kind="speech")
    hide eveina

    n "Эриан не ответил, продолжая буравить девушку взглядом." (show_side="none", show_kind="speech")

    show erian thinking at erian_right 
    er "Ты и правда ничего не знаешь о случившемся, так ведь?" (show_side="right", show_kind="speech")
    hide erian  

    show eveina annoyed at eveina_left
    ev "Да откуда мне знать, если ты говоришь загадками!" (show_side="left", show_kind="speech")
    hide eveina

    show erian normal at erian_right 
    er "Значит, от тебя никакой пользы." (show_side="right", show_kind="speech")
    hide erian 

    show eveina annoyed at eveina_left
    ev "Как и от тебя, в общем-то..." (show_side="left", show_kind="speech")
    hide eveina

    n "Он уже приготовился уколоть её ещё раз — но коридор наполнился голосом Леи." (show_side="none", show_kind="speech")

    show leya normal at leya_right
    le "Эвейна, идём! Я стащила немного сладких батончиков из столовой. Ещё тёплые!" (show_side="right", show_kind="speech")
    hide leya 

    n "Эвейна кивнула Лее, а затем обернулась к Эриану." (show_side="none", show_kind="speech")

    show eveina normal at eveina_left
    ev "Это Лея, моя соседка." (show_side="left", show_kind="speech")
    ev "Лея, это Эриан. Он… периодически появляется и разрушает мой покой. С грацией и сарказмом." (show_side="left", show_kind="speech")
    hide eveina

    show leya eyebrow at leya_right
    le "Приятно… эм… познакомиться." (show_side="right", show_kind="speech")
    hide leya 

    n "Лея посмотрела на него слегка удивлённо. Эриан склонил голову в знак приветствия." (show_side="none", show_kind="speech")

    show erian smile at erian_right 
    er "Рад знакомству, Лея." (show_side="right", show_kind="speech")
    hide erian 

    n "Его лицо в этот момент стало почти безэмоциональным. Никакой иронии. Никакой маски. Лишь спокойная вежливость. Совершенно не похоже на того Эриана, которого она знала." (show_side="none", show_kind="speech")

    show eveina eyebrow at eveina_left
    ev_thought "О, так тебе не чужды манеры, Эриан?" (show_side="left", show_kind="thought")
    hide eveina

    show erian normal at erian_right 
    er "Удачного вечера. Берегите сладкое. Оно склонно к исчезновению." (show_side="right", show_kind="speech")
    hide erian 

    n "Он растворился в людском потоке, не обернувшись." (show_side="none", show_kind="speech")
    n "Лея проводила его взглядом, будто сбрасывая с себя остатки наваждения. Потом схватила Эвейну за локоть и потащила прочь." (show_side="none", show_kind="speech")

    show leya smile at leya_right
    le "Скорее пойдем! Нам срочно нужно обсудить кое-что важное!" (show_side="right", show_kind="speech")
    hide leya 
    show leya eyebrow at leya_right
    le "Например, как ты умудряешься выглядеть так свежо после своих взрывоопасных выходок?" (show_side="right", show_kind="speech")
    hide leya 
    show leya smile at leya_right
    le "Да-да, в столовой уже все говорят о том, как ты заставила Вирта заикаться на собственной лекции!" (show_side="right", show_kind="speech")
    hide leya 

    n "Она говорила быстро, сбивая темп, резко уводя тему в сторону." (show_side="none", show_kind="speech")
    n "Вместе они направились в свою комнату — обсуждать последние академические сплетни и уничтожать украденные батончики." (show_side="none", show_kind="speech")

    jump scene_3_9
