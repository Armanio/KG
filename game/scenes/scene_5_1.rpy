label scene_5_1:
    $ previous_scene = "scene_4_7"
    $ next_scene = "scene_5_2"
    $ current_scene = "scene_5_1"
    call fade_to_black(1.2, 0.8)
    scene bg night_garden at bg_fullscreen with dissolve

    n "Сад тонул в медленно сгущающихся сумерках. Воздух был тёплым, почти неподвижным, только светящиеся листья на высоких деревьях мерцали в такт её пульсу." (show_side="none", show_kind="speech")
    n "Эвейна сидела под старым деревом, притихшая, обняв колени так крепко, будто могла таким образом удержать свои мысли внутри." (show_side="none", show_kind="speech")
    n "Время в саду растянулось — и теперь казалось, что весь этот мир свёлся к её безмолвному, упрямому ожиданию. Крохотная точка внутри огромной ночи." (show_side="none", show_kind="speech")
    n "Она уже поверила, что никто не придёт. Почти встала — и тогда он вышел из тени." (show_side="none", show_kind="speech")

    show eveina normal at eveina_left
    ev_thought "Всё-таки пришёл." (show_side="left", show_kind="thought")
    hide eveina 

    n "Эриан стоял, не двигаясь, словно материализовался из самой темноты. Его лицо было спокойным, но в глазах читалась напряжённость. Голос прозвучал сухо, с язвительным оттенком." (show_side="none", show_kind="speech")

    show erian normal at erian_right
    er "Как мило, что ты снова решила поискать меня здесь." (show_side="right", show_kind="speech")
    hide erian

    show eveina eyebrow at eveina_left
    ev_thought "Оу, да ты в отличном настроении... Как раз то, что нужно для этого разговора." (show_side="left", show_kind="thought")
    hide eveina 

    n "Эвейна молча смотрела на него, ожидая продолжения. Долго ждать не пришлось." (show_side="none", show_kind="speech")

    show erian normal at erian_right
    er "У тебя интересные способы добывать информацию, Эвейна." (show_side="right", show_kind="speech")
    hide erian

    show eveina angry at eveina_left
    ev_thought "Ну что на этот раз я сделала не так?" (show_side="left", show_kind="thought")
    hide eveina
    show eveina eyebrow at eveina_left
    ev "О чём ты?" (show_side="left", show_kind="speech")
    hide eveina

    show erian annoyed at erian_right
    er "Что происходит между тобой и Виртом?" (show_side="right", show_kind="speech")
    hide erian

    show eveina eyebrow at eveina_left
    ev "Что?" (show_side="left", show_kind="speech")
    hide eveina

    n "Мужчина сделал два резких, почти угрожающих шага вперед, и замер, словно пытаясь контролировать нечто большее, чем просто раздражение." (show_side="none", show_kind="speech")

    show erian normal at erian_right
    er "Наблюдал тут за вами в архиве. Не слышал, о чём вы говорили." (show_side="right", show_kind="speech")
    hide erian
    show erian annoyed at erian_right
    er "Но этого и не требовалось." (show_side="right", show_kind="speech")
    hide erian
    show erian thinking at erian_right
    er "Кто бы мог подумать, что сам декан опустится перед тобой на колени?" (show_side="right", show_kind="speech")
    hide erian
    show erian annoyed at erian_right
    er "Какого это — ощущать его руки на своём лице?" (show_side="right", show_kind="speech")
    hide erian

    show eveina wondered at eveina_left
    ev "Ты... рехнулся?" (show_side="left", show_kind="speech")
    hide eveina

    show erian normal at erian_right
    er "Просто делаю вывод." (show_side="right", show_kind="speech")
    hide erian
    show erian thinking at erian_right
    er "Знаешь, ты умеешь быть… весьма убедительной, когда тебе что-то нужно." (show_side="right", show_kind="speech")
    hide erian
    show erian annoyed at erian_right
    er "Даже я мог бы повестись на это. Если бы ты вообще меня интересовала." (show_side="right", show_kind="speech")
    hide erian

    n "Он смотрел на неё, словно отдавая ей должное. Без злобы. Но с еле скрываемым разочарованием." (show_side="none", show_kind="speech")

    show erian thinking at erian_right
    er "Не осуждаю. Все мы что-то продаём." (show_side="right", show_kind="speech")
    hide erian
    show erian eyebrow at erian_right
    er "Главное — не забыть, сколько ты за это хочешь." (show_side="right", show_kind="speech")
    hide erian

    n "Эвейна побледнела. Cлова кольнули слишком больно, заставив девушку отшатнуться." (show_side="none", show_kind="speech")

    show eveina angry at eveina_left
    ev "Я большей чуши в жизни не слышала. Ты... ты просто отватителен." (show_side="left", show_kind="speech")
    hide eveina

    n "Эриан холодно улыбнулся." (show_side="none", show_kind="speech")

    show erian smile wild at erian_right
    er "И всё же ты идёшь именно сюда, когда тебе что-то нужно." (show_side="right", show_kind="speech")
    hide erian

    n "Молчание повисло между ними, как тонкая проволока, пока девушка путалась в своих мыслях и искала за что зацепиться. Этот диалог явно зашёл не туда." (show_side="none", show_kind="speech")

    show eveina annoyed at eveina_left
    ev "Какое тебе вообще дело до Вирта?" (show_side="left", show_kind="speech")
    hide eveina
    show eveina eyebrow at eveina_left
    ev "Впрочем, неважно." (show_side="left", show_kind="speech")
    ev "Я пришла не за этим." (show_side="left", show_kind="speech")
    hide eveina

    n "Весь его вид говорил: ну давай, расскажи мне, зачем ты пришла, чтобы я мог выдать очередную колкость." (show_side="none", show_kind="speech")
    n "Эвейна глубоко вздохнула, пытаясь успокоиться. И на выдохе выпалила:" (show_side="none", show_kind="speech")

    show eveina eyebrow at eveina_left
    ev "Кто ты такой, Эриан?" (show_side="left", show_kind="speech")
    hide eveina

    n "Он непонимающе уставился на неё." (show_side="none", show_kind="speech")

    show erian eyebrow at erian_right
    er "Что?" (show_side="right", show_kind="speech")
    hide erian

    show eveina eyebrow at eveina_left
    ev "Кто." (show_side="left", show_kind="speech")
    hide eveina

    show erian eyebrow at erian_right
    er "Что?" (show_side="right", show_kind="speech")
    hide erian

    show eveina annoyed at eveina_left
    ev "В этом диалоге слишком много «что». Отвечай." (show_side="left", show_kind="speech")
    hide eveina

    n "Его взгляд стал непроницаемым. В первый раз за всё их общение Эриан действительно не знал, что сказать." (show_side="none", show_kind="speech")
    n "Он не был сбит с толку. Нет, он замер, как зверь, заметивший ловушку слишком поздно. И его взгляд не предвещал ничего хорошего." (show_side="none", show_kind="speech")
    n "Тогда она начала." (show_side="none", show_kind="speech")
    n "Медленно, по пунктам, по обрывкам: его появление, странные знания, то, как он исчезает, как о нём не помнит Лея. Его реплики и взгляды об Академии, отсутствие цифрового следа." (show_side="none", show_kind="speech")
    n "А он всё стоял, молча, изучающе смотря на неё. Казалось, всё напряжение мира сейчас сошлось в одной точке — в его неподвижности." (show_side="none", show_kind="speech")
    n "Дослушав её до конца, Эриан не торопился с ответом, лишь неспеша блуждал непроницаемым взглядом, раздумывая над своими следующими словами." (show_side="none", show_kind="speech")

    show erian normal at erian_right
    er "Фантазии тебе не занимать." (show_side="right", show_kind="speech")
    hide erian

    show eveina annoyed at eveina_left
    ev "Отвечай." (show_side="left", show_kind="speech")
    hide eveina

    n "Он склонил голову вбок, будто оценивал — а стоит ли она правды? И это мимолетное движение заставило девушку сглотнуть, отсылая память к недавней сцене, когда он нависал над ней, зажав ей рот ладонью." (show_side="none", show_kind="speech")

    show erian eyebrow at erian_right
    er "Полагаю, ты уже всё решила?" (show_side="right", show_kind="speech")
    hide erian

    show eveina normal at eveina_left
    ev "Ну... Я думаю, ты — либо плод моего больного воображения, либо... ты илейн." (show_side="left", show_kind="speech")
    hide eveina

    n "Янтарные радужки устремленных на неё глаз стали медленно темнеть, а сам он вдруг показался совершенно чужим и пугающе опасным." (show_side="none", show_kind="speech")

    show erian annoyed at erian_right
    er "Интересное замечание, учитывая, что народ Илейн славится тем, что их никто не помнит." (show_side="right", show_kind="speech")
    er "Но вот же ты — живой пример!" (show_side="right", show_kind="speech")
    hide erian
    show erian smile wild at erian_right
    er "Ты ведь помнишь все наши маленькие приключения, Эвейна?" (show_side="right", show_kind="speech")
    hide erian

    show eveina thinking at eveina_left
    ev_thought "Слишком хорошо..." (show_side="left", show_kind="thought")
    hide eveina 

    n "Девушка на миг смутилась под пронзительным взглядом. Щеки залились румянцем, служа напоминанием обо всех его выходках, словах, прикосновениях." (show_side="none", show_kind="speech")
    n "Но отступать было поздно. Не сейчас. Сейчас она вытащит из него всю правду, чего бы ей это не стоило." (show_side="none", show_kind="speech")

    show eveina eyebrow at eveina_left
    ev "Это... потому что ты хочешь, чтобы я помнила? Или… я просто не могу тебя забыть?" (show_side="left", show_kind="speech")
    hide eveina
    show eveina thinking at eveina_left
    ev "Может, ты тут не единственный с суперспособностями." (show_side="left", show_kind="speech")
    ev "Или..." (show_side="left", show_kind="speech")
    hide eveina

    n "Она на секунду замешкалась, стоит ли произносить последнюю догадку. Но его проницательность оказалась куда проворнее." (show_side="none", show_kind="speech")

    show erian eyebrow at erian_right
    er "Или я просто не решился их применить?" (show_side="right", show_kind="speech")
    hide erian
    show erian smile wild at erian_right
    er "Я же такой нерешительный." (show_side="right", show_kind="speech")
    hide erian

    n "Он был мрачнее тучи. Эвейна — уверенней бронепоезда на полном ходу. На секунду их взгляды встретились — и в этом столкновении было больше истины, чем во всех словах до этого." (show_side="none", show_kind="speech")

    show eveina normal at eveina_left
    ev "Если ты илейн — ты мог бы заставить меня забыть. Но ты не сделал этого. Потому что знаешь — тебе нужна моя помощь." (show_side="left", show_kind="speech")
    hide eveina

    n "Она понимала, что играет с огнём, но не знала, что именно станет его топливом, а поэтому не успела осознать произошедшее в следующий момент." (show_side="none", show_kind="speech")
    n "Эриан в два прыжка оказался возле неё, заставив её вжаться в дерево. Он опёрся на ствол рукой на уровне её лица, отрезая ей путь к побегу." (show_side="none", show_kind="speech")
    n "Золотистые глаза нещадно прожигали насквозь. Девушке на мгновение показалось, что в них горит пламя, когда он медленно наклонился к её лицу и прошептал:" (show_side="none", show_kind="speech")

    show erian annoyed at erian_right
    er "Правда, Эвейна? Считаешь, что мне нужна твоя помощь?" (show_side="right", show_kind="speech")
    hide erian
    show erian smile wild at erian_right
    er "А я то думал, это ты без меня шагу не можешь ступить." (show_side="right", show_kind="speech")
    hide erian

    n "Эвейна сглотнула и опустила глаза. Меньше всего ей хотелось сейчас разозлить его. Но и отступать было некуда. Её голос звучал тихо, но твёрдо:" (show_side="none", show_kind="speech")

    show eveina normal at eveina_left
    ev "Правда. А ещё ты знаешь, что мне тоже нужна твоя помощь." (show_side="left", show_kind="speech")
    hide eveina

    n "Он криво усмехнулся. Пальцы свободной руки потянулись к её лицу, заставляя её вздрогнуть." (show_side="none", show_kind="speech")
    n "Но они лишь аккуратно убрали с её лица прядь волос, что упала на глаза." (show_side="none", show_kind="speech")
    n "Девушка машинально облизнула вдруг ставшие сухими губы. Заметив это движение, взгляд Эриана на секунду обратился к ним, а потом вернулся к её глазам с холодной улыбкой." (show_side="none", show_kind="speech")

    show erian smile wild at erian_right
    er "Эвейна, на меня не действуют твои трюки." (show_side="right", show_kind="speech")
    hide erian

    show eveina angry at eveina_left
    ev_thought "Какие к чёрту трюки, придурок?" (show_side="left", show_kind="thought")
    hide eveina 

    n "Дрожа всем телом, Эвейна с усилием подняла на него взгляд." (show_side="none", show_kind="speech")

    show eveina normal at eveina_left
    ev "Эриан, я здесь не за тем, чтобы выводить тебя на чистую воду. Мне правда нужна твоя помощь." (show_side="left", show_kind="speech")
    ev "И чтобы ты доверился мне. Как я доверилась тебе." (show_side="left", show_kind="speech")
    hide eveina

    n "Он не отвечал. Лишь смотрел в её глаза, пытаясь разглядеть в них хотя бы намёк на ложь. И не увидел там ничего кроме страха, обёрнутого в решительность безумно упёртой девушки." (show_side="none", show_kind="speech")

    show erian thinking at erian_right
    er "Чего ты хочешь, Эвейна?" (show_side="right", show_kind="speech")
    hide erian

    show eveina thinking at eveina_left
    ev_thought "Пожалуй, не лучшее время для шуток..." (show_side="left", show_kind="thought")
    hide eveina 
    show eveina normal at eveina_left
    ev "Робопони." (show_side="left", show_kind="speech")
    hide eveina 
    show eveina thinking at eveina_left
    ev_thought "Отличные последние слова. Пусть высекут их на моём надгробии." (show_side="left", show_kind="thought")
    hide eveina 

    n "Эриан застыл. Второй раз за разговор она лишила его способности говорить. Затем он сделал шаг назад и захохотал." (show_side="none", show_kind="speech")

    show erian smile at erian_right
    er "Робопони? Это ещё что за херня?" (show_side="right", show_kind="speech")
    hide erian

    n "Эвейна сбивчиво объяснила:" (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev "В детстве в нашей школе у всех детей был свой робопони. Ну, как маленькая лошадка, только робот..." (show_side="left", show_kind="speech")
    ev "Он их катал по лужайке и умел делать всякие трюки." (show_side="left", show_kind="speech")
    hide eveina
    show eveina normal at eveina_left
    ev "Я отчаянно его хотела, но папа сказал, что они травмоопасны, и не купил мне его." (show_side="left", show_kind="speech")
    ev "И вот мне 24 года, а в моей жизни так и не случился робопони." (show_side="left", show_kind="speech")
    hide eveina

    n "Новый приступ хохота разнёсся по саду." (show_side="none", show_kind="speech")

    show erian smile at erian_right
    er "Эвейна, клянусь тебе, ты — самая безумная женщина, что я встречал в своей жизни." (show_side="right", show_kind="speech")
    hide erian
    show erian intrigued at erian_right
    er "Ещё сильная. И смелая. Но, в основном, безумная." (show_side="right", show_kind="speech")
    hide erian

    n "Эвейна сделала глубокий вдох." (show_side="none", show_kind="speech")

    show eveina normal at eveina_left
    ev "Это значит да?" (show_side="left", show_kind="speech")
    ev "Ты доверишься мне?" (show_side="left", show_kind="speech")
    hide eveina

    n "Он опустил взгляд. Молчание затягивалось. У Эвейны больше не было аргументов, поэтому она просто ждала." (show_side="none", show_kind="speech")
    n "И он заговорил. Медленно, осторожно подбирая слова:" (show_side="none", show_kind="speech")

    show erian thinking at erian_right
    er "Когда-то я доверился человеку. Учёному. Он называл себя Кайр Далон." (show_side="right", show_kind="speech")
    er "Он входил в состав группы ученых-исследователей, чьей задачей было изучение нашего образа жизни и технологий." (show_side="right", show_kind="speech")
    er "Для этого им выдали андроидов-аватаров, которые управлялись с безопасного от влияния нейрополей расстояния." (show_side="right", show_kind="speech")
    er "Через этого андроида мы общались с Далоном многие месяцы. Мы разговаривали часами напролёт. Обо всём на свете." (show_side="right", show_kind="speech")
    er "О космических кораблях и системах их навигации. О нейрополях и особенностях строения наших зданий." (show_side="right", show_kind="speech")
    hide erian
    show erian normal at erian_right
    er "О женщине, в которую он был влюблен, и которая предпочла ему другого." (show_side="right", show_kind="speech")
    hide erian
    show erian upset at erian_right
    er "О страшном диагнозе, что ей поставили и о том, как он готов перевернуть всю вселенную в поисках лечения." (show_side="right", show_kind="speech")
    hide erian
    show erian normal at erian_right
    er "Я рассказал ему всё, что знал о влиянии нейрополей на человеческое сознание." (show_side="right", show_kind="speech")
    er "Потому что считал его другом. Верил, что это поможет ему спасти любимую." (show_side="right", show_kind="speech")
    hide erian
    show erian thinking at erian_right
    er "А потом он исчез. Их исследования завершились, и больше никто не приходил." (show_side="right", show_kind="speech")
    hide erian
    show erian upset at erian_right
    er "Мне было жаль, что он так и не вернулся. Но я знал — у него есть цель, которая дороже ему всей своей жизни." (show_side="right", show_kind="speech")
    hide erian
    show erian annoyed at erian_right
    er "А потом случилось страшное. То, с чем мы никогда не сталкивались." (show_side="right", show_kind="speech")
    hide erian
    show erian thinking at erian_right
    er "Пропала молодая девушка илейн. Почти твоего возраста." (show_side="right", show_kind="speech")
    er "Спустя несколько месяцев пропал ещё один илейн. А потом ещё." (show_side="right", show_kind="speech")
    hide erian
    show erian normal at erian_right
    er "Официальные запросы к вашему правительству и к руководству Академии не дали результата." (show_side="right", show_kind="speech")
    hide erian
    show erian annoyed at erian_right
    er "Они даже проблемы не поняли — {i}«подумаешь, пару молодых людей пропали — просто нашли приключений на свои задницы»{/i}." (show_side="right", show_kind="speech")
    er "Ответ звучал примерно так." (show_side="right", show_kind="speech")
    hide erian
    show erian normal at erian_right
    er "И тогда я начал копать. Поиски привели меня к некоему лекарству, «разработанному совместно с Илейн»." (show_side="right", show_kind="speech")
    hide erian
    show erian annoyed at erian_right
    er "И какого же было моё удивление, когда создателем этого лекарства я обнаружил своего старого друга." (show_side="right", show_kind="speech")
    hide erian

    n "Эриан отстранился на несколько шагов и поднял в небо тяжелый взгляд." (show_side="none", show_kind="speech")

    show erian thinking at erian_right
    er "Я не знаю, как связаны пропавшие Илейн, лекарство, Далон и Академия. Но я знаю, что они связаны." (show_side="right", show_kind="speech")
    hide erian
    show erian normal at erian_right
    er "Моя цель — остановить исчезновения. Пока не стало слишком поздно." (show_side="right", show_kind="speech")
    hide erian

    n "Он медленно развернулся к ней. Тон стал мягче." (show_side="none", show_kind="speech")

    show erian thinking at erian_right
    er "Ты хочешь спасти отца." (show_side="right", show_kind="speech")
    er "Я хочу спасти свой народ." (show_side="right", show_kind="speech")
    hide erian
    show erian normal at erian_right
    er "Похоже, у нас есть что-то общее." (show_side="right", show_kind="speech")
    hide erian

    show eveina thinking at eveina_left
    ev_thought "Ага. Комплекс бога и одержимость идеей: спаси или умри. Очаровательно." (show_side="left", show_kind="thought")
    hide eveina

    show eveina normal at eveina_left
    ev "Так… мы команда? Ты правда на моей стороне?" (show_side="left", show_kind="speech")
    hide eveina

    n "Тишина стала мягче. Листья над ними шептали — казалось, весь сад задержал дыхание. Эриан долго смотрел на неё, о чём-то размышляя. Затем коротко кивнул." (show_side="none", show_kind="speech")

    show erian thinking at erian_right
    er "Пока твоя сторона совпадает с моей — да." (show_side="right", show_kind="speech")
    hide erian
    show erian intrigued at erian_right
    er "Но не обольщайся. Я не меняю цели. Даже ради таких хорошеньких, как ты." (show_side="right", show_kind="speech")
    hide erian

    n "Эвейна ощутила хрупкое облегчение. Как будто они, балансируя на острие лезвия, всё-таки нашли равновесие. Но тут…" (show_side="none", show_kind="speech")

    show eveina wondered at eveina_left
    ev_thought "Что значит — пока?" (show_side="left", show_kind="thought")
    hide eveina
    show eveina eyebrow at eveina_left
    ev "О чём ты?" (show_side="left", show_kind="speech")
    hide eveina

    n "Эриан посмотрел на неё как на несмышленого ребёнка." (show_side="none", show_kind="speech")

    show erian intrigued at erian_right
    er "Милая маленькая Эвейна, ты правда не замечаешь тут конфликта интересов?" (show_side="right", show_kind="speech")
    hide erian  
    show erian normal at erian_right
    er "Ты ищешь создателя лекарства, чтобы он помог тебе спасти отца." (show_side="right", show_kind="speech")
    er "Я ищу создателя лекарства, чтобы остановить его во что бы то ни стало." (show_side="right", show_kind="speech")
    hide erian  
    show erian thinking at erian_right
    er "Как думаешь, как скоро наши интересы разойдутся?" (show_side="right", show_kind="speech")
    hide erian

    n "Внутри что-то с хрустом оторвалось и глухо упало. Кажется, её взгляд стал слишком выразительным — Эриан дёрнулся в её сторону, но затем остановился." (show_side="none", show_kind="speech")
    n "Будто хотел защитить её от своих собственных слов, но потом понял, насколько это нелепая затея." (show_side="none", show_kind="speech")

    show eveina sad at eveina_left
    ev "Значит, в какой-то момент… мы окажемся по разные стороны?" (show_side="left", show_kind="speech")
    hide eveina

    n "Эриан прикрыл глаза. А когда открыл — на его лице появилась кривая, полная горечи усмешка. В этой улыбке было столько усталости, что Эвейне захотелось прикоснуться к его щеке." (show_side="none", show_kind="speech")

    show erian thinking at erian_right
    er "Не в какой-то." (show_side="right", show_kind="speech")
    hide erian
    show erian normal at erian_right
    er "В точке, которая уже здесь." (show_side="right", show_kind="speech")
    er "Мы просто делаем вид, что всё ещё на одной стороне. Потому что сейчас это… удобно." (show_side="right", show_kind="speech")
    hide erian

    show eveina upset at eveina_left
    ev "..." (show_side="left", show_kind="speech")
    hide eveina

    n "Слова царапнули сердце. Она опустила глаза — в них блеснули слёзы. Эриан сделал шаг ближе и оказался перед ней." (show_side="none", show_kind="speech")

    show erian thinking at erian_right
    er "В одном ты была права с самого начала." (show_side="right", show_kind="speech")
    hide erian
    show erian normal at erian_right
    er "Ты мне нужна, Эвейна." (show_side="right", show_kind="speech")
    er "А ты хочешь быть нужной. Так что… давай пока не разрушать это хрупкое равновесие." (show_side="right", show_kind="speech")
    hide erian

    n "Он коснулся её щеки тыльной стороной пальцев." (show_side="none", show_kind="speech")

    show erian normal at erian_right
    er "Я помогу тебе найти его. И мы вместе попросим его вылечить твоего отца, если он на это способен." (show_side="right", show_kind="speech")
    er "Но после этого всё должно прекратиться." (show_side="right", show_kind="speech")
    hide erian

    show eveina sad at eveina_left
    ev "Обещаешь?" (show_side="left", show_kind="speech")
    hide eveina

    show erian normal at erian_right
    er "Обещаю." (show_side="right", show_kind="speech")
    hide erian

    n "Она ничего не ответила. Просто стояла перед ним — в этом странном союзе, полном недосказанностей и взаимного риска." (show_side="none", show_kind="speech")
    n "С ощущением, что обрела самого сильного и самого ненадежного союзника из всех возможных." (show_side="none", show_kind="speech")
    n "Внезапно Эриан ухмыльнулся, преврав поток беспокойных мыслей в голове девушки, и тихо произнёс:" (show_side="none", show_kind="speech")

    show erian intrigued at erian_right
    er "Я только сейчас понял." (show_side="right", show_kind="speech")
    hide erian
    show erian normal at erian_right
    er "Ты выяснила, что я представитель враждебной расы, но вместо того, чтобы пойти и рассказать об этом Вирту или кому-то ещё — ты прискакала ночью в сад, где нас никто не увидит, чтобы выяснить со мной отношения." (show_side="right", show_kind="speech")
    hide erian
    show erian smile at erian_right
    er "Эвейна, признайся честно, ты безумна?" (show_side="right", show_kind="speech")
    hide erian

    jump scene_5_2

