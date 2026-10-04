label scene_4_6:
    $ previous_scene = "scene_4_5"
    $ next_scene = "scene_4_7"
    $ current_scene = "scene_4_6"

    # =========================================================
    # СЦЕНА 4_6 — «БЕССОННИЦА / КОРИДОР / ЭРИАН ПРИКРЫВАЕТ»
    # Структура: бессонница после поцелуя (новое начало)
    #            → выход в коридор → Сайф → Эриан
    #            → кто-то идёт (Каэль) → прикрытие
    #            → «тебе нужно в архив»
    # Начало — новый текст. Далее — оригинал 4_3 строки 7–304.
    # =========================================================

    call fade_to_black(1.2, 0.8)
    scene bg eveina_room_night at bg_fullscreen with dissolve
    # play music "bgm/quiet_night.ogg" fadein 2.0

    # --- Бессонница ---

    n "После чёртового поцелуя с чёртовым Каэлем сон стал невозможным. Эвейна лежала на спине, уставившись в потолок." (show_side="none", show_kind="speech")
    n "Мысли крутились, сбивались, возвращались к одному и тому же — как нелепо всё произошло. И как жестоко он с ней поступил." (show_side="none", show_kind="speech")
    n "Она несколько раз переворачивалась с боку на бок, вжималась в подушку, натягивала одеяло, откидывала его." (show_side="none", show_kind="speech")
    n "Ничего не помогало." (show_side="none", show_kind="speech")
    n "Даже воспоминание о закрытой секции архива, которое ещё утром вытягивало из неё все силы, теперь отступило в тень." (show_side="none", show_kind="speech")

    show eveina annoyed at eveina_left
    ev_thought "Ошибка! Поверить не могу... Какого чёрта ты полез ко мне с поцелуями?" (show_side="left", show_kind="thought")
    hide eveina
    show eveina thinking at eveina_left
    ev_thought "«Эвейна, у тебя есть шанс меня остановить...» Ага, как же..." (show_side="left", show_kind="thought")
    hide eveina
    show eveina angry at eveina_left
    ev_thought "Нет у меня шанса, идиот — ты заткнул мне рот своим языком!" (show_side="left", show_kind="thought")
    hide eveina
    show eveina annoyed at eveina_left
    ev_thought "Что за херню ты устроил вообще..." (show_side="left", show_kind="thought")
    ev_thought "Это такой извращённый способ выпроводить меня из лаборатории?" (show_side="left", show_kind="thought")
    hide eveina
    show eveina angry at eveina_left
    ev_thought "Или… хуже того — какой-то больной эксперимент?" (show_side="left", show_kind="thought")
    hide eveina

    if kael_first_kiss == "continue":
        show eveina upset thinking at eveina_left
        ev_thought "Боже, ну почему я его не оттолкнула, когда был шанс?" (show_side="left", show_kind="thought")
        hide eveina

    n "Пальцы нащупали край пледа. Сердце стучало не в такт. Она будто снова стояла в той лаборатории, прижатая к его груди сильной рукой." (show_side="none", show_kind="speech")
    n "Где-то к утру Эвейна всё же провалилась в тревожный, отрывистый сон, но и он не принёс облегчения." (show_side="none", show_kind="speech")

    scene bg eveina_room_night at bg_fullscreen with dissolve

    n "Когда часы снова перевалили за полночь, она бросила попытки уснуть и тихо выбралась из комнаты." (show_side="none", show_kind="speech")

    # --- Коридор (из оригинала 4_3, строки 7–304) ---

    scene bg forbidden_corridor at bg_fullscreen with dissolve
    # play music "bgm/forbidden_zone.ogg" fadein 2.0

    n "Сердце стучало в ушах — громко, будто хотело выдать её с потрохами." (show_side="none", show_kind="speech")
    n "В коридоре царила тьма. Только редкие голографические лампы дышали тусклым светом." (show_side="none", show_kind="speech")
    n "Она знала, что делает глупость. Но глупость была слишком похожа на необходимость." (show_side="none", show_kind="speech")
    n "Девушка продолжала двигаться вперед, замечая, что коридоры становились всё незнакомее." (show_side="none", show_kind="speech")
    n "Ландшафт Академии будто изменился: стены вытягивались, повороты повторялись, а указатели исчезали." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev_thought "Это уже не та Академия. Это… что-то другое. Слепая зона." (show_side="left", show_kind="thought")
    hide eveina
    n "Она открыла карту и сверилась с ней." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev_thought "Направо до конца, направо до первого перекрестка, налево и прямо вниз." (show_side="left", show_kind="thought")
    hide eveina
    show eveina normal at eveina_left
    ev_thought "Звучит несложно." (show_side="left", show_kind="thought")
    hide eveina

    n "Когда она остановилась на очередной развилке, ощущение собственного бессилия накрыло с головой. Ей нужно было налево, но коридор уходил только вправо и прямо. Она вскинула запястье и активировала ИИ." (show_side="none", show_kind="speech")

    show sf at ai_right
    ai "Полночь. Прекрасное время для студенческих подвигов." (show_side="right", show_kind="speech")
    hide sf

    show eveina normal at eveina_left
    ev "Тише. Помоги. Я запуталась." (show_side="left", show_kind="speech")
    hide eveina

    show sf at ai_right
    ai "Прилежные студентки спят." (show_side="right", show_kind="speech")
    hide sf

    show eveina annoyed at eveina_left
    ev "Я буду очень прилежной с утра. Но сейчас мне нужно попасть в закрытую секцию." (show_side="left", show_kind="speech")
    hide eveina

    show sf at ai_right
    ai "Тебе не приходило в голову, что она называется закрытой потому что... ну... закрыта?" (show_side="right", show_kind="speech")
    ai "Помнится, мы были солидарны в том, что исключение — не лучший вариант для нас обоих." (show_side="right", show_kind="speech")
    hide sf

    show eveina annoyed at eveina_left
    ev "Слушай, давай решать проблемы по мере их поступления!" (show_side="left", show_kind="speech")
    hide eveina

    n "После короткой паузы ИИ вздохнул." (show_side="none", show_kind="speech")

    show sf at ai_right
    ai "Хорошо. Ты не дошла до конца коридора — тебе туда, затем налево. После — вниз по лестнице. Не промахнись." (show_side="right", show_kind="speech")
    hide sf

    n "Она двинулась вперёд." (show_side="none", show_kind="speech")

    show eveina eyebrow at eveina_left
    ev "Левый коридор, да? Там нет ни указателей, ни замков. Только… пустота." (show_side="left", show_kind="speech")
    hide eveina

    show sf at ai_right
    ai "Ты за пределами доступного студентам пространства Академии. Здесь не ходят те, кто не понимает, где находится." (show_side="right", show_kind="speech")
    ai "Вернись, пока не стало поздно." (show_side="right", show_kind="speech")
    hide sf

    show eveina normal at eveina_left
    ev "Не могу. Я почти у цели. Я знаю." (show_side="left", show_kind="speech")
    hide eveina

    show sf at ai_right
    ai "Ты не знаешь. Ты угадываешь. Это не одно и то же." (show_side="right", show_kind="speech")
    hide sf

    show eveina thinking at eveina_left
    ev "Если бы я действовала логично, меня бы здесь вообще не было." (show_side="left", show_kind="speech")
    hide eveina

    show sf at ai_right
    ai "Ты ведь в курсе, что всё это — плохая идея. Запретные сектора названы так не ради драматизма." (show_side="right", show_kind="speech")
    hide sf

    show eveina normal at eveina_left
    ev "А если именно в них — всё, что нужно? Всё, что кто-то прячет?" (show_side="left", show_kind="speech")
    hide eveina

    show sf at ai_right
    ai "Ты пойдёшь туда, даже если я откажусь помогать." (show_side="right", show_kind="speech")
    hide sf

    n "Это не было вопросом. Лишь констатацией раздражающего факта." (show_side="none", show_kind="speech")

    show eveina intrigued at eveina_left
    ev "Конечно. Но мне будет спокойнее, если ты будешь рядом." (show_side="left", show_kind="speech")
    hide eveina

    show sf at ai_right
    ai "Иди, неугомонная студентка." (show_side="right", show_kind="speech")
    ai "И...не забудь дышать, а то сердце из грудной клетки выскочит." (show_side="right", show_kind="speech")
    hide sf

    n "Девушка сделала глубокий вдох и тут же замерла, почуствовав знакомый холодок на затылке. За очередным поворотом в полумраке мелькнула фигура." (show_side="none", show_kind="speech")
    n "Она вздрогнула, едва не вскрикнув, и резко отключила браслет. В нескольких шагах от неё из тени вынырнул…" (show_side="none", show_kind="speech")

    show erian angry at erian_right
    er "..." (show_side="right", show_kind="speech")
    hide erian

    n "В его взгляде читалось не удивление, а тёмное раздражение. Как у хищника, которому испортили охоту." (show_side="none", show_kind="speech")
    n "Он медленно двинулся на неё, отчего Эвейна попятилась назад. В почти полной тишине, прерываемой лишь вдохами и шорохом шагов, его шёпот звучал страшнее любого крика." (show_side="none", show_kind="speech")

    show erian angry at erian_right
    er "Ты серьёзно? Это… Это даже для тебя слишком." (show_side="right", show_kind="speech")
    er "Почему ты постоянно так себя ведёшь — сначала делаешь, а уже потом думаешь?" (show_side="right", show_kind="speech")
    hide erian

    show eveina angry at eveina_left
    ev "А ты что здесь забыл?" (show_side="left", show_kind="speech")
    hide eveina

    n "Во тьме коридора светились только две пары глаз — испуганные серые и полные ярости янтарные." (show_side="none", show_kind="speech")
    n "Вопрос остался без ответа. Эриан тяжело вздохнул, будто сдерживал эмоции, которые были готовы прорваться наружу." (show_side="none", show_kind="speech")

    show erian angry at erian_right
    er "Ты хоть представляешь, где ты? Как вообще сюда попала?" (show_side="right", show_kind="speech")
    hide erian

    show eveina eyeroll at eveina_left
    ev "По навигатору. С очень… капризным голосом." (show_side="left", show_kind="speech")
    hide eveina

    show erian angry at erian_right
    er "Он что, заблудился, ведя тебя в твою комнату?" (show_side="right", show_kind="speech")
    hide erian
    show erian angry wild at erian_right
    er "Или он вёл тебя в мою?" (show_side="right", show_kind="speech")
    hide erian

    n "Эвейна захлебнулась от возмущения, снова позабыв о мурашках на коже, вызванных одним его появлением в поле её зрения." (show_side="none", show_kind="speech")

    show eveina angry at eveina_left
    ev "Ага, чтобы задушить тебя подушкой во сне." (show_side="left", show_kind="speech")
    hide eveina

    n "Парень вдруг засмеялся, легко и непринужденно, будто услышал хорошую шутку. Перепалка повисла в воздухе, позволив девушке слегка расслабиться." (show_side="none", show_kind="speech")

    show eveina annoyed at eveina_left
    ev "Рада, что тебя так веселит новость о твоей скорой..." (show_side="left", show_kind="speech")
    hide eveina

    n "Вдруг Эриан замер, а его режущий взгляд упёрся в неё. Прежде чем она успела понять, что происходит, его рука резко обвила её запястье." (show_side="none", show_kind="speech")

    show eveina wondered at eveina_left
    ev "Ты что тво..." (show_side="left", show_kind="speech")
    hide eveina

    n "Рывок — и Эвейна врезалась спиной в холодную стену. От силы удара перехватило дыхание." (show_side="none", show_kind="speech")
    n "Правая ладонь точным решительным движением накрыла её губы. Левая обхватила оба её запястья в подобие наручников." (show_side="none", show_kind="speech")
    n "Огромное по сравнению с ней тело Эриана прижалось к ней вплотную. Она, кажется, впервые осознала насколько он больше неё. Их взгляды встретились и Эвейна в ужасе распахнула глаза." (show_side="none", show_kind="speech")
    n "Сердце ухало где-то в ушах, перебивая мелькнувшую в голове мысль:" (show_side="none", show_kind="speech")

    show eveina wondered at eveina_left
    ev_thought "Возможно, не стоило..." (show_side="left", show_kind="thought")
    ev_thought "...в тёмном коридоре, где никто не увидит и не услышит..." (show_side="left", show_kind="thought")
    ev_thought "...выводить из себя самого раздражительного человека..." (show_side="left", show_kind="thought")
    ev_thought "...с весьма сомнительными представлениями о личных границах." (show_side="left", show_kind="thought")
    hide eveina

    n "В ответ на её мысли парень холодно улыбнулся." (show_side="none", show_kind="speech")

    show erian smile wild at erian_right
    er "Ты слишком шумная." (show_side="right", show_kind="speech")
    hide erian

    n "А потом она услышала. Шаги. Быстрые. Чёткие. Кто-то приближался." (show_side="none", show_kind="speech")
    n "Глаза Эриана метнулись в сторону, затем снова к ней. Он накрыл её своей тенью, как будто пытался сделать невидимой." (show_side="none", show_kind="speech")

    show eveina wondered at eveina_left
    ev_thought "Он серьёзно решил, что будет лучше, если нас застанут здесь в этой позе?" (show_side="left", show_kind="thought")
    hide eveina
    show eveina annoyed at eveina_left
    ev_thought "Спасибо, конечно, что не решил меня придушить... но... он совсем рехнулся?" (show_side="left", show_kind="thought")
    hide eveina

    n "Его лоб коснулся её лба, а губы казались в миллиметре от её кожи, заставив её вздрогнуть. Тихое дыхание обожгло её щёки, когда он шепнул одними губами:" (show_side="none", show_kind="speech")

    show erian normal at erian_right
    er "Тсс...Не дыши." (show_side="right", show_kind="speech")
    hide erian

    n "Сама не зная почему, Эвейна послушно замерла и задержала дыхание." (show_side="none", show_kind="speech")
    n "Шаги были совсем близко. Она почувствовала, как тело Эриана напряглось. Он прикрыл глаза. Между бровей залегла складка." (show_side="none", show_kind="speech")
    n "Мимо них прошёл человек. И она узнала его резкую походку." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev_thought "Каэль..." (show_side="left", show_kind="thought")
    hide eveina

    n "Он пронёсся, не заметив их, как будто их и не существовало." (show_side="none", show_kind="speech")
    n "Немного погодя, Эриан оторвался от её лба и замер в нескольких сантиметрах над ней, смотря ей в глаза." (show_side="none", show_kind="speech")
    n "Вдалеке стихли звуки шагов. Эвейна удивлённо вздохнула." (show_side="none", show_kind="speech")

    show eveina eyebrow at eveina_left
    ev_thought "Ты отпустишь меня? Или…" (show_side="left", show_kind="thought")
    hide eveina

    n "Эриан не двигался, продолжая держать её. Она чувствовала, как под его пальцами дрожат её губы." (show_side="none", show_kind="speech")
    n "И он чувствовал это тоже. Его дыхание стало глубже. Между ними пульсировало что-то дикое, почти запрещённое." (show_side="none", show_kind="speech")
    n "Он оторвал взгляд от её глаз и чуть отстранился, оглядев её сверху. Дрожащую, с немым вопросом в глазах." (show_side="none", show_kind="speech")
    n "На его лице неторопливо расплылась дьявольская ухмылка, а в глазах промелькнули всполохи пламени." (show_side="none", show_kind="speech")
    n "И только потом, с замедленной решимостью, он убрал руку с её лица. Пальцы скользнули по скуле, будто задержавшись на прощание, и упёрлись в стену." (show_side="none", show_kind="speech")
    n "Лениво отстранившись лишь на несколько сантиметров, Эриан сделал глубокий вдох и прошептал:" (show_side="none", show_kind="speech")

    show erian intrigued at erian_right
    er "Не шуми, он всё ещё может вернуться." (show_side="right", show_kind="speech")
    hide erian
    show erian smile wild at erian_right
    er "И перестань тереться о мой член. Он уже и так понял, что ты рядом." (show_side="right", show_kind="speech")
    hide erian

    n "Эвейна просто захлебнулась от собственного возмущения. Серые глаза прожгли самодовольное лицо, когда она прошипела:" (show_side="none", show_kind="speech")

    show eveina annoyed at eveina_left
    ev "Отпусти меня!" (show_side="left", show_kind="speech")
    hide eveina

    n "Словно желая придать веса своим словам, девушка дёрнулась всем телом, и тут же пожалела об этом, почувствовав, как что-то твёрдое упёрлось ей в живот. Эриан медленно прикрыл глаза и выпустил воздух через стиснутые зубы." (show_side="none", show_kind="speech")

    show erian thinking at erian_right
    er "Любишь же ты поиграть с огнём..." (show_side="right", show_kind="speech")
    er "Чего дрожишь? Это от страха…" (show_side="right", show_kind="speech")
    hide erian
    show erian intrigued at erian_right
    er "или от того, что я слишком близко?" (show_side="right", show_kind="speech")
    hide erian

    n "Он склонил голову чуть набок. Губы снова скривились в ухмылке, но глаза были серьёзны. И в этой серьёзности — опасное притяжение." (show_side="none", show_kind="speech")
    n "Смущённо опустив глаза, девушка с новой волной неловкости осознала — в этом вопросе не просто издёвка. Он точно знает, что она чувствует. Возможно, лучше, чем она сама." (show_side="none", show_kind="speech")
    n "По её коже пробегали разряды тока, беря начало там, где его руки ещё недавно её касались, и это не было похоже на то, что она ощущала ранее." (show_side="none", show_kind="speech")
    n "Тело будто предавало её, требуя снова оказаться в его власти. Это было неправильно. Всё рядом с ним было неправильно." (show_side="none", show_kind="speech")
    n "С трудом собрав волю в маленькие женские кулачки, она выдавила из себя хриплый шёпот." (show_side="none", show_kind="speech")

    show eveina normal at eveina_left
    ev "Ты... слишком..." (show_side="left", show_kind="speech")
    hide eveina

    show eveina thinking at eveina_left
    ev_thought "...близко?" (show_side="left", show_kind="thought")
    ev_thought "...далеко?" (show_side="left", show_kind="thought")
    hide eveina
    show eveina angry at eveina_left
    ev_thought "Раздражаешь!" (show_side="left", show_kind="thought")
    hide eveina
    show eveina intrigued at eveina_left
    ev_thought "Точно, вот что я чувствую! Ты просто меня бесишь до чёртиков." (show_side="left", show_kind="thought")
    hide eveina
    show eveina upset thinking at eveina_left
    ev_thought "Только отодвинься от меня... пожалуйста!" (show_side="left", show_kind="thought")
    hide eveina

    n "Ей было страшно признавать, что бы она сделала, что позволила, если бы он не сдвинулся с места. Но Эриан всё же отступил. И это было облегчением. И разочарованием." (show_side="none", show_kind="speech")
    n "Его взгляд всё ещё был прикован к ней. Эвейна глубоко вздохнула, пытаясь вернуть самообладание." (show_side="none", show_kind="speech")

    show eveina eyebrow at eveina_left
    ev "Почему он нас не увидел? Он ведь…" (show_side="left", show_kind="speech")
    hide eveina

    n "Эриан пропустил вопрос мимо ушей. Зато задал свой." (show_side="none", show_kind="speech")

    show erian eyebrow at erian_right
    er "Что ты тут делаешь, Эвейна?" (show_side="right", show_kind="speech")
    hide erian

    show eveina annoyed at eveina_left
    ev "Ты сам сказал, чтобы я искала ответы самостоятельно, вот я и ищу!" (show_side="left", show_kind="speech")
    hide eveina

    show erian intrigued at erian_right
    er "Надеешься, что нужное тебе исследование будет валяться в коридоре?" (show_side="right", show_kind="speech")
    hide erian

    show eveina annoyed at eveina_left
    ev "Надеялась, что смогу попасть в закрытую секцию архива, узнать, кто, чёрт возьми, такой Кайр Далон и не встретить здесь тебя!" (show_side="left", show_kind="speech")
    hide eveina

    n "Когда она произнесла имя — Кайр Далон — в его лице что-то неуловимо изменилось. Ухмылку заменил серьёзный настороженный взгляд." (show_side="none", show_kind="speech")
    n "Он несколько секунд сверлил её глазами, из-за чего девушка снова вжалась в стену, а потом без спроса схватил её за руку и потащил за собой дальше по коридору." (show_side="none", show_kind="speech")

    show eveina annoyed at eveina_left
    ev "Ну и куда ты меня ведёшь?" (show_side="left", show_kind="speech")
    hide eveina

    show erian normal at erian_right
    er "Тебе нужно в архив, а мне нужно, чтобы тебя тут не застукали и не подняли шум." (show_side="right", show_kind="speech")
    er "Так что иди молча." (show_side="right", show_kind="speech")
    hide erian

    n "Не успела Эвейна открыть рот, чтобы возразить, как поймала предупреждающий взгляд парня на себе и благоразумно решила промолчать." (show_side="none", show_kind="speech")
    n "В конце концов, в отличие от неё, он явно знал куда идти." (show_side="none", show_kind="speech")

    jump scene_4_7
