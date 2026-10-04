label scene_3_2:
    $ previous_scene = "scene_3_1"
    $ next_scene = "scene_3_3"
    $ current_scene = "scene_3_2"

    # =========================================================
    # СЦЕНА 3_2 — «САД / ЭРИАН / УСЛОВИЕ»
    # Структура: ярость после Каэля → сад → трава → Эриан спасает
    #            → развилка → вопрос о Далоне → условие (три года)
    #            → «этика стала переменной» → уходит → рефлексия
    # Близко к оригинальной scene_3_3.
    # Отличие: Эвейна идёт не к Эриану — она идёт от Каэля.
    # Книги в сумке нет — кража была в Гл.2.
    # =========================================================

    call fade_to_black(1.2, 0.8)
    scene bg corridor at bg_fullscreen with dissolve
    # play music "bgm/corridor_tension.ogg" fadein 2.0

    n "Коридор был пуст. Эвейна шла, не разбирая пути." (show_side="none", show_kind="speech")

    show eveina annoyed at eveina_left
    ev_thought "Многие даже не пытались..." (show_side="left", show_kind="thought")
    hide eveina
    show eveina angry at eveina_left
    ev_thought "А когда я попыталась — меня выставили за дверь." (show_side="left", show_kind="thought")
    ev_thought "На глазах у всех." (show_side="left", show_kind="thought")
    hide eveina
    show eveina upset thinking at eveina_left
    ev_thought "За что?" (show_side="left", show_kind="thought")
    hide eveina

    n "Шаги становились резче. Она не замечала этого." (show_side="none", show_kind="speech")

    show eveina upset thinking at eveina_left
    ev_thought "Чем я это заслужила? Тем, что не сдалась?" (show_side="left", show_kind="thought")
    hide eveina
    show eveina angry at eveina_left
    ev_thought "Что я сделала этому надменному куску аугментированного..." (show_side="left", show_kind="thought")
    hide eveina

    n "Додумать мысль до конца не вышло. Впереди оказалась дверь в сад." (show_side="none", show_kind="speech")
    n "Она толкнула её, не останавливаясь." (show_side="none", show_kind="speech")

    # --- Сад ---

    scene bg garden at bg_fullscreen with dissolve
    # play music "bgm/sunset_mystery.ogg" fadein 2.0

    n "Закатное солнце скользило мягким светом по коже — Эвейна опустилась у самого края воды, не выбирая места." (show_side="none", show_kind="speech")
    n "Всё вокруг дышало умиротворением: трава пружинила под ладонью, озеро сияло бликами, воздух был насыщен влажным запахом земли и зелени." (show_side="none", show_kind="speech")
    n "Внутри — не было ничего похожего." (show_side="none", show_kind="speech")

    show eveina angry at eveina_left
    ev_thought "Один только Каэль чего стоит." (show_side="left", show_kind="thought")
    hide eveina
    show eveina annoyed at eveina_left
    ev_thought "Или эти накрахмаленные студентики с бесконечно надменными выражениями лиц." (show_side="left", show_kind="thought")
    hide eveina
    show eveina eyebrow at eveina_left
    ev_thought "Хотя эта планета в целом сильно давит на мой уровень нормы." (show_side="left", show_kind="thought")
    hide eveina

    n "Злость уходила медленно — как вода сквозь песок. Неохотно." (show_side="none", show_kind="speech")
    n "Она откинулась назад, упёршись локтями в траву, и уставилась в небо." (show_side="none", show_kind="speech")
    n "Рядом был куст с тонкими стеблями и мелкими игольчатыми листьями." (show_side="none", show_kind="speech")
    n "Рассеянно потянулась к ближайшему — сорвала, не думая, сунула в рот." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev_thought "Прямо как на ферме у тёти, куда мы ездили с папой в детстве." (show_side="left", show_kind="thought")
    hide eveina

    n "Улыбка мелькнула — и тут же исчезла. Что-то пошло не так." (show_side="none", show_kind="speech")
    n "Сначала лёгкое покалывание на языке. Потом — жжение." (show_side="none", show_kind="speech")
    n "Спустя мгновение рот вспыхнул огнём." (show_side="none", show_kind="speech")

    show eveina wondered at eveina_left
    ev_thought "Ммф..." (show_side="left", show_kind="thought")
    hide eveina

    n "Эвейна резко наклонилась, кашляя, пытаясь избавиться от жгучей зелени. Глаза заслезились, она схватилась за горло." (show_side="none", show_kind="speech")
    n "Именно в этот момент сбоку раздался лёгкий, уверенный шаг." (show_side="none", show_kind="speech")

    show erian normal at erian_right
    er "..." (show_side="right", show_kind="speech")
    hide erian

    show eveina wondered at eveina_left
    ev_thought "О боже, только не сейчас..." (show_side="left", show_kind="thought")
    hide eveina

    n "В несколько точных движений Эриан оказался позади, опустился на траву и, не спрашивая, притянул Эвейну к себе. Её плечи оказались у него на коленях, а затылок — на его бедре." (show_side="none", show_kind="speech")
    n "Он придерживал её голову — мягко, но крепко, не позволяя подняться. Аккуратно убрал её руки с шеи. Расстегнул две верхние пуговицы рубашки." (show_side="none", show_kind="speech")
    n "Эвейна не сопротивлялась — если не считать судорог и учащённого дыхания." (show_side="none", show_kind="speech")
    n "Сквозь плёнку из слёз она видела, как он хмурится, глядя на неё сверху вниз. Оглядывается вокруг, будто ищет что-то в траве. Возвращается взглядом к ней." (show_side="none", show_kind="speech")
    n "Не теряя ни секунды, Эриан сорвал с земли несколько травинок, разминая их между пальцами." (show_side="none", show_kind="speech")
    n "Прежде чем Эвейна успела понять, что он делает — точным движением засунул измятую смесь ей в рот и бесцеремонно захлопнул его, придерживая за подбородок." (show_side="none", show_kind="speech")
    n "Рот вскипел во второй раз. Страшная мысль прошила сознание." (show_side="none", show_kind="speech")

    show eveina angry at eveina_left
    ev_thought "Господи, этот псих решил меня прикончить!" (show_side="left", show_kind="thought")
    hide eveina

    n "Глаза на миг вспыхнули уничтожающим взглядом. А потом..." (show_side="none", show_kind="speech")
    n "Горечь отступила. Прохлада проникла внутрь. Эвейна сглотнула и тяжело выдохнула — впервые за долгую минуту." (show_side="none", show_kind="speech")
    n "Её затылок всё ещё покоился у него на коленях, придерживаемый его рукой. Она чувствовала, как его дыхание касается её щеки." (show_side="none", show_kind="speech")
    n "На лице Эриана играла знакомая полуухмылка, но взгляд был серьёзнее, чем обычно." (show_side="none", show_kind="speech")
    n "Он не делал ни одного лишнего движения — но она отчётливо ощущала: слегка поглаживая запястья, внимательно наблюдая за её взглядом и дыханием, он контролировал каждую реакцию её организма." (show_side="none", show_kind="speech")

    show eveina eyebrow at eveina_left
    ev_thought "Он что, выглядит обеспокоенным?" (show_side="left", show_kind="thought")
    hide eveina

    n "Стоило ей задуматься об этом, как Эриан тут же вернулся к прежнему себе. Голос зазвучал лениво, с ноткой раздражения." (show_side="none", show_kind="speech")

    show erian thinking at erian_right
    er "Заскучала по остроте ощущений?" (show_side="right", show_kind="speech")
    hide erian
    show erian eyebrow at erian_right
    er "Не обязательно было совать в рот что попало." (show_side="right", show_kind="speech")
    hide erian

    n "Голос Эвейны слегка хрипел." (show_side="none", show_kind="speech")

    show eveina normal at eveina_left
    ev "Я… просто задумалась." (show_side="left", show_kind="speech")
    hide eveina

    show erian intrigued at erian_right
    er "Обо мне?" (show_side="right", show_kind="speech")
    hide erian

    n "Она закатила глаза. Никакой страх перед этим человеком сейчас не встал бы между ней и необходимостью ответить." (show_side="none", show_kind="speech")

    show eveina eyeroll at eveina_left
    ev "Да, Эриан, ведь именно мысли о тебе вызывают во мне желание самоубиться." (show_side="left", show_kind="speech")
    hide eveina
    show eveina thinking at eveina_left
    ev_thought "Ну не прибьёт же он меня сразу после того, как спас?" (show_side="left", show_kind="thought")
    hide eveina
    show eveina intrigued at eveina_left
    ev_thought "А даже если так — это того стоило." (show_side="left", show_kind="thought")
    hide eveina

    n "Эриан криво усмехнулся. С вызовом, с тенью насмешки — и с лёгким интересом. Эвейна зацепилась взглядом за последнее." (show_side="none", show_kind="speech")

    show eveina wondered at eveina_left
    ev_thought "Он и правда играет со мной." (show_side="left", show_kind="thought")
    hide eveina
    show eveina thinking at eveina_left
    ev_thought "И чёрт бы его побрал, ему это нравится." (show_side="left", show_kind="thought")
    hide eveina

    show eveina eyebrow at eveina_left

    $ play_along_with_erian = renpy.call_screen("choice",
    items=[
    ("Стоит попробовать.", True),
    ("О, нет, спасибо, хватило с меня одного укуса.", False)
    ], who="Эвейна", what="{i}Интересно, а что если я подыграю?{/i}", _last_say_who="ev_thought")
    hide eveina

    if play_along_with_erian == True:

        n "Дыхание уже выровнялось, хрипы ушли — лишь горло немного саднило." (show_side="none", show_kind="speech")
        n "Рука Эриана лежала на её плече, а большой палец, еле касаясь, поглаживал кожу в изгибе шеи." (show_side="none", show_kind="speech")
        n "Отчего-то его ухмылка уже не казалась такой пугающей, а её поза — такой уж неуместной." (show_side="none", show_kind="speech")
        n "И тогда она прикрыла глаза, слегка склонив голову к его руке — так, что вся его ладонь оказалась на её шее." (show_side="none", show_kind="speech")
        n "Через прикрытые ресницы она видела, как его брови сошлись на переносице, зрачки расширились, а взгляд стал слегка удивлённым. Но руку он так и не убрал." (show_side="none", show_kind="speech")
        n "Наоборот — пальцы еле ощутимым движением начали поглаживать кожу, отчего та мгновенно покрылась мурашками." (show_side="none", show_kind="speech")
        n "Эриан как загипнотизированный смотрел на движение собственных пальцев, словно не верил, что это делает он. С каждым движением взгляд темнел, а ладонь медленно сползала вниз и достигла ключицы." (show_side="none", show_kind="speech")
        n "Лишь задев воротник рубашки, он вдруг остановился и нахмурился ещё больше." (show_side="none", show_kind="speech")
        n "Девушка облизнула губы, наслаждаясь вкусом маленькой победы. До тех пор, пока он не нагнулся чуть ниже, чтобы почти ласково произнести:" (show_side="none", show_kind="speech")

        show erian smile wild at erian_right
        er "В следующий раз выбирай яд посильнее. Эта попытка выглядела жалкой." (show_side="right", show_kind="speech")
        hide erian

        n "По телу пробежал разряд. Глаза девушки широко распахнулись, уткнувшись в его губы, чуть дрогнувшие от её реакции." (show_side="none", show_kind="speech")
        n "Играть с Эрианом в какие бы то ни было игры моментально расхотелось." (show_side="none", show_kind="speech")

        show eveina thinking at eveina_left
        ev_thought "Чёрт, что там было про «не подставлять шею»?" (show_side="left", show_kind="thought")
        hide eveina
        show eveina normal at eveina_left
        ev_thought "Надо встать. Немедленно." (show_side="left", show_kind="thought")
        hide eveina

        n "Но тело не двигалось. В её глазах промелькнул намёк на страх, что не ускользнуло от его взгляда. Уголок губы Эриана снова пополз вверх, обнажая клык." (show_side="none", show_kind="speech")
        n "Парень медленно, будто завороженный собственным действием, провёл большим пальцем от ключицы до самого подбородка." (show_side="none", show_kind="speech")

    elif play_along_with_erian == False:

        n "Дыхание уже выровнялось, хрипы ушли — лишь горло немного саднило." (show_side="none", show_kind="speech")
        n "Рука Эриана лежала на её плече, а большой палец, еле касаясь, поглаживал кожу в изгибе шеи." (show_side="none", show_kind="speech")
        n "Отчего-то его ухмылка уже не казалась такой пугающей, а её поза — такой уж неуместной." (show_side="none", show_kind="speech")

        show eveina thinking at eveina_left
        ev_thought "Помнится, что-то там было про «не подставлять шею»?" (show_side="left", show_kind="thought")
        hide eveina
        show eveina normal at eveina_left
        ev_thought "Надо встать. Немедленно." (show_side="left", show_kind="thought")
        hide eveina

        n "Но тело не двигалось. В её глазах промелькнул намёк на панику, что не ускользнуло от его взгляда. Уголок губы Эриана снова пополз вверх, обнажая клык." (show_side="none", show_kind="speech")
        n "Ладонь аккуратно опустилась на её плечо — давая ясно понять, что ей некуда бежать." (show_side="none", show_kind="speech")

    # --- Общий финал обеих веток ---

    show erian intrigued at erian_right
    er "Знаешь, что самое восхитительное в тебе, Эвейна?" (show_side="right", show_kind="speech")
    hide erian

    show eveina intrigued at eveina_left
    ev_thought "Правильный ответ — всё?" (show_side="left", show_kind="thought")
    hide eveina

    show erian smile wild at erian_right
    er "Ты не знаешь, когда нужно бояться." (show_side="right", show_kind="speech")
    hide erian

    n "Только насладившись сполна реакцией девушки, Эриан убрал руку, позволив ей сесть и опереться на ствол дерева." (show_side="none", show_kind="speech")
    n "Расстояние между ними оставалось вызывающе маленьким." (show_side="none", show_kind="speech")
    n "Эвейна молчала, затаившись. Он тоже не делал попыток заговорить." (show_side="none", show_kind="speech")
    n "И в этом молчании жило нечто большее — вопрос, который давно искал выхода." (show_side="none", show_kind="speech")

    show eveina eyebrow at eveina_left
    ev "Почему ты всегда оказываешься рядом?" (show_side="left", show_kind="speech")
    hide eveina

    show erian normal at erian_right
    er "Ты удивительно предсказуемая." (show_side="right", show_kind="speech")
    hide erian
    show erian thinking at erian_right
    er "Но ты слишком эффектно задыхалась." (show_side="right", show_kind="speech")
    hide erian
    show erian intrigued at erian_right
    er "Я подумал: если уже наблюдаю за трагедией, то почему бы не взять в руки режиссуру?" (show_side="right", show_kind="speech")
    hide erian

    n "Он провёл тыльной стороной ладони по краю её рукава — лёгкое движение, от которого кожа снова вспыхнула мурашками." (show_side="none", show_kind="speech")
    n "Эвейна замерла. Готовая сбежать — и не двигалась." (show_side="none", show_kind="speech")

    # --- Вопрос о Далоне ---

    show eveina annoyed at eveina_left
    ev "Зачем ты вообще здесь?" (show_side="left", show_kind="speech")
    hide eveina

    n "Она одёрнула себя. Смысла врать не было. Втянула воздух ноздрями и на выдохе выпалила:" (show_side="none", show_kind="speech")

    show eveina eyebrow at eveina_left
    ev "Кто такой Кайр Далон?" (show_side="left", show_kind="speech")
    hide eveina

    n "Непроницаемый взгляд Эриана резко упёрся в неё. В полной тишине он просто смотрел — слишком долго, чтобы это было просто «Не знаю»." (show_side="none", show_kind="speech")
    n "Затем встал, отряхнул ладони от травы и, не оборачиваясь, произнёс:" (show_side="none", show_kind="speech")

    show erian eyebrow at erian_right
    er "Умно. Но ты затеяла опасную игру." (show_side="right", show_kind="speech")
    er "Поговорим, когда ты сама захочешь ответить на мои вопросы." (show_side="right", show_kind="speech")
    hide erian

    show eveina wondered at eveina_left
    ev_thought "Вот оно..." (show_side="left", show_kind="thought")
    ev_thought "Сейчас он всё расскажет!" (show_side="left", show_kind="thought")
    hide eveina

    show eveina eyebrow at eveina_left
    ev "И что за вопросы?" (show_side="left", show_kind="speech")
    hide eveina

    show erian normal at erian_right
    er "Расскажи, что здесь произошло три года назад." (show_side="right", show_kind="speech")
    hide erian

    show eveina wondered at eveina_left
    ev_thought "Три года назад?" (show_side="left", show_kind="thought")
    hide eveina
    show eveina thinking at eveina_left
    ev_thought "О чём он вообще?" (show_side="left", show_kind="thought")
    hide eveina

    show eveina normal at eveina_left
    ev "Я не знаю, что произошло три года назад." (show_side="left", show_kind="speech")
    ev "Меня здесь тогда не было." (show_side="left", show_kind="speech")
    hide eveina

    n "Долгие секунды две пары глаз сверлили друг друга." (show_side="none", show_kind="speech")
    n "Эриан смотрел на неё так, будто проверял — не врёт ли. А она и правда не врала." (show_side="none", show_kind="speech")

    show erian eyebrow at erian_right
    er "Тогда узнай." (show_side="right", show_kind="speech")
    hide erian

    n "Пауза. Она понимала, что он тоже ищет ответ — но другой. И что у него его нет." (show_side="none", show_kind="speech")
    n "Это меняло расстановку сил." (show_side="none", show_kind="speech")

    show eveina eyebrow at eveina_left
    ev_thought "Он ищет так же, как и я. Только не то же самое." (show_side="left", show_kind="thought")
    hide eveina

    n "Девушка открыла рот, чтобы спросить дальше. Но Эриан обернулся — и в его взгляде проскользнуло что-то новое. Что-то, похожее на ярость." (show_side="none", show_kind="speech")
    n "И под этим взглядом ни один звук из её рта так и не посмел вылететь." (show_side="none", show_kind="speech")

    show erian normal at erian_right
    er "В Академии есть двери, за которыми этика давно стала переменной." (show_side="right", show_kind="speech")
    er "И мне неважно, покрываешь ты их или ведёшь свою собственную игру." (show_side="right", show_kind="speech")
    hide erian
    show erian thinking at erian_right
    er "Возвращайся, когда у тебя будут ответы." (show_side="right", show_kind="speech")
    hide erian
    show erian normal at erian_right
    er "Тогда ты, возможно, окажешься полезной." (show_side="right", show_kind="speech")
    hide erian

    n "Он сделал шаг назад. Закат окрасил его лицо золотым светом." (show_side="none", show_kind="speech")

    show erian normal at erian_right
    er "До встречи, Эвейна." (show_side="right", show_kind="speech")
    hide erian
    show erian thinking at erian_right
    er "Посоветовал бы тебе быть разумнее. Но это ведь не про тебя, верно?" (show_side="right", show_kind="speech")
    hide erian
    show erian intrigued at erian_right
    er "Мне даже интересно, сколько слоёв ещё вскроется, прежде чем ты сломаешься." (show_side="right", show_kind="speech")
    hide erian

    n "Он исчез между деревьями так же внезапно, как появился." (show_side="none", show_kind="speech")
    n "А она осталась сидеть у дерева. Без ответов. Зато с новым вопросом, который теперь пульсировал в ней." (show_side="none", show_kind="speech")

    # --- Рефлексия ---

    show eveina upset thinking at eveina_left
    ev_thought "Итак, пришла за ответами, а получила только больше вопросов..." (show_side="left", show_kind="thought")
    hide eveina
    show eveina eyebrow at eveina_left
    ev_thought "«Этика стала переменной»… что он имел в виду?" (show_side="left", show_kind="thought")
    hide eveina
    show eveina thinking at eveina_left
    ev_thought "И что произошло три года назад? Почему он не может найти это сам?" (show_side="left", show_kind="thought")
    hide eveina
    show eveina annoyed at eveina_left
    ev_thought "И с чего это я вдруг стану полезной, только если узнаю ответ?" (show_side="left", show_kind="thought")
    hide eveina
    show eveina eyebrow at eveina_left
    ev_thought "Я вообще-то всегда полезна. Польза — моё второе..." (show_side="left", show_kind="thought")
    hide eveina
    show eveina thinking at eveina_left
    ev_thought "Так, не отвлекайся." (show_side="left", show_kind="thought")
    hide eveina
    show eveina eyebrow at eveina_left
    ev_thought "Это как-то связано с Далоном? Поэтому Эриан и читал те старые книги?" (show_side="left", show_kind="thought")
    hide eveina
    show eveina thinking at eveina_left
    ev_thought "Мне нужно что-то, что я могу использовать в качестве козыря..." (show_side="left", show_kind="thought")
    hide eveina
    show eveina normal at eveina_left
    ev_thought "Хотя, он так смотрел — на секунду мне показалось, что этим козырем могу быть я сама." (show_side="left", show_kind="thought")
    hide eveina
    show eveina eyeroll at eveina_left
    ev_thought "Впрочем, рассчитывать на такую удачу было бы глупо." (show_side="left", show_kind="thought")
    ev_thought "Нужно что-то другое. Вопрос только — что." (show_side="left", show_kind="thought")
    hide eveina

    n "Эвейна ещё некоторое время сидела под деревом, наблюдая за тем, как горизонт поглощает жёлтый диск солнца." (show_side="none", show_kind="speech")
    n "Ответ на последний вопрос так и не появился сам собой." (show_side="none", show_kind="speech")
    n "Значит, надо идти за ним." (show_side="none", show_kind="speech")

    jump scene_3_3
