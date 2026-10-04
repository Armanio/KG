label scene_7_4:
    $ previous_scene = "scene_7_3"
    $ next_scene = "scene_7_5"
    $ current_scene = "scene_7_4"
    call fade_to_black(1.2, 0.8)
    scene bg eveina_room at bg_fullscreen with dissolve

    n "Дверь в комнату мягко закрылась. Аурелиан помог Эвейне добраться до кровати и осторожно уложил её." (show_side="none", show_kind="speech")
    n "Она ещё была бледной, глаза чуть затуманены. Но тело уже слушалось, а голова почти не кружилась." (show_side="none", show_kind="speech")
    n "На столе небрежно валялась книга, та самая — из архива, которую Эвейна давно обещала вернуть." (show_side="none", show_kind="speech")
    n "Он скользнул по ней взглядом, но ничего не сказал. Вместо этого нагнулся, аккуратно поднял плед с кресла и накрыл её." (show_side="none", show_kind="speech")
    n "А потом сел рядом на край кровати." (show_side="none", show_kind="speech")
    n "Как будто это было совершенно нормально — декану Академии сидеть на постели потерявшей сознание студентки." (show_side="none", show_kind="speech")
    n "Эвейна смотрела на то, как осторожно он разглаживает края пледа и ощутила волну тепла по всему телу. Даже немного улыбнулась." (show_side="none", show_kind="speech")

    show virt smile at virt_right
    vi "Вам лучше?" (show_side="right", show_kind="speech")
    hide virt

    show eveina normal at eveina_left
    ev "Думаю, я буду в порядке." (show_side="left", show_kind="speech")
    hide eveina

    show virt upset at virt_right
    vi "Что с вами произошло?" (show_side="right", show_kind="speech")
    hide virt

    show eveina thinking at eveina_left
    ev "Не уверена, что знаю ответ на этот вопрос." (show_side="left", show_kind="speech")
    hide eveina

    n "Он замолчал на секунду, словно что-то взвешивал внутри. Потом осторожно заметил." (show_side="none", show_kind="speech")

    show virt thinking at virt_right
    vi "Каэль не допустил бы вас к эксперименту, если бы не был уверен в программе." (show_side="right", show_kind="speech")
    vi "Значит, дело не в ней." (show_side="right", show_kind="speech")
    hide virt

    show eveina upset at eveina_left
    ev "Дело не в ней…" (show_side="left", show_kind="speech")
    ev "Думаю, дело во мне. Я завалила эксперимент." (show_side="left", show_kind="speech")
    hide eveina

    n "Его рука легким движением подхватила ладонь Эвейны и слегка сжала её в ободряющем жесте." (show_side="none", show_kind="speech")

    show virt normal at virt_right
    vi "Не вините себя." (show_side="right", show_kind="speech")
    vi "Человеческий мозг — самая непредсказуемая система в известной нам Вселенной." (show_side="right", show_kind="speech")
    vi "Мы по-прежнему знаем о нём меньше, чем хотелось бы признать." (show_side="right", show_kind="speech")
    vi "Даже спустя десятки лет существования Академии." (show_side="right", show_kind="speech")
    hide virt

    n "Он осмотрелся. Скользнул взглядом по комнате — по подушке на полу, по разбросанным конспектам, по пустой чашке." (show_side="none", show_kind="speech")
    n "И вдруг, совершенно будничным видом спросил:" (show_side="none", show_kind="speech")

    show virt thinking at virt_right
    vi "Где у вас тут чайник?" (show_side="right", show_kind="speech")
    hide virt

    show eveina eyebrow at eveina_left
    ev "Чайника нет." (show_side="left", show_kind="speech")
    hide eveina

    show virt intrigued at virt_right
    vi "Какое упущение." (show_side="right", show_kind="speech")
    hide virt
    show virt smile at virt_right
    vi "Распоряжусь принести." (show_side="right", show_kind="speech")
    hide virt

    n "Они замолчали, просто смотря друг на друга в этой неожиданно уютной, не требующей слов, тишине." (show_side="none", show_kind="speech")
    n "Наконец, он вздохнул и привычным жестом провёл рукой по волосам — как всегда, когда задумывался." (show_side="none", show_kind="speech")

    show virt thinking at virt_right
    vi "Сегодня… вы выбили у меня землю из-под ног, мисс Хейла." (show_side="right", show_kind="speech")
    hide virt

    n "Эвейна слегка усмехнулась. Но прежде чем успела что-то ответить — он продолжил:" (show_side="none", show_kind="speech")

    show virt normal at virt_right
    vi "Через два дня у нас посадка на шаттл." (show_side="right", show_kind="speech")
    vi "Вам нужно восстановиться до этого времени." (show_side="right", show_kind="speech")
    hide virt

    n "Она вскинула брови и медленно приподнялась на локтях." (show_side="none", show_kind="speech")

    show eveina wondered at eveina_left
    ev "У нас?" (show_side="left", show_kind="speech")
    hide eveina

    n "В глазах тут же заплясали чёрные точки. Голова закружилась, и она едва не упала обратно — но он уже поддерживал её. И осторожно помог улечься." (show_side="none", show_kind="speech")

    show virt smile at virt_right
    vi "Не думали же вы, что я отправлю вас одну в дальнюю поездку, будучи вашим наставником?" (show_side="right", show_kind="speech")
    hide virt
    show virt normal at virt_right
    vi "Я за вас отвечаю, мисс Хейла." (show_side="right", show_kind="speech")
    hide virt

    n "Эвейна задумалась. Что-то в груди стало слишком тесным, теплым и грустным одновременно." (show_side="none", show_kind="speech")
    n "Он будто понял, почувствовал или прочитал это в её глазах. Приблизился к ней — слишком близко для декана." (show_side="none", show_kind="speech")
    n "И всё же — это не казалось неправильным." (show_side="none", show_kind="speech")

    show virt normal at virt_right
    vi "Я же говорил вам…" (show_side="right", show_kind="speech")
    vi "Я рядом, если понадоблюсь." (show_side="right", show_kind="speech")
    vi "Можете на меня положиться." (show_side="right", show_kind="speech")
    hide virt

    n "Аурелиан протянул руку и легким почти неощутимым движением убрал с её лица прядь волос." (show_side="none", show_kind="speech")

    show virt smile at virt_right
    vi "Отдыхайте." (show_side="right", show_kind="speech")
    hide virt

    n "Он поднялся и ушёл. Тихо, как будто не хотел разрушить тепло, что на секунду воцарилось между ними." (show_side="none", show_kind="speech")
    n "Эвейна осталась лежать на кровати, не двигаясь. Потолок казался слишком далёким, а дыхание — странно лёгким." (show_side="none", show_kind="speech")
    n "Она позволила себе улыбнуться. Совсем чуть-чуть, только уголками губ. И медленно прикрыла глаза, пыталась сохранить в памяти это мгновение — тихое, настоящее, человеческое." (show_side="none", show_kind="speech")
    n "Но мысли и не думали искать покоя." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev_thought "Вирт сказал, что на него можно положиться. И разве хоть раз дал в этом усомниться?" (show_side="left", show_kind="thought")
    hide eveina
    show eveina eyebrow at eveina_left
    ev_thought "А Эриан... Что он хотел скрыть от меня?" (show_side="left", show_kind="thought")
    hide eveina
    show eveina upset thinking at eveina_left
    ev_thought "Та девушка... жива ли она? Мог ли он..." (show_side="left", show_kind="thought")
    ev_thought "Боже, нет... если бы она была мертва, об этом уже было бы известно, так ведь?" (show_side="left", show_kind="thought")
    hide eveina
    show eveina annoyed at eveina_left
    ev_thought "Он всегда ускользает, как вода сквозь пальцы." (show_side="left", show_kind="thought")
    hide eveina
    show eveina eyebrow at eveina_left
    ev_thought "Что, если я сделала ошибку, доверившись ему? Что, если от моего выбора пострадает папа?" (show_side="left", show_kind="thought")
    hide eveina
    show eveina thinking at eveina_left
    ev_thought "Знал ли он, что я собираюсь участвовать в эксперименте? Знал ли, чем это обернётся?" (show_side="left", show_kind="thought")
    ev_thought "Почему не сказал об этом ни слова?" (show_side="left", show_kind="thought")
    hide eveina
    show eveina annoyed at eveina_left
    ev_thought "И почему это задевает сильнее, чем сам факт того, что он что-то стёр из моей памяти?" (show_side="left", show_kind="thought")
    hide eveina
    show eveina eyebrow at eveina_left
    ev_thought "Почему же всё так сложно..." (show_side="left", show_kind="thought")
    hide eveina

    n "Она перевернулась на бок, уставившись в стену. Внутри всё шевелилось." (show_side="none", show_kind="speech")
    n "Она не просила его забрать это воспоминание. Не давала согласия забыть его." (show_side="none", show_kind="speech")
    n "И всё же — он выбрал за неё. И никогда об этом не упоминал." (show_side="none", show_kind="speech")
    n "Словно бы это вообще не имело значения. Но как это могло не иметь значение?" (show_side="none", show_kind="speech")

    show eveina annoyed at eveina_left
    ev_thought "Он был... пугающим. Жестоким." (show_side="left", show_kind="thought")
    hide eveina
    show eveina thinking at eveina_left
    ev_thought "Если подумать, он и раньше бывал несдержанным, но не так..." (show_side="left", show_kind="thought")
    hide eveina
    show eveina thinking at eveina_left
    ev_thought "Сколько всего масок у тебя, Эриан?" (show_side="left", show_kind="thought")
    ev_thought "Что ещё ты скрыл от меня?" (show_side="left", show_kind="thought")
    hide eveina

    n "Мысли метались в голове, не давая покоя, одна цеплялась за другую, и никакая не давала ответов." (show_side="none", show_kind="speech")
    n "Вдруг ей вспомнилось." (show_side="none", show_kind="speech")

    show eveina wondered at eveina_left
    ev_thought "Сон! Мне же снился похожий сон..." (show_side="left", show_kind="thought")
    hide eveina
    show eveina normal at eveina_left
    ev_thought "Значит, это был не сон." (show_side="left", show_kind="thought")
    hide eveina
    show eveina angry at eveina_left
    ev_thought "Чёрт возьми, я же тогда места себе не находила!" (show_side="left", show_kind="thought")
    ev_thought "Думала, что... да что я тогда только не думала!" (show_side="left", show_kind="thought")
    ev_thought "Чёртов Эриан! Сколько же от тебя проблем..." (show_side="left", show_kind="thought")
    hide eveina

    n "Эвейна долго не могла успокоиться, прокручивая в голове слабый отголосок воспоминания, оставшийся после неудачного эксперимента." (show_side="none", show_kind="speech")
    n "Те ощущения, что тогда изводили её: панический страх, засохшие дорожки слёз на лице, красный след и боль, пронзающая запястье. Всё, что тогда казалось бредом, теперь вдруг обрело смысл." (show_side="none", show_kind="speech")
    n "Засыпая, она точно решила для себя: никогда больше не позволит этому случиться. И как только встанет с этой кровати, их с Эрианом ждёт серьёзный разговор." (show_side="none", show_kind="speech")

    jump scene_7_5
