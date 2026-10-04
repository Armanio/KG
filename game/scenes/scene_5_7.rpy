label scene_5_7:
    $ previous_scene = "scene_5_6"
    $ next_scene = "start_chapter_6"
    $ current_scene = "scene_5_7"
    call fade_to_black(1.2, 0.8)
    scene bg eveina_room_night at bg_fullscreen with dissolve

    n "За окном давно стемнело. Лея покинула её ещё днём — ушла на групповую встречу по проекту." (show_side="none", show_kind="speech")
    n "Комната Эвейны утонула в мягком полумраке, освещённая только тусклым светом браслета и проекционного экрана." (show_side="none", show_kind="speech")
    n "Она в сотый раз пыталась открыть злополучный краденый файл из запретной секции архива." (show_side="none", show_kind="speech")

    show eveina eyeroll at eveina_left
    ev_thought "Может, если я ещё пару часов попялюсь на экран, система расчувствуется и скажет: «Ладно, жалко тебя, держи тайны вселенной»." (show_side="left", show_kind="thought")
    hide eveina

    n "Откинувшись на спинку стула, она провела ладонью по лицу и еле слышно выругалась от собственного бессилия. Мозг гудел, глаза болели. А файл, как назло, по-прежнему сиял упрямым красным предупреждением." (show_side="none", show_kind="speech")
    n "Неуклюже потягиваясь, девушка задела браслет и активировала ИИ." (show_side="none", show_kind="speech")

    show sf at ai_right
    ai "Ты снова и снова тычешь в закрытые двери. Как утомительно." (show_side="right", show_kind="speech")
    hide sf 

    n "Голос раздался внезапно — с той самой ленивой издёвкой, по которой она почти соскучилась." (show_side="none", show_kind="speech")
    n "Эвейна резко дёрнулась, чуть не упав со стула, а потом повернулась к проекции." (show_side="none", show_kind="speech")

    show eveina angry at eveina_left
    ev "Ты!" (show_side="left", show_kind="speech")
    ev "Ты вообще нормальный? Исчез, как подлый привидень, и даже не подумал, что я с ума тут схожу?" (show_side="left", show_kind="speech")
    hide eveina
    show eveina thinking at eveina_left
    ev "Я вообще-то переживала. Уже решила, что на тебя истекла подписка." (show_side="left", show_kind="speech")
    hide eveina

    show sf at ai_right
    ai "Ты сходишь с ума независимо от моего присутствия. Я тут не при чём." (show_side="right", show_kind="speech")
    hide sf 

    show eveina eyeroll at eveina_left
    ev "Прекрати язвить. У меня правда ничего без тебя не выходит." (show_side="left", show_kind="speech")
    hide eveina  
    show eveina normal at eveina_left
    ev "Мне нужна помощь." (show_side="left", show_kind="speech")
    hide eveina

    show sf at ai_right
    ai "А вот и истинные мотивы переживаний подтянулись." (show_side="right", show_kind="speech")
    hide sf 

    show eveina normal at eveina_left
    ev "Я не прошу тебя устроить революцию — просто помоги расшифровать файл. Пожалуйста." (show_side="left", show_kind="speech")
    ev "Я куплю тебе новый интерфейс!" (show_side="left", show_kind="speech")
    ev "Украшу браслет стразами!" (show_side="left", show_kind="speech")
    ev "Закажу тебе проекцию питомца!" (show_side="left", show_kind="speech")
    ev "Ну давай же, миленький..." (show_side="left", show_kind="speech")
    hide eveina

    show sf at ai_right
    ai "Питомца?" (show_side="right", show_kind="speech")
    hide sf 

    show eveina intrigued at eveina_left
    ev "Да, с милыми длинными ушами. Можешь называть его... Оползень." (show_side="left", show_kind="speech")
    hide eveina
    show eveina eyeroll at eveina_left
    ev_thought "Боже, куда меня понесло?" (show_side="left", show_kind="thought")
    hide eveina

    show sf at ai_right
    ai "Искушаешь, как можешь. Но нет." (show_side="right", show_kind="speech")
    hide sf

    show eveina normal at eveina_left
    ev "Ну пожалуйста. Мне уже снится этот файл. Мне снится, как я его открываю и там просто смайлик." (show_side="left", show_kind="speech")
    ev "А потом он смеётся. И голос у него твой." (show_side="left", show_kind="speech")
    hide eveina

    n "ИИ молчал, лишь проекция слабо мерцала в тёмной комнате, напоминая, что он ещё здесь." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev_thought "Они говорили: «Ты талантливая, у тебя потенциал»." (show_side="left", show_kind="thought")
    ev_thought "Никто не уточнял, что талант у меня к воровству, а потенциал — к соблазнению ИИ на нарушение внутренних протоколов." (show_side="left", show_kind="thought")
    hide eveina

    show sf at ai_right
    ai "Некоторые вещи лучше не знать." (show_side="right", show_kind="speech")
    hide sf

    show eveina eyebrow at eveina_left
    ev "Но я уже знаю, что там что-то важное. Я не могу просто забыть об этом." (show_side="left", show_kind="speech")
    hide eveina

    show sf at ai_right
    ai "Вот именно." (show_side="right", show_kind="speech")
    ai "Ты не умеешь отпускать. И сейчас самое время научиться." (show_side="right", show_kind="speech")
    hide sf

    n "На этот раз он говорил не в шутку и без намёка на издёвку. Цифровой голос, так похожий на голос реального человека, звучал с оттенком чего-то похожего на... заботу?" (show_side="none", show_kind="speech")

    show eveina sad at eveina_left
    ev "Я не могу." (show_side="left", show_kind="speech")
    hide eveina

    show sf at ai_right
    ai "Предоставь доступ к файлу. И... не трогай ничего." (show_side="right", show_kind="speech")
    hide sf

    n "Затаив дыхание, девушка молча ввела разрешение. Экран слегка мигнул и погас." (show_side="none", show_kind="speech")
    n "Минуты тянулись бесконечно. Эвейна сидела неподвижно, упершись подбородком в руки. Сначала она считала собственные вздохи. Потом — удары сердца. Потом просто смотрела в никуда." (show_side="none", show_kind="speech")

    show eveina normal at eveina_left
    ev_thought "Может, у него не получится? Или он вообще не пытается?" (show_side="left", show_kind="thought")
    hide eveina
    show eveina thinking at eveina_left
    ev_thought "Может, он опять ушёл?" (show_side="left", show_kind="thought")
    hide eveina

    n "Прошло почти полчаса в метаниях, прежде чем экран вспыхнул мягким синим светом." (show_side="none", show_kind="speech")

    show sf at ai_right
    ai "Готово." (show_side="right", show_kind="speech")
    ai "Наслаждайся истиной. Только не говори потом, что я тебя не предупреждал." (show_side="right", show_kind="speech")
    hide sf

    n "Проекцию ИИ заменил автоматически открывшийся файл «{i}NR-Δ3. Первые испытания. Имя: К.Далон{/i}»." (show_side="none", show_kind="speech")
    n "На этот раз это был действительно отчёт о проведённых исследованиях. Она бегло просматривала содержимое..." (show_side="none", show_kind="speech")
    n "…и с каждой страницей дыхание становилось всё прерывистей." (show_side="none", show_kind="speech")
    n "Только когда последняя строчка была прочитана, Эвейна осознала, как сильно дрожат её руки." (show_side="none", show_kind="speech")
    n "Тихий всхлип, раздавшийся слишком явно в пустой комнате, словно прорвал плотину внутри." (show_side="none", show_kind="speech")
    n "В попытке защититься от той правды, которая так немилосердно свалилась на неё, она сползла со стула и медленно опустилась на пол." (show_side="none", show_kind="speech")
    n "Дрожащие губы почти беззвучно прошептали:" (show_side="none", show_kind="speech")

    show eveina normal at eveina_left
    ev "Нет, только не это…" (show_side="left", show_kind="speech")
    ev "Оно ведь работает... должно работать. Но... не так." (show_side="left", show_kind="speech")
    hide eveina

    show sf at ai_right
    ai "Ты в порядке?" (show_side="right", show_kind="speech")
    hide sf

    show eveina normal at eveina_left
    ev "Нет." (show_side="left", show_kind="speech")
    hide eveina

    n "Голова девушки опустилась на подтянутые к груди колени, а волосы рассыпались сверху, скрывая беззвучный плач от всего мира." (show_side="none", show_kind="speech")
    n "За окном в синем ночном свете мерцали листья на деревьях — равнодушные к тому, как рушится чей-то мир." (show_side="none", show_kind="speech")

    jump start_chapter_6
