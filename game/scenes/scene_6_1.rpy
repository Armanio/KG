label scene_6_1:
    $ previous_scene = "scene_5_6"
    $ next_scene = "scene_6_2"
    $ current_scene = "scene_6_1"
    call fade_to_black(1.2, 0.8)
    scene bg eveina_room_night at bg_fullscreen with dissolve

    n "Свет проекции мягко пульсировал на запястье, отбрасывая блики на потолок. ИИ молчал, но оставался активным в безмолвном присутствии, будто сам он принимал сторону наблюдателя." (show_side="none", show_kind="speech")
    n "Эвейна в который раз просматривала содержимое расшифрованного файла. Каждая страница этого отчёта звучала как приговор всему: решимости найти лечение, надежде спасти отца, союзу с Эрианом." (show_side="none", show_kind="speech")
    n "С последним было особенно трудно. Со своей мотивацией и ожиданиями она как-нибудь разберётся, это не первый тупик на её пути." (show_side="none", show_kind="speech")
    n "Но мысль о том, что случится, расскажи она об этом файле Эриану, терзала её." (show_side="none", show_kind="speech")

    show eveina eyebrow at eveina_left
    ev_thought "Показать ему?" (show_side="left", show_kind="thought")
    hide eveina
    show eveina thinking at eveina_left
    ev_thought "А если он увидит в этих строках подтверждение худшего?" (show_side="left", show_kind="thought")
    ev_thought "Если поймёт, что всё, во что я верю — ложь? Начнёт отговаривать от идеи спасти отца..." (show_side="left", show_kind="thought")
    hide eveina
    show eveina annoyed at eveina_left
    ev_thought "Что, если откажется помогать?" (show_side="left", show_kind="thought")
    ev_thought "А если не покажу — как быстро он поймёт, что я что-то скрываю? Он ведь знает о файле и моих попытках его открыть..." (show_side="left", show_kind="thought")
    hide eveina
    show eveina angry at eveina_left
    ev_thought "Чёрт!" (show_side="left", show_kind="thought")
    hide eveina
    show eveina thinking at eveina_left
    ev_thought "Если я покажу ему это — пути назад не будет." (show_side="left", show_kind="thought")
    ev_thought "Если не покажу — рано или поздно обвинит меня в предательстве." (show_side="left", show_kind="thought")
    hide eveina
    show eveina upset at eveina_left
    ev_thought "И в том, и в другом случае... выглядит так, будто это конец." (show_side="left", show_kind="thought")
    hide eveina

    n "Она прижала кулаки к губам. Внутри всё кричало: {i}«Подожди, подумай ещё раз, побереги это хрупкое равновесие между вами»{/i}." (show_side="none", show_kind="speech")
    n "Но… он обещал быть рядом. Обещал быть на её стороне. Не то, чтобы она полностью ему верила... но разве не лучше сейчас узнать цену его словам?" (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev_thought "Ну вот. Доверие. Самая редкая валюта Академии." (show_side="left", show_kind="thought")
    hide eveina
    show eveina normal at eveina_left
    ev_thought "Ставлю на кон." (show_side="left", show_kind="thought")
    hide eveina

    n "Эвейна поднялась и потянулась за курткой. Собравшись и едва не столкнувшись с Леей в дверях, бросила ей:" (show_side="none", show_kind="speech")

    show eveina normal at eveina_left
    ev "Не жди меня. Мне нужно проветриться." (show_side="left", show_kind="speech")
    hide eveina

    n "И выскользнула из комнаты в ночь, оставляя за спиной недоумённый голос соседки:" (show_side="none", show_kind="speech")

    show leya eyebrow at  leya_right
    le "Снова? Если бы не знала тебя, решила бы, что у тебя появился парень, которого ты от всех скрываешь..." (show_side="right", show_kind="speech")
    hide leya

    show eveina thinking at eveina_left
    ev_thought "Ох, Лея... Ты одновременно и невероятно близка к истине, и бесконечно далека от неё." (show_side="left", show_kind="thought")
    hide eveina
    show eveina upset thinking at eveina_left
    ev_thought "Я не заслуживаю подругу, которая никогда не задаёт лишних вопросов. Не заслуживаю тебя." (show_side="left", show_kind="thought")
    hide eveina

    scene bg night_garden at bg_fullscreen with dissolve

    n "Сад встретил её прохладой и светящимися отблесками, прогоняя из головы девушки мысли о Лее." (show_side="none", show_kind="speech")
    n "Эвейна быстрым шагом добралась до знакомого места. Остановилась, переводя дыхание, и вгляделась в темноту." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev_thought "Ну конечно. Гениально." (show_side="left", show_kind="thought")
    ev_thought "Прибежать в сад посреди ночи, надеясь, что таинственный инопланетный парень с ворохом секретов вынырнет из кустов по первому зову." (show_side="left", show_kind="thought")
    hide eveina
    show eveina annoyed at eveina_left
    ev_thought "Почему бы и нет?" (show_side="left", show_kind="thought")
    hide eveina

    n "Она нервно обернулась, обводя взглядом ночной сад и переминаясь с ноги на ногу." (show_side="none", show_kind="speech")

    show eveina annoyed at eveina_left
    ev_thought "А если он не придёт? Я буду стоять тут одна, под деревом, как героиня плохо написанной драмы." (show_side="left", show_kind="thought")
    ev_thought "И кто вообще сказал, что он придёт? Он же не телепат…" (show_side="left", show_kind="thought")
    hide eveina
    show eveina thinking at eveina_left
    ev_thought "Хотя, кто его знает..." (show_side="left", show_kind="thought")
    hide eveina
    show eveina normal at eveina_left
    ev_thought "Может, стоит вернуться в комнату? Перенести разговор на утро. Всё обдумать." (show_side="left", show_kind="thought")
    hide eveina
    show eveina eyebrow at eveina_left
    ev_thought "Но... если я сейчас уйду — вдруг к утру передумаю?" (show_side="left", show_kind="thought")
    hide eveina

    n "Секунды тянулись, и каждая порождала новую каплю сомнения. Девушка стояла, крепко прижав к груди руку с браслетом, словно он был и сокровищем и проклятием одновременно." (show_side="none", show_kind="speech")
    n "И когда уже почти собралась отступить, вдруг поняла... нет, не так... почувствовала, что он здесь." (show_side="none", show_kind="speech")
    n "Словно на секунду весь сад замер от его приближения, а потом запульсировал снова, подстраиваясь под новый ритм. Знакомый холодок пробежал от шеи до затылка, не оставляя сомнений." (show_side="none", show_kind="speech")
    n "В подтверждение её мыслей из тени вынырнул раздражённый голос:" (show_side="none", show_kind="speech")

    show erian annoyed at erian_right
    er "Так и будешь прибегать сюда каждый раз, как только твой мир начинает трещать по швам?" (show_side="right", show_kind="speech")
    hide erian

    show eveina thinking at eveina_left
    ev_thought "Когда-нибудь я обязательно спрошу, как он это делает..." (show_side="left", show_kind="thought")
    hide eveina
    show eveina annoyed at eveina_left
    ev "Мог бы для разнообразия обрадоваться моему присутствию." (show_side="left", show_kind="speech")
    hide eveina
    show eveina normal at eveina_left
    ev "Я вскрыла файл." (show_side="left", show_kind="speech")
    hide eveina

    n "Эриан вопросительно поднял бровь. Она опустилась на землю у дерева, и подняла на него взгляд, выжидая." (show_side="none", show_kind="speech")
    n "Недовольно сведя брови и хмыкнув, парень опустился рядом с ней. Эвейна вытащила из браслета голографическую проекцию — та медленно ожила в воздухе, осветив их лица." (show_side="none", show_kind="speech")
    n "Девушка пролистывала файл, строчка за строчкой, всё глубже вчитываясь в материалы." (show_side="none", show_kind="speech")

    show eveina normal at eveina_left
    ev "Вот. Это — отчёт о первой версии препарата NR-Δ3. Более чем двадцатилетней давности." (show_side="left", show_kind="speech")
    ev "Это, вероятно, не финальная формула..." (show_side="left", show_kind="speech")
    hide eveina

    n "Она медленно втянула воздух ртом в попытке сбросить внутреннее напряжение, в этот раз вызванное не присутствием Эриана. И продолжила:" (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev "Здесь указано: восстановление когнитивных функций возможно... но только временно. И только при контакте с Илейн." (show_side="left", show_kind="speech")
    hide eveina

    n "Пролистнув вниз страницы, Эвейна указала пальцем на график с двумя линиями." (show_side="none", show_kind="speech")
    
    show eveina normal at eveina_left
    ev "Смотри. Стабильность принимающих лекарство в присутствии Илейн — держится на протяжении почти трёх месяцев. Именно столько проходили первые испытания." (show_side="left", show_kind="speech")
    ev "Без них — через 48, максимум 72 часа: ухудшение. Галлюцинации. Импульсивное поведение. Регресс." (show_side="left", show_kind="speech")
    ev "Они фиксировали даже отчуждение от собственного «я»." (show_side="left", show_kind="speech")
    hide eveina

    n "Она зачитала вслух один абзац:" (show_side="none", show_kind="speech")

    show eveina sad at eveina_left
    ev "{i}«Пациент 14: Я слышу мысли как голос, но он не мой. Уберите его из моей головы!»{/i}" (show_side="left", show_kind="speech")
    ev "В формулу вносили изменения, меняли состав, пропорции, способы экстракции и время нахождение рядом с Илейн." (show_side="left", show_kind="speech")
    ev "Но результат был один. Поведение испытуемых становилось неконтролируемым." (show_side="left", show_kind="speech")
    hide eveina

    n "Лицо Эриана оставалось непроницаемым. Эвейна пролистала отчёт к последним строкам." (show_side="none", show_kind="speech")

    show eveina normal at eveina_left
    ev "И вот это. Финальный комментарий." (show_side="left", show_kind="speech")
    ev "{i}«Это больше, чем химия. Это — совсем иной, недоступный нам уровень взаимодействия. Препарат — не лекарство. Это зависимость. Зависимость от Илейн.»{/i}" (show_side="left", show_kind="speech")
    ev "Подпись: Далон." (show_side="left", show_kind="speech")
    hide eveina

    n "В воздухе зависла тревожная тишина. Отблески голубого солнца на деревьях дрожали, отражаясь в глазах Эриана." (show_side="none", show_kind="speech")

    show erian thinking at erian_right
    er "Из чего было произведено лекарство?" (show_side="right", show_kind="speech")
    hide erian

    show eveina upset thinking at eveina_left
    ev "Эриан..." (show_side="left", show_kind="speech")
    hide eveina

    show erian annoyed at erian_right
    er "Из чего они его делали, Эвейна?" (show_side="right", show_kind="speech")
    hide erian

    show eveina upset at eveina_left
    ev "Основой стала сыворотка из крови Илейн." (show_side="left", show_kind="speech")
    hide eveina

    n "Он не проронил ни слова. Они сидели рядом, касаясь друг друга плечами, но Эвейна почти физически ощущала, как между ними разверзлась земля, порождая огромную бездонную пропасть." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev_thought "Скажи хоть что-нибудь." (show_side="left", show_kind="thought")
    ev_thought "Только не то, что заставит меня пожалеть о своём решении. Пожалуйста." (show_side="left", show_kind="thought")
    hide eveina

    n "Наконец, Эриан тяжело вздохнул, его голос звучал глухо и отстранённо." (show_side="none", show_kind="speech")

    show erian thinking at erian_right
    er "Это отчёт двадцатипятилетней давности. Всё могло измениться." (show_side="right", show_kind="speech")
    er "Не стоит делать выводы раньше времени." (show_side="right", show_kind="speech")
    hide erian

    n "Эвейна, затаив дыхание, почувствовала, как с неё сходит часть напряжения. Она наблюдала за безжизненным блуждающим взглядом и не находила слов." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev_thought "Что за Илейн участвовали в этом эксперименте?" (show_side="left", show_kind="thought")
    ev_thought "Делали ли они это добровольно? Были ли теми самыми пропавшими молодыми парнями и девушками, которых искал Эриан?" (show_side="left", show_kind="thought")
    ev_thought "Каково сейчас Эриану слышать о том, что для кого-то они — просто материал, ставший наркотиком." (show_side="left", show_kind="thought")
    hide eveina

    show eveina normal at eveina_left
    ev "Эриан..." (show_side="left", show_kind="speech")
    ev "Ты знаешь тех Илейн из отчёта? Думаешь, это..." (show_side="left", show_kind="speech")
    hide eveina

    n "Лицо парня оставалось непроницаемой маской, когда он медленно перевёл взгляд на Эвейну, заставляя её умолкнуть." (show_side="none", show_kind="speech")

    show erian normal at erian_right
    er "Завтра рано вставать. Иди отдохни." (show_side="right", show_kind="speech")
    hide erian

    show eveina normal at eveina_left
    ev "Давай поговорим. Пожалуйста." (show_side="left", show_kind="speech")
    hide eveina

    show erian thinking at erian_right
    er "Не о чем тут разговаривать." (show_side="right", show_kind="speech")
    hide erian

    show eveina sad at eveina_left
    ev "Эриан..." (show_side="left", show_kind="speech")
    hide eveina

    show erian thinking at erian_right
    er "Не сейчас, Эвейна." (show_side="right", show_kind="speech")
    hide erian

    n "Словно вторя его словам, где-то вдали яркой вспышкой прорезала небо молния. А затем прогремел гром. Начиналась гроза." (show_side="none", show_kind="speech")
    n "Парень поднялся и протянул ей руку. Эвейна, игнорируя руку, поднялась следом, сделала шаг, неловко запнулась о корень, спрятанный в траве и полетела прямо в его сторону." (show_side="none", show_kind="speech")
    n "Эриан поймал её так, будто она ничего не весила, горячие ладони обхватили талию. Запах хвои и сырого мха окутал её, когда лицо и руки упёрлись в его грудь." (show_side="none", show_kind="speech")
    n "Эвейна замерла, боясь спугнуть это новое, совсем не похожее на прежнее, ощущение — легкие покалывание мурашек в местах, где его тело касалось её, вызывая внутри предательское желание, чтобы это не заканчивалось." (show_side="none", show_kind="speech")
    n "Голос над головой прозвучал низко, с нескрываемой усмешкой:" (show_side="none", show_kind="speech")

    show erian intrigued at erian_right
    er "Ты неустойчива. В прямом и переносном смысле." (show_side="right", show_kind="speech")
    hide erian

    n "Она медленно подняла взгляд на его линию ключиц, торчащих из-под растёгнутой рубашки, шею, на которой виднелась пульсирующая жилка, губы, растянутые в лёгком оскале, обнажающем клыки." (show_side="none", show_kind="speech")
    n "А затем их глаза встретились, её — слегка удивлённые и его — потемневшие и изучающие её реакцию. В животе Эвейны завязался тугой узел." (show_side="none", show_kind="speech")

    show eveina sad at eveina_left
    ev "Я понимаю, что ты сейчас чувствуешь..." (show_side="left", show_kind="speech")
    hide eveina

    show erian intrigued at erian_right
    er "Серьезно? И что же я сейчас чувствую?" (show_side="right", show_kind="speech")
    hide erian

    show eveina upset at eveina_left
    ev "Этот отчёт... он подтверждение моих самых страшных кошмаров..." (show_side="left", show_kind="speech")
    ev "Какие бы цели они ни преследовали... нет никакого оправдания тому, что они делали с этими пациентами... и с Илейн..." (show_side="left", show_kind="speech")
    hide eveina

    n "Не успев договорить, Эвейна почувствовала, как его грудь напряглась под её руками. Эриан ослабил хватку на её талии и чуть отстранился." (show_side="none", show_kind="speech")
    n "Эвейна замерла и непонимающе уставилась на него. Он медленно наклонился к её уху и обжигая щеку горячим дыханием, тихо произнес:" (show_side="none", show_kind="speech")

    show erian normal at erian_right
    er "Мы обсудим это позже. А сейчас — правда, тебе лучше отдохнуть." (show_side="right", show_kind="speech")
    hide erian

    n "Эвейна задрожала от его дыхания, от темного огня, плескающегося в его радужках." (show_side="none", show_kind="speech")

    show eveina normal at eveina_left
    $ erian_first_kiss = renpy.call_screen("choice", 
    items=[
    ("Ты остался со мной.", True),
    ("Ты успокоился.", False)
    ], who="Эвейна", what="Мне сейчас не отдых нужен. Мне нужно, чтобы...", _last_say_who="ev")
    hide eveina

    if erian_first_kiss == True:
        show eveina upset thinking at eveina_left
        ev "Чтобы ты был... на моей стороне." (show_side="left", show_kind="speech")
        hide eveina

        show erian thinking at erian_right
        er "На твоей стороне, говоришь..." (show_side="right", show_kind="speech")
        hide erian  

        n "Эриан сделал шаг вперёд, сокращая дистанцию." (show_side="none", show_kind="speech")

        show erian thinking at erian_right
        er "Ты только что нашла своё лекарство, Эвейна. Вот оно, течёт в моих моих венах!" (show_side="right", show_kind="speech")
        er "Нужно всего лишь посадить меня на поводок — и твой отец будет здоров." (show_side="right", show_kind="speech")
        hide erian  
        show erian eyebrow at erian_right
        er "Разве не этого ты так хотела? Разве не готова была пожертвовать многим ради спасения своего отца?" (show_side="right", show_kind="speech")
        hide erian  
        show erian annoyed at erian_right
        er "Так как ты можешь судить того, кто сделал тоже самое? Чем ты от него отличаешься?" (show_side="right", show_kind="speech")
        er "Чего ты ожидала вообще, придя сюда? Что я прочитаю это и сам застегну на себе ошейник?" (show_side="right", show_kind="speech")
        hide erian

        n "Девушка дернулась как от пощечины. Глаза сердито уставились на него, а руки уперлись в его грудь в попытке отстраниться." (show_side="none", show_kind="speech")

        show eveina angry at eveina_left
        ev "Я ожидала, что ты не предашь меня так же, как тебя предал Далон, при первой возможности." (show_side="left", show_kind="speech")
        hide eveina

        n "Он отпустил её талию." (show_side="none", show_kind="speech")
        n "Но в следующую же секунду спина Эвейны врезалась в шершавый ствол дерева, придавленная весом его тела." (show_side="none", show_kind="speech")
        n "Лицо Эриана оказалось совсем близко. Он больше не улыбался. Его губы почти касались её губ." (show_side="none", show_kind="speech")

        show erian annoyed at erian_right
        er "А с чего бы вдруг мне оставаться на твоей стороне?" (show_side="right", show_kind="speech")
        hide erian

        show eveina angry at eveina_left
        ev "Потому что не все люди одинаковы! Я — не он, и никогда бы так с тобой не поступила." (show_side="left", show_kind="speech")
        hide eveina

        show erian annoyed at erian_right
        er "И я просто должен в это поверить?" (show_side="right", show_kind="speech")
        hide erian

        show eveina angry at eveina_left
        ev "Ты просто невыносим..." (show_side="left", show_kind="speech")
        hide eveina

        n "Эвейна инстинктивно сглотнула, почувствовав его ладонь на своей шее, сжимающей её мягко, пугающе мягко. Будто говоря: {i}«Ещё одно неверное слово, и оно станет последним.»{/i}" (show_side="none", show_kind="speech")

        show eveina thinking at eveina_left
        ev_thought "Чёрт возьми, как заставить тебя доверять мне?" (show_side="left", show_kind="thought")
        hide eveina
        show eveina normal at eveina_left
        ev "Эриан, я пришла сюда показать тебе этот отчёт, прекрасно понимая, как ты можешь на него отреагировать." (show_side="left", show_kind="speech")
        ev "Мне было чертовски страшно делать это, и всё же я здесь." (show_side="left", show_kind="speech")
        ev "Потому что я выбрала сторону. Теперь выбор за тобой..." (show_side="left", show_kind="speech")
        hide eveina

        show erian annoyed at erian_right
        er "Я свой выбор давно сделал." (show_side="right", show_kind="speech")
        hide erian

        show eveina angry at eveina_left
        ev "Тогда либо отпусти меня, либо... не знаю." (show_side="left", show_kind="speech")
        ev "Сделай хоть что-то! Потому что я безумно устала чувствовать себя как в ловушке рядом с тобой." (show_side="left", show_kind="speech")
        hide eveina

        n "Наступило молчание, прерываемое лишь тяжёлыми вдохами, неровным биением сердца и плавящейся под его прикосновениями кожей." (show_side="none", show_kind="speech")
        n "Янтарный взгляд прожигал насквозь, будто в надежде где-то глубоко под кожей найти ответы на вопросы, которые никто не задавал вслух." (show_side="none", show_kind="speech")
        
        show erian intrigued at erian_right
        er "Может, мне нравится, когда ты ощущаешь себя в ловушке." (show_side="right", show_kind="speech")
        hide erian

        show eveina angry at eveina_left
        ev "Это твой ответ?" (show_side="left", show_kind="speech")
        hide eveina

        show erian normal at erian_right
        er "Хочешь услышать мой ответ?" (show_side="right", show_kind="speech")
        er "Я просто не привык брать, пока не уверен, что это — моё." (show_side="right", show_kind="speech")
        hide erian

        n "Он медленно провёл тыльной стороной пальцев по её щеке, как будто проверяя, насколько она готова принадлежать ему." (show_side="none", show_kind="speech")
        n "Затем — по линии шеи, скользя вниз, к ключице. Неспешно, наблюдая за реакцией." (show_side="none", show_kind="speech")
        n "Наклонился к её шее и оставил на ней мимолётный укус, тут же проведя по оставшемуся следу языком, а потом снова вернулся взглядом к губам." (show_side="none", show_kind="speech")

        show erian normal at erian_right
        er "Мы оба на эмоциях. И я вижу, чего ты добиваешься. А у меня закончились и аргументы, и терпение." (show_side="right", show_kind="speech")
        er "Но если я уступлю — это ничего между нами не изменит. Ты уверена?" (show_side="right", show_kind="speech")
        hide erian

        n "Её дыхание сбилось. Но она не отвела взгляда, и в них он видел согласие." (show_side="none", show_kind="speech")
        n "И в следующий момент его губы смяли её — твёрдо, безжалостно, дико в своей власти. Эвейна лишь успела издать приглушенный стон." (show_side="none", show_kind="speech")
        n "Его тело прижалось к ней всем весом, бедра — впритык, ни сантиметра воздуха между ними." (show_side="none", show_kind="speech")
        n "Рука, уверенно скользнувшая вверх по её талии, проникла под одежду. Горячая ладонь обхватила кожу на рёбрах и заскользила вверх, к груди." (show_side="none", show_kind="speech")
        n "Эвейна ответила сразу — без остатка, без сомнений. Её губы изучали его, пальцы вплетались в его волосы, притягивая ближе. Всем телом она прижалась к нему, выгибаясь навстречу." (show_side="none", show_kind="speech")
        n "Одежда мешала, но она будто не замечала этого — имело значение только кожа под его ладонью, только прерывистое биение её сердца, отбивающего ритм где-то в горле." (show_side="none", show_kind="speech")
        n "Поцелуй стал глубже. Эриан не просил — он утверждал. Его язык вошёл в её рот с точной, хищной уверенностью, а губы не отпускали ни на секунду — требовательно, почти жестоко." (show_side="none", show_kind="speech")
        n "Мир сузился до ощущения того, как его рука ласкала её тело. До низкого, едва слышного стона в его горле. До её дрожащего вздоха, когда пальцы дотронулись до нижнего края груди." (show_side="none", show_kind="speech")
        n "Когда её тело выгнулось ему навстречу, всё вокруг вдруг изменилось." (show_side="none", show_kind="speech")
        n "Начало дрожать. Не от страсти. Из-за него. Сквозь опущенные ресницы Эвейна заметила какой-то свет." (show_side="none", show_kind="speech")
        n "Она замерла. Его глаза внезапно распахнулись. И они — сияли. Буквально. Радужки испускали золотое свечение, а зрачки стали узкими, вертикальными." (show_side="none", show_kind="speech")
        n "Но даже не это было самым удивительным." (show_side="none", show_kind="speech")
        n "Трава на поляне, нависающие над ними ветви дерева — всё вокруг также светилось этим золотистым светом." (show_side="none", show_kind="speech")
        n "Он поймал её застывший взгляд — и тут же отшатнулся. Не потому что испугался. А потому что на секунду потерял контроль." (show_side="none", show_kind="speech")
    
        show erian annoyed at erian_right
        er "Проклятье." (show_side="right", show_kind="speech")
        hide erian

        n "Эвейна лишь успела заметить непонятное выражение на его лице, когда он поспешно отвернулся." (show_side="none", show_kind="speech")
        n "Стоя к ней спиной, он тяжело дышал, плечи дрожали в стальном напряжении. Его пальцы сжались в кулаки. Он не говорил ни слова." (show_side="none", show_kind="speech")
        n "Эвейна удивленно смотрела, как свечение вокруг медленно тает в темноте, а потом сделала шаг вперед и обхватила маленькой ладонью его запястье." (show_side="none", show_kind="speech")

        show eveina normal at eveina_left
        ev "Эриан…" (show_side="left", show_kind="speech")
        hide eveina

        n "Он молчал, не смотря на неё, но его пальцы, дрогнув на секунду в сомнении, следом переплелись с её." (show_side="none", show_kind="speech")
        n "Словно говорили: {i}«Ты всё ещё нужна мне. Просто молчи об этом.»{/i}" (show_side="none", show_kind="speech")

    elif erian_first_kiss == False:
        show eveina upset thinking at eveina_left
        ev "Чтобы ты размышлял логически." (show_side="left", show_kind="speech")
        hide eveina

        show erian thinking at erian_right
        er "Логически, говоришь..." (show_side="right", show_kind="speech")
        hide erian  

        n "Эриан сделал шаг назад, вскинув подбородок и смотря на неё свысока, отчего ей вдруг захотелось вжаться в ствол дерева позади неё." (show_side="none", show_kind="speech")

        show erian annoyed at erian_right
        er "Ну давай прикинем {i}логически{/i}..." (show_side="right", show_kind="speech")
        hide erian 
        show erian thinking at erian_right
        er "Ты только что нашла своё лекарство, Эвейна. Вот оно, течёт в моих венах!" (show_side="right", show_kind="speech")
        er "Нужно всего лишь посадить меня на поводок — и твой отец будет здоров." (show_side="right", show_kind="speech")
        hide erian  
        show erian eyebrow at erian_right
        er "Разве не этого ты так хотела? Разве не готова была пожертвовать многим ради спасения своего отца?" (show_side="right", show_kind="speech")
        hide erian  
        show erian smile wild at erian_right
        er "Так как ты можешь судить того, кто сделал тоже самое? Чем ты от него отличаешься?" (show_side="right", show_kind="speech")
        er "Чего ты ожидала вообще, придя сюда? Что я прочитаю это и сам застегну на себе ошейник?" (show_side="right", show_kind="speech")
        hide erian

        n "Девушка дернулась как от пощечины. Глаза сердито уставились на него, а руки сжались в кулаки от внезапного желания стереть с его лица эту кривую надменную ухмылку." (show_side="none", show_kind="speech")

        show eveina angry at eveina_left
        ev "А не пойти ли тебе к чёрту, Эриан?" (show_side="left", show_kind="speech")
        ev "Не ожидала, что ты предашь меня так же быстро, как тебя предал Да..." (show_side="left", show_kind="speech")
        hide eveina

        n "Метнувшийся в неё обжигающий своей яростью взгляд заставил её замолчать. Эриан больше не улыбался." (show_side="none", show_kind="speech")
        n "Безумная мысль о том, что ей удалось таки лишить его привычного оскала, отчего-то совсем не принесла облегчения." (show_side="none", show_kind="speech")

        show erian annoyed at erian_right
        er "А с чего бы вдруг мне оставаться на твоей стороне?" (show_side="right", show_kind="speech")
        hide erian

        show eveina angry at eveina_left
        ev "Потому что не все люди одинаковы!" (show_side="left", show_kind="speech")
        hide eveina

        show erian annoyed at erian_right
        er "У меня сложилось обратное впечатление." (show_side="right", show_kind="speech")
        hide erian

        show eveina angry at eveina_left
        ev "Ты просто невыносим..." (show_side="left", show_kind="speech")
        hide eveina

        n "Эвейна инстинктивно сглотнула, когда он сделал угрожающий шаг в её сторону. Всем своим видом говоря: {i}«Ещё одно неверное слово, и оно станет последним.»{/i}" (show_side="none", show_kind="speech")

        show eveina thinking at eveina_left
        ev_thought "Чёрт возьми, как заставить тебя доверять мне?" (show_side="left", show_kind="thought")
        hide eveina
        show eveina normal at eveina_left
        ev "Эриан, я пришла сюда показать тебе этот отчёт, прекрасно понимая, как ты можешь на него отреагировать." (show_side="left", show_kind="speech")
        ev "Мне было чертовски страшно делать это, и всё же я здесь." (show_side="left", show_kind="speech")
        ev "Потому что я выбрала сторону. Теперь выбор за тобой..." (show_side="left", show_kind="speech")
        hide eveina

        show erian annoyed at erian_right
        er "Я свой выбор давно сделал." (show_side="right", show_kind="speech")
        hide erian

        show eveina angry at eveina_left
        ev "Тогда либо помоги мне, либо..." (show_side="left", show_kind="speech")
        ev "Хотя, знаешь... просто катись к чёрту! Справлюсь са..." (show_side="left", show_kind="speech")
        hide eveina

        n "Последнее слово застряло где-то в глотке, когда ладонь Эриана врезалась в ствол дерева в нескольких сантиметрах от её лица." (show_side="none", show_kind="speech")
        n "Эвейна невольно зажмурилась. Осознание, что и кому она только что выкрикнула медленно накатывалось на неё вместе с волнами паники от звука тяжелого дыхания у её макушки." (show_side="none", show_kind="speech")
        n "Эриан почти ласково положил руку на её шею, сжимая некрепко, но очень убедительно. Слегка встряхнул, желая заставить смотреть на него. Но от страха у девушки будто свело мыщцы и она никак не могла распахнуть глаза." (show_side="none", show_kind="speech")
        n "Вкладчивый шепот коснулся её слуха, заставив задрожать всем телом." (show_side="none", show_kind="speech")

        show erian annoyed at erian_right
        er "Забыла с кем говоришь?" (show_side="right", show_kind="speech")
        hide erian

        show eveina sad at eveina_left
        ev_thought "Дура! Дура, дура, дура!" (show_side="left", show_kind="thought")
        hide eveina
        show eveina upset thinking at eveina_left
        ev_thought "Он же не..." (show_side="left", show_kind="thought")
        hide eveina

        show erian wild smile at erian_right
        er "Напомнить тебе, благодаря кому ты смогла добраться до тех крупиц правды, что есть у тебя сейчас?" (show_side="right", show_kind="speech")
        er "Могу забрать все воспоминания о них..." (show_side="right", show_kind="speech")
        hide erian

        show eveina upset thinking at eveina_left
        ev_thought "Нет, пожалуйста, только не это..." (show_side="left", show_kind="thought")
        hide eveina

        n "Страх поглотил её целиком. Всё тело будто завибрировало в такт её тихому хрипу, что вырвался из горла, когда пальцы сжали шею чуть сильнее." (show_side="none", show_kind="speech")

        show erian annoyed at erian_right
        er "Или лучше заставить тебя забыть о своём отце?" (show_side="right", show_kind="speech")
        hide erian

        n "Осознав сказанное, Эвейна резко распахнула глаза. И застыла в изумлении. Взгляд Эриана был совсем рядом, прожигал её своей яростью и — сиял. Буквально. Радужки испускали золотое свечение, а зрачки стали узкими, вертикальными." (show_side="none", show_kind="speech")
        n "Но даже не это было самым удивительным. Трава на поляне, нависающие над ними ветви дерева — всё вокруг также светилось этим золотистым светом." (show_side="none", show_kind="speech")
        n "Он поймал её застывший взгляд — и тут же отшатнулся. Не потому что испугался показаться таким. А потому что понял, что потерял контроль." (show_side="none", show_kind="speech")

        show erian annoyed at erian_right
        er "Проклятье." (show_side="right", show_kind="speech")
        hide erian

        n "Эвейна лишь успела заметить непонятное выражение на его лице, когда он поспешно отвернулся." (show_side="none", show_kind="speech")
        n "Стоя к ней спиной, он тяжело дышал, плечи дрожали в стальном напряжении. Его пальцы сжались в кулаки. Он не говорил ни слова." (show_side="none", show_kind="speech")

        show eveina sad at eveina_left
        ev "Эриан…" (show_side="left", show_kind="speech")
        hide eveina

        show erian annoyed at erian_right
        er "Убирайся." (show_side="right", show_kind="speech")
        hide erian

        show eveina upset thinking at eveina_left
        ev_thought "Нельзя уходить... нельзя позволить ему отнять то, что у меня есть..." (show_side="left", show_kind="thought")
        hide eveina

        n "Эвейна удивленно смотрела, как свечение вокруг медленно тает в темноте, а потом сделала шаг вперед и коснулась его локтя." (show_side="none", show_kind="speech")

        show eveina sad at eveina_left
        ev "Эриан... извини меня." (show_side="left", show_kind="speech")
        hide eveina

        show erian annoyed at erian_right
        er "Уходи, Эвейна." (show_side="right", show_kind="speech")
        hide erian

        show eveina eyebrow at eveina_left
        ev "Нет. Мы далеко зашли. И чтобы тут не произошло, оно не должно помешать нам достичь цели." (show_side="left", show_kind="speech")
        show eveina annoyed at eveina_left
        ev "Я остаюсь. И ты тоже." (show_side="left", show_kind="speech")
        hide eveina

        n "Маленькая ладонь неуверенно обхватила его запястье. Эриан молчал, не смотря на неё, но его пальцы, дрогнув на секунду в сомнении, следом переплелись с её." (show_side="none", show_kind="speech")
        n "Словно говорили: {i}«Ты права. Просто молчи.»{/i}" (show_side="none", show_kind="speech")

    n "Некоторое время они просто стояли. Наконец, тяжело вздохнув, он расправил плечи и вновь посмотрел на неё. От свечения не осталось и следа." (show_side="none", show_kind="speech")
    n "Его взгляд пробежался по её лицу, ища намеки на страх или сожаление. И не найдя их, он хрипло произнес:" (show_side="none", show_kind="speech")

    show erian normal at erian_right
    er "Пойдем. Провожу." (show_side="right", show_kind="speech")
    hide erian

    n "Без слов они дошли до общежития." (show_side="none", show_kind="speech")

    show erian normal at erian_right
    er "Спокойной ночи, Эвейна." (show_side="right", show_kind="speech")
    hide erian

    n "Он только кивнул и ушёл в ночь, не дожидаясь ответа. Эвейна осталась стоять, задумчиво наблюдая за скрывающейся в тенях фигурой." (show_side="none", show_kind="speech")

    show eveina upset thinking at eveina_left
    ev_thought "Ну что, гордишься собой, Эвейна?" (show_side="left", show_kind="thought")
    hide eveina
    show eveina thinking at eveina_left
    ev_thought "По своей же прихоти чуть не лишилась союзника, информации, которую нашла, а то и своей памяти." (show_side="left", show_kind="thought")

    if erian_first_kiss == True:
        ev_thought "В попытке успокоить — вывела его из себя. А потом этот поцелуй..." (show_side="left", show_kind="thought")
        hide eveina
        show eveina eyeroll at eveina_left
        ev_thought "Чёрт, как это произошло? О чём я только думала?" (show_side="left", show_kind="thought")
        hide eveina
    elif erian_first_kiss == False:
        ev_thought "В попытке успокоить — вывела его из себя. А потом..." (show_side="left", show_kind="thought")
        hide eveina
        show eveina eyeroll at eveina_left
        ev_thought "Чёрт, о чём я только думала? Что, если бы он не остановился?" (show_side="left", show_kind="thought")
        ev_thought "Что, если бы и правда стёр память о папе?" (show_side="left", show_kind="thought")
        hide eveina

    show eveina upset thinking at eveina_left
    ev_thought "Сегодня я была на грани. Знала же, кто он и как опасен. Но с чего-то взяла, что честность — это выход..." (show_side="left", show_kind="thought")
    ev_thought "Слишком глупо. Слишком необдуманно. Так нельзя." (show_side="left", show_kind="thought")   
    hide eveina
    show eveina annoyed at eveina_left
    ev_thought "К чёрту честность. К чёрту попытки быть «правильной»." (show_side="left", show_kind="thought")
    ev_thought "Не хочется этого признавать, но Эриан был прав, когда говорил, что все в Академии либо скрывают что-то, либо пытаются узнать чужие секреты. Другие здесь просто не выживают." (show_side="left", show_kind="thought")
    ev_thought "Не стану умнее прямо сейчас — и пойду в расход." (show_side="left", show_kind="thought")
    hide eveina

    n "Эвейна опустила взгляд на дрожащие пальцы и медленно сжала их в кулак." (show_side="none", show_kind="speech")

    show eveina upset thinking at eveina_left
    ev_thought "Я же справлюсь, правда?" (show_side="left", show_kind="thought")
    hide eveina 

    jump scene_6_2
