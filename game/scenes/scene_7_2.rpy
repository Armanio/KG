label scene_7_2:
    $ previous_scene = "scene_7_1"
    $ next_scene = "scene_7_3"
    $ current_scene = "scene_7_2"
    call fade_to_black(1.2, 0.8)
    scene bg lab at bg_fullscreen with dissolve

    n "Эвейна и Каэль работали молча. Точнее — сосредоточенно. Без слов, но с тем уровнем понимания, который приходит после долгих часов рядом." (show_side="none", show_kind="speech")
    n "Параметры задачи, визуализация синхронизации, демонстрационная среда. Всё складывалось, всё было почти готово." (show_side="none", show_kind="speech")

    show kael normal at kael_right
    ka "Осталась только презентация." (show_side="right", show_kind="speech")
    ka "Мы должны показать, что протокол работает в реальном времени." (show_side="right", show_kind="speech")
    ka "Один доброволец, одно заданное воспоминание." (show_side="right", show_kind="speech")
    hide kael

    show eveina eyebrow at eveina_left
    ev "А кто будет этим добровольцем?" (show_side="left", show_kind="speech")
    hide eveina

    show kael thinking at kael_right
    ka "Ситуации бывают разные. Иногда — один из студентов. Иногда — ассистенты." (show_side="right", show_kind="speech")
    ka "Иногда я сам." (show_side="right", show_kind="speech")
    hide kael
    show kael normal at kael_right
    ka "Особенно когда мне важно понять эффект изнутри." (show_side="right", show_kind="speech")
    hide kael

    n "Эвейна молча кивнула, смотря на график синхронизации на экране." (show_side="none", show_kind="speech")

    show eveina normal at eveina_left
    ev "Я могу быть добровольцем." (show_side="left", show_kind="speech")
    ev "Это моя работа. Моё решение." (show_side="left", show_kind="speech")
    hide eveina

    n "Каэль долго изучал её взглядом, пытаясь найти намёки на сомнение. Но не нашёл, и ничего не возразил." (show_side="none", show_kind="speech")

    show kael thinking at kael_right
    ka "В таком случае…" (show_side="right", show_kind="speech")
    hide kael
    show kael normal at kael_right
    ka "Мне придётся разрушить одно из твоих воспоминаний." (show_side="right", show_kind="speech")
    hide kael

    show eveina eyebrow at eveina_left
    ev "Разрушить?" (show_side="left", show_kind="speech")
    hide eveina

    show kael normal at kael_right
    ka "Удалить. Временно." (show_side="right", show_kind="speech")
    hide kael

    n "Она нажала несколько кнопок на терминале, бросила победный взгляд на интерфейс. А потом легко, с тенью смеха произнесла:" (show_side="none", show_kind="speech")

    show eveina intrigued at eveina_left
    ev "Ну, можешь стереть что-нибудь неважное." (show_side="left", show_kind="speech")
    ev "Например, тот поцелуй, который ты всё равно считаешь ошибкой." (show_side="left", show_kind="speech")
    hide eveina

    n "Ответом ей стало молчание. Пальцы Каэля замерли над терминалом. Он так и не поднял головы, но всё в его теле стало другим. Жёстче. Замкнутей." (show_side="none", show_kind="speech")
    n "Эвейна тут же пожалела о сказанном. Как будто одним словом стёрла всё то, что начинало быть нормальным." (show_side="none", show_kind="speech")

    show eveina annoyed at eveina_left
    ev_thought "Гениально, Эвейна." (show_side="left", show_kind="thought")
    ev_thought "Пять секунд — и ты снова выстрелила себе в ногу." (show_side="left", show_kind="thought")
    hide eveina
    show eveina angry at eveina_left
    ev_thought "Тебя вообще к людям-то можно подпускать?" (show_side="left", show_kind="thought")
    hide eveina

    n "В этой, вдруг ставшей такой неуютной, тишине они продолжили работу. Прошло около двадцати минут, прежде чем Каэль вдруг заговорил." (show_side="none", show_kind="speech")
    n "Его голос звучал тихо, ровно, почти без эмоций. Почти." (show_side="none", show_kind="speech")

    show kael thinking at kael_right
    ka "Я не отказываюсь от своих слов." (show_side="right", show_kind="speech")
    ka "Это была ошибка." (show_side="right", show_kind="speech")
    hide kael

    show eveina eyebrow at eveina_left
    ev "Что?" (show_side="left", show_kind="speech")
    hide eveina

    show kael serious at kael_right
    ka "Я не должен был этого делать." (show_side="right", show_kind="speech")
    ka "Не должен был позволять себе такого." (show_side="right", show_kind="speech")
    hide kael

    if kael_first_kiss == "continue": 

        n "Сердце Эвейны сжалось, графики в интерфейсе вдруг перестали быть важными. Она не поднимала глаз." (show_side="none", show_kind="speech")
        n "Словно боялась — увидеть в его взгляде то, что не сможет выдержать. Что скажет:{i}«Да, ты действительно зря позволила этому случится.»{/i}" (show_side="none", show_kind="speech")

        show kael thinking at kael_right
        ka "Но я никогда…" (show_side="right", show_kind="speech")
        ka "Ни за что не хотел бы, чтобы ты это забыла." (show_side="right", show_kind="speech")
        hide kael
        show kael normal at kael_right
        ka "И если бы можно было повторить — я бы снова сделал то же самое." (show_side="right", show_kind="speech")
        hide kael
        show kael thinking at kael_right
        ka "Иногда разум даёт сбой." (show_side="right", show_kind="speech")
        hide kael
        show kael sad at kael_right
        ka "А иногда… он просто устал притворяться, что не чувствует." (show_side="right", show_kind="speech")
        hide kael

        n "Эвейна решила, что ослышалась." (show_side="none", show_kind="speech")

        show eveina wondered at eveina_left
        ev_thought "Он сейчас что..." (show_side="left", show_kind="thought")
        ev_thought "Сказал, что чувствует ко мне что-то?" (show_side="left", show_kind="thought")
        hide eveina

        n "Она застыла в нерешительности, не смея поднять глаза и увидеть там подтверждение своих мыслей." (show_side="none", show_kind="speech")

    elif kael_first_kiss == "stop":
        n "Сердце Эвейны сжалось, графики в интерфейсе вдруг перестали быть важными. Она не поднимала глаз." (show_side="none", show_kind="speech")
        n "Словно боялась — увидеть в его взгляде то, что не сможет выдержать. Что скажет:{i}«Да, ты действительно всё испортила.»{/i}" (show_side="none", show_kind="speech")

        show kael thinking at kael_right
        ka "Но я никогда…" (show_side="right", show_kind="speech")
        ka "Ни за что не хотел бы, чтобы ты это забыла." (show_side="right", show_kind="speech")
        hide kael
        show kael normal at kael_right
        ka "И если бы можно было повторить — я бы снова сделал то же самое." (show_side="right", show_kind="speech")
        hide kael
        show kael thinking at kael_right
        ka "Даже зная, что ты меня остановишь. Особенно, зная это." (show_side="right", show_kind="speech")
        hide kael

        n "Эвейна замерла в нерешительности, не понимая как трактовать эти слова." (show_side="none", show_kind="speech")

        show eveina wondered at eveina_left
        ev_thought "Он же не хочет сказать, что и правда что-то чувствует ко мне? " (show_side="left", show_kind="thought")
        ev_thought "Бред какой-то..." (show_side="left", show_kind="thought")
        hide eveina

        n "Так и сидела, не смея поднять глаза и увидеть в его глаза истину." (show_side="none", show_kind="speech")

    n "А потом еле слышно произнесла:" (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    $ kael_second_kiss = renpy.call_screen("choice", 
    items=[
    ("Ты всегда можешь напомнить.", True),
    ("Он всё равно был ошибкой.", False)
    ], who="Эвейна", what="Если вдруг забуду…", _last_say_who="ev")
    hide eveina

    if kael_second_kiss == True:   

        n "Каэль, как обычно сидевший на соседнем терминале, медленно повернулся к ней. Ноги задели край её кресла, когда он наклонился ближе." (show_side="none", show_kind="speech")
        n "Он упёрся рукой в интерфейс терминала, отчего экран жалобно пискнул, а сам наклонился, нависая над ней, как тень, пронизывающая до кончиков пальцев." (show_side="none", show_kind="speech")
        n "Его рука зависла в воздухе — между ней и её лицом. Пальцы остановились в считанных миллиметрах от её лица, будто спрашивая разрешения." (show_side="none", show_kind="speech")
        n "А затем опустились ниже. Прохладные, гладкие, бережные — скользнули под подбородок. И осторожно подняли его, заставляя её взглянуть ему в глаза." (show_side="none", show_kind="speech")

        show kael thinking at kael_right
        ka "Даже если это было ошибкой…" (show_side="right", show_kind="speech")
        hide kael
        show kael normal at kael_right
        ka "Я готов ошибаться снова." (show_side="right", show_kind="speech")
        ka "Если ты позволишь." (show_side="right", show_kind="speech")
        hide kael

        n "Она не ответила. В этом не было нужды, всё, что необходимо — уже было сказано, а остальное казалось лишним." (show_side="none", show_kind="speech")
        n "Эвейна потянулась к нему — на этот раз сама, без колебаний. И их губы встретились." (show_side="none", show_kind="speech")
        n "Поцелуй был сначала осторожным. Почти робким, как дыхание перед сном. Её губы дрогнули от прохладного прикосновения, а его — сжались, будто спрашивая: «{i}Уверена?{/i}»" (show_side="none", show_kind="speech")
        n "А мгновение спустя последнии сомнения испарились. Каэль углубил поцелуй, его губы жадно, медленно брали то, о чём давно грезил их владелец." (show_side="none", show_kind="speech")
        n "С той нарастающей страстью, которая сгорает на языке и требует большего." (show_side="none", show_kind="speech")
        n "Его рука скользнула вниз по её талии. Пальцы лёгким движением потянули девушку за собой, заставляя встать, чтобы тут же легко подхватить её." (show_side="none", show_kind="speech")
        n "Не разрывая поцелуй, Эвейна оказалась на краю терминала, где секунду назад сидел он, а Каэль — между её раздвинутых ног." (show_side="none", show_kind="speech")
        n "Одна рука сжала её бёдро — крепко, будто он боялся отпустить, вторая — обвила за талию и придвинула ближе к себе." (show_side="none", show_kind="speech")
        n "Тело Эвейны отозвалось с готовностью, которая удивила её саму. Осторожность исчезла, остался только жар, который с каждым прикосновением разгорался с новой силой." (show_side="none", show_kind="speech")
        n "Cловно лесной пожар, сносящий все преграды на своём пути." (show_side="none", show_kind="speech")

        show eveina thinking at eveina_left
        ev_thought "Я не должна так чувствовать." (show_side="left", show_kind="thought")
        ev_thought "Но, чёрт, я чувствую." (show_side="left", show_kind="thought")
        hide eveina

        n "Его язык неторопливо прошёлся по её зубам, прежде чем скользнуть внутрь и переплестись с её, вызывая вздох возбуждения." (show_side="none", show_kind="speech")
        n "Пальцы девушки зарылись в его волосы на затылке, проводя ногтями по коже." (show_side="none", show_kind="speech")
        n "Каэль тихо выдохнул ей в губы, а потом снова впился в них. С новой жаждой. Он держал её бережно, но крепко. Нежно проводя пальцами вдоль бедра, а потом сжимая его ладонью." (show_side="none", show_kind="speech") 
        n "Легким движением пальцев скользя по линии талии и вызывая волны мурашек, разбегающихся в разные стороны, и заставляя Эвейну прижиматься крепче к нему." (show_side="none", show_kind="speech")
        n "Тело Эвейны плавилось под его натиском, без всякой надежды на исцеление. В животе дрожало от возбуждения свернутое в узел желание быть с ним, быть его." (show_side="none", show_kind="speech")
        n "Сердце стучало где-то в горле, дыхание сбилось и будто стало совсем ненужным, голова кружилась от переизбытка ощущений и недостатка кислорода." (show_side="none", show_kind="speech")
        n "Эвейна чувствовала, как ласкающие талию пальцы нащупали застёжку на её брюках. Как уверенно двинулась вверх вторая рука, намереваясь избавить её от такой ненужной сейчас блузки." (show_side="none", show_kind="speech")
        n "Как её собственные пальцы легли на молнию его комбинезона и осторожно потянули вниз." (show_side="none", show_kind="speech")
        n "Казалось, ничто не могло остановить этих двоих оторваться друг от друга в этот момент. Ну, практически ничего..." (show_side="none", show_kind="speech")
        n "Тишину разорвал шум открывающейся двери, а следом за ним — звук шагов." (show_side="none", show_kind="speech")
        n "Они отпрянули, как по команде. Каэль, одним резким движением застегнув молнию, вернулся в свою обычную позу: стоящий рядом, отстранённый, будто и не двигался." (show_side="none", show_kind="speech")
        n "Эвейна — мягко соскользнула с терминала, вернулась в кресло и сделала вид, что работает, пряча румянец на щеках волосами." (show_side="none", show_kind="speech")
        n "В лабораторию вошёл профессор Эзари. Что-то бурча себе под нос, оглянулся на них." (show_side="none", show_kind="speech")

        show ezari normal at ezari_right
        ez "Всё готово к завтрашней демонстрации?" (show_side="right", show_kind="speech")
        hide ezari

        show kael normal at kael_right
        ka "Почти. Осталась упаковка." (show_side="right", show_kind="speech")
        hide kael

        show ezari normal at ezari_right
        ez "Хм. Не забудьте о времени. И не спалите мне оборудование." (show_side="right", show_kind="speech")
        hide ezari

        n "Он ушёл вглубь лаборатории. Тишина снова опустилась — почти как покрывало после бури." (show_side="none", show_kind="speech")
        n "Каэль наклонился вперёд, слегка коснувшись волос девушки. В его голосе прозвучала еле заметная усмешка, когда он шепнул ей на ухо:" (show_side="none", show_kind="speech")

        show kael intrigued at kael_right
        ka "Никогда ещё не получал такого удовольствия от собственных ошибок." (show_side="right", show_kind="speech")
        hide kael

        n "Эвейна молча улыбнулась. Сердце ещё отбивало ускоренный ритм — даже когда она поднялась, попрощалась с ним и с профессором, и вышла в коридор." (show_side="none", show_kind="speech")
        n "В груди горело, но это был не стыд. Это было темное, глубоко проникшее в её тело желание. Огонь, который он разжег в ней." (show_side="none", show_kind="speech")
        n "Их ошибка. И то, как сильно она хотела, чтобы они повторили её. Снова." (show_side="none", show_kind="speech")
    
    if kael_second_kiss == False:   

        show eveina thinking at eveina_left
        ev "Не обязательно зацикливаться на ошибках." (show_side="left", show_kind="speech")
        ev "Мы... вроде неплохо ладим." (show_side="left", show_kind="speech")
        hide eveina

        n "Каэль, как обычно сидевший на соседнем терминале, медленно повернулся к ней. Ноги задели край её кресла, когда он наклонился ближе, а изучающий взгляд упёрся в Эвейну." (show_side="none", show_kind="speech")

        show kael thinking at kael_right
        ka "Ладим?" (show_side="right", show_kind="speech")
        ka "Ты так это называешь?" (show_side="right", show_kind="speech")
        hide kael

        show eveina intrigued at eveina_left
        ev "Ну...да. Работается с тобой вполне сносно. Мы даже могли бы стать друзьями, втереться друг другу в доверие." (show_side="left", show_kind="speech")
        ev "А потом я надавлю на твоё чувство вины за поцелуй или стану шантажировать рассказать о нём и — получу высший бал по нейроанализу." (show_side="left", show_kind="speech")
        ev "Ммм... такой простой и прекрасный план." (show_side="left", show_kind="speech")    
        hide eveina    

        n "Каэль завис. Буквально — внезапно он перестал двигаться, и даже, кажется, дышать. Просто прожигал дыру в девушке холодным и ничего не выражающим взглядом." (show_side="none", show_kind="speech")

        show kael eyebrow at kael_right
        ka "Ты ведь сейчас несерьёзно?" (show_side="right", show_kind="speech")
        hide kael   

        show eveina smile at eveina_left
        ev "Боже, Каэль, ну конечно, я несерьёзно! У меня слишком плохо развит навык шантажа для такой аферы." (show_side="left", show_kind="speech")
        hide eveina

        n "Это фраза точно не помогла. Кажется, мозг Каэля перегрелся и решил уйти в ждущий режим. Иначе просто нечем было объяснить полную беспомощность и недоумение, с которыми он на неё смотрел." (show_side="none", show_kind="speech")

        show eveina thinking at eveina_left
        ev_thought "Чёрт... ладно, надо было помягче. А то так и довести парня недолго." (show_side="left", show_kind="thought")
        hide eveina      
        show eveina smile at eveina_left
        ev "Мне правда кажется, что мы могли бы подружиться." (show_side="left", show_kind="speech")
        hide eveina

        n "Взгляд Каэля наконец обрёл осозанность, но вместе с этим всё его тело напряглось. Будто кто-то решил вторгнуться в его зону комфорта. Интересно, кто бы это мог быть?" (show_side="none", show_kind="speech")

        show kael serious at kael_right
        ka "Подружиться? Я твой преподаватель, Эвейна." (show_side="right", show_kind="speech")
        hide kael   

        show eveina smile at eveina_left
        ev "Об этом стоило вспомнить, когда лез ко мне с поцелуями." (show_side="left", show_kind="speech")
        hide eveina

        show kael thinking at kael_right
        ka "Справедливо." (show_side="right", show_kind="speech")
        hide kael
        show kael eyebrow at kael_right
        ka "Но зачем тебе со мной дружить?" (show_side="right", show_kind="speech")
        hide kael   

        show eveina eyebrow at eveina_left
        ev "Вот так, значит? Не «зачем {i}мне с тобой{/i}», а «зачем {i}тебе со мной{/i}»?" (show_side="left", show_kind="speech")
        hide eveina

        show kael normal at kael_right
        ka "Зачем {i}мне{/i} это делать, я и сам разберусь." (show_side="right", show_kind="speech")
        hide kael  

        n "Эвейна вспыхнула. Она тут перед ним душу обнажает, а он «сам разберётся»!" (show_side="none", show_kind="speech")

        show eveina annoyed at eveina_left
        ev "Ну вот и я сама разберусь!" (show_side="left", show_kind="speech")
        hide eveina

        n "Каэль прищурил холодный взгляд." (show_side="none", show_kind="speech")

        show kael serious at kael_right
        ka "Никаких поблажек по учёбе." (show_side="right", show_kind="speech")
        hide kael 

        show eveina eyebrow at eveina_left
        ev "И никаких поцелуев." (show_side="left", show_kind="speech")
        hide eveina

        show kael intrigued at kael_right
        ka "Пока ты сама не попросишь." (show_side="right", show_kind="speech")
        hide kael

        show eveina annoyed at eveina_left
        ev "Пока?.." (show_side="left", show_kind="speech")
        hide eveina

        show kael normal at kael_right
        ka "Если. Если ты сама не попросишь." (show_side="right", show_kind="speech")
        hide kael

        n "Они продолжали холодно смотреть друг на друга в полном молчании. Эвейна пыталась найти в каменном выражении хотя бы намёк на ложь или шутку. И не найдя — молча протянула ему ладонь." (show_side="none", show_kind="speech")

        show eveina intrigued at eveina_left
        ev "По рукам." (show_side="left", show_kind="speech")
        hide eveina

        show kael normal at kael_right
        ka "Договорились." (show_side="right", show_kind="speech")
        hide kael

        n "Сухое рукопожатие ознаменовало странное начало новой дружбы." (show_side="none", show_kind="speech")

    jump scene_7_3
