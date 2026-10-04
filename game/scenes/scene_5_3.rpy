label scene_5_3:
    $ previous_scene = "scene_5_2"
    $ next_scene = "scene_5_4"
    $ current_scene = "scene_5_3"
    call fade_to_black(1.2, 0.8)
    scene bg archive at bg_fullscreen with dissolve

    n "За дальним столом, спрятавшись в тени живой стены, Эвейна сосредоточенно стучала по сенсору терминала." (show_side="none", show_kind="speech")
    n "Экран раз за разом отказывался распознать её зашифрованный файл, несмотря на все уловки." (show_side="none", show_kind="speech")
    n "Она изменила кодировку, приписала файл к учебной библиотеке, выдала его за материалы для курса биогенной памяти…" (show_side="none", show_kind="speech")
    n "И всё равно — отказ." (show_side="none", show_kind="speech")

    show eveina normal at eveina_left
    ev_thought "Ну давай же. Притворись обычным учебным файлом. Притворяйся — как и половина Академии." (show_side="left", show_kind="thought")
    hide eveina

    show erian normal at erian_right
    er "Прекрасная техника. Особенно момент, где ты подменила классификационный код." (show_side="right", show_kind="speech")
    hide erian
    show erian intrigued at erian_right
    er "Восхищён твоей преступной карьерой, Эвейна." (show_side="right", show_kind="speech")
    hide erian

    n "Эвейна вздрогнула, быстро обернулась — Эриан стоял, скрестив руки и не утруждая себя вежливостью." (show_side="none", show_kind="speech")

    show erian normal at erian_right
    er "..." (show_side="right", show_kind="speech")
    hide erian

    show eveina annoyed at eveina_left
    ev "Если ты пришёл снова понаблюдать, как я мучаюсь — проходи мимо." (show_side="left", show_kind="speech")
    hide eveina

    show erian normal at erian_right
    er "Если бы хотел наблюдать за страданиями — остался бы в аудитории на лекции Кайстра." (show_side="right", show_kind="speech")
    hide erian
    show erian thinking at erian_right
    er "Это куда более изысканный садизм." (show_side="right", show_kind="speech")
    hide erian

    show eveina eyebrow at eveina_left
    ev "Может, вместо подглядывания попробуешь помочь?" (show_side="left", show_kind="speech")
    hide eveina

    show erian eyebrow at erian_right
    er "А я думал, ты предпочитаешь самостоятельность…" (show_side="right", show_kind="speech")
    hide erian
    show erian intrigued at erian_right
    er "Но если хочешь, я с радостью спасу тебя от очередного приступа беспомощности." (show_side="right", show_kind="speech")
    hide erian

    n "Он подошёл ближе, не спрашивая, обхватил за ребра, поднял и поставил рядом с креслом, на которое опустился сам." (show_side="none", show_kind="speech")
    n "Игнорируя возмущенный взгляд, склонился над экраном. От него пахло лесом, свежестью и чем-то, что невозможно было определить." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev_thought "Почему у меня каждый раз от его приближения будто кожа становится тоньше?" (show_side="left", show_kind="thought")
    ev_thought "Это так Илейн влияют на людей?" (show_side="left", show_kind="thought")
    hide eveina

    n "На долгие минуты между ними повисла тишина. Эриан пробовал разные обходы, пальцы плясали над экраном." (show_side="none", show_kind="speech")
    n "Он раздраженно шептал что-то на непонятном языке интерфейсов, но файл оставался глух." (show_side="none", show_kind="speech")

    show eveina eyebrow at eveina_left
    ev "Зачем ты вообще ходишь на лекции, Эриан? Ты же не учишься на самом деле." (show_side="left", show_kind="speech")
    hide eveina

    n "Не отрывая взгляда от терминала, парень ответил." (show_side="none", show_kind="speech")

    show erian normal at erian_right
    er "В основном, наблюдаю. Ищу точки пересечения, невидимо связывающие людей." (show_side="right", show_kind="speech")
    hide erian
    show erian thinking at erian_right
    er "Информацию, которая поможет мне подобраться ещё на шаг ближе к Далону." (show_side="right", show_kind="speech")
    hide erian
    show erian intrigued at erian_right
    er "А иногда просто любопытно послушать, что вы о нас напридумывали." (show_side="right", show_kind="speech")
    hide erian

    n "Наконец, сдавшись, он откинулся на спинку стула." (show_side="none", show_kind="speech")

    show erian normal at erian_right
    er "Либо это самый капризный файл в истории, либо ты ему просто не нравишься." (show_side="right", show_kind="speech")
    hide erian

    show eveina intrigued at eveina_left
    ev "Думаешь, я его обижала?" (show_side="left", show_kind="speech")
    hide eveina

    show erian intrigued at erian_right 
    er "Учитывая твою манеру общаться с людьми, боюсь подумать, чего от тебя натерпелся он." (show_side="right", show_kind="speech")
    hide erian

    show eveina normal at eveina_left
    ev_thought "Ну эй!" (show_side="left", show_kind="thought")
    hide eveina

    n "Забывшись, Эвейна раздраженно стукнула Эриана по плечу. Он медленно повернулся к ней и она тут сжалась под его тяжёлым взглядом." (show_side="none", show_kind="speech")

    show eveina normal at eveina_left
    ev_thought "Ой, это я зря…" (show_side="left", show_kind="thought")
    hide eveina

    n "Ухмыльнувшись произведённым эффектом, Эриан встал и потянулся как сытый кот." (show_side="none", show_kind="speech")

    show erian normal at erian_right
    er "Пойдём прогуляемся. Здесь пахнет разочарованием." (show_side="right", show_kind="speech")
    er "И мне скучно." (show_side="right", show_kind="speech")
    er "В саду хотя бы несёт только вашей высокомерной флорой с теплиц." (show_side="right", show_kind="speech")
    hide erian

    show eveina eyebrow at eveina_left
    ev "Высокомерной флорой?" (show_side="left", show_kind="speech")
    hide eveina

    show erian thinking at erian_right
    er "Они отказываются мне отвечать." (show_side="right", show_kind="speech")
    hide erian

    show eveina thinking at eveina_left
    ev_thought "О, ты ещё и с растениями общаешься?" (show_side="left", show_kind="thought")
    hide eveina

    n "Эвейна смотрела вслед уходящему Эриану и размышляла, стоит ли ей следовать за ним." (show_side="none", show_kind="speech")
    n "Даже сейчас он казался ей не самым надежным напарником, не говоря уже о прогулках с ним по витееватым тропинкам сада вдали от чужих глаз." (show_side="none", show_kind="speech")
    n "Но любопытство в очередной раз определило её дальнейшие шаги. Здравый смысл в её поступках вообще редко брал вверх над остальными эмоциями." (show_side="none", show_kind="speech")
    n "Девушка выскочила из кресла и быстрым шагом направилась к выходу." (show_side="none", show_kind="speech")

    scene bg garden at bg_fullscreen with fade

    n "В саду было безлюдно, как всегда в это время. Они неспешно добрели до уже знакомого дерева." (show_side="none", show_kind="speech")
    n "Эриан устроился под ним, вытянув ноги. Эвейна осторожно села рядом." (show_side="none", show_kind="speech")

    show eveina normal at eveina_left
    ev "Скажи мне… почему я тебя всегда помню?" (show_side="left", show_kind="speech")
    hide eveina

    n "Эриан не торопился с ответом, лениво скользя взглядом по листьям." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev_thought "Только не молчи..." (show_side="left", show_kind="thought")
    ev_thought "Я и так уже выстроила столько стен, что хватит на ядерный бункер." (show_side="left", show_kind="thought")
    hide eveina

    n "Словно прочитав её мысли, парень, наконец, перевёл на неё взгляд и холодно улыбнулся." (show_side="none", show_kind="speech")

    show erian intrigued at erian_right
    er "Кто сказал, что ты помнишь {i}всегда{/i}?" (show_side="right", show_kind="speech")
    er "Я просто… позволяю это. Иногда." (show_side="right", show_kind="speech")
    hide erian

    n "От его взгляда сердце пропустило удар." (show_side="none", show_kind="speech")

    show eveina normal at eveina_left
    ev "Ты стирал мне память?" (show_side="left", show_kind="speech")
    hide eveina

    show erian normal at erian_right
    er "Наверно, ты уже слышала о том, что стирать человеческую память естественно для... для Илейн." (show_side="right", show_kind="speech")
    er "Чтобы этого не происходило, приходится прилагать некоторые усилия." (show_side="right", show_kind="speech")
    er "Впрочем, удерживать твою память проще, чем чужую." (show_side="right", show_kind="speech")
    hide erian  
    show erian intrigued at erian_right
    er "Но даже ты — не исключение. Хочешь, и твою сотру? До основания." (show_side="right", show_kind="speech")
    hide erian

    n "Были ли эти слова угрозой? Предупреждением? Или просто демонстрацией силы? Эвейна судорожно сглотнула, понимая, что единственное, чего в этих словах не было — так это намёка на шутку." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev_thought "Серьезно, Эриан?" (show_side="left", show_kind="thought")
    ev_thought "Сначала предлагаешь помощь, а потом пытаешься запугать?" (show_side="left", show_kind="thought")
    hide eveina

    show eveina annoyed at eveina_left
    ev "То есть, я для тебя игрушка?" (show_side="left", show_kind="speech")
    hide eveina

    show erian intrigued at erian_right
    er "Скорее, инструмент. Хотя польза от тебя пока стремится к нулю." (show_side="right", show_kind="speech")
    hide erian

    n "В его улыбке не было теплоты. Эвейне нахмурилась и отвернулась, пряча от него своё лицо." (show_side="none", show_kind="speech")

    show eveina sad at eveina_left
    ev_thought "Наивно было полагать, что прошлый наш разговор что-то изменит." (show_side="left", show_kind="thought")
    ev_thought "Эриан в принципе не страдает доверием к человеческому роду, так с чего бы вдруг стал доверять мне?" (show_side="left", show_kind="thought")
    hide eveina
    show eveina thinking at eveina_left
    ev_thought "Он специально меня пугает?" (show_side="left", show_kind="thought")
    ev_thought "Специально отталкивает?" (show_side="left", show_kind="thought")
    hide eveina

    n "Эриан будто и не заметил перемен в её настроении. Почти ласково погладив кору дерева между ними, он продолжил:" (show_side="none", show_kind="speech")

    show erian eyebrow at erian_right
    er "Лучше бы ты спросила, каково это — контролировать себя, когда рядом не только ты." (show_side="right", show_kind="speech")
    er "Когда нужно удерживать память в тебе, но вычищать из остальных." (show_side="right", show_kind="speech")
    er "Когда приходится регулировать каждое внимание, каждый взгляд." (show_side="right", show_kind="speech")
    hide erian

    show eveina annoyed at eveina_left
    ev_thought "Примерно так же сложно, как терпеть тебя?" (show_side="left", show_kind="thought")
    hide eveina

    n "Она вздохнула и снова повернулась к нему. В конце концов, ей нужны были ответы." (show_side="none", show_kind="speech")

    show eveina normal at eveina_left
    ev "Хорошо." (show_side="left", show_kind="speech")
    hide eveina
    show eveina eyebrow at eveina_left
    ev "И каково это?" (show_side="left", show_kind="speech")
    hide eveina

    show erian normal at erian_right 
    er "Это как жонглировать мечами." (show_side="right", show_kind="speech")
    er "Пока ты сосредоточен — всё летит. Но стоит только зазеваться — тебя же и порежет." (show_side="right", show_kind="speech")
    hide erian

    n "Эвейна медленно кивнула, принимая такой ответ." (show_side="none", show_kind="speech")

    show eveina eyebrow at eveina_left
    ev "Тогда как получилось, что Каэль не заметил нас там в коридоре?" (show_side="left", show_kind="speech")
    hide eveina
    show eveina normal at eveina_left
    ev "Это не было похоже на стирание памяти." (show_side="left", show_kind="speech")
    hide eveina

    show erian normal at erian_right
    er "Я могу делать так, чтобы человек не только не запоминал — но и не замечал." (show_side="right", show_kind="speech")
    er "Перенаправлять концентрацию на что-то иное." (show_side="right", show_kind="speech")
    er "Работает, пока я незаметен. Пока никто не смотрит слишком пристально." (show_side="right", show_kind="speech")
    hide erian
    show erian thinking at erian_right
    er "Но тогда было сложно. Каэль — почти как замок без ключа." (show_side="right", show_kind="speech")
    er "Чтобы остаться незаметным для него, приходится тратить вдвое больше сил." (show_side="right", show_kind="speech")
    hide erian
    show erian annoyed at erian_right
    er "И даже тогда... не всегда срабатывает. В нём есть что-то, что блокирует мои способности." (show_side="right", show_kind="speech")
    hide erian

    show eveina thinking at eveina_left
    ev "Это звучит очень в стиле Каэля." (show_side="left", show_kind="speech")
    hide eveina

    n "Он не ответил, продолжая задумчиво смотреть куда-то вдаль, будто и не слышал её." (show_side="none", show_kind="speech")
    n "На некоторое время между ними повисло молчание, пока Эвейна размышляла, что ещё она может спросить, не вызвав в нём новую вспышку гнева." (show_side="none", show_kind="speech")
    n "Наконец, Эриан откинулся на дерево, прикрыл глаза и лениво произнес." (show_side="none", show_kind="speech")

    show erian thinking at erian_right
    er "Я буквально слышу, как новый вопрос пытается выбраться из твоей черепной коробки." (show_side="right", show_kind="speech")
    hide erian

    show eveina annoyed at eveina_left
    ev "А ты что, каждый день встречаешь представителей других рас?" (show_side="left", show_kind="speech")
    hide eveina

    n "Он удивленно посмотрел на неё, на здание Академии вдалеке, и снова на неё. Потом сузил глаза." (show_side="none", show_kind="speech")

    show erian eyebrow at erian_right
    er "Ты это сейчас серьёзно спрашиваешь?" (show_side="right", show_kind="speech")
    hide erian

    n "Осознав нелепость вопроса, девушка тихо хихикнула. Эриан недовольно вздохнул и вернулся в прежнюю позу." (show_side="none", show_kind="speech")

    show erian normal at erian_right
    er "Следующий вопрос." (show_side="right", show_kind="speech")
    hide erian

    show eveina annoyed at eveina_left
    ev "Почему ты меня укусил тогда в архиве? Это было очень...невежливо." (show_side="left", show_kind="speech")
    hide eveina

    show erian thinking at erian_right
    er "Я ж сказал, хотел кое-что проверить." (show_side="right", show_kind="speech")
    hide erian

    show eveina annoyed at eveina_left
    ev "Что именно?" (show_side="left", show_kind="speech")
    hide eveina

    show erian thinking at erian_right
    er "Твою реакцию." (show_side="right", show_kind="speech")
    hide erian

    show eveina annoyed at eveina_left
    ev "Ну просто великолепное оправдание." (show_side="left", show_kind="speech")
    hide eveina

    show erian intrigued at erian_right
    er "Я и не пытался оправдываться." (show_side="right", show_kind="speech")
    hide erian

    show eveina eyeroll at eveina_left
    ev "Ладно, и что это тебе дало?" (show_side="left", show_kind="speech")
    hide eveina

    show erian intrigued at erian_right
    er "Многое." (show_side="right", show_kind="speech")
    hide erian

    show eveina angry at eveina_left
    ev "И рассказывать об этом ты мне не собираешься?" (show_side="left", show_kind="speech")
    hide eveina

    show erian smile at erian_right
    er "Всё верно." (show_side="right", show_kind="speech")
    hide erian

    show eveina thinking at eveina_left
    ev_thought "Есть ли человек, который раздражает меня больше, чем ты сейчас?" (show_side="left", show_kind="thought")
    hide eveina
    show eveina angry at eveina_left
    ev "Не делай так больше." (show_side="left", show_kind="speech")
    hide eveina

    show erian smile at erian_right
    er "Только если сама попросишь." (show_side="right", show_kind="speech")
    hide erian

    show eveina eyeroll at eveina_left
    ev "Пфф... не надейся." (show_side="left", show_kind="speech")
    hide eveina
    show eveina normal at eveina_left
    ev "А почему ты не стёр память мне?" (show_side="left", show_kind="speech")
    hide eveina

    show erian thinking at erian_right
    er "Я ждал тебя." (show_side="right", show_kind="speech")
    hide erian

    show eveina eyebrow at eveina_left
    ev "Ждал?" (show_side="left", show_kind="speech")
    hide eveina

    show erian thinking at erian_right
    er "Ещё до твоего прибытия я просматривал документы Академии." (show_side="right", show_kind="speech")
    hide erian
    show erian normal at erian_right
    er "И наткнулся на запись о твоём зачислении по рекомендации." (show_side="right", show_kind="speech")
    hide erian

    show eveina normal at eveina_left
    ev "О, эти таинственные рекомендации. Все о них слышали, но никто не знает, чьи они." (show_side="left", show_kind="speech")
    hide eveina

    n "Долгий тяжелый взгляд был явным признаком того, что Эвейна снова сказала что-то не то." (show_side="none", show_kind="speech")

    show erian eyebrow at erian_right
    er "Ты правда не знаешь?" (show_side="right", show_kind="speech")
    hide erian

    show eveina normal at eveina_left
    ev "Если бы знала, передала бы рекомендателю корзинку с пирожками, украденную из столовой." (show_side="left", show_kind="speech")
    hide eveina

    show erian normal at erian_right
    er "Рекомендацию к зачислению тебе дал человек по имени Кайр Далон." (show_side="right", show_kind="speech")
    hide erian

    n "Сердце стукнуло слишком громко где-то в глотке, а потом замерло в ожидании. Эвейна резко выпрямилась и уставилась на него, широко распахнув глаза. Но Эриан уже изучал её реакцию." (show_side="none", show_kind="speech")

    show eveina wondered at eveina_left
    ev_thought "Да ты шутишь..." (show_side="left", show_kind="thought")
    hide eveina

    show erian eyebrow at erian_right
    er "Вот почему я подошёл к тебе." (show_side="right", show_kind="speech")
    er "Почему остался рядом." (show_side="right", show_kind="speech")
    hide erian
    show erian normal at erian_right
    er "Ты связана с ним. А значит — ты ключ к его местонахождению." (show_side="right", show_kind="speech")
    hide erian

    show eveina wondered at eveina_left
    ev "Я… не понимаю." (show_side="left", show_kind="speech")
    ev "Какое он имеет ко мне отношение?" (show_side="left", show_kind="speech")
    hide eveina   
    show eveina annoyed at eveina_left
    ev "Но теперь мне точно нужно это выяснить." (show_side="left", show_kind="speech")
    hide eveina

    n "Она переваривала новую информацию. Он наклонился ближе, дыша ей почти в висок." (show_side="none", show_kind="speech")

    show erian normal at erian_right
    er "Я буду рядом, когда это случится. Хочу это увидеть." (show_side="right", show_kind="speech")
    hide erian
    show erian intrigued at erian_right
    er "Люблю эту твою решительность." (show_side="right", show_kind="speech")
    er "Особенно в моменты, когда ты не понимаешь, в какое пекло лезешь." (show_side="right", show_kind="speech")
    hide erian

    n "Он смотрел на неё — долго, пристально. Словно ждал, дрогнет ли. Но вместо этого…" (show_side="none", show_kind="speech")
    n "Поддавшись внезапному импульсу Эвейна опустила глаза, протянула руку и мягко коснулась его пальцев своими." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev_thought "Ты ведь нарочно так говоришь? Пугаешь, отталкиваешь, ведёшь себя грубо?" (show_side="left", show_kind="thought")
    ev_thought "Думаешь, я тоже могу предать, как когда это сделал Далон?" (show_side="left", show_kind="thought")
    hide eveina

    n "Эриан нахмурился, медленно перевёл взгляд на их руки. Его пальцы дрогнули и замерли в нерешительности." (show_side="none", show_kind="speech")
    n "А потом переплелись с её." (show_side="none", show_kind="speech")
    n "Он снова откинулся на ствол дерева и закрыл глаза." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev_thought "Теперь всё будет иначе." (show_side="left", show_kind="thought") 
    ev_thought "Я не боюсь тебя, Эриан. Больше не боюсь." (show_side="left", show_kind="thought")
    hide eveina
    show eveina normal at eveina_left
    ev_thought "Зато теперь знаю, чего боишься ты." (show_side="left", show_kind="thought")
    ev_thought "И если ты думаешь, что я могу предать тебя..." (show_side="left", show_kind="thought")
    hide eveina
    show eveina thinking at eveina_left
    ev_thought "... то ты, без сомнений, прав." (show_side="left", show_kind="thought")
    hide eveina
    show eveina normal at eveina_left
    ev_thought "Поэтому, пожалуйста, не вставай между мной и спасением моего отца." (show_side="left", show_kind="thought")
    hide eveina

    jump scene_5_4
