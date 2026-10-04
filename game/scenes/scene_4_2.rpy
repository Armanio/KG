label scene_4_2:
    $ previous_scene = "scene_4_1"
    $ next_scene = "scene_4_3"
    $ current_scene = "scene_4_2"
    call fade_to_black(1.2, 0.8)

    scene bg virt_cabinet at bg_fullscreen with dissolve
    # play music "bgm/office_theme.ogg" fadein 2.0

    n "Утро не обещало ничего хорошего: сообщение от Вирта пришло с пометкой «Срочно». Эвейна уронила ложку в чашку — чай плеснул через край, но она даже не заметила." (show_side="none", show_kind="speech")
    n "Текст был безупречно лаконичен:" (show_side="none", show_kind="speech")
    n "🔔{i}Отправитель: Проф. А. Вирт\nТема: Визит\nСообщение:\nМисс Хейла, прошу вас подойти в мой кабинет после завтрака.\nПо возможности, до начала утренних занятий.\n— А. Вирт{/i}" (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev_thought "Всё. Попалась. Моя комната — склад краденого." (show_side="left", show_kind="thought")
    hide eveina
    show eveina eyebrow at eveina_left
    ev_thought "Видимо, на очереди отчисление и публичная порка?" (show_side="left", show_kind="thought")
    hide eveina 

    n "Пальцы дрожали, когда она стучала по панели двери. Та открылась с мягким шуршанием. Кабинет встречал тишиной и... отсутствием самого Вирта за столом." (show_side="none", show_kind="speech")
    n "Вместо этого он ходил из угла в угол, держа в руках кружку с дымящимся напитком. На его лице было что-то неуловимо бодрое." (show_side="none", show_kind="speech")
    n "Он выглядел не как человек, который собирается читать нотации. Скорее — как тот, кто только что услышал очень хорошую новость." (show_side="none", show_kind="speech")

    show eveina eyebrow at eveina_left
    ev_thought "Выглядит так, будто выиграл в лотерею. Порка отменяется?" (show_side="left", show_kind="thought")
    hide eveina 

    show virt normal at virt_right
    vi "Мисс Хейла. Спасибо, что пришли так быстро." (show_side="right", show_kind="speech")
    hide virt

    n "Он подошёл ближе, мягко улыбнулся и, поставив кружку, кивнул на планшет на столе. На экране Эвейна разглядела один из отчетов по её лабораторной практике." (show_side="none", show_kind="speech")

    show virt smile at virt_right
    vi "Я посмотрел ваше решение по задаче Идентики. И... должен признаться, я впечатлён." (show_side="right", show_kind="speech")
    hide virt

    show eveina wondered at eveina_left
    ev_thought "Но не так, как я сейчас..." (show_side="left", show_kind="thought")
    hide eveina
    show eveina eyebrow at eveina_left
    ev "Это... неожиданно, профессор." (show_side="left", show_kind="speech")
    hide eveina 

    show virt smile at virt_right
    vi "Что именно? То, что вы справились? Или то, что я об этом узнал?" (show_side="right", show_kind="speech")
    hide virt

    n "Он говорил это с мягкой искренней улыбкой. И от этого становилось только тревожнее." (show_side="none", show_kind="speech")

    show virt smile at virt_right
    vi "У вас редкий ум. И редкая смелость. Не каждый студент вообще пытается решать подобные задачи, не говоря уже об успешной попытке." (show_side="right", show_kind="speech")
    vi "Вы не просто повторили известное. Вы дали новое направление." (show_side="right", show_kind="speech")
    hide virt

    n "Эвейна опустила взгляд. Но внутри разлилось тепло. Вирт говорил не как преподаватель. Как... друг, которому действительно не всё равно. И это подкупало." (show_side="none", show_kind="speech")

    show virt smile at virt_right
    vi "Полагаю, вы произвели впечатление не только на меня. Каэль очень тепло отзывался о ваших способностях на его занятиях." (show_side="right", show_kind="speech")
    hide virt

    show eveina eyebrow at eveina_left
    ev_thought "Каэль и тепло в одном предложении? Мы точно об одном Каэле?" (show_side="left", show_kind="thought")
    hide eveina 

    show virt normal at virt_right
    vi "Он уже начал разработку прототипа на основе вашего решения и обязательно пригласит вас поучаствовать в подготовке эксперимента." (show_side="right", show_kind="speech")
    vi "Я хотел, чтобы вы понимали — как наставник я горжусь вашими успехами." (show_side="right", show_kind="speech")
    hide virt

    n "Аурелиан сделал паузу и посмотрел ей в глаза. Эвейна была сбита с толку." (show_side="none", show_kind="speech")

    show eveina normal at eveina_left
    ev "Я… э… Спасибо." (show_side="left", show_kind="speech")
    hide eveina

    n "На несколько секунд оба замолкли. Взгляд профессора стал ещё теплее." (show_side="none", show_kind="speech")

    show virt normal at virt_right
    vi "Чай? Мне бы хотелось послушать вас. Если вы, конечно, позволите." (show_side="right", show_kind="speech")
    hide virt

    n "Не дожидаясь ответа, он взял чайник со стола и налил дымящийся напиток во вторую чашку. По комнате разлился неповторимый травяной аромат." (show_side="none", show_kind="speech")

    show virt normal at virt_right
    vi "Я хотел бы обсудить с вами…" (show_side="right", show_kind="speech")
    vi "Вы всё ещё проводите в архивах гораздо больше времени, нежели другие студенты." (show_side="right", show_kind="speech")
    vi "Не считаете, что пришло время рассказать, что вы так настойчиво изучаете?" (show_side="right", show_kind="speech")
    hide virt

    n "Вопрос застал Эвейну врасплох. Она лихорадочно соображала." (show_side="none", show_kind="speech")

    show eveina wondered at eveina_left
    ev_thought "Что я ему скажу?" (show_side="left", show_kind="thought")
    hide eveina
    show eveina thinking at eveina_left
    ev_thought "Что у меня в браслете живёт ворованный ИИ?" (show_side="left", show_kind="thought")
    ev_thought "Что я ищу имя, стёртое из всех баз данных?" (show_side="left", show_kind="thought")
    hide eveina
    show eveina eyebrow at eveina_left
    ev_thought "Что мне даром не сдалось их образование, если оно не поможет мне вылечить отца?" (show_side="left", show_kind="thought")
    hide eveina

    n "Вирт сделал шаг ей навстречу и протянул чашку. Эвейна на автомате сделала шаг назад. Не от страха — от неожиданности его вопроса." (show_side="none", show_kind="speech")

    show virt normal at virt_right
    vi "Осторожнее!" (show_side="right", show_kind="speech")
    hide virt

    n "Слишком поздно." (show_side="none", show_kind="speech")
    n "Спина Эвейны ударилась о стеллаж. Один из фиолетовых плодов, свисающих с декоративного растения, сорвался и с сокрушительной мягкостью шлёпнулся ей на макушку." (show_side="none", show_kind="speech")
    n "И взорвался. Ярко-синие капли разлетелись по её волосам, щекам, даже за воротник. Несколько капель попали на лицо самого Вирта." (show_side="none", show_kind="speech")

    show eveina wondered at eveina_left
    ev "Упс." (show_side="left", show_kind="speech")
    hide eveina

    n "Реакция профессора была молниеносной. Обе чашки оказались на столе. Аурелиан схватил со стола салфетки и вернулся к девушке." (show_side="none", show_kind="speech")
    n "Эвейна удивленно моргнула, когда рука с салфеткой аккуратно промокнула капли на её лице." (show_side="none", show_kind="speech")

    show eveina wondered at eveina_left
    ev_thought "Так, это явно не то, чем должен был закончится этот разговор..." (show_side="left", show_kind="thought")
    hide eveina

    n "Девушка опустила глаза, но ощущения никуда делись. Она чувствовала, как Вирт осторожно коснулся её виска, убрал прядь, промокнул щёку." (show_side="none", show_kind="speech")
    n "Чувствовала, как его дыхание касается её кожи. Как салфетка спустилась к подбородку и провела линию вдоль шеи." (show_side="none", show_kind="speech")
    n "Из под опущенных ресниц Эвейна заметила, как прядь его волос упала Вирту на лицо. Он будто этого не заметил." (show_side="none", show_kind="speech")

    show eveina intrigued at eveina_left
    ev_thought "По канонам любой мелодрамы между нами должна пробежать искра." (show_side="left", show_kind="thought")
    hide eveina

    n "От нелепости ситуации Эвейна не смогла скрыть улыбку. Аурелиан мягко улыбнулся в ответ." (show_side="none", show_kind="speech")

    show virt intrigued at virt_right
    vi "..." (show_side="right", show_kind="speech")
    hide virt

    show eveina smile at eveina_left
    ev_thought "А от этой улыбки девичье сердце должно забиться быстрее." (show_side="left", show_kind="thought")
    hide eveina

    n "Он выкинул за спину первую салфетку и второй аккуратно провёл по волосам. В этот момент свисающая со лба прядь задела каплю на его лице." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev_thought "Чёрт, и на него попало..." (show_side="left", show_kind="thought")

    $ help_virt_with_spot = renpy.call_screen("choice", 
    items=[
    ("Стереть её.", True),
    ("Не двигаться. Сам разберётся.", False)
    ], who="Эвейна", what="Стоит...", _last_say_who="ev")
    hide eveina

    if help_virt_with_spot == True:
        n "Эвейна, не до конца осознавая, что делает, взяла ещё одну салфетку из его рук и, аккуратно промокнула синее пятно на его скуле." (show_side="none", show_kind="speech")
        n "Затем она попыталась стереть его, проведя почти до линии губ, наблюдая, как уголок его губы дрогнул, задевая салфетку." (show_side="none", show_kind="speech")
        n "Эвейна слегка улыбнулась в ответ и аккуратным движением стерла вторую каплю на его подбородке. А потом третью - почти на кончике носа." (show_side="none", show_kind="speech")
        n "Его губы снова дрогнули, приковывая взгляд девушки к очерченным линиям, красивому изгибу. Лишь на мгновение Эвейна дала волю своим мыслям, закусив собственную губу. И этого мгновения хватило, чтобы всё изменилось." (show_side="none", show_kind="speech")
        n "Когда она подняла глаза, то натолкнулась на взгляд, полный удивления... и чего-то ещё, чего там быть не должно. Взгляд стал темнее, глубже. Словно внутри него что-то качнулось." (show_side="none", show_kind="speech")
        n "Эвейна завороженно смотрела на серые радужки, медленно скрывающиеся за чернотой бездны расшираяющихся зрачков. И продолжала касаться уголка его щеки салфеткой." (show_side="none", show_kind="speech")
        n "Несколько секунд они просто смотрели друг на друга, словно загипнотизированные. Потом профессор медленно прикрыл глаза. И отстранился." (show_side="none", show_kind="speech")

        show virt serious at virt_right
        vi "Спасибо. Вот..." (show_side="right", show_kind="speech")
        hide virt

        n "Вирт протянул ей ещё несколько салфеток и отвернулся, проводя рукой по своим волосам." (show_side="none", show_kind="speech")
        n "Пока девушка наугад стирала с себя остатки пятен, он так и стоял, не поворачиваясь к ней лицом." (show_side="none", show_kind="speech")

        show eveina eyebrow at eveina_left
        ev_thought "Мне же не показалось?" (show_side="left", show_kind="thought")
        hide eveina
        show eveina wondered at eveina_left
        ev_thought "Нужно срочно это заканчивать." (show_side="left", show_kind="thought")
        hide eveina

        show eveina normal at eveina_left
        ev "Профессор, мне… нужно привести себя в порядок. До лекции." (show_side="left", show_kind="speech")
        hide eveina
        show eveina upset thinking at eveina_left
        ev "Простите за беспорядок." (show_side="left", show_kind="speech")
        hide eveina

        n "Аурелиан, будто очнувшись, обвёл кабинет растерянным взглядом, а потом взглянул на неё." (show_side="none", show_kind="speech")

    if help_virt_with_spot == False:
        n "Эвейна смиренно стояла, позволяя стирать с себя следы устроенной ей же маленькой катастрофы и наблюдая, как уголки губ профессора дрожат, скрывая улыбку." (show_side="none", show_kind="speech")
        n "Наконец, стерев последние капли, он придирчиво осмотрел студентку и, видимо, оставшись довольным своей работой, сделал шаг назад." (show_side="none", show_kind="speech")

        show virt intrigued at virt_right
        vi "Ну вот... Теперь вы сможете добраться до комнаты, не привлекая лишнего внимания." (show_side="right", show_kind="speech")
        hide virt

        show eveina upset thinking at eveina_left
        ev "Простите за беспорядок." (show_side="left", show_kind="speech")
        hide eveina


    show virt intrigued at virt_right
    vi "Это всего лишь плод. И очень точное попадание." (show_side="right", show_kind="speech")
    hide virt

    n "Эвейна смущённо направилась к выходу, стараясь не смотреть назад." (show_side="none", show_kind="speech")

    show virt normal at virt_right
    vi "Мисс Хейла." (show_side="right", show_kind="speech")
    hide virt

    n "Девушка обернулась в дверях." (show_side="none", show_kind="speech")

    show virt normal at virt_right
    vi "Совсем забыл вам сказать." (show_side="right", show_kind="speech")
    vi "Вчера вечером на вашем браслете был зафиксирован временный программный сбой." (show_side="right", show_kind="speech")
    hide virt
    show virt normal at virt_right
    vi "Судя по всему, ничего критичного, но если заметите аномалии в его работе, обратитесь ко мне за заменой." (show_side="right", show_kind="speech")
    hide virt

    n "Она молча кивнула и вышла. Дверь кабинета закрылась, заставив Эвейну почти бегом броситься прочь от неё." (show_side="none", show_kind="speech")
    
    show eveina angry at eveina_left
    ev_thought "Сбой произошёл! Сбой! Чёртов сбой программы!" (show_side="left", show_kind="thought")
    hide eveina

    jump scene_4_3
