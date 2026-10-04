label scene_4_5:
    $ previous_scene = "scene_4_4"
    $ next_scene = "scene_4_6"
    $ current_scene = "scene_4_5"

    # =========================================================
    # СЦЕНА 4_5 — «ОТРАБОТКА / ПОЦЕЛУЙ»
    # Источник: оригинальная scene_4_4, строки 119-403
    # Изменения: header, jump в конце → scene_4_6
    #            второй сбой имплантов добавлен в ветку continue
    # =========================================================

    call fade_to_black(1.2, 0.8)

    scene bg lab at bg_fullscreen with dissolve

    n "На отработке Каэль посадил её за терминал, дав задание откалибровать своё решение задачи Идентики. Не худший вариант. Было даже увлекательно." (show_side="none", show_kind="speech")
    n "Он сидел рядом, на соседнем терминале, закинув одну ногу на кресло. Иногда наклонялся, указывал на параметры, подсказывал." (show_side="none", show_kind="speech")
    n "Говорил сухо, но без колкостей, почти вежливо, что было совсем не в его стиле. До одного момента." (show_side="none", show_kind="speech")

    show kael normal at kael_right
    ka "Ты так и не ответила мне в первую встречу. Зачем ты поступила в Академию, Хейла? Только не говори мне про мечты и вдохновение." (show_side="right", show_kind="speech")
    hide kael

    show eveina normal at eveina_left
    ev_thought "Ого... Каэль, ты что, решил со мной просто поболтать?" (show_side="left", show_kind="thought")
    hide eveina 
    show eveina annoyed at eveina_left
    ev_thought "Извини, сегодня настроение не располагает к откровениям. Благодаря тебе, в основном." (show_side="left", show_kind="thought")
    hide eveina 
    show eveina intrigued at eveina_left
    ev "Мне говорили, тут можно найти подходящую пассию." (show_side="left", show_kind="speech")
    hide eveina

    n "Брови Каэля впервые на её памяти взлетели вверх в изумлении. Он подозрительно прищурился." (show_side="none", show_kind="speech")

    show kael eyebrow at kael_right
    ka "Пассию?" (show_side="right", show_kind="speech")
    hide kael

    show eveina thinking at eveina_left
    ev_thought "Записать на будущее: сарказм и Каэль — вещи несовместимые." (show_side="left", show_kind="thought")
    hide eveina
    show eveina normal at eveina_left
    ev "Это шутка, Каэль." (show_side="left", show_kind="speech")
    hide eveina
    show eveina eyebrow at eveina_left
    ev_thought "Слышал такое слово?" (show_side="left", show_kind="thought")
    hide eveina
    show eveina normal at eveina_left
    ev "Нечего особенно рассказывать. Всё как у всех. Я тут, чтобы получить знания и построить карьеру в научной сфере." (show_side="left", show_kind="speech")
    hide eveina

    n "Он посмотрел на неё без привычного скепсиса и надменности. Но и мягкости в его взгляде не было, скорее ленивый интерес." (show_side="none", show_kind="speech")

    show kael normal at kael_right
    ka "Тяга к знаниями, значит. Карьера... И вправду, всё как у всех." (show_side="right", show_kind="speech")
    hide kael
    show kael thinking at kael_right
    ka "Только интересно... что из этого становится причиной того, что некоторые прибегают к не самым этичным методам достижения своих целей." (show_side="right", show_kind="speech")
    hide kael

    n "Как только до неё дошел смысл его слов, во рту вдруг стало сухо. Эвейна сглотнула." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev_thought "Да чтоб тебя..." (show_side="left", show_kind="thought")
    hide eveina

    show kael thinking at kael_right
    ka "Люди редко действуют из чистого порыва. Особенно — в науке." (show_side="right", show_kind="speech")
    hide kael
    show kael normal at kael_right
    ka "За каждым «я хочу понять» почти всегда стоит «я хочу доказать»." (show_side="right", show_kind="speech")
    hide kael
    show kael serious at kael_right
    ka "Себе. Другим. Одному конкретному человеку." (show_side="right", show_kind="speech")
    hide kael

    show eveina thinking at eveina_left
    ev_thought "О чём именно он знает? О книге? Об ИИ? О закрытом архиве? Обо всём?" (show_side="left", show_kind="thought")
    hide eveina
    show eveina angry at eveina_left
    ev_thought "Чёрт!" (show_side="left", show_kind="thought")
    hide eveina

    n "Он наклонился, внимательно глядя в её глаза. Изучая каждую реакцию на его слова." (show_side="none", show_kind="speech")

    show kael serious at kael_right
    ka "В таких поступках нет благородства. Есть только импульс. Голод. Претензия." (show_side="right", show_kind="speech")
    ka "Немного самонадеянности и капля вседозволенности." (show_side="right", show_kind="speech")
    hide kael

    show eveina annoyed at eveina_left
    ev_thought "Ты понятия не имеешь, о чём говоришь. Чёрт, ты просто складываешь из меня уравнение!" (show_side="left", show_kind="thought")
    hide eveina

    n "Будто и не ожидая ответа, Каэль снова откинулся назад и ненадолго задумался над своими словами, глядя в потолок." (show_side="none", show_kind="speech")

    show kael thinking at kael_right
    ka "Да. Вседозволенность — первопричина. Как иначе объяснить кражу под носом у профессора?" (show_side="right", show_kind="speech")
    hide kael

    n "Он даже не смотрел в её сторону, говоря это. А зря. Потому что в следующее мгновение Эвейна сорвалась." (show_side="none", show_kind="speech")
    n "Она вскочила из-за терминала. Её руки тряслись, а взгляд в этот момент мог бы выжечь на лбу Каэля нехорошее слово." (show_side="none", show_kind="speech")

    show eveina angry at eveina_left
    ev "Ты ничего обо мне не знаешь! Хватит! Просто… отвяжись!" (show_side="left", show_kind="speech")
    hide eveina

    n "Его взгляд вернулся к ней — такой же спокойный и оценивающий, лишь слегка удивленный." (show_side="none", show_kind="speech")

    show kael eyebrow at kael_right
    ka "Я назвал очевидное. Ты же предпочла кричать. Интересно." (show_side="right", show_kind="speech")
    hide kael

    n "На его лице не отражалось ни единой эмоции, кроме капли заинтересованности. Не настолько важной, чтобы он сменил расслабленную позу, но настолько, чтобы внимательный взгляд продолжал изучать её." (show_side="none", show_kind="speech")

    show eveina wondered at eveina_left
    ev_thought "Господи, да он же и правда видит во мне лабораторную мышь!" (show_side="left", show_kind="thought")
    hide eveina

    n "Осознание этого факта, впрочем, не добавило спокойствия Эвейне. Напротив, где-то в горле заклокотала ярость." (show_side="none", show_kind="speech")
    n "Следующие слова вылетели из её рта, до того, как она успела осознать, что говорит." (show_side="none", show_kind="speech")

    show eveina angry at eveina_left
    ev "Хватит! Перестань смотреть как псих, который хочет разобрать меня на запчасти!" (show_side="left", show_kind="speech")
    hide eveina

    n "Его губы дрогнули. В единственном биологическом глазу заплескался расплавленный металл. А из искуственного, казалось, сейчас начнут вылетать искры. Каэль медленно встал." (show_side="none", show_kind="speech")

    show kael eyebrow at kael_right
    ka "Может, и хочу." (show_side="right", show_kind="speech")
    hide kael
    show kael angry at kael_right
    ka "А может, хочу, чтобы ты вспомнила, что разговариваешь не с соседкой по комнате, а с тем, кто тебя сюда допустил." (show_side="right", show_kind="speech")
    hide kael

    n "Холодный липкий страх пронзил сердце Эвейны, пульс затрепыхался где-то в горле. Каэль снова отвернулся к терминалу и не обращал на неё внимания." (show_side="none", show_kind="speech")

    show eveina wondered at eveina_left
    ev_thought "Я что, серьезно назвала преподавателя психом?" (show_side="left", show_kind="thought")
    hide eveina
    show eveina annoyed at eveina_left
    ev_thought "Да я сама ненормальная!" (show_side="left", show_kind="thought")
    hide eveina
    show eveina sad at eveina_left
    ev_thought "Я же сейчас вылечу отсюда…" (show_side="left", show_kind="thought")
    hide eveina

    n "Немного постояв в нерешительности, она снова села за терминал, чувствуя, как её всю трясёт." (show_side="none", show_kind="speech")
    n "До конца отработки они почти не разговаривали. Он почти всё время молчал, анализируя её работу, иногда давая короткие сухие комментарии. Она боялась произнести хоть слово, переваривая ситуацию и выполняя его указания." (show_side="none", show_kind="speech")
    n "Когда они закончили, был уже поздний вечер. Руки не слушались, а голова была тяжёлой. Девушка собиралась уйти, когда Каэль встал и окликнул её." (show_side="none", show_kind="speech")

    show kael normal at kael_right
    ka "Подожди. Нам стоит обсудить то, что произошло." (show_side="right", show_kind="speech")
    hide kael

    n "Эвейна остановилась и устало выдохнула." (show_side="none", show_kind="speech")

    show eveina eyeroll at eveina_left 
    ev_thought "Да, Каэль, полночь — самая пора для обсуждения того, как я ворую вещи и нарушаю субординацию." (show_side="left", show_kind="thought")
    hide eveina
    show eveina sad at eveina_left 
    ev_thought "Боже, как же стыдно." (show_side="left", show_kind="thought")
    hide eveina
    show eveina normal at eveina_left 
    ev "Я… извини. Я не должна была так себя вести. Просто... я устала." (show_side="left", show_kind="speech")
    hide eveina

    n "Он не ответил. Она отвернулась, заканчивая этот разговор. И в этот момент его ладонь поймала её запястье. Мягко, но крепко." (show_side="none", show_kind="speech")

    show eveina normal at eveina_left 
    ev "Каэль, я правда…" (show_side="left", show_kind="speech")
    hide eveina
   
    n "Она повернулась и застыла в нерешительности. Он был прямо перед ней, на расстоянии нескольких сантиметров. Его глаза изучающе смотрели на неё." (show_side="none", show_kind="speech")
    n "Лицо — непроницаемо, как всегда. Но что-то в позе и жестах всё же заставило решить Эвейну, что он борется с сомнением." (show_side="none", show_kind="speech")

    show eveina eyebrow at eveina_left 
    ev_thought "Ты же не собираешься…" (show_side="left", show_kind="thought")
    hide eveina

    n "Будто в ответ на её мысли Каэль задумчиво произнёс:" (show_side="none", show_kind="speech")

    show kael normal at kael_right
    ka "Эвейна, я собираюсь тебя поцеловать." (show_side="right", show_kind="speech")
    ka "И у тебя есть шанс меня остановить." (show_side="right", show_kind="speech")
    hide kael

    show eveina wondered at eveina_left 
    ev "Что ты..." (show_side="left", show_kind="speech")
    hide eveina

    n "Слова застряли в глотке, пока девушка в немом шоке наблюдала, словно со стороны, как лицо Каэля приближается к ней." (show_side="none", show_kind="speech")
    n "Она так и не успела понять, что именно собиралась сказать, но это вдруг стало неважно, потому что в следующий момент прохладные губы мягко коснулись её." (show_side="none", show_kind="speech")
    n "Его ладонь отпустила запястье и скользнула к её талии. Одним точным движением он притянул её ближе, плотно, без колебаний." (show_side="none", show_kind="speech")
    n "Глаза Эвейны широко распахнулись от неожиданности. Всё вдруг перестало быть важным — имел значение только настойчивый поцелуй, лишивший её всякой возможности к сопротивлению." (show_side="none", show_kind="speech")

    scene bg kael first kiss at bg_fullscreen with dissolve
    pause
    
    n "Каэль целовал так, будто ожидал, что она сейчас оттолкнёт его, но до этого момента не собирался останавливаться." (show_side="none", show_kind="speech")

    #show eveina wondered at eveina_left 
    ev_thought "Что ты творишь... Ты не должен..." (show_side="left", show_kind="thought")
    #hide eveina

    n "Мысли метались, бились в черепной коробке, как вспугнутые птицы. Она не знала, за что схватиться: за обиду, за страх, за стыд." (show_side="none", show_kind="speech")
    n "Но его рука крепко прижимала её талию. Её грудь упиралась в него. А его дыхание захватывало и смешивалось с её собственным." (show_side="none", show_kind="speech")

    #show eveina wondered at eveina_left 
    ev_thought "Прекрати. Это ошибка. Это…" (show_side="left", show_kind="thought")
    #hide eveina

    $ kael_first_kiss = renpy.call_screen("choice", 
    items=[
    ("остановись!", "stop"),
    ("не останавливайся...", "continue")
    ], who="Эвейна", what="Пожалуйста...", _last_say_who="ev_thought")

    if kael_first_kiss == "stop":
        n "Руки Эвейны упёрлись в грудь Каэля и слегка на неё надавили. Она не была уверена, что это возымеет хоть какой-то эффект. Впрочем, она сейчас вообще ни в чём не была уверена." (show_side="none", show_kind="speech")

        scene bg lab at bg_fullscreen with dissolve

        n "Каэль отпрянул как по команде. Ещё затуманненный взгляд пробежался по резко вздымающейся девичьей груди, рукам, что только что его оттолкнули. Между бровей парня залегла глубокая складка." (show_side="none", show_kind="speech")

        show eveina upset thinking at eveina_left 
        ev "Каэль... не думаю, что стоило..." (show_side="left", show_kind="speech")
        hide eveina

        n "Наконец, он холодно посмотрел в её глаза и, словно солдат на плацдарме, отчеканил каждое слово:" (show_side="none", show_kind="speech")

        show kael angry at kael_right
        ka "Да. Это была ошибка." (show_side="right", show_kind="speech")
        hide kael

        n "После чего развернулся и скрылся между рядов терминалов. Эвейна осталась стоять на месте, чувствуя, как её заполняют две эмоции: недоумение и... унижение." (show_side="none", show_kind="speech")
        n "Сердце билось в горле, в голове медленно нарастала лавина вопросов. Ватные ноги еле держали, а щеки горели ярким пламенем." (show_side="none", show_kind="speech")

        show eveina wondered at eveina_left
        ev_thought "Ошибка…" (show_side="left", show_kind="thought")
        ev_thought "Зачем он тогда это сделал? О чём он только думал?" (show_side="left", show_kind="thought")
        hide eveina


    elif kael_first_kiss == "continue":
        n "Его язык мягко прошёлся по нижней губе, а следом уверенно толкнулся внутрь приоткрытого от удивления рта, заставив девушку вздрогнуть." (show_side="none", show_kind="speech")
        n "Волна возбуждения, зародившись где-то внутри, пронеслась по всему телу, вынося из головы все границы разумного." (show_side="none", show_kind="speech")
        n "И Эвейна не заметила, как сдалась. С её губ сорвался еле слышный стон. Она прижалась к нему всем телом и ответила на поцелуй." (show_side="none", show_kind="speech")
        n "Почти с жадностью, почти со злостью — за всю эту усталость, за раздражение, за напряжение между ними, которое наконец прорвалось наружу." (show_side="none", show_kind="speech")
        n "Язык переплёлся с его языком в диком танце, вызывая тягучее ощущение внизу живота." (show_side="none", show_kind="speech")

        #show eveina intrigued at eveina_left 
        ev_thought "Пошло всё к чёрту, пусть это не заканчивается..." (show_side="left", show_kind="thought")
        #hide eveina

        scene bg lab at bg_fullscreen with dissolve

        n "И именно в этот момент он остановился. Резко, почти грубо отстранился, будто обжёгся." (show_side="none", show_kind="speech")

        # --- Второй сбой имплантов — явный, на её глазах ---
        n "Пальцы коснулись виска — тот же жест, что она не видела на практике. Но сейчас — у неё на глазах." (show_side="none", show_kind="speech")
        n "Секунда. Дыхание сбилось. Потемневший взгляд выдавал ещё теплющееся внутри желание, но глаза снова смотрели на неё холодным изучающим взглядом." (show_side="none", show_kind="speech")

        show eveina eyebrow at eveina_left
        ev_thought "Что это было?" (show_side="left", show_kind="thought")
        hide eveina

        n "Словно солдат на плацдарме он отчеканил каждое слово:" (show_side="none", show_kind="speech")

        show kael serious at kael_right
        ka "Это была ошибка." (show_side="right", show_kind="speech")
        hide kael

        n "После чего развернулся и скрылся между рядов терминалов. Эвейна осталась стоять на месте, чувствуя, как её заполняют две эмоции: недоумение и... унижение." (show_side="none", show_kind="speech")
        n "Сердце билось в горле, в голове медленно нарастала лавина вопросов. Ватные ноги еле держали, а щеки горели ярким пламенем." (show_side="none", show_kind="speech")

        show eveina wondered at eveina_left
        ev_thought "Ошибка…" (show_side="left", show_kind="thought")
        ev_thought "Зачем он тогда это сделал? И… чёрт, почему я ему ответила?" (show_side="left", show_kind="thought")
        hide eveina


    n "Из глубины лаборатории раздался его голос. Чёткий. Уравновешенный. Будто не принадлежавший тому, кто только что её поцеловал." (show_side="none", show_kind="speech")
    
    show kael normal at kael_right
    ka "На сегодня мы закончили." (show_side="right", show_kind="speech")
    hide kael

    n "Девушка не попрощалась. Но уходя, с каждым шагом чувствовала, как внутри неё расползается что-то необратимое." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev_thought "Ты всё контролируешь, да?" (show_side="left", show_kind="thought")
    hide eveina
    show eveina annoyed at eveina_left
    ev_thought "Ты выбивал меня из равновесия с первого дня." (show_side="left", show_kind="thought")
    ev_thought "А потом наблюдал, изучая каждую мою реакцию." (show_side="left", show_kind="thought")
    ev_thought "Но это... Это чересчур даже для тебя..." (show_side="left", show_kind="thought")
    hide eveina
    show eveina angry at eveina_left
    ev_thought "Сам ты — ошибка, Каэль!" (show_side="left", show_kind="thought")
    hide eveina
    jump scene_4_6
