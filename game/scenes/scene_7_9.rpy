label scene_7_9:
    $ previous_scene = "scene_7_8"
    $ next_scene = "scene_7_10"
    $ current_scene = "scene_7_9"
    call fade_to_black(1.2, 0.8)
    scene bg shuttle_3 at bg_fullscreen with dissolve

    n "Остаток пути они практически не разговаривали." (show_side="none", show_kind="speech") 
    n "Вирт держался безупречно холодно и спокойно. Так, что к нему нельзя было придраться — но от одного его взгляда можно было замёрзнуть до костей." (show_side="none", show_kind="speech")
    n "Каждое его движение стало точным, механическим. Фразы — исключительно по делу. Ни одного лишнего слова. Ни одного взгляда дольше положенного." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev_thought "Он ничего не сказал. И, кажется, именно это больнее всего." (show_side="left", show_kind="thought")
    ev_thought "Я видела его сдержанным. Знала его раздраженным." (show_side="left", show_kind="thought")
    hide eveina
    show eveina sad at eveina_left
    ev_thought "Но таким отстранённым — никогда." (show_side="left", show_kind="thought")
    ev_thought "И всё, что я могу делать сейчас — это сидеть рядом в одном купе, потому что отсюда некуда сбежать." (show_side="left", show_kind="thought")
    hide eveina
    show eveina thinking at eveina_left
    ev_thought "Идеальная тюрьма должна выглядеть именно так." (show_side="left", show_kind="thought")
    hide eveina
    show eveina upset at eveina_left
    ev_thought "И, может быть, я это заслужила?" (show_side="left", show_kind="thought")
    hide eveina

    n "Всю ночь Эвейна не могла уснуть. Свет в купе был приглушён, только слабое голубоватое мерцание панели освещало лицо Вирта." (show_side="none", show_kind="speech")
    n "Аурелиан сидел за столом, не двигаясь. Но Эвейна чувствовала, как его взгляд то и дело обращался к ней." (show_side="none", show_kind="speech")

    show virt normal at virt_right
    vi "Ты снова замёрзла." (show_side="right", show_kind="speech")
    hide virt

    n "Она вздрогнула от того, что он заговорил, внезапно нарушив тишину. И снова на «ты». Голос его снова был тихим. Тёплым. Тем самым — настоящим." (show_side="none", show_kind="speech")
    n "Он поднялся, подошёл, взял плед с верхней полки и накрыл её осторожно, словно боялся потревожить." (show_side="none", show_kind="speech")

    show eveina normal at eveina_left
    ev "Не уходи." (show_side="left", show_kind="speech")
    hide eveina

    n "Мужчина послушно сел рядом. Тишина в купе вдруг стала другой — не пустой и холодной, а наполненной." (show_side="none", show_kind="speech")

    show eveina sad at eveina_left
    ev "Не будь со мной снова холодным." (show_side="left", show_kind="speech")
    ev "Пожалуйста." (show_side="left", show_kind="speech")
    hide eveina

    show virt normal at virt_right
    vi "Я и не хочу быть холодным." (show_side="right", show_kind="speech")
    vi "Не с тобой." (show_side="right", show_kind="speech")
    hide virt

    show eveina normal at eveina_left
    ev "Тогда… каким ты хочешь быть?" (show_side="left", show_kind="speech")
    hide eveina

    n "Он медленно потянулся вперёд. Его пальцы коснулись её щеки — легко, почти невесомо." (show_side="none", show_kind="speech")
    n "Большой палец скользнул к виску, потом к шее и к ключице, обнажённой от соскользнувшего с плеча воротника." (show_side="none", show_kind="speech")

    show virt smile at virt_right
    vi "Вот таким." (show_side="right", show_kind="speech")
    hide virt

    n "Он наклонился и нежно, едва касаясь, поцеловал её в висок. Потом ниже. В плечо, в изгиб шеи — туда, где словно птица в клетке, билась жилка под кожей." (show_side="none", show_kind="speech")
    n "Тепло от мягких губ, ласкающих кожу, медленно разливалось по телу, оставляя лишь чувство защищённости — будто рядом с ним можно не бояться, будто всё действительно в порядке." (show_side="none", show_kind="speech")

    show eveina normal at eveina_left
    ev "Аурелиан." (show_side="left", show_kind="speech")
    hide eveina

    n "Девушка потянулась к нему и профессор притянул её к себе, обняв осторожно, как хрупкую чашу." (show_side="none", show_kind="speech")
    n "Она уткнулась носом в ямочку между ключицами, обхватила руками шею и глубоко вдохнула знакомый запах. Сквозь ткань чувствовала, как его ладонь гладит её по спине." (show_side="none", show_kind="speech")
    n "Закрыла глаза и потянулась к нему губами. Он мягко коснулся её губ своими и отстранился." (show_side="none", show_kind="speech")
    n "Только один звук вырвался из её губ — стон, тихий, почти благодарный. Как отклик на прикосновение, которого она ждала все эти дни." (show_side="none", show_kind="speech")

    show virt normal at virt_right
    vi "Эвейна…" (show_side="right", show_kind="speech")
    hide virt

    n "Она услышала, но не открыла глаз. Чувствовала, как он касается её губ. Ещё. Ещё раз. И снова мягко шепчет её имя." (show_side="none", show_kind="speech")

    show virt normal at virt_right
    vi "Эвейна." (show_side="right", show_kind="speech")
    vi "Проснись." (show_side="right", show_kind="speech")
    hide virt

    n "Девушка вздрогнула. Распахнула глаза — и сразу наткнулась на его взгляд." (show_side="none", show_kind="speech")
    n "Профессор стоял рядом, с лёгким беспокойством смотря на неё." (show_side="none", show_kind="speech")

    show virt normal at virt_right
    vi "Вы снова плохо спали?" (show_side="right", show_kind="speech")
    hide virt

    n "Эвейна быстро села, резко откидывая волосы с лица. Лицо горело от смущения и осознания, что поцелуй ей только приснился." (show_side="none", show_kind="speech")

    show eveina normal at eveina_left
    ev "Н-нет. Не совсем." (show_side="left", show_kind="speech")
    hide eveina

    n "Он склонился над ней — не касаясь, но внимательно осматривая её. Лицо как всегда было сдержанным и спокойным, но… в глазах — едва заметный блеск." (show_side="none", show_kind="speech")
    n "Она пыталась собраться с мыслями, но ощущение тепла на коже было ещё слишком ощутимым." (show_side="none", show_kind="speech")
    n "И тут до неё дошло. Впрочем, не только до неё." (show_side="none", show_kind="speech")

    show virt normal at virt_right
    vi "Вы… что-то прошептали во сне." (show_side="right", show_kind="speech")
    vi "Кажется, моё имя?" (show_side="right", show_kind="speech")
    hide virt

    n "Он старался говорить буднично. Но уголок его губ чуть дрогнул. Профессор отвёл взгляд ровно настолько, чтобы она успела заметить эту почти-улыбку." (show_side="none", show_kind="speech")

    show eveina wondered at eveina_left
    ev_thought "Нет. Нет-нет-нет." (show_side="left", show_kind="thought")
    ev_thought "Это ещё хуже, чем если бы он просто услышал, как я храплю." (show_side="left", show_kind="thought")
    hide eveina   
    show eveina eyeroll at eveina_left
    ev_thought "Он слышал, как я простонала его имя. Боже." (show_side="left", show_kind="thought")
    hide eveina   
    show eveina thinking at eveina_left
    ev "Я… это были не вы." (show_side="left", show_kind="speech")
    ev "То есть, вы, но не тот вы, в смысле, это был... кошмар! Мне снился экзамен, и вы его принимали... И я не сдала..." (show_side="left", show_kind="speech")
    hide eveina

    n "Он повернулся обратно. И, не сдержавшись, тихо хмыкнул." (show_side="none", show_kind="speech")

    show virt intrigued at virt_right
    vi "Не знал, что я такой страшный экзаменатор." (show_side="right", show_kind="speech")
    hide virt

    n "Совершенно невозмутимо Аурелиан протянул ей стакан с водой. Как будто не слышал ничего важного. Как будто совсем не видел, как её уши полыхают до корней волос." (show_side="none", show_kind="speech")
    n "Эвейна с благодарностью взяла стакан, спрятав за ним смущенный взгляд. И если бы могла, вылезла бы в открытый космос." (show_side="none", show_kind="speech")

    show eveina angry at eveina_left
    ev_thought "Я убью себя. Или его." (show_side="left", show_kind="thought")
    ev_thought "Но скорее — себя." (show_side="left", show_kind="thought")
    hide eveina

    show virt normal at virt_right
    vi "Пора собираться. Мы прилетели." (show_side="right", show_kind="speech")
    hide virt

    jump scene_7_10