label scene_7_8:
    $ previous_scene = "scene_7_7"
    $ next_scene = "scene_7_9"
    $ current_scene = "scene_7_8"
    call fade_to_black(1.2, 0.8)
    scene bg shuttle_3 at bg_fullscreen with dissolve

    n "Утро третьего дня полета выдалось холодным. И шаттл слегка покачивался, будто специально, чтобы сделать их пространство ещё теснее." (show_side="none", show_kind="speech")
    n "Эвейна сидела на краю капсулы, наматывая волосы в небрежный узел. Вирт по обыкновению сидел за столом." (show_side="none", show_kind="speech")
    n "Пальцы скользили по экрану. Он выглядел сосредоточенным до невозможности. Впрочем, когда было иначе?" (show_side="none", show_kind="speech")
    n "Она поймала себя на мысли, что так и не застала его спящим. Декан ложился позже неё и вставал значительно раньше." (show_side="none", show_kind="speech")
    n "Ей было скучно. И девушка не нашла лучше развлечения, чем поддразнить профессора в очередной раз." (show_side="none", show_kind="speech")

    show eveina normal at eveina_left
    ev "Я пойду в душ." (show_side="left", show_kind="speech")
    ev "И вам лучше не смотреть, когда я выйду." (show_side="left", show_kind="speech")
    hide eveina
    show eveina intrigued at eveina_left
    ev "А то потом скажете, что я сбила вас с морального с курса, профессор." (show_side="left", show_kind="speech")
    hide eveina

    n "Аурелиан не ответил. Просто поднял на неё слишком спокойный взгляд своих голубых глаз. А затем встал и вышел из купе, оставив планшет на столе." (show_side="none", show_kind="speech")

    show eveina eyeroll at eveina_left
    ev_thought "Я ж просто пошутила, чего так смотреть..." (show_side="left", show_kind="thought")
    hide eveina

    n "Горячий душ принёс долгожданное тепло. Эвейна выходила из ванной, когда капли воды ещё стекали по спине." (show_side="none", show_kind="speech")
    n "Комбинезон, который она планировала надеть, был уже на ней, но молния… заклинила прямо у поясницы. И никак не хотела двигаться выше." (show_side="none", show_kind="speech")
    n "Девушка сделала несколько акробатических движений в попытке застегнуть её." (show_side="none", show_kind="speech")
    n "А пока возилась с ней, краем глаза заметила горящий экран. Девушка застыла на мгновение, пальцы отпустили молнию. Один шаг — и планшет у неё в руках." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev_thought "Просто посмотрю." (show_side="left", show_kind="thought")
    ev_thought "Если он как-то связан с Далоном… Я не могу позволить себе упустить этот шанс." (show_side="left", show_kind="thought")
    hide eveina

    n "Она открыла меню, и замерла в нерешительности. Вирт скоро вернётся, а с чего начать — совершенно неясно." (show_side="none", show_kind="speech")
    n "Быстрым движением Эвейна активировала ИИ в браслете." (show_side="none", show_kind="speech")

    show eveina normal at eveina_left
    ev "Сайф. Помоги. У меня в руках планшет Вирта. С чего начать поиски?" (show_side="left", show_kind="speech")
    hide eveina

    show sf at ai_right
    sf "Ты сейчас всерьёз?" (show_side="right", show_kind="speech")
    sf "Xочешь, чтобы нас с тобой вместе отчислили с формулировкой «за идиотизм»?" (show_side="right", show_kind="speech")
    hide sf

    show eveina normal at eveina_left
    ev "Сайф, ну пожалуйста… Сделай это. Если ты не поможешь, мне придётся искать вслепую." (show_side="left", show_kind="speech")
    hide eveina

    show sf at ai_right
    sf "Ты потеряла голову. Это уже даже не вседозволенность. Это отчаянная глупость." (show_side="right", show_kind="speech")
    hide sf

    show eveina annoyed at eveina_left
    ev "У всех какой-то пунктик о том, чтобы упрекать меня во вседозволенности?" (show_side="left", show_kind="speech")
    hide eveina

    show sf at ai_right
    sf "Я здесь не для того, чтобы гладить тебя по голове. Ответ — нет." (show_side="right", show_kind="speech")
    sf "И будь уверена, это ещё самый мягкий способ сказать тебе, что ты лезешь в пекло с голыми руками." (show_side="right", show_kind="speech")
    hide sf

    n "Сайф отключился. Эвейна выругалась и, положив планшет на край стола, снова потянулась к молнии на пояснице." (show_side="none", show_kind="speech")
    n "Именно в этот момент открылась дверь. На долю секунды Вирт замер в дверях, будто оценивая, не шутка ли это." (show_side="none", show_kind="speech")
    n "Взгляд скользнул на стоящую вполоборота у стола Эвейну: её руки на молнии, расстёгнутая ткань едва прикрывает низ спины." (show_side="none", show_kind="speech")
    n "Он не сказал ни слова. Девушка подняла на него умолящие глаза." (show_side="none", show_kind="speech")

    show eveina sad at eveina_left
    ev "Не справилась с молнией." (show_side="left", show_kind="speech")
    hide eveina

    n "Он осторожно подошёл к ней и встал за спиной. Медленно убрал с её спины влажные волосы — движение мягкое, почти бережное, будто она могла рассыпаться от одного неловкого касания." (show_side="none", show_kind="speech")
    n "Теплые пальцы легли по краям молнии, едва касаясь обнаженной кожи на пояснице. Её спина дрогнула — но она не отстранилась." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev_thought "Спокойно. Сейчас он думает о том, как справиться с молнией. А не о том, как ты дрожишь от его прикосновений." (show_side="left", show_kind="thought")
    hide eveina

    n "Вирт медленно застёгивал молнию, как хирург, который боялся порезать что-то важное." (show_side="none", show_kind="speech")
    n "Пальцы скользили по обнажённой спине — от пояса вверх, нежно касаясь каждого позвонка." (show_side="none", show_kind="speech")
    n "Когда молния достигла верха — он не убрал руку, лишь замер. Эвейна медленно обернулась." (show_side="none", show_kind="speech")
    n "Но он не смотрел на неё, он смотрел на включенный планшет, что лежал на столе. Сдвинутый." (show_side="none", show_kind="speech")
    n "Аурелиан напрягся мгновенно. Резко отстранился, будто её кожа внезапно обожгла его." (show_side="none", show_kind="speech")
    n "Взял планшет. Осмотрел его. Потом отключил экран и опустил планшет обратно." (show_side="none", show_kind="speech")
    n "Пауза повисла между ними, натянутая до предела. Он так и не взглянул на неё." (show_side="none", show_kind="speech")

    show virt serious jacket at virt_right
    vi "Надень что-нибудь тёплое. Здесь прохладно." (show_side="right", show_kind="speech")
    hide virt

    n "И вышел. Она медленно подошла к своему креслу, села." (show_side="none", show_kind="speech")
    n "Комбинезон был застёгнут, но ей казалось, что спина всё ещё горит. Места прикосновения его пальцев — не просто ощущались, а обжигали." (show_side="none", show_kind="speech")
    n "Она оглядела комнату — будто впервые. Планшет на столе. Чашка недопитого чая. Её полотенце, оставленное на его кресле. Всё на месте. Кроме него." (show_side="none", show_kind="speech")

    show eveina upset at eveina_left
    ev_thought "Ты перегнула. Господи, ты понимала, что перегибаешь." (show_side="left", show_kind="thought")
    ev_thought "Но теперь… он тоже понимает. Чёрт..." (show_side="left", show_kind="thought")
    hide eveina

    n "Она обхватила колени руками и уткнулась в них лбом. Губы дрожали — от чего? От стыда? От злости? От всепоглощающего чувства вины?" (show_side="none", show_kind="speech")
    n "Она не смогла бы ответить на этот вопрос, но никогда ещё не чувствовала себя такой грязной, как сейчас." (show_side="none", show_kind="speech")

    jump scene_7_9
