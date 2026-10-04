label scene_7_10:
    $ previous_scene = "scene_7_9"
    $ next_scene = "start_chapter_8"
    $ current_scene = "scene_7_10"
    call fade_to_black(1.2, 0.8)
    scene bg city at bg_fullscreen with dissolve

    n "Город показался за окном транспорта, везущего их из космопорта, внезапно — без резких переходов, без архитектурной помпы." (show_side="none", show_kind="speech")
    n "Сначала появились бело-серые фасады, окна, балконы с растениями в гравиподвесах. А за ними показались бесконечные домики пригорода, в котором проживала большая часть среднего класса." (show_side="none", show_kind="speech")

    show virt serious jacket at virt_right
    vi "Я снял номер в отеле недалеко от вашего дома." (show_side="right", show_kind="speech")
    vi "Помните, вы под моей ответственностью." (show_side="right", show_kind="speech")
    hide virt

    n "Он произнёс это ровно, не глядя на неё, словно зачитал пункт из техники безопасности. Но когда Эвейна скосила на него взгляд, он добавил чуть тише:" (show_side="none", show_kind="speech")

    show virt normal jacket at virt_right
    vi "И, кроме того… я хотел быть рядом, если вам что-то потребуется." (show_side="right", show_kind="speech")
    hide virt

    n "Эвейна опустила глаза, не зная, что на это ответить. Ей всё ещё было стыдно: за сон, за попытку покопаться в его планшете, за то, что отвечала молчанием и недоверием на его искреннюю заботу." (show_side="none", show_kind="speech")
    n "Слишком многое болело внутри, чтобы начинать разговор. И слишком многое ждало впереди." (show_side="none", show_kind="speech")

    scene bg home_dining_room at bg_fullscreen with dissolve

    n "Дом был почти таким, как она его запомнила. Мягкое освещение, запах трав, фоновый шум города за окном." (show_side="none", show_kind="speech")
    n "Сиделка открыла дверь, ласково кивнула — и отступила." (show_side="none", show_kind="speech")

    show nurse normal at nurse_left
    nu "Проходите, дорогие мои. Мистер Хейла, у нас гости!" (show_side="right", show_kind="speech")
    hide nurse

    n "Риан Хейла сидел в кресле в гостиной, наблюдая за закатным небом через большое окно. На коленях лежала раскрытая книга, развернутая на середине. Растерянный взгляд блуждал, устремлённый в пространство." (show_side="none", show_kind="speech")

    show eveina sad at eveina_left
    ev_thought "А вдруг он меня не узнает? А вдруг в его мире больше не существует дочери?" (show_side="left", show_kind="thought")
    hide eveina

    n "Эвейна сделала неуверенный шаг вперед и отец, наконец, поднял на неё глаза. На секунду всё застыло в ожидании, а потом его лицо осветилось. Губы дрогнули, а руки потянулись вперёд." (show_side="none", show_kind="speech")

    show rian normal at rian_right
    ri "Эвейна?.." (show_side="right", show_kind="speech")
    hide rian

    n "Сквозь смех и слёзы девушка бросилась к нему, как будто вернулась домой после сотен лет изгнания. Грубоватые ладони сомкнулись вокруг Эвейны, прячя её в объятиях." (show_side="none", show_kind="speech")

    show rian normal at rian_right
    ri "Ты стала совсем взрослой. Такая красивая... Такая… ты." (show_side="right", show_kind="speech")
    hide rian

    n "Они говорили, не замолкая. Ни о чём и обо всём на свете: о погоде и еде на ужин, его самочувствии и последних новостях." (show_side="none", show_kind="speech")
    n "Эвейна рассказывала об Академии, о друзьях, об особенностях илейнской флоры. Отец смеялся, плакал, прячя слезы, перебивал, уточняя детали и ошибаясь в словах." (show_side="none", show_kind="speech")
    n "Вирт всё это время стоял чуть поодаль, не мешая их единению и не встревая в беседу." (show_side="none", show_kind="speech")
    n "Лишь позже, когда разговор немного угас, отец Эвейны взглянул на него." (show_side="none", show_kind="speech")

    show eveina normal at eveina_left
    ev "Пап, это профессор Аурелиан Вирт. Мой…" (show_side="left", show_kind="speech")
    hide eveina

    n "Она запнулась, не зная, как его лучше представить. Вирт пришёл ей на помощь." (show_side="none", show_kind="speech")

    show virt smile jacket at virt_right
    vi "Профессор Вирт, мистер Хейла. Думаю, мисс Хейла хотела сказать, что я декан её факультета." (show_side="right", show_kind="speech")
    hide virt

    show rian normal at rian_right
    ri "Мою дочь сопровождает декан. Надо же..." (show_side="right", show_kind="speech")
    ri "Лицо у вас… знакомое, профессор." (show_side="right", show_kind="speech")
    hide rian

    show virt thinking jacket at virt_right
    vi "Мне часто это говорят." (show_side="right", show_kind="speech")
    hide virt

    n "И тут Эвейна отметила нечто странное — Вирт смотрел в сторону, чуть дольше, чем нужно. Как будто не был до конца искренним в этот момент." (show_side="none", show_kind="speech")
    n "Но сейчас ей было не до этого. Её отец здесь, он её помнит, он улыбается ей, как раньше. И не было ничего важнее этого момента." (show_side="none", show_kind="speech")

    call fade_to_black(1.2, 0.8)
    scene bg home_bedroom at bg_fullscreen with dissolve

    n "Следующие два дня Эвейна почти не отходила от отца. Проводила с ним всё свободное время. Читала вслух его книгу, показывала старые фото." (show_side="none", show_kind="speech")
    n "Вспоминала с ним детство — его шутки, её первые шаги, их вечерние прогулки." (show_side="none", show_kind="speech")

    show eveina smile tshirt at eveina_left
    ev "А помнишь, пап, как мы с тобой в детстве ездили на ферму к тёте Лаизе?" (show_side="left", show_kind="speech")
    ev "Ты тогда учил меня кататься верхом, а потом мы устроили пикник под деревом." (show_side="left", show_kind="speech")
    hide eveina

    show rian normal at rian_right
    ri "Конечно, помню, ты так хорошо держалась в седле! Вытворяла такие безумные вещи..." (show_side="right", show_kind="speech")
    ri "Я в ту неделю нашёл на своей голове первые седые волосы." (show_side="right", show_kind="speech")
    hide rian

    show eveina smile tshirt at eveina_left
    ev "Да, я тогда была в абсолютном восторге от лошадей..." (show_side="left", show_kind="speech")
    ev "А когда мы вернулись назад, я увидела у одноклассников в школе робопони, и очень просила тебя его купить мне." (show_side="left", show_kind="speech")
    hide eveina

    show rian sad at rian_right
    ri "А я разве не купил?" (show_side="right", show_kind="speech")
    hide rian

    show eveina thinking tshirt at eveina_left
    ev "Нет, пап, не купил..." (show_side="left", show_kind="speech")
    ev "Сказал, что к вам в больницу ежедневно доставляют детей с травмами после катания на них, и что они очень опасны..." (show_side="left", show_kind="speech")
    hide eveina

    show rian normal at rian_right
    ri "Да, точно... сколько же там было переломов, не сосчитать." (show_side="right", show_kind="speech")
    hide rian

    show eveina smile tshirt at eveina_left
    ev "А помнишь, как ты отвёз меня в ботанический сад на Гелиосе?" (show_side="left", show_kind="speech")
    ev "Там были собраны кусочки фауны из всех известных человечеству биомов, и ты знал всё-всё про каждое из них..." (show_side="left", show_kind="speech")
    ev "Ты говорил, что мама очень любила растения и научила тебя в них разбираться..." (show_side="left", show_kind="speech")
    hide eveina

    n "И он вспоминал. Иногда. Но всё чаще — терялся. Взамен фраз — обрывки. Вместо имён — тени. Эвейна терялась в такие моменты." (show_side="none", show_kind="speech")
    n "Но ей всегда приходила на помощь Мари. Сиделка не злилась, но всегда прямо указывала на его ошибки." (show_side="none", show_kind="speech")

    show nurse normal at nurse_left
    nu "Ну что вы такое говорите, мистер Хейла. Всё было иначе..." (show_side="right", show_kind="speech")
    hide nurse

    n "И в эти моменты лицо её отца менялось. Становилось виноватым. Почти ущербным. Он теребил пальцами одежду, потуплял взгляд, словно хотел исчезнуть." (show_side="none", show_kind="speech")
    n "И каждый раз в этот миг что-то ломалось внутри Эвейны." (show_side="none", show_kind="speech")

    show eveina upset tshirt at eveina_left
    ev_thought "Я должна была быть здесь раньше..." (show_side="left", show_kind="thought")
    ev_thought "Нет, я должна успеть. Вернуть ему всё, что он потерял..." (show_side="left", show_kind="thought")
    hide eveina 

    call fade_to_black(1.2, 0.8)
    scene bg home_dining_room at bg_fullscreen with dissolve

    n "Утром третьего дня пришло время прощаться. Аурелиан приехал рано, чтобы помочь ей со сборами." (show_side="none", show_kind="speech")
    n "Вскоре вещи были собраны, а завтрак окончен. Сиделка убирала со стола, Эвейна помогала навести порядок, чтобы хоть чем-то себя занять." (show_side="none", show_kind="speech")
    n "Когда они закончили с уборкой — девушка направилась в комнату к отцу, чтобы попрощаться. Но не дойдя до неё, услышала приглушенные голоса." (show_side="none", show_kind="speech")
    n "Её отец и Вирт разговаривали о чём-то. Она остановилась в коридоре. И прислушалась." (show_side="none", show_kind="speech")

    show virt normal jacket at virt_right
    vi "…Я не могу остановить это. Не могу исправить." (show_side="right", show_kind="speech")
    hide virt

    show rian sad at rian_right
    ri "Я и не ждал. Мы оба знаем, что есть вещи, которые не лечатся." (show_side="right", show_kind="speech")
    ri "Но если ты и правда… ты рядом с ней…" (show_side="right", show_kind="speech")
    ri "Позаботься о ней." (show_side="right", show_kind="speech")
    ri "Она не такая сильная, какой кажется. Но она всё, что у меня есть." (show_side="right", show_kind="speech")
    hide rian 

    n "На какое-то время повисла тишина, а потом Аурелиан тихо, как клятву произнёс:" (show_side="none", show_kind="speech")

    show virt normal jacket at virt_right
    vi "Обещаю." (show_side="right", show_kind="speech")
    hide virt

    n "Эвейна развернулась и вышла. Слёзы жгли глаза, но девушка твёрдо решила не давать себе слабину." (show_side="none", show_kind="speech")

    show eveina upset tshirt at eveina_left
    ev_thought "Не сейчас, Эвейна. Сегодня папа не увидит твоих слёз." (show_side="left", show_kind="thought")
    hide eveina 

    n "Позже были крепкие долгие объятия, теплые слова." (show_side="none", show_kind="speech")
    n "Она не могла оторваться от отца, боясь, что как только отпустит его - он сразу про неё забудет." (show_side="none", show_kind="speech")

    show eveina smile tshirt at eveina_left
    ev "Я скоро снова приеду тебя проведать, пап. Обещаю." (show_side="left", show_kind="speech")
    hide eveina

    show rian normal at rian_right
    ri "Конечно. Я буду тебя ждать, зайчонок." (show_side="right", show_kind="speech")
    ri "Помни, тебя ждёт большое будущее." (show_side="right", show_kind="speech")
    ri "А я буду держаться столько, сколько потребуется, чтобы это увидеть." (show_side="right", show_kind="speech")
    hide rian

    show virt normal jacket at virt_right
    vi "Без сомнений. Я помогу ей всем, чем смогу, мистер Хейла." (show_side="right", show_kind="speech")
    vi "Спасибо за теплый приём." (show_side="right", show_kind="speech")
    hide virt

    show nurse normal at nurse_left
    nu "Хорошей дороги, мисс Хейла, профессор Вирт. Мы будем ждать от вас весточки по возвращению." (show_side="right", show_kind="speech")
    hide nurse

    scene bg city at bg_fullscreen with dissolve

    n "Профессор и Эвейна сели в транспорт молча. Но когда он начал движение, девушка не выдержала. Опустила глаза и беззвучно заплакала." (show_side="none", show_kind="speech")
    n "Волосы скрыли её лицо от всего мира, и она не увидела, но почувствовала, как её притянули к себе теплые руки Аурелиана. Девушка склонилась к нему и уткнулась лицом в его грудь." (show_side="none", show_kind="speech")
    n "Вирт не сказал ни слова. Он просто положил руку ей на спину, медленно поглаживая. Не пытался утешать, просто был рядом, подставляя плечо, ведь знал, что в этот момент — никаких слов быть не может." (show_side="none", show_kind="speech")
    
    show eveina sad tshirt at eveina_left
    ev_thought "А если он и правда… не вспомнит меня больше? Если это был последний раз?.." (show_side="left", show_kind="thought")
    hide eveina

    n "Снаружи сменялись виды. Внутри — всё горело от боли. И лишь крепкие объятия, в которые она с готовностью завернулась словно в кокон, успокаивали и дарили надежду." (show_side="none", show_kind="speech")

    jump start_chapter_8
