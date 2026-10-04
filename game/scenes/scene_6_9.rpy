label scene_6_9:
    $ previous_scene = "scene_6_8"
    $ next_scene = "scene_6_10"
    $ current_scene = "scene_6_9"
    call fade_to_black(1.2, 0.8)
    scene bg corridor_3 at bg_fullscreen with dissolve

    n "День первых отчётных экзаменов начался слишком рано и слишком нервно. Скорый завтрак, дрожь в животе и список экзаменаторов, каждое имя в котором отзывалось по-своему." (show_side="none", show_kind="speech")
    n "Эвейна с утра не позволяла себе никаких мыслей, кроме одной единственной, что стала её путеводной нитью." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev_thought "Облажаться — не вариант. У нас договоренность с Виртом." (show_side="left", show_kind="thought")
    ev_thought "Сначала тесты. Потом — отец. Всё просто. Всё по плану." (show_side="left", show_kind="thought")
    hide eveina

    n "Экзамены проходили в формате индивидуальных собеседований. Пять преподавателей. Пять кабинетов. Один шанс." (show_side="none", show_kind="speech")

    scene bg ezari_cabinet at bg_fullscreen with dissolve

    n "Первым её пригласил профессор Эзари." (show_side="none", show_kind="speech")

    show ezari normal at ezari_right
    ez "..." (show_side="right", show_kind="speech")
    hide ezari

    n "Каждая его фраза звучала так, будто от неё зависит научная карьера. Он задавал вопросы по биологии, местной флоре, включая особенности симбиотических растений Ил’Эйны." (show_side="none", show_kind="speech")
    n "Эвейна знала, что он любил факты, терпеть не мог лишние слова. Поэтому отвечала коротко, чётко. Иногда даже быстрее, чем он успевал задать уточнение." (show_side="none", show_kind="speech")

    show ezari normal at ezari_right
    ez "Назовите три причины, по которым симбиотические мхи Ил’Эйны не поддаются искусственному культивированию." (show_side="right", show_kind="speech")
    hide ezari

    show eveina thinking at eveina_left
    $ ezari_first_exam = renpy.call_screen("choice", 
    items=[
    ("Носитель, фотонная реакция и... что-то ещё?", "right_answer"),
    ("Магнитное поле Ил'Эйн, особенности размножения и... что-то ещё?", "wrong_answer"),
    ("Благословления Ил'Эйн, волшебной палочки и пары крепких слов?", "joke")
    ], who="Эвейна", what="Три? Разве на лекции он называл не две причины? И что это было?", _last_say_who="ev_thought")

    if ezari_first_exam == "right_answer":
        ev_thought "Что ж... попробуем наугад." (show_side="left", show_kind="thought")
        hide eveina
        show eveina normal at eveina_left
        ev "Отсутствие соответствующего носителя, нестабильность фотонной реакции и… зависимость от присутствия Илейн." (show_side="left", show_kind="speech")
        hide eveina

        show ezari normal at ezari_right
        ez "Вы уверены в последнем пункте?" (show_side="right", show_kind="speech")
        hide ezari

        show eveina normal at eveina_left
        ev "Не уверена. Но могу выдвинуть гипотезу по косвенным признакам." (show_side="left", show_kind="speech")
        hide eveina

        show ezari normal at ezari_right
        ez "Хм. Сочетание смелости и осторожной честности. Это редкость." (show_side="right", show_kind="speech")
        ez "Достаточно. Высший балл." (show_side="right", show_kind="speech")
        hide ezari
    elif  ezari_first_exam == "wrong_answer":
        ev_thought "Надо было слушать лекции внимательнее..." (show_side="left", show_kind="thought")
        hide eveina
        show eveina normal at eveina_left
        ev "Влияние магнитных полей планеты, особенности их размножения и… зависимость от присутствия Илейн?" (show_side="left", show_kind="speech")
        hide eveina

        show ezari normal at ezari_right
        ez "Смелые предположения. Жаль, что верным оказалось только одно из трёх." (show_side="right", show_kind="speech")
        ez "Хм. На остальные вопросы вы ответили сносно." (show_side="right", show_kind="speech")
        ez "Достаточно. Не высший бал, но проверка пройдена." (show_side="right", show_kind="speech")
        hide ezari
        
    elif  ezari_first_exam == "joke":
        hide eveina
        show eveina eyebrow at eveina_left
        ev_thought "Все любят шутки, так?" (show_side="left", show_kind="thought")
        hide eveina

        show eveina normal at eveina_left
        ev "Благословления Ил'Эйн, волшебной палочки и... я бы сказала, упорства учёных, но скорее всего это что-то связанное с Илейн, так?" (show_side="left", show_kind="speech")
        hide eveina

        show ezari angry at ezari_right
        ez "Вместо оттачивания чувства юмора, я бы посоветовал вам уделить больше внимания теории." (show_side="right", show_kind="speech")
        hide ezari

        show eveina eyeroll at eveina_left
        ev_thought "Видимо, всё-таки не все. Зануда." (show_side="left", show_kind="thought")
        hide eveina

        show ezari normal at ezari_right
        ez "Впрочем, на остальные вопросы вы ответили сносно." (show_side="right", show_kind="speech")
        ez "Достаточно, это тянет на удовлетворительно. Вы свободны." (show_side="right", show_kind="speech")
        hide ezari

    show eveina thinking at eveina_left
    ev_thought "Один есть. Осталось четыре." (show_side="left", show_kind="thought")
    hide eveina

    scene bg raukt_cabinet at bg_fullscreen

    n "Второй экзаменатор — профессор Раукт. Её кабинет больше походил на операционную, чем на личное пространство." (show_side="none", show_kind="speech")
    n "Серена сидела за столом, выпрямив спину и смотря прямо на Эвейну. Сухая, как сухожилие, и такая же неумолимая. Что, впрочем, не мешало ей сохранять здоровую долю сарказма в своих вопросах." (show_side="none", show_kind="speech")
    n "Вопросы касались строения мозга. Как работает память, что произойдёт, если нарушить междолевую связность, какие части мозга за что отвечают." (show_side="none", show_kind="speech")

    show serena normal at serena_right
    sr "Мисс Хейла, если я поврежу ваш гиппокамп — что с вами будет?" (show_side="right", show_kind="speech")
    hide serena

    show eveina thinking at eveina_left
    $ raukt_first_exam = renpy.call_screen("choice", 
    items=[
    ("Раукт это оценит!", "joke"),
    ("Раукт это оценит, но бал будет ниже плинтуса.", "serious_answer")
    ], who="Эвейна", what="Так и тянет пошутить...", _last_say_who="ev_thought")

    if raukt_first_exam == "joke":
        hide eveina
        show eveina normal at eveina_left
        ev "Новые воспоминания не будут формироваться." (show_side="left", show_kind="speech")
        ev "А поэтому придётся каждый раз заново знакомиться с преподавателями и нарисовать себе карту до комнаты." (show_side="left", show_kind="speech")
        hide eveina

        show serena smile at serena_right
        sr "И что, каждый день будете слушать одни и те же лекции?" (show_side="right", show_kind="speech")
        hide serena

        show eveina normal at eveina_left
        ev "Скорее, каждый день думать, что это — первый. Страшнее всего — экзамены. Постоянно как в первый раз." (show_side="left", show_kind="speech")
        hide eveina

        show serena normal at serena_right
        sr "Хорошо. Этого достаточно." (show_side="right", show_kind="speech")
        hide serena
        show serena smile at serena_right
        sr "Примите к сведению: вы на удивление хорошо подготовлены." (show_side="right", show_kind="speech")
        sr "Сдержанно рекомендую." (show_side="right", show_kind="speech")
        hide serena

    elif raukt_first_exam == "serious_answer":
        hide eveina
        show eveina normal at eveina_left
        ev "Память пострадает. Новые воспоминания не будут формироваться." (show_side="left", show_kind="speech")
        hide eveina

        show serena normal at serena_right
        sr "А что в таком случае будет именно с вами?" (show_side="right", show_kind="speech")
        hide serena

        show eveina normal at eveina_left
        ev "Ну, диплома мне, скорее всего, уже не видать." (show_side="left", show_kind="speech")
        hide eveina

        show serena normal at serena_right
        sr "Склонна согласиться. Хорошо, этого достаточно." (show_side="right", show_kind="speech")
        hide serena

    show eveina thinking at eveina_left
    ev_thought "Два. Уже дышать чуть легче. Но всё самое интересное — впереди." (show_side="left", show_kind="thought")
    hide eveina

    scene bg virt_cabinet at bg_fullscreen with dissolve

    n "Третьим её встретил профессор Вирт. В его кабинете царила атмосфера спокойствия, как будто и воздух здесь был сдержанным." (show_side="none", show_kind="speech")
    n "Аурелиан внимательно рассматривал её. В его глазах была видна еле уловимая усталость, но в остальном — сосредоточенность." (show_side="none", show_kind="speech")

    show virt normal at virt_right
    vi "Как вы себя чувствуете, мисс Хейла? И как прошли предыдущие собеседования?" (show_side="right", show_kind="speech")
    hide virt

    if raukt_first_exam == "joke" and ezari_first_exam == "right_answer":

        show eveina normal at eveina_left
        ev "Всё в порядке. Отвечала уверенно." (show_side="left", show_kind="speech")
        hide eveina
    else:
        show eveina normal at eveina_left
        ev "Сделала всё, что в моих силах, профессор." (show_side="left", show_kind="speech")
        hide eveina

    n "Он кивнул. И, пролистав пару строк в на планшете, поднял на неё глаза." (show_side="none", show_kind="speech")

    show virt serious at virt_right with dissolve
    vi "Тогда начнём." (show_side="right", show_kind="speech")
    vi "Этика — не просто знание норм. Это способность принимать решения, когда нормы конфликтуют. Поэтому — ситуация." (show_side="right", show_kind="speech")
    vi "У пациента обнаружено редкое нейропсихическое расстройство." (show_side="right", show_kind="speech")
    vi "Его сознание фрагментировано — в разное время проявляются разные аспекты личности." (show_side="right", show_kind="speech")
    vi "Один из этих аспектов — агрессивен, но обладает уникальными аналитическими способностями, которых нет у основной личности." (show_side="right", show_kind="speech")
    vi "Вы можете стабилизировать пациента, устранив агрессивную личность. Но вместе с ней исчезнут и эти способности." (show_side="right", show_kind="speech")
    vi "Или оставить всё как есть — с риском, что пациент однажды навредит окружающим." (show_side="right", show_kind="speech")
    vi "Ваше решение?" (show_side="right", show_kind="speech")
    hide virt

    n "Эвейна некоторое время молчала, подбирая правильные слова для аргументации." (show_side="none", show_kind="speech")

    show eveina normal at eveina_left
    ev "Стабилизировать." (show_side="left", show_kind="speech")
    ev "Но не потому что он опасен. А потому что он — человек. И если личность внутри него склонна к разрушению, значит, его сознание уже страдает." (show_side="left", show_kind="speech")
    ev "Не могу считать эти способности оправданием боли — ни его, ни потенциальной жертвы его агрессии." (show_side="left", show_kind="speech")
    ev "А если эти способности так ценны — пусть мы научимся развивать их иначе." (show_side="left", show_kind="speech")
    ev "Без разрушения и агрессии. Не все жертвы оправданы." (show_side="left", show_kind="speech")
    hide eveina

    n "После долгой паузы Вирт снова кивнул." (show_side="none", show_kind="speech") 

    show virt normal at virt_right
    vi "Высший балл." (show_side="right", show_kind="speech")
    hide virt

    n "Когда она поднялась из-за стола, профессор слегка улыбнулся." (show_side="none", show_kind="speech")

    show virt smile at virt_right
    vi "Удачи, мисс Хейла." (show_side="right", show_kind="speech")
    hide virt

    show eveina thinking at eveina_left
    ev_thought "Спасибо, профессор. Уж мы с вами знаем, что она мне понадобится." (show_side="left", show_kind="thought")
    hide eveina

    scene bg kaistr_cabinet at bg_fullscreen with dissolve

    n "Стоило ей только войти в четвертый кабинет — и воздух сразу изменился." (show_side="none", show_kind="speech")
    n "Как будто здесь всё было напоказ: осанка, молчание, планшет, лежаший ровно перпендикулярно краю стола. Даже её отражение в стеклянной панели выглядело чуть... враждебным." (show_side="none", show_kind="speech")

    show kaistr normal at kaistr_right
    kr "Мисс Хейла. Поздравляю. Влиятельные друзья — это надёжная стратегия." (show_side="right", show_kind="speech")
    hide kaistr
    show kaistr intrigued at kaistr_right
    kr "Особенно, если без них вы ни на что не годитесь." (show_side="right", show_kind="speech")
    hide kaistr

    n "Эвейна напряглась, сжав руки в кулаки." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev_thought "Не поддавайся." (show_side="left", show_kind="thought") 
    ev_thought "Знала же, что он скажет что-то в этом духе..." (show_side="left", show_kind="thought")
    hide eveina

    n "Он поднял взгляд и посмотрел прямо на неё. Как мясник смотрит на непослушного быка на скотобойне." (show_side="none", show_kind="speech")

    show kaistr normal at kaistr_right
    kr "Конфликт между нами считаю закрытым. Но вы выбрали очень прямую линию поведения." (show_side="right", show_kind="speech")
    kr "А такие линии редко ведут к вершинам. Чаще — к пропастям." (show_side="right", show_kind="speech")
    hide kaistr

    n "Он сделал паузу, постучав длинным пальцем по столу." (show_side="none", show_kind="speech")

    show kaistr normal at kaistr_right
    kr "Что ж, приступим..." (show_side="right", show_kind="speech")
    kr "Если бы вам предложили признание: «Вы здесь только потому, что система дала слабину». Что бы вы ответили?" (show_side="right", show_kind="speech")
    hide kaistr

    show eveina angry at eveina_left
    ev_thought "Это он про мои рекомендации?" (show_side="left", show_kind="thought")
    hide eveina
    show eveina normal at eveina_left
    ev "Что система дала шанс. А я — его использовала. Слаба не система. Слабы те, кто боится конкуренции." (show_side="left", show_kind="speech")
    hide eveina

    show kaistr intrigued at kaistr_right
    kr "Вы говорите, как человек, который хочет власти. Но ведёте себя, как человек, который хочет быть услышанным." (show_side="right", show_kind="speech")
    kr "Вы уверены, что знаете, чего хотите?" (show_side="right", show_kind="speech")
    hide kaistr

    show eveina angry at eveina_left
    ev_thought "Взять этот планшет со стола и навсегда стереть им с твоего лица эту самодовольную ухмылку?" (show_side="left", show_kind="thought")
    hide eveina

    show eveina normal at eveina_left
    ev "Пока не уверена." (show_side="left", show_kind="speech")
    ev "Но я уверена, что хочу добраться до ответа на этот вопрос сама." (show_side="left", show_kind="speech")
    hide eveina
    show eveina annoyed at eveina_left
    ev "А не получать его из чьих-то уст или по чьей-то милости." (show_side="left", show_kind="speech")
    hide eveina

    n "Лоренс откинулся на спинку стула и оглядел её с ног до головы оценивающим взглядом." (show_side="none", show_kind="speech")

    show kaistr annoyed at kaistr_right
    kr "Советы даю редко. Но вам стоит подумать: что вы хотите от этой Академии — доказать, или получить?" (show_side="right", show_kind="speech")
    hide kaistr

    show eveina thinking at eveina_left
    $ kaistr_first_exam = renpy.call_screen("choice", 
    items=[
    ("Нет, не стоит.", "silence"),
    ("Ещё как стоит!", "answer")
    ], who="Эвейна", what="Ответить придурку?", _last_say_who="ev_thought")
    hide eveina

    if kaistr_first_exam == "silence":
        n "Эвейна выдержала паузу. Она чувствовала, что он провоцирует её на необдуманные действия." (show_side="none", show_kind="speech")
        n "И знала: одно неосторожное слово — и он воспользуется им как поводом." (show_side="none", show_kind="speech")

        show kaistr intrigued at kaistr_right
        kr "Рад, что вы научились понимать, когда стоит держать свой острый язычок за зубами." (show_side="right", show_kind="speech")
        hide kaistr
        show kaistr normal at kaistr_right
        kr "Удовлетворительно. Свободны." (show_side="right", show_kind="speech")
        hide kaistr

    if  kaistr_first_exam == "answer":
        show eveina intrigued at eveina_left
        ev "Вы путаете меня с собой профессор." (show_side="left", show_kind="speech")
        ev "Абсолютно не в моих правилах ждать от кого-либо подачек или признания." (show_side="left", show_kind="speech")
        ev "Всё, что я получу от Академии — я получу, потому что заслужила это своими силами, а не потому что вылизала чью-то зажиревшую задницу." (show_side="left", show_kind="speech")
        hide eveina

        show kaistr annoyed at kaistr_right
        kr "Язычок бы ваш стоило подрезать, а то вдруг зацепится за что-то. Будет неприятно." (show_side="right", show_kind="speech")
        kr "Выметайтесь из моего кабинета, вам здесь, кроме проваленного экзамена, ловить нечего." (show_side="right", show_kind="speech")
        hide kaistr

    show eveina angry at eveina_left
    ev_thought "Когда-нибудь. Когда это всё закончится..." (show_side="left", show_kind="thought")
    ev_thought "Я напишу целый доклад о том, почему ты не должен учить студентов." (show_side="left", show_kind="thought")
    hide eveina

    n "Она развернулась на каблуках и вылетела за дверь, не оборачиваясь." (show_side="none", show_kind="speech")

    scene bg kael_cabinet at bg_fullscreen with dissolve

    n "Войдя в следующий кабинет, она всё ещё была на взводе. Каэль не поднял глаз, вводя что-то в терминале. И, не смотря на неё, бросил:" (show_side="none", show_kind="speech")

    show kael normal at kael_right
    ka "Высший балл." (show_side="right", show_kind="speech")
    hide kael

    n "Эвейна удивленно моргнула и уставилась на него в недоумении." (show_side="none", show_kind="speech")

    show eveina wondered at eveina_left
    ev "А… Ты не будешь задавать вопросы?" (show_side="left", show_kind="speech")
    hide eveina

    show kael normal at kael_right
    ka "Я и так знаю всё, что нужно." (show_side="right", show_kind="speech")
    ka "Если бы мне пришлось выбирать — сидеть здесь или с тобой над задачей Идентики… Меня бы здесь не было." (show_side="right", show_kind="speech")
    ka "Но, увы, выбора у меня тоже не было." (show_side="right", show_kind="speech")
    hide kael

    n "Он сделал жест рукой, отпуская её. Но прежде чем она успела повернуться — Каэль всё же поднял на неё глаза. И замер." (show_side="none", show_kind="speech")
    n "Эвейна, сама не замечая этого, всё ещё была напряжённой, словно струна. Пальцы на руках сжаты в кулаки, плечи приподняты." (show_side="none", show_kind="speech")
    n "На лице — выражение, будто её только что пытались смять в бумажный комок." (show_side="none", show_kind="speech")
    n "Каэль долго оценивающе смотрел на неё, пока в его глазах не промелькнуло сомнение — на мгновение ему показалось, что это он сделал что-то не так." (show_side="none", show_kind="speech")
    n "Она заметила это и, осознав, как выглядит со стороны, позволила себе расслабиться. Из груди вырвался тяжелый выдох, вместе с которым плечи опустились, а кулаки разжались." (show_side="none", show_kind="speech")

    show eveina eyeroll at eveina_left
    ev "Я бы тоже с удовольствием пропустила предыдущий кабинет. Или хотя бы ударила кое-кого планшетом по лбу." (show_side="left", show_kind="speech")
    hide eveina

    n "В его глазах мелькнуло что-то недоброе. Но он ничего не ответил." (show_side="none", show_kind="speech")

    show eveina eyebrow at eveina_left
    ev "Ты всегда так ненавидел экзамены?" (show_side="left", show_kind="speech")
    hide eveina

    show kael thinking at kael_right
    ka "С юности. Особенно — когда сам их сдавал." (show_side="right", show_kind="speech")
    hide kael

    show eveina eyebrow at eveina_left
    ev "Погоди, ты… нервничал?" (show_side="left", show_kind="speech")
    hide eveina

    show kael smile at kael_right
    ka "Естественно. Один раз даже забыл, как зовут преподавателя. Неловко вышло. Особенно когда он оказался моим наставником на следующие два года." (show_side="right", show_kind="speech")
    hide kael

    show eveina annoyed at eveina_left
    ev "А теперь сам пугаешь студентов до дрожи в коленях. Интересная эволюция." (show_side="left", show_kind="speech")
    hide eveina

    show kael intrigued at kael_right
    ka "Это форма мести. Медленная, системная и совершенно легальная." (show_side="right", show_kind="speech")
    hide kael

    n "Хмыкнув, Эвейна обвела кабинет взглядом." (show_side="none", show_kind="speech")

    show eveina normal at eveina_left
    ev "Тут... уютно. В кабинете." (show_side="left", show_kind="speech")
    hide eveina

    show kael eyebrow at kael_right
    ka "Только ты можешь так сказать про помещение с голыми стенами и терминалом." (show_side="right", show_kind="speech")
    hide kael

    show eveina thinking at eveina_left
    ev "Ну, здесь пахнет наукой. Это по мне." (show_side="left", show_kind="speech")
    hide eveina

    show kael normal at kael_right
    ka "Знаю. Именно поэтому и не стал гнать тебя вон при первой нашей встрече." (show_side="right", show_kind="speech")
    hide kael

    show eveina intrigued at eveina_left
    ev "А я думала — ты просто был заинтригован." (show_side="left", show_kind="speech")
    hide eveina

    show kael smile at kael_right
    ka "И это тоже. Признаться, хотел проверить, как быстро ты сбежишь." (show_side="right", show_kind="speech")
    hide kael

    show eveina eyebrow at eveina_left
    ev "И?" (show_side="left", show_kind="speech")
    hide eveina

    n "Взгляд Каэля оторвался от терминала и упёрся в Эвейну." (show_side="none", show_kind="speech")

    show kael normal at kael_right
    ka "А ты не сбежала." (show_side="right", show_kind="speech")
    hide kael

    n "Под его пристальным взглядом Эвейна вздохнула ещё раз, коротко кивнула и вышла." (show_side="none", show_kind="speech")

    scene bg corridor_3 at bg_fullscreen with dissolve

    n "На выходе из коридора экзаменаторов она заметила Лею — та ожидала своей очереди." (show_side="none", show_kind="speech")

    show leya eyebrow at leya_right
    le "Как прошло?" (show_side="right", show_kind="speech")
    hide leya

    if ezari_first_exam == "right_answer" and raukt_first_exam == "joke":
        show eveina normal at eveina_left
        ev "Вроде неплохо. Высший бал от всех, кроме Кайстра." (show_side="left", show_kind="speech")
        hide eveina
        show leya eyebrow at leya_right
        le "Ого. Не удивлюсь, если ты окажешься лучшей на курсе. Значит, подготовка не прошла даром?" (show_side="right", show_kind="speech")
        hide leya
        show eveina smile at eveina_left
        ev "Скажем так, Вирт дал мне хороший стимул." (show_side="left", show_kind="speech")
        hide eveina
    else:
        show eveina normal at eveina_left
        ev "Вроде неплохо. Но могло быть и лучше." (show_side="left", show_kind="speech")
        hide eveina
        show leya eyebrow at leya_right
        le "Ну, неплохо звучит... неплохо? Я к тому, что ты сделала всё, что могла, верно?" (show_side="right", show_kind="speech")
        hide leya
        show eveina smile at eveina_left
        ev "Скажем так, Вирт дал мне хороший стимул." (show_side="left", show_kind="speech")
        hide eveina
    if kaistr_first_exam == "answer":
        show eveina upset thinking at eveina_left
        ev "С Кайстром только немного пошло не по плану... надеюсь, мне за это опять не прилетит." (show_side="left", show_kind="speech")
        hide eveina
        show leya eyebrow at leya_right
        le "Опять? Ну зачем ты..." (show_side="right", show_kind="speech")
        hide leya
        show eveina normal at eveina_left
        ev "Не бери в голову, разберусь." (show_side="left", show_kind="speech")
        hide eveina

    n "Лея мотнула головой и подняла палец вверх, направляясь к первой двери." (show_side="none", show_kind="speech")

    show eveina smile at eveina_left
    ev "Удачи с экзаменами." (show_side="left", show_kind="speech")
    hide eveina

    n "Проводив Лею взглядом, Эвейна свернула за угол и направилась в сторону архива. Туда, где вопросы задаёт она." (show_side="none", show_kind="speech")

    jump scene_6_10
