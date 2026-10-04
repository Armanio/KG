label scene_8_8:
    $ previous_scene = "scene_8_7"
    $ next_scene = "scene_8_9"
    $ current_scene = "scene_8_8"
    call fade_to_black(1.2, 0.8)
    scene bg forest at bg_fullscreen with dissolve

    n "Эриан проснулся, лёжа на траве. Утреннее солнце пробивалось сквозь ветви дерева над ним. Он моргнул и медленно поднялся." (show_side="none", show_kind="speech")
    n "Трава в радиусе трёх метров от места, где он только что лежал, выглядела сухой и поблекшей. Она была мертва. Как было мертво и дерево, раскинувшее над ним свои ветви." (show_side="none", show_kind="speech")
    n "Он сделал к нему несколько неуверенных шагов и прикоснулся к стволу." (show_side="none", show_kind="speech")

    show erian thinking at erian_right
    er "Прости меня. Так было нужно." (show_side="right", show_kind="speech")
    hide erian

    n "Внезапно его накрыла волна тошноты, заставляя парня осесть вдоль ствола и опереться на него спиной." (show_side="none", show_kind="speech")

    show erian annoyed at erian_right
    er_thought "Бери себя в руки. Тебе срочно нужно в Академию." (show_side="right", show_kind="thought")
    hide erian

    n "Но тошнота не проходила. Он прикрыл глаза, борясь с ней, и прокручивал в голове события последней недели." (show_side="none", show_kind="speech")

    call fade_to_black(1.2, 0.8)
    scene bg kosmodrom at bg_fullscreen with dissolve

    n "Когда Эриан узнал, что Эвейна улетает, было уже поздно. Он должен был её остановить. Убедить. Задержать. Оставить здесь." (show_side="none", show_kind="speech")
    n "Она была его лучшим шансом за много лет, первой реальной возможностью подобраться к Далону. Он мчался к шаттлу как безумный. Но остановился, не выходя из тени, когда увидел его." (show_side="none", show_kind="speech")

    show erian eyebrow at erian_right
    er_thought "А Вирту-то что здесь нужно?" (show_side="right", show_kind="thought")
    hide erian

    n "Вирт перекинулся парой фраз с Эвейной, подхватил её сумку и подтолкнул к трапу." (show_side="none", show_kind="speech")

    show erian annoyed at erian_right
    er_thought "Проклятье!" (show_side="right", show_kind="thought")
    hide erian
    show erian thinking at erian_right
    er_thought "Я должен быть там." (show_side="right", show_kind="thought")
    hide erian

    scene bg shuttle at bg_fullscreen with dissolve 

    n "Он даже не успел подумать о последствиях — уже оказался на борту. Незаметный никому, словно тень, ходил по коридору шаттла, пока не увидел свободное купе." (show_side="none", show_kind="speech")

    show erian smile at erian_right
    er_thought "Первый класс. Великолепно." (show_side="right", show_kind="thought")
    hide erian

    n "Три дня в полёте истощили его. Бесконечная концентрация требовала много сил, ведь никто не должен был его заметить. Даже во сне. Особенно во сне." (show_side="none", show_kind="speech")
    n "Это вытягивало все силы, а подпитки не было. Его родная планета была в миллионах километров. И Эриан медленно умирал." (show_side="none", show_kind="speech")
    n "Большую часть времени он лежал на кровати, стараясь не тратить силы." (show_side="none", show_kind="speech")

    show erian intrigued at erian_right
    er_thought "Какой нелепый конец — забыл, кто я есть, и бросился спасать принцессу аки рыцарь из её любимых сказок." (show_side="right", show_kind="thought")
    hide erian

    n "Парень горько усмехнулся своим мыслям, словно невовремя прозвучавшей хорошей шутке." (show_side="none", show_kind="speech")
    n "Конечно, он знал, что вовсе не спасал не принцессу. Принцесса была ключом к логову дракона. А ему нужен был сам дракон." (show_side="none", show_kind="speech")

    scene bg city at bg_fullscreen with dissolve 

    n "Когда шаттл приземлился, Эриан, пошатываясь, неуверенным шагом вышел последним. Вызвал транспорт и направился следом за Виртом и Эвейной." (show_side="none", show_kind="speech")

    scene bg eveina_home at bg_fullscreen with dissolve 

    n "Как только они остановились у старого, некогда богатого дома, он позволил себе выдохнуть." (show_side="none", show_kind="speech")

    show erian normal at erian_right
    er_thought "Значит, это её дом." (show_side="right", show_kind="thought")
    hide erian

    n "Он не знал, сколько они пробудут здесь, но надеялся, что ему хватит сил." (show_side="none", show_kind="speech")

    show erian thinking at erian_right
    er_thought "Да я еле держусь на ногах..." (show_side="right", show_kind="thought")
    hide erian
    show erian normal at erian_right
    er_thought "Нужно хоть что-то, иначе меня ждёт здесь самый бесславный конец из всех возможных." (show_side="right", show_kind="thought")
    hide erian
    show erian annoyed at erian_right
    er_thought "Неясно только, можно ли оставлять её без присмотра..." (show_side="right", show_kind="thought")
    hide erian
    show erian thinking at erian_right
    er_thought "Подумать только, ушёл на пару дней, а она успела слинять на другой конец вселенной..." (show_side="right", show_kind="thought")
    hide erian
    show erian annoyed at erian_right
    er_thought "Ещё и назвав придурком на прощание." (show_side="right", show_kind="thought")
    hide erian
    show erian smile at erian_right
    er_thought "Надо отдать ей должное — никому ещё с такой легкость не удавалось заморочить мне голову." (show_side="right", show_kind="thought")
    er_thought "Кто бы мог подумать, что из-за этой пигалицы придётся покинуть планету." (show_side="right", show_kind="thought")
    hide erian
    show erian smile wild at erian_right
    er_thought "О, Эвейна, вот доберусь до тебя..." (show_side="right", show_kind="thought")
    hide erian

    n "Мысль о том, что её ждёт, стоит ему до неё добраться, вызвало воспоминание о её хрупком теле, прижатом к стене его грудью. О его ладони, под которой приятно дрожали её губы. О её широко распахнутых глазах..." (show_side="none", show_kind="speech")
    n "Вспомнил он и о том, что тогда читал в её взгляде: испуганном, но почти готовом переступить ту границу, сохранить которую ему стоило немалых усилий." (show_side="none", show_kind="speech")

    show erian intrigued at erian_right
    er_thought "Ничего, ещё поговорим с тобой, Каэ'нари..." (show_side="right", show_kind="thought")
    hide erian  
    
    n "Поразмышляв немного о том, где он может получить так необходимую ему энергию, парень направился к ближайшему парку." (show_side="none", show_kind="speech")

    show erian annoyed at erian_right
    er_thought "Если сбежишь от меня снова — найду и посажу на цепь." (show_side="right", show_kind="thought")
    hide erian

    scene bg city_garden at bg_fullscreen with dissolve 

    n "Стараясь не привлекать внимание, он осторожно ступил на идеальный газон и присел под деревом." (show_side="none", show_kind="speech")

    show erian thinking at erian_right
    er "{i}Да, я знаю, мы с тобой не друзья. Но мне нужно немного сил.{/i}" (show_side="right", show_kind="speech")
    hide erian

    n "Дерево не ответило на его зов. Зато трава под ладонями отозвалась, и он блаженно закрыл глаза, откидывая голову на ствол." (show_side="none", show_kind="speech")

    show erian smile at erian_right
    er "{i}Спасибо тем, кто в погоне за развитием не забыл оставить маленькие оазисы вроде этого на своих планетах.{/i}" (show_side="right", show_kind="speech")
    hide erian

    n "Через пару часов он как ни в чем не бывало поднялся, оставив за собой выжженное пятно, и пошёл к дому Эвейны." (show_side="none", show_kind="speech")

    scene bg eveina_home at bg_fullscreen with dissolve 

    n "Пару дней Эриан наблюдал за домом издалека в надежде поймать момент, когда Эвейна будет одна. Но она буквально прилипла к своему старику." (show_side="none", show_kind="speech")
    n "Не отходила от него ни на час, засыпала на диване в его комнате, и постоянно о чём-то с ним говорила." (show_side="none", show_kind="speech")

    show erian annoyed at erian_right
    er "{i}Чёрт, да оторвись ты от него! Не умрёт твой отец от того, что ты перестанешь на него смотреть.{/i}" (show_side="right", show_kind="speech")
    hide erian

    n "Даже несмотря на приличное расстояние, Эриан отчётливо ощущал, что с ним что-то не так. Будто что-то в нём было сломано. Но это неважно, важна была только она." (show_side="none", show_kind="speech")
    n "А она крайне невовремя решила строить из себя идеальную дочь, вызывая в нём одну за другой волны раздражения, которые приходилось гасить внутри, чтобы они не сжирали остатки сил." (show_side="none", show_kind="speech")

    show erian annoyed at erian_right
    er "{i}Проклятье, Эвейна! Только выйди из этого чёртового сарая на минуту, тут же впечатаю тебя в стену и заставлю объясниться.{/i}" (show_side="right", show_kind="speech")
    hide erian

    n "Но Эвейна не выходила. Парень порывался ворваться внутрь, но не был уверен в своих силах — что если он не сможет стереть кому-то память? Риски были слишком велики." (show_side="none", show_kind="speech")
    n "На третье утро Вирт приехал с чемоданом. Заподозрив неладное, илейн подошёл ближе к входной двери и облокотился на слегка обветшалую стену прямо за деканом." (show_side="none", show_kind="speech")

    show nurse normal at nurse_left
    nu "Доброе утро, профессор Вирт, я как раз поставила чайник." (show_side="right", show_kind="speech")
    hide nurse

    show virt smile at virt_right
    vi "Благодарю, Мари. Мне будет не хватать вашего чая." (show_side="right", show_kind="speech")
    hide virt

    show erian annoyed at erian_right
    er_thought "Только не говори, что она остаётся…" (show_side="right", show_kind="thought")
    er_thought "Верни её назад! Мы ещё не закончили! Она мне нужна." (show_side="right", show_kind="thought")
    hide erian

    n "Аурелиан был глух к его немым просьбам, а поэтому Эриан решил, что пришло время действовать." (show_side="none", show_kind="speech")
    n "Вместе с Виртом он тенью вошел в её дом." (show_side="none", show_kind="speech")

    scene bg  home_dining_room at bg_fullscreen with dissolve 

    n "Эвейна сидела за столом, ковыряла остатки еды. Её отец устало улыбался, глядя на неё, пока веселая женщина в фартуке убирала посуду, напевая себе под нос какую-то мелодию." (show_side="none", show_kind="speech")

    show nurse normal at nurse_left
    nu "Эвейна, ты совсем не притронулась к еде. Не понравилась моя готовка?" (show_side="right", show_kind="speech")
    hide nurse

    show eveina normal at eveina_left
    ev "Нет, всё было хорошо, просто... кусок в горло не лезет." (show_side="left", show_kind="speech")
    hide eveina

    show rian normal at rian_right
    vi "Твои блюда прекрасны, как всегда, Мари. Эвейна, попробуй вот эти булочки, они ещё теплые..." (show_side="right", show_kind="speech")
    hide rian

    show eveina normal at eveina_left
    ev "Спасибо, пап. Возьму одну... в дорогу." (show_side="left", show_kind="speech")
    hide eveina

    n "Эриан неуверенно застыл. Всё здесь ощущалось таким обыденным и простым. И он сам казался себе совершенно неуместным в этом месте." (show_side="none", show_kind="speech")
    n "Отец Эвейны встал, опираясь на Вирта, и удалился в свою комнату. Эриан заметил взгляд Вирта, обернувшего на Эвейну перед выходом, будто проверяющим, что она не последовала за ними." (show_side="none", show_kind="speech")

    show erian thinking at erian_right
    er "{i}Это странно...{/i}" (show_side="right", show_kind="speech")
    hide erian 
    show erian eyebrow at erian_right
    er "{i}Вирт что, знаком с её отцом?{/i}" (show_side="right", show_kind="speech")
    hide erian

    n "Бросив взгляд на меланхолично убирающую со стола Эвейну, парень бесшумно проследовал за мужчинами, остановившись в дверях комнаты." (show_side="none", show_kind="speech")
    
    scene bg home_bedroom at bg_fullscreen with dissolve 

    n "Декан помог отцу Эвейны лечь в кровать, накрыл пледом и тихо спросил:" (show_side="none", show_kind="speech")

    show virt thinking at virt_right
    vi "Она знает, Риан? Эвейна знает?" (show_side="right", show_kind="speech")
    hide virt

    n "На лице Риана отразилось непонимание. Он растерянно огляделся. Лишь спустя долгих пару секунд пришло осознание." (show_side="none", show_kind="speech")

    show rian sad at rian_right
    ri "Ты про Диану и...? Про то, что мы с ними сделали?" (show_side="right", show_kind="speech")
    hide rian

    n "Вирт медленно кивнул." (show_side="none", show_kind="speech")

    show rian sad at rian_right
    ri "Меня преследует это во снах." (show_side="right", show_kind="speech")
    ri "Но нет, конечно нет. Она не знает. Не думаю, что я когда-нибудь смогу ей такое сказать." (show_side="right", show_kind="speech")
    hide rian

    n "Вирт молчал, опустив взгляд на свои руки, словно провинившийся школьник, не находящий слов в своё оправдание." (show_side="none", show_kind="speech")

    show rian sad at rian_right
    ri "Оно ведь не работает, да? Никогда не работало?" (show_side="right", show_kind="speech")
    hide rian

    n "Эриан услышал звук приближающихся шагов и замер. Но шаги внезапно стихли. Аурелиан покачал головой и поднял взгляд на отца Эвейны." (show_side="none", show_kind="speech")

    show virt sad at virt_right
    vi "Я не могу остановить это. Не могу исправить." (show_side="right", show_kind="speech")
    hide virt

    show rian normal at rian_right
    ri "Я и не ждал." (show_side="right", show_kind="speech")
    hide rian
    show rian sad at rian_right
    ri "Мы оба знаем, что есть вещи, которые не лечатся." (show_side="right", show_kind="speech")
    ri "Теперь знаем..." (show_side="right", show_kind="speech")
    hide rian
    show rian normal at rian_right
    ri "Но если ты и правда… рядом с ней. Обещай, что позаботишься о ней." (show_side="right", show_kind="speech")
    ri "Это всё, что я могу для неё сделать." (show_side="right", show_kind="speech")
    hide rian
    show rian sad at rian_right
    ri "Ей понадобится поддержка, когда меня не станет." (show_side="right", show_kind="speech")
    hide rian

    show virt serious at virt_right
    vi "Обещаю." (show_side="right", show_kind="speech")
    hide virt

    n "Эриан стоял в дверях и сжимал руки в кулаки, чтобы не сорваться прямо здесь. Отрезвляющий звук удаляющихся шагов напомнил, зачем он здесь." (show_side="none", show_kind="speech")

    show erian normal at erian_right
    er_thought "Не сейчас... не здесь." (show_side="right", show_kind="thought")
    hide erian
    show erian thinking at erian_right
    er_thought "Она слышала это? Понимает ли, что она услышала?" (show_side="right", show_kind="thought")
    hide erian

    n "Он вновь почувствовал, как подкашиваются ноги." (show_side="none", show_kind="speech")

    show erian annoyed at erian_right
    er_thought "Пора валить, пока не упал тут замертво." (show_side="right", show_kind="thought")
    hide erian

    n "Неспешно Эриан вышел из дома, отметив стоявшую у двери сумку Эвейны. Но это уже перестало иметь смысл. Он узнал всё, что нужно." (show_side="none", show_kind="speech")

    scene bg forest at bg_fullscreen with dissolve 
    
    n "Эриан открыл глаза и медленно поднялся, виновато коснувшись дерева в последний раз." (show_side="none", show_kind="speech")
    n "После чего оглядел себя, стряхнул сухую травинку с одежды, и направился в сторону Академии." (show_side="none", show_kind="speech")

    jump scene_8_9
