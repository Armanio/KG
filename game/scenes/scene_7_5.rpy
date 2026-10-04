label scene_7_5:
    $ previous_scene = "scene_7_4"
    $ next_scene = "scene_7_6"
    $ current_scene = "scene_7_5"
    call fade_to_black(1.2, 0.8)
    scene bg eveina_room at bg_fullscreen with dissolve

    n "Свет пробивался сквозь полупрозрачные шторы. Эвейна проснулась от ощущения, будто тело само решило, что пора." (show_side="none", show_kind="speech")
    n "Не по будильнику в браслете, не от тревоги внутри, а просто потому что впервые за долго время выспалась." (show_side="none", show_kind="speech")
    n "Улыбнувшись, девушка потянулась и заметила, что на браслете мигают уведомления. Пальцы тут же потянулись к экрану. Все сообщения были от Леи." (show_side="none", show_kind="speech")

    n "{i}«Привет, спящая красавица. Очень жаль, что всё прошло так. Мы все за тебя переживали.»{/i}" (show_side="none", show_kind="speech")
    n "{i}«И да… об этом уже знает вся Академия. Точнее, её болтливая половина.»{/i}" (show_side="none", show_kind="speech")
    n "{i}«На столе — маленький подарок тебе. Принесли, пока ты спала.»{/i}" (show_side="none", show_kind="speech")
    n "{i}«Передай своему дарителю, что кружек и чайных ложек у нас тоже нет.»{/i}" (show_side="none", show_kind="speech")

    n "Эвейна медленно повернула голову и увидела на столе чайник. Губы непроизвольно расплылись в улыбке." (show_side="none", show_kind="speech")

    show eveina smile at eveina_left
    ev "О вашей любви к чаю, профессор Вирт, можно слагать легенды." (show_side="left", show_kind="speech")
    hide eveina

    n "В попытке продлить состояние безмятежности, что подарил ей здоровый сон, девушка прикрыла глаза. Но в голове в тот же момент всплыла сцена, которую не звали." (show_side="none", show_kind="speech")
    n "Ночной сад. Светящееся изнутри тело, лежащее в волнах света. Резкий рывок, боль в запястье и страх за свою жизнь." (show_side="none", show_kind="speech")
    n "Волна злости поднялась в ней с новой силой." (show_side="none", show_kind="speech")

    show eveina angry at eveina_left
    ev_thought "Эриан, чёртов ты…" (show_side="left", show_kind="thought")
    ev_thought "Вот погоди, доберусь до тебя и засуну твою улыбку тебе в..." (show_side="left", show_kind="thought")
    hide eveina

    n "Сон сняло как рукой, Эвейна резко подскочила и села, отчего тут же закружилась голова." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev_thought " Видимо, последствия эксперимента..." (show_side="left", show_kind="thought")
    hide eveina
    show eveina angry at eveina_left
    ev_thought "Но тебя это не спасёт." (show_side="left", show_kind="thought")
    hide eveina
   
    n "Чуть помедлив, девушка встала с постели, быстро привела себя в порядок и решительно отправилась на поиски." (show_side="none", show_kind="speech")

    scene bg garden at bg_fullscreen with dissolve

    n "Но Эриана нигде не оказалось. Архив — пуст. В саду — никого. Ни тени, наблюдающей за ней возле арки. Ни насмешливого голоса за спиной." (show_side="none", show_kind="speech")
    n "Только косые взгляды студентов, что слышали о её вчерашних злоключениях." (show_side="none", show_kind="speech")

    show eveina angry at eveina_left
    ev_thought "Спрятался от меня, потому что всё-таки умеешь читать мысли, трусливый лжец?" (show_side="left", show_kind="thought")
    hide eveina

    n "Эвейна долго бродила, но с каждой минутой в теле скапливалась усталость. Не просто физическая — что-то глубже, будто утекало желание жить." (show_side="none", show_kind="speech")
    n "Поняв, что недолго ещё сможет держаться на ногах, она вернулась к дереву, сорвала на нём самый большой лист, что нашла и нацарапала на нём короткое: {i}«Лечу домой. Не теряй.»{/i}." (show_side="none", show_kind="speech")
    n "Затем критичным взглядом посмотрела на свои каракули и внесла правки: {i}«Лечу домой. Не {s}теряй{/s} ищи. Придурок»{/i}." (show_side="none", show_kind="speech")
    n "Аккуратно свернув лист, девушка воткнула его в кору на уровне глаз, так, чтобы он был достаточно заметен, но не привлекал к себе явного внимания." (show_side="none", show_kind="speech")
    n "После чего с чувством выполненного долга вернулась в комнату." (show_side="none", show_kind="speech")

    scene bg eveina_room at bg_fullscreen with dissolve

    n "Лея встретила её в дверях и, не говоря ни слова, ласково обняла её." (show_side="none", show_kind="speech")

    show leya normal at leya_right
    le "Чай?" (show_side="right", show_kind="speech")
    hide leya

    show eveina smile at eveina_left
    ev "Обожаю, когда ты задаёшь правильные вопросы." (show_side="left", show_kind="speech")
    hide eveina

    show leya thinking at leya_right
    le "Я порывалась вероломно похитить чайные пары из столовой..." (show_side="right", show_kind="speech")
    hide leya

    show eveina intrigued at eveina_left
    ev "Берёшь с меня пример?" (show_side="left", show_kind="speech")
    hide eveina

    show leya thinking at leya_right
    le "Не совсем. У тебя лучше получается." (show_side="right", show_kind="speech")
    le "Меня на месте преступления с ложками в зубах застукал Вирт." (show_side="right", show_kind="speech")
    hide leya
    show leya normal at leya_right
    le "Посмотрел на меня как-то странно, а потом придержал дверь, помогая выйти." (show_side="right", show_kind="speech")
    hide leya
    show leya eyebrow at leya_right
    le "Это можно считать преступлением?" (show_side="right", show_kind="speech")
    hide leya

    show eveina smile at eveina_left
    ev "Конечно! И вы с Виртом в нём — подельники." (show_side="left", show_kind="speech")
    hide eveina

    show leya normal at leya_right
    le "Посажу завтра дерево в саду." (show_side="right", show_kind="speech")
    hide leya

    n "Эвейна вопросительно подняла бровь, но уже поняла, к чему та ведёт. Слишком уж хорошо они узнали друг друга за короткое время." (show_side="none", show_kind="speech")

    show leya eyebrow at leya_right
    le "Что? Не смотри так на меня, я забочусь о своей карме!" (show_side="right", show_kind="speech")
    hide leya

    show eveina smile at eveina_left
    ev "За Вирта тоже посади. И если там есть место под лесополосу, то можешь вспомнить и своей скромной соседке." (show_side="left", show_kind="speech")
    hide eveina

    n "Лея прыснула и отмахнулась. Пока она возилась с чайником, Эвейна упала на кровать и активировала Сайфа." (show_side="none", show_kind="speech")

    show sf at ai_right
    sf "Ну наконец-то ты про меня вспомнила. Как ты себя чувствуешь?" (show_side="right", show_kind="speech")
    hide sf

    show eveina eyebrow at eveina_left
    ev "Ты за мной подглядывал?" (show_side="left", show_kind="speech")
    hide eveina

    show sf at ai_right
    sf "Пульс, давление, температура, датчик эмоций." (show_side="right", show_kind="speech")
    sf "Ты сама поместила меня в браслет — теперь у меня встроенные привилегии." (show_side="right", show_kind="speech")
    sf "Поэтому я знаю, что ты вчера пережила пиковую нагрузку. Ужасающе неловко для живого организма." (show_side="right", show_kind="speech")
    hide sf

    show eveina thinking at eveina_left
    ev_thought "Запомнить на будущее: снимать браслет, если отправлюсь на свидание." (show_side="left", show_kind="thought")
    hide eveina
    show eveina normal at eveina_left
    ev "Я завалила эксперимент." (show_side="left", show_kind="speech")
    hide eveina

    show leya eyebrow at leya_right
    le "А по-моему, это он завалил тебя. Буквально." (show_side="right", show_kind="speech")
    hide leya

    show sf at ai_right
    sf "Ты всего лишь студентка. Много на себя берёшь. Если и винить кого-то, то твоего преподавателя." (show_side="right", show_kind="speech")
    hide sf

    show leya normal at leya_right
    le "Поддерживаю. Полностью." (show_side="right", show_kind="speech")
    hide leya

    n "Лея протянула Эвейне кружку ароматного напитка." (show_side="none", show_kind="speech")

    show eveina normal at eveina_left
    ev "Спасибо за заботу, вы оба… Но не думаю, что Каэль мог предусмотреть то, что произошло." (show_side="left", show_kind="speech")
    hide eveina
    show eveina eyebrow at eveina_left
    ev "Сайф… Ты можешь взломать чью-то личную почту?" (show_side="left", show_kind="speech")
    hide eveina

    show sf at ai_right
    sf "Определённо плохой вопрос. И весьма подозрительный. Какого именно «кого-то»?" (show_side="right", show_kind="speech")
    hide sf

    show eveina thinking at eveina_left
    ev "Ну, скажем… Кайстра." (show_side="left", show_kind="speech")
    hide eveina

    n "С соседней кровати донёсся резкий кашель. Лея выпучила глаза, поперхнувшись чаем." (show_side="none", show_kind="speech")

    show leya eyebrow at leya_right
    le "Ты сошла с ума?! Эвейна, это Кайстр! Это… Кайстр!" (show_side="right", show_kind="speech")
    hide leya

    show eveina normal at eveina_left
    ev "У него могут быть связи с создателем лекарства. А это — шанс. Возможно, единственный." (show_side="left", show_kind="speech")
    hide eveina

    show sf at ai_right
    sf "Очень плохая идея. Очень опасная идея." (show_side="right", show_kind="speech")
    hide sf

    show eveina normal at eveina_left
    ev "Я знаю. Но, пожалуйста. Ты можешь мне помочь?" (show_side="left", show_kind="speech")
    hide eveina

    n "ИИ долго молчал. Не то чтобы обдумывал, скорее — проверял, готова ли она к тому, о чём просит." (show_side="none", show_kind="speech")

    show sf at ai_right
    sf "Я не дам тебе доступ." (show_side="right", show_kind="speech")
    sf "Но… Я могу просмотреть его переписку сам. И сообщить тебе, если найду что-то важное." (show_side="right", show_kind="speech")
    hide sf

    n "Эвейна прикрыла глаза и выдохнула с облегчением." (show_side="none", show_kind="speech")

    show eveina intrigued at eveina_left
    ev "Сайф… Я тебя люблю." (show_side="left", show_kind="speech")
    hide eveina

    show sf at ai_right
    sf "Вот и началось." (show_side="right", show_kind="speech")
    sf "Первый шаг — признание. Второй — зависимость." (show_side="right", show_kind="speech")
    sf "Третий — я получаю кольцо и… чайник?" (show_side="right", show_kind="speech")
    hide sf

    show leya smile at leya_right
    le "Пф-ф!" (show_side="right", show_kind="speech")
    hide leya

    n "Лея зашлась заливистым смехом. ИИ отключился, оставив Эвейну лежать, прижимая к себе чашку. Подруга тоже растянулась на своей кровати, и в комнате стало тихо." (show_side="none", show_kind="speech")
    n "На мгновение — всё было просто. Лея перевернулась на бок, подтянув одеяло под подбородок." (show_side="none", show_kind="speech")

    show leya eyebrow at leya_right
    le "Расскажешь, откуда у нас чайник?" (show_side="right", show_kind="speech")
    hide leya

    show eveina thinking at eveina_left
    ev "Нет." (show_side="left", show_kind="speech")
    hide eveina

    show leya normal at leya_right
    le "Я так и подумала. Что ж, сохраним интригу." (show_side="right", show_kind="speech")
    hide leya
    show leya eyebrow at leya_right
    le "Ви… Ты ведь понимаешь, во что лезешь, да?" (show_side="right", show_kind="speech")
    hide leya

    n "Эвейна повернула голову в сторону Леи. Та смотрела на неё серьёзно, без улыбки." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev "Не совсем. Но знаю, зачем это делаю." (show_side="left", show_kind="speech")
    hide eveina

    show leya normal at leya_right
    le "Меня это пугает. Потому что каждый раз, когда ты идёшь «за правдой», ты оставляешь где-то там кусок себя." (show_side="right", show_kind="speech")
    le "Ты не похожа на человека, которому нравится воровать, проникать куда-то, куда ему нельзя, или читать чужие личные переписки..." (show_side="right", show_kind="speech")
    le "А я просто… не хочу, чтобы в какой-то момент тебя стало слишком мало." (show_side="right", show_kind="speech")
    hide leya

    n "В груди что-то дрогнуло. Она ведь и сама не раз думала о том, как далеко готова зайти. И как после этого будет себя чувствовать." (show_side="none", show_kind="speech")

    show eveina normal at eveina_left
    ev "Я буду осторожной. Обещаю." (show_side="left", show_kind="speech")
    hide eveina

    show leya normal at leya_right
    le "Ты не умеешь быть осторожной." (show_side="right", show_kind="speech")
    le "Просто... если что-то случится — скажи мне." (show_side="right", show_kind="speech")
    le "Мы вместе побежим за помощью к Вирту. Или сожжём все улики против тебя в дальнем уголке сада. Только позволь тебе помочь." (show_side="right", show_kind="speech")
    hide leya

    n "Эвейна устало улыбнулась. И всё, что смогла произнести в ответ — это тихое:" (show_side="none", show_kind="speech")

    show eveina normal at eveina_left
    ev "Договорились." (show_side="left", show_kind="speech")
    hide eveina

    n "Слов было достаточно, и наступила тишина. Вскоре девушка провалилась в сон." (show_side="none", show_kind="speech")

    jump scene_7_6
