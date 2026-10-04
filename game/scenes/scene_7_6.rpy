label scene_7_6:
    $ previous_scene = "scene_7_5"
    $ next_scene = "scene_7_7"
    $ current_scene = "scene_7_6"
    call fade_to_black(1.2, 0.8)
    scene bg eveina_room at bg_fullscreen with dissolve
    
    n "Утро началось с вежливого, но от этого не менее раздражающего стука в дверь. Эвейна, открыв один глаз, недовольно окинула взглядом комнату и с облегчением заметила, что Лея уже встала." (show_side="none", show_kind="speech")

    show eveina eyeroll tshirt at eveina_left
    ev "Лея, это точно к тебе..." (show_side="left", show_kind="speech") 
    hide eveina

    show leya normal at leya_right
    le "Сомневаюсь, но ход твоих мыслей я поняла." (show_side="right", show_kind="speech")
    hide leya

    n "Торопливо приводя волосы в порядок, Лея добралась до двери, открыла её... И тут же закрыла." (show_side="none", show_kind="speech")

    show leya angry at leya_right
    le "Эвейна, что ты опять натворила?" (show_side="right", show_kind="speech")
    hide leya

    show eveina eyebrow tshirt at eveina_left
    ev "Что? Ничего я..." (show_side="left", show_kind="speech") 
    hide eveina

    show leya eyebrow at leya_right
    le "Там Вирт!" (show_side="right", show_kind="speech")
    hide leya

    show eveina wondered tshirt at eveina_left
    ev "Кто?.. А ему что здесь... Чёрт! Шаттл!" (show_side="left", show_kind="speech") 
    hide eveina

    n "Словно ужаленная, Эвейна подскочила с постели, и тут же осела обратно из-за головокружения." (show_side="none", show_kind="speech")

    show eveina angry tshirt at eveina_left
    ev_thought "Как не вовремя..." (show_side="left", show_kind="thought") 
    hide eveina

    n "Но уже через несколько секунд она начала быстро одеваться, раскидывая неподходящие вещи по комнате." (show_side="none", show_kind="speech")

    show leya angry at leya_right
    le "Тебе твоими расследованиями совсем память отбило?!" (show_side="right", show_kind="speech")
    hide leya

    show eveina annoyed tshirt at eveina_left
    ev "А ты что, только что захлопнула дверь перед деканом?" (show_side="left", show_kind="speech") 
    hide eveina

    show leya eyebrow at leya_right
    le "Ну... он как раз отвернулся, и я запаниковала... Скажу ему, что это была ты!" (show_side="right", show_kind="speech")
    hide leya

    n "В дверь снова постучали, на этот раз чуть более настойчиво." (show_side="none", show_kind="speech")

    show eveina eyeroll tshirt at eveina_left
    ev "Да открой уже эту чёртову дверь." (show_side="left", show_kind="speech") 
    hide eveina

    n "Лея придирчивым взглядом оглядела соседку, застегивающую на себе брюки и только потом снова открыла дверь." (show_side="none", show_kind="speech")

    show leya smile at leya_right
    le "Доброе утро, профессор!" (show_side="right", show_kind="speech")
    hide leya

    show virt normal at virt_right
    vi "Доброе утро, мисс Таласа. Я не помешал?" (show_side="right", show_kind="speech")
    hide virt

    show leya normal at leya_right
    le "Нет, что вы...Извините, мы просто не ожидали..." (show_side="right", show_kind="speech")
    hide leya

    show eveina thinking at eveina_left
    ev_thought "Сколько терпения у этого человека?" (show_side="left", show_kind="thought") 
    hide eveina

    n "Вирт учтиво кивнул и перевёл взгляд на Эвейну, которая в спешке закидывала случайные вещи в сумку. Глаза внимательно изучали её, будто всё ещё проверяли: стоит ли пускать её за пределы Академии." (show_side="none", show_kind="speech")

    show virt intrigued at virt_right
    vi "Полагаю, спешные сборы не позволили вам ответить на мои сообщения?" (show_side="right", show_kind="speech")
    hide virt

    show eveina eyebrow at eveina_left
    ev_thought "Ого, ирония!" (show_side="left", show_kind="thought") 
    hide eveina
    show eveina normal at eveina_left
    ev "Да, да, я почти готова!" (show_side="left", show_kind="speech") 
    hide eveina

    show virt normal at virt_right
    vi "Можете не торопиться. У вас ещё есть полчаса." (show_side="right", show_kind="speech")
    hide virt
    show virt thinking at virt_right
    vi "Только сперва отметьте свои прогулы в расписании, чтобы не получить ещё одно дисциплинарное в своё отсутствие." (show_side="right", show_kind="speech")
    hide virt

    show eveina normal at eveina_left
    ev "Что? А, да, конечно." (show_side="left", show_kind="speech") 
    hide eveina

    show virt normal at virt_right
    vi "И сходите на завтрак. Буду ждать вас у шаттла." (show_side="right", show_kind="speech")
    hide virt

    n "Он в последний раз обвёл взглядом комнату, которую Эвейна минуту назад превратила в обитель хаоса, развернулся и вышел." (show_side="none", show_kind="speech")

    show leya normal at leya_right
    le "Кошмар, теперь он будет думать, что у нас тут всегда вот так..." (show_side="right", show_kind="speech")
    hide leya

    n "Лея забегала по комнате, поднимая брошенные вещи." (show_side="none", show_kind="speech")

    show eveina normal at eveina_left
    ev "Во-первых, не всегда, а в особых случаях." (show_side="left", show_kind="speech") 
    hide eveina
    show eveina eyeroll at eveina_left
    ev "А во-вторых — не всё ли равно?" (show_side="left", show_kind="speech") 
    hide eveina

    scene bg dining_room at bg_fullscreen with dissolve

    n "В столовую Лея отправилась раньше и к приходу соседки уже собрала для неё завтрак. Но Эвейна едва прикоснулась к еде. Аппетит был где-то на другом конце вселенной." (show_side="none", show_kind="speech")
    n "В последний момент она вспомнила: никого не предупредила. Села в уголке, записала короткое видео отцу — почти нейтральное, даже без нервной дрожи в голосе." (show_side="none", show_kind="speech")
    n "А после сразу написала сиделке, что скоро будет. В ответ пришло: {i}«Ждём. Приятной дороги.»{/i}" (show_side="none", show_kind="speech")
    n "И только тогда вернулась к еде. Но попробовать не успела — пришло сообщение от Вирта: {i}«Жду на посадочной станции.»{/i}" (show_side="none", show_kind="speech")

    n "Эвейна бросила короткое «обещай, что не умрёшь» Лее, схватила сумку и направилась к шлюзу." (show_side="none", show_kind="speech")

    scene bg shuttle_3 at bg_fullscreen with dissolve

    n "Их разместили в одном купе. Тихий отсек с двумя кресла-кроватями, столом между ними, уборной, прихожей и панелью вызова." (show_side="none", show_kind="speech")
    n "Шаттл гудел, вибрация шла по полу — размеренная, убаюкивающая." (show_side="none", show_kind="speech")
    n "Эвейна устроилась в кресле. Не успела даже пристегнуться, как глаза снова сами закрылись." (show_side="none", show_kind="speech")
    n "Последние мысли пронеслись в её проваливающемся в сон сознании, вызывая улыбку." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev_thought "Интересно, одно купе — это чтобы я не натворила чего по пути?" (show_side="left", show_kind="thought") 
    hide eveina

    n "Очнулась от лёгкого движения. Кто-то накрыл её пледом. Неспеша потянулась, открыла глаза — напротив, за столом, сидел Вирт." (show_side="none", show_kind="speech")
    n "Что-то в его внешности изменилось, и девушке потребовалась целая минута, чтобы понять что именно: на нём не было преподавательской мантии." (show_side="none", show_kind="speech")
    n "В остальном он не изменял себе — работал с документами в обычной манере, словно и не покидал своего кабинета. Его задумчивый взгляд скользнул по ней и через мгновение лицо смягчилось." (show_side="none", show_kind="speech")

    show virt normal jacket at virt_right
    vi "Наконец-то. Проснулись." (show_side="right", show_kind="speech")
    vi "Чаю?" (show_side="right", show_kind="speech")
    hide virt

    n "Она кивнула. Поднялась — и тут же стала оседать обратно. Темнота. Шум в ушах. Мир качнулся и пол ушёл из под ног. Падая, Эвейна с раздражением успела подумать:" (show_side="none", show_kind="speech")

    show eveina angry at eveina_left
    ev_thought "Чёрт. Да сколько это будет продолжаться?" (show_side="left", show_kind="thought")
    hide eveina

    n "Аурелиан подхватил её уверенным движением. Плавно, но с той силой, от которой у неё в животе всё сжалось. Его рука оказалась под её лопатками, вторая — обвила талию, прижимая к себе." (show_side="none", show_kind="speech")
    n "Лицо почти уткнулось в шею мужчины, а руки легли на равномерно вздымающуюся грудь. Эвейна почувствовала еле уловимый запах прохладной горечи чая, тёплого мускуса и чего-то древесного." (show_side="none", show_kind="speech")

    show virt normal jacket at virt_right
    vi "Ты в порядке? Голова?" (show_side="right", show_kind="speech")
    hide virt 

    n "Она кивнула и его пальцы дрогнули. Прежде чем отпустить — скользнули вдоль её спины, по линии позвоночника." (show_side="none", show_kind="speech")
    n "Медленно, будто он боялся, что как только отпустит, она упадет снова. На секунду Эвейне даже показалось, что он не хотел отпускать вовсе." (show_side="none", show_kind="speech")

    show eveina normal at eveina_left
    ev_thought "Как сказал бы Эриан: «Весьма самодовольная фантазия». Хотя..." (show_side="left", show_kind="thought")
    hide eveina
    show eveina thinking at eveina_left
    ev_thought "Если он каждый раз после головокружения будет обращаться ко мне на «ты» таким голосом…" (show_side="left", show_kind="thought")
    ev_thought "И ловить в такие объятия..." (show_side="left", show_kind="thought")
    hide eveina
    show eveina intrigued at eveina_left
    ev_thought "...я не против падать по расписанию." (show_side="left", show_kind="thought")
    hide eveina

    show virt normal jacket at virt_right
    vi "Точно всё хорошо?" (show_side="right", show_kind="speech")
    hide virt 

    show eveina normal at eveina_left
    ev "Уже лучше. Спасибо." (show_side="left", show_kind="speech")
    hide eveina

    n "Вирт отстранился, сел обратно в кресло, продолжая внимательно следить за каждым её движением." (show_side="none", show_kind="speech")

    show virt thinking jacket at virt_right
    vi "Не уверен, стоило ли лететь. Было слишком мало времени на восстановление." (show_side="right", show_kind="speech")
    hide virt 

    n "Эвейна бросила на него испуганный взгляд." (show_side="none", show_kind="speech")

    show eveina wondered at eveina_left
    ev_thought "Ох, только не это! Если он сейчас развернёт корабль и вернёт меня назад..." (show_side="left", show_kind="thought")
    hide eveina

    show virt thinking jacket at virt_right
    vi "Расслабьтесь. Я не собираюсь отменять поездку. Просто… беспокоюсь." (show_side="right", show_kind="speech")
    hide virt 

    show eveina normal at eveina_left
    ev "Мне правда уже лучше." (show_side="left", show_kind="speech")
    hide eveina

    n "Он снова кивнул и нажатием кнопки на панели заказал в купе обед. За обедом они вернулись к обсуждению эксперимента." (show_side="none", show_kind="speech")

    show virt normal jacket at virt_right
    vi "Ваше решение… и Каэля — уже вышло за пределы Академии. Благодаря эксперименту и шуму вокруг него, это вызвало интерес у некоторых ученых." (show_side="right", show_kind="speech")
    vi "Вас теперь знают. В узких кругах." (show_side="right", show_kind="speech")
    hide virt 

    show eveina upset at eveina_left
    ev "В смысле — знают, как девочку, сорвавшую демонстрацию?" (show_side="left", show_kind="speech")
    hide eveina

    show virt normal jacket at virt_right
    vi "Вы ничего не срывали, Эвейна. Провалы случаются у всех." (show_side="right", show_kind="speech")
    vi "Любому успеху предшествует сотня провалов. Просто большинство из них никто не видит." (show_side="right", show_kind="speech")
    hide virt

    show eveina thinking at eveina_left
    ev "Только вот мой наблюдала куча народу." (show_side="left", show_kind="speech")
    hide eveina

    n "Он криво усмехнулся, и в этой усмешке было скрытое сожаление. Так улыбаются те, кто знает, о чём она говорит." (show_side="none", show_kind="speech")

    show virt normal jacket at virt_right
    vi "Через это проходит каждый учёный. Спросите на досуге у Каэля, сколько раз его эксперименты с имплантами заканчивались неудачей." (show_side="right", show_kind="speech")
    hide virt

    n "Эвейна невольно замерла, вспоминая их разговоры на досуге, а затем поспешно отвела глаза и нацепила скучающий вид." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev "Каэль не похож на человека, готового говорить по душам со студентами." (show_side="left", show_kind="speech")
    hide eveina

    show virt thinking jacket at virt_right
    vi "Странно. Мне казалось, вы нашли общий язык." (show_side="right", show_kind="speech")
    hide virt

    show eveina thinking at eveina_left
    ev_thought "Ох, как двусмысленно и неловко..." (show_side="left", show_kind="thought")
    hide eveina

    n "В наступившей тишине взгляд Эвейны бегал по купе, ища подходящую тему, чтобы больше не говорить о Каэле." (show_side="none", show_kind="speech")

    show eveina normal at eveina_left
    ev "Простите, что я… до сих пор не вернула книгу. Из архива." (show_side="left", show_kind="speech")
    hide eveina

    n "Аурелиан некоторое время молчал, глядя на неё." (show_side="none", show_kind="speech")

    show virt serious jacket at virt_right
    vi "Зачем вы её взяли?" (show_side="right", show_kind="speech")
    hide virt 
    show virt thinking jacket at virt_right
    vi "Это же просто история колонизации." (show_side="right", show_kind="speech")
    hide virt 

    show eveina thinking at eveina_left
    ev "Мне... была интересна эта тема." (show_side="left", show_kind="speech")
    hide eveina

    show virt eyebrow jacket at virt_right
    vi "Это та книга навела вас на вопросы об этичности сотрудничества с Илейн?" (show_side="right", show_kind="speech")
    hide virt 

    show eveina eyeroll at eveina_left
    ev_thought "Блестяще, Эвейна. Мастерский выбор тем." (show_side="left", show_kind="thought") 
    ev_thought "Меняешь одно эмоциональное дерьмо на другое." (show_side="left", show_kind="thought")
    hide eveina

    n "Эвейна устало выходнула, отложила приборы и растянулась в капсуле, зевая." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev "Возможно. Уже и не вспомню." (show_side="left", show_kind="speech")
    hide eveina
    show eveina normal at eveina_left
    ev "Извините, профессор. Я ещё не восстановилась после эксперимента и очень устала. Давайте поговорим позже." (show_side="left", show_kind="speech")
    hide eveina
    show eveina annoyed at eveina_left
    ev_thought "Чёрт возьми, Эвейна, что ты несёшь? Он сейчас точно найдёт на этой посудине кнопку разворота на 180 градусов!" (show_side="left", show_kind="thought") 
    hide eveina

    n "Но Аурелиан молча отложил еду и более не настаивал на диалоге. Какое-то время девушка лениво глядела в потолок, нервно теребя плед пальцами и переживая из-за встречи с отцом." (show_side="none", show_kind="speech")
    n "Мысли метались от радости к отчаянию и обратно, набирая амплитуду и вновь затихая, пока не пришёл сон — быстро и без предупреждения." (show_side="none", show_kind="speech")

    call fade_to_black(1.2, 0.8)

    n "Но он не был добр." (show_side="none", show_kind="speech")
    n "Ей снилось, как она выходит с трапа. И уже у ворот слышит, как кто-то говорит:" (show_side="none", show_kind="speech")
    unknown "Он умер." (show_side="right", show_kind="speech")
    n "Её мир разрушился. Слёзы. Паника. Боль." (show_side="none", show_kind="speech")

    show eveina sad at eveina_left
    ev "Я обещала тебя спасти." (show_side="left", show_kind="speech")
    ev "Я должна была…" (show_side="left", show_kind="speech")
    ev "И не смогла." (show_side="left", show_kind="speech")
    hide eveina

    scene bg shuttle_3 at bg_fullscreen with dissolve

    n "Из-за резкого пробуждения, Эвейна не сразу поняла, где находится." (show_side="none", show_kind="speech")
    n "Лишь спустя мгновение осознала, что её укутали теплые надежные объятия." (show_side="none", show_kind="speech")
    n "Вирт сидел на краю кресла и крепко прижимал девушку к своей груди, пальцами зарывшись в её волосы." (show_side="none", show_kind="speech")

    show virt normal jacket at virt_right
    vi "Это был сон, Эвейна. Только сон. Всё в порядке, ты в безопасности." (show_side="right", show_kind="speech")
    hide virt

    n "Она не отвечала, только прерывисто, сбивчиво дышала, пока он продолжал держать её в объятиях. Щекой Эвейна ощущала ровные удары его сердца о грудную клетку, и этот ритм успокаивал." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev_thought "Наверно, мне должно быть неловко. Но пусть это продлится ещё чуть-чуть." (show_side="left", show_kind="thought")
    hide eveina

    n "Эвейна уткнулась в его грудь и тихо всхлипнула. Они так и сидели без единого движения. Словно замерли в моменте, который не требовал объяснений." (show_side="none", show_kind="speech")
    n "Потом он осторожно вздохнул, зная, что следующее движение всё изменит. И только тогда медленно, с усилием отстранился." (show_side="none", show_kind="speech")
    n "Слишком мягко, но это всё равно ощущалось как потеря. Не до конца осознавая свои действия, девушка подняла на него глаза и попыталась удержать его, потянув пальцами за рукав." (show_side="none", show_kind="speech")
    n "Вирт в ответ мягко покачал головой, почти с сожалением." (show_side="none", show_kind="speech")

    show virt normal jacket at virt_right
    vi "Я — твой преподаватель, Эвейна. Более того... я преподаю этику." (show_side="right", show_kind="speech")
    vi "И уже перешёл все возможные грани допустимого." (show_side="right", show_kind="speech")
    vi "Мне стоит хотя бы иногда соблюдать приличия." (show_side="right", show_kind="speech")
    hide virt

    show eveina eyeroll at eveina_left
    ev_thought "Знали бы вы профессор, что я сейчас думаю о ваших приличиях..." (show_side="left", show_kind="thought")
    ev_thought "Может, ещё лекцию прочтёте — как не чувствовать то, что я чувствую, когда декан гладит тебя по волосам?" (show_side="left", show_kind="thought")
    hide eveina

    n "Эвейна опустила глаза и медленно разжала пальцы. Он встал. Она поднялась следом за ним — медленно, ещё не до конца проснувшись, не до конца отпустив объятие, в котором только что пряталась от всего мира." (show_side="none", show_kind="speech")
    n "Их тела почти соприкоснулись. Пространства между ними было меньше, чем нужно, чтобы дышать спокойно. Запах его рубашки — тот самый, с оттенком чая, мускуса и выветрившегося дерева — будто остался на её коже." (show_side="none", show_kind="speech")
    n "Она неловко сделала шаг в сторону, задевая его своей грудью. Вирт едва заметно вздрогнул, сурово посмотрев на неё." (show_side="none", show_kind="speech")
    n "Эвейна поймала взгляд, ставший вдруг темным как ночное море. А затем, смутившись, опустила глаза, протиснулась между ним и креслом, чтобы скрыться в ванной комнате." (show_side="none", show_kind="speech")

    scene bg shuttle_bathroom at bg_fullscreen with dissolve

    n "Пока вода стекала по лицу, смывая слёзы, сон, близость и неловкость, мозг Эвейны лихорадочно соображал." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev_thought "Три дня. Одно купе. Один преподаватель с высокими моральными принципами." (show_side="left", show_kind="thought")
    ev_thought "И моя несчастная самодисциплина, которая уже готова медленно снимать с себя одежду под его взглядом." (show_side="left", show_kind="thought")
    hide eveina
    show eveina eyebrow at eveina_left
    ev_thought "Что может пойти не так?" (show_side="left", show_kind="thought")
    hide eveina

    jump scene_7_7
