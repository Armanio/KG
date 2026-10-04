label scene_7_7:
    $ previous_scene = "scene_7_6"
    $ next_scene = "scene_7_8"
    $ current_scene = "scene_7_7"
    call fade_to_black(1.2, 0.8)
    scene bg shuttle_3 at bg_fullscreen with dissolve

    n "Первую половину дня девушка провела, лёжа в капсуле. Глядя в потолок и пытаясь найти хоть что-то интересное в паттерне освещения. Безуспешно." (show_side="none", show_kind="speech")
    n "Рабочий планшет казался чужим, мозг не хотел думать, а тело — шевелиться." (show_side="none", show_kind="speech")
    n "Вирт всё это время сидел за столом, как воплощение собранности, перебирая документы, просматривая отчёты и делая заметки." (show_side="none", show_kind="speech")

    show eveina normal at eveina_left
    ev_thought "Удивительно. Он даже дышит с четко выверенными паузами." (show_side="left", show_kind="thought")
    ev_thought "Кажется, если бы купе загорелось, он бы сначала закончил работу над документом, а уже потом взялся за огнетушитель." (show_side="left", show_kind="thought")
    hide eveina

    n "Она смотрела, как он работает. И думала — кем он был до всего этого?" (show_side="none", show_kind="speech")
    n "До преподавания, до идеальных галстуков и тембра, которым можно всыпать студенту, не повышая голос." (show_side="none", show_kind="speech")
    n "И тут в голове щёлкнуло: {i}фото{/i}. Тот выпускной разворот, где среди тридцати студентов стояли Вирт, Кайстр… и Далон." (show_side="none", show_kind="speech")

    show eveina eyebrow at eveina_left
    ev "Профессор Вирт, вы… Поддерживаете связь с теми, с кем учились?" (show_side="left", show_kind="speech")
    hide eveina

    n "Он поднял взгляд. Слегка прищурился, будто пытаясь понять, что стоит за этим вопросом." (show_side="none", show_kind="speech")

    show virt thinking jacket at virt_right
    vi "С некоторыми — да. Кто-то продолжает работу в Академии." (show_side="right", show_kind="speech")
    vi "Кто-то ушёл в полевые проекты — в колониях, на дальних маршрутах." (show_side="right", show_kind="speech")
    vi "А кто-то… завёл семьи, обзавёлся детьми." (show_side="right", show_kind="speech")
    hide virt
    show virt normal jacket at virt_right
    vi "Я давно не интересовался. Если честно — и времени на это не было." (show_side="right", show_kind="speech")
    hide virt

    show eveina thinking at eveina_left
    ev_thought "Работает в Академии... это он о Кайстре, очевидно. Или есть кто-то ещё?" (show_side="left", show_kind="thought")
    ev_thought "Что до остальных пунктов... тут даже не спросить точнее, не вызвав подозрений..." (show_side="left", show_kind="thought")
    hide eveina

    n "Эвейна медленно кивнула, размышляя над тем, что ещё она может выяснить. И сама не осознала, как из её рта вырвался следующий вопрос." (show_side="none", show_kind="speech")

    show eveina eyebrow at eveina_left
    ev "А вы? Никогда не думали… о семье?" (show_side="left", show_kind="speech")
    hide eveina

    n "Внимательный взгляд, обращенный на неё, мягко намекнул Эвейне, что задавать подобные вопросы профессору — плохой тон, заставив ту неловко опустить глаза." (show_side="none", show_kind="speech")
    n "Аурелиан ещё пару секунд рассматривал её, а потом вновь окунулся в работу. Его ответ прозвучал отстранённо, как давно пережитая рефлексия." (show_side="none", show_kind="speech")

    show virt normal jacket at virt_right
    vi "Я выбрал Академию." (show_side="right", show_kind="speech")
    vi "А этот выбор не предполагает… связей, которые нельзя прервать." (show_side="right", show_kind="speech")
    hide virt

    show eveina thinking at eveina_left
    ev_thought "Говорит так, будто у него не сердце, а методический комитет." (show_side="left", show_kind="thought")
    hide eveina
    show eveina normal at eveina_left
    ev_thought "Но что-то ведь там стучит?" (show_side="left", show_kind="thought")
    hide eveina

    n "Некоторое время они молчали. Девушка уже готова была вновь погрузиться в скуку, когда он положил планшет на стол." (show_side="none", show_kind="speech")

    show virt intrigued jacket at virt_right
    vi "Кстати. Хотите посмотреть, кто стал главной темой обсуждений в Journal of Neural Memory Systems?" (show_side="right", show_kind="speech")
    hide virt

    n "Эвейна вскинула бровь, на что профессор легким движением головы позвал её к себе. Помня свои предыдущие попытки упасть в небытие, она медленно поднялась из кресла." (show_side="none", show_kind="speech")
    n "Аурелиан открыл статью, показывая её студентке. Наклонившись над плечом профессора, Эвейна снова вдохнула его запах, замечая, как мысли снова убегают в непрошенное русло." (show_side="none", show_kind="speech")
    n "Её волосы скользнули по его щеке. Грудь — мягко, но ощутимо, упёрлась в плечо." (show_side="none", show_kind="speech")
    n "Мужчина напрягся, почувствовав её прикосновение. Взгляд метнулся вбок, но когда он понял, насколько её лицо близко, не осмелился поворачиваться, чтобы не усугубить ситуацию." (show_side="none", show_kind="speech")
    n "Нахмурившись, он вернул свой взгляд на планшет." (show_side="none", show_kind="speech")

    show eveina intrigued at eveina_left
    ev_thought "Один сантиметр ближе — и его идеальная сдержанность дала трещину." (show_side="left", show_kind="thought")
    hide eveina

    n "Эвейна наклонилась ещё чуть ниже, прочитала заголовок статьи и... искренне удивилась." (show_side="none", show_kind="speech")

    show eveina eyebrow at eveina_left
    ev "Выходит… нашу с Каэлем работу уже цитируют?" (show_side="left", show_kind="speech")
    hide eveina

    show virt serious jacket at virt_right
    vi "Не только вашу. Но да, как я говорил, вы — теперь повод для обсуждения." (show_side="right", show_kind="speech")
    hide virt
    show virt thinking jacket at virt_right
    vi "Новые «звезды» в научных кругах загораются нечасто." (show_side="right", show_kind="speech")
    hide virt
    show virt smile jacket at virt_right
    vi "Это не я придумал, это буквально цитата...вот здесь..." (show_side="right", show_kind="speech")
    hide virt

    n "Он пролистнул ниже, указывая на последний абзац." (show_side="none", show_kind="speech") 

    show eveina intrigued at eveina_left
    ev "Ого, мне уже пора задуматься над собственным имиджем?" (show_side="left", show_kind="speech")
    hide eveina

    show virt smile jacket at virt_right
    vi "Как наставник я бы посоветовал вам задуматься над своей дисциплиной." (show_side="right", show_kind="speech")
    hide virt 

    n "Эвейна недовольно хмыкнула, но спорить не стала. Взгляд зацепился за знакомое имя в статье и она перегнулась через плечо, чтобы пролистнуть статью чуть выше." (show_side="none", show_kind="speech")

    show eveina intrigued at eveina_left
    ev "Тут и о Каэле написано... «молодой ученый, уже на несколько голов обошедший всех предшественников в сфере нейроаугментаций»..." (show_side="left", show_kind="speech")
    hide eveina
    
    n "Эвейна чуть сбилась в конце, заметив, как от её движения напряглась шея мужчины, а пальцы сильнее сжали планшет. Её губы дрогнули, скрывая победную улыбку." (show_side="none", show_kind="speech")

    show eveina intrigued at eveina_left
    ev_thought "Упс... Профессор, держитесь за свои моральные принципы также крепко, как держите этот планшет." (show_side="left", show_kind="thought")
    ev_thought "Я знаю, что делаю. И вы знаете." (show_side="left", show_kind="thought")
    hide eveina

    n "Это было неправдой. Эвейна не понимала до конца, что именно она творила, и не знала, к чему это может привести." (show_side="none", show_kind="speech")
    n "Поэтому встретив тяжелый взгляд профессора решила, что лучше отступить. Девушка неспеша отстранилась и вернулась в свое кресло с ощущением маленького триумфа." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev_thought "Невероятно глупая и рисковая затея..." (show_side="left", show_kind="thought")
    hide eveina
    show eveina intrigued at eveina_left
    ev_thought "Но, чёрт, много ли студенток могут похвастаться тем, что Вирт смотрит на них так?" (show_side="left", show_kind="thought")
    ev_thought "Просто не могу не поддразнить Его Сдержанное Высочество ещё немного..." (show_side="left", show_kind="thought")
    hide eveina

    n "Вирт, впрочем, её чувств не разделял. Складка между его бровей не разгладилась, наоборот, как будто стала ещё глубже." (show_side="none", show_kind="speech")
    n "Он с сомнением постучал пальцем по столу, словно размышляя, не совершил ли ошибку, определяя их в одно купе." (show_side="none", show_kind="speech")
    n "Затем бросил взгляд на статью в планшете, привычным жестом откинул волосы с лица и обратился к ней." (show_side="none", show_kind="speech")

    show virt serious jacket at virt_right
    vi "Не все будут довольны вашими успехами." (show_side="right", show_kind="speech")
    vi "Думаю, для вас не секрет, что Академия элитарна. И слишком многое держится на старых связях." (show_side="right", show_kind="speech")
    vi "Вам стоит быть аккуратнее. Особенно в новых знакомствах. И в предложениях, которые могут за ними последовать." (show_side="right", show_kind="speech")
    vi "Вам также стоит понимать, что под вас могут начать копать, чтобы выяснить, кто вы и что стоит за вашим открытием." (show_side="right", show_kind="speech")
    hide virt

    n "Эвейна, поёжившись, кивнула, с тревогой обдумывая новую информацию." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev_thought "А если уже начали? Скелетов в моём шкафу хватит на небольшое кладбище." (show_side="left", show_kind="thought")
    hide eveina
    show eveina normal at eveina_left
    ev_thought "Сайф… Он так и не ответил. А если уже залез в почту Кайстра? Что, если оставил след?" (show_side="left", show_kind="thought")
    hide eveina
    show eveina thinking at eveina_left
    ev_thought "Чёрт, связываться с ним сейчас себе дороже..." (show_side="left", show_kind="thought")
    hide eveina
    show eveina normal at eveina_left
    ev_thought "Лучше делать вид, что это меня не задевает." (show_side="left", show_kind="thought")
    hide eveina
    show eveina eyebrow at eveina_left
    ev_thought "Иначе копать под меня начнёт уже сам Вирт." (show_side="left", show_kind="thought")
    hide eveina

    n "Эта мысль заставила её тело напрячься, но виду подавать было нельзя." (show_side="none", show_kind="speech") 

    show eveina eyeroll at eveina_left
    ev_thought "Спокойно, Эвейна." (show_side="left", show_kind="thought")
    hide eveina
    show eveina thinking at eveina_left
    ev_thought "Ты обязательно подумаешь об этом, когда вернёшься в Академию." (show_side="left", show_kind="thought")
    ev_thought "Сейчас не время." (show_side="left", show_kind="thought")
    hide eveina

    n "Заставляя себя отвлечься, она продолжила лениво наблюдать за профессором, который уже вернулся к работе." (show_side="none", show_kind="speech")
    n "Отчего-то мысль о том, как этот сдержанный мужчина реагирует на её близость, вызывала азарт и заставляла её искать продолжения, игнорируя все риски своего поведения." (show_side="none", show_kind="speech")

    show eveina normal at eveina_left
    ev_thought "Ещё два дня." (show_side="left", show_kind="thought")
    ev_thought "Два дня, чтобы понять — кто из нас играет всерьёз." (show_side="left", show_kind="thought")
    hide eveina

    jump scene_7_8
