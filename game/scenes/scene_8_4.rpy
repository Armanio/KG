label scene_8_4:
    $ previous_scene = "scene_8_3"
    $ next_scene = "scene_8_5"
    $ current_scene = "scene_8_4"
    call fade_to_black(1.2, 0.8)
    scene bg lab at bg_fullscreen with dissolve

    n "Эвейна сама не понимала, как ноги привели её в лабораторию. Наверно, так на подсознательном уровне работает страх одиночества." (show_side="none", show_kind="speech")
    n "Каэль по обыкновению стоял у консоли. Не обернулся, но Эвейна заметила, как он замер, услышав знакомые шаги." (show_side="none", show_kind="speech")

    show kael normal at kael_right
    ka "Неожиданно." (show_side="right", show_kind="speech")
    ka "Тебя, кажется, освободили от занятий до конца дня." (show_side="right", show_kind="speech")
    hide kael

    n "Девушка неуверенно подошла ближе, теребя рукой браслет." (show_side="none", show_kind="speech")

    show eveina normal at eveina_left
    ev "Я хотела закончить решение." (show_side="left", show_kind="speech")
    ev "Хотела бы доработать программу. То, что не доделала." (show_side="left", show_kind="speech")
    hide eveina

    n "Каэль медленно к ней повернулся, пробегая оценивающим взглядом по уставшему лицу, темным кругам под горящими решительностью глазами." (show_side="none", show_kind="speech")

    show kael serious at kael_right
    ka "Ты уверена?" (show_side="right", show_kind="speech")
    hide kael

    n "Она кивнула." (show_side="none", show_kind="speech")

    show kael eyebrow at kael_right
    ka "После всего, что произошло?" (show_side="right", show_kind="speech")
    hide kael

    n "Она снова кивнула. Каэль прищурился." (show_side="none", show_kind="speech")

    show kael serious at kael_right
    ka "Я должен спросить: как ты себя чувствуешь?" (show_side="right", show_kind="speech")
    hide kael

    show eveina normal at eveina_left
    ev "В порядке. Я в порядке." (show_side="left", show_kind="speech")
    ev_thought "Это не совсем правда. Но хуже уже не будет." (show_side="left", show_kind="thought")
    hide eveina

    show kael serious at kael_right
    ka "А выглядишь так, будто тебе стоит хорошенько выспаться." (show_side="right", show_kind="speech")
    hide kael

    show eveina thinking at eveina_left
    ev_thought "А вот и комплименты от Каэля подоспели." (show_side="left", show_kind="thought")
    hide eveina
    show eveina annoyed at eveina_left
    ev "Мы будем обсуждать мой внешний вид или начнём работать?" (show_side="left", show_kind="speech")
    hide eveina

    show kael serious at kael_right
    ka "Как скажешь." (show_side="right", show_kind="speech")
    hide kael
    show kael normal at kael_right
    ka "Если ты действительно хочешь вернуться к твоему решению..." (show_side="right", show_kind="speech")
    ka "Я помогу." (show_side="right", show_kind="speech")
    hide kael

    n "Он сделал шаг в сторону и разблокировал один из терминалов. Свет вспыхнул, структура сети раскрылась на экране." (show_side="none", show_kind="speech")
    n "Работать начали молча. Но минут через десять он вдруг заговорил." (show_side="none", show_kind="speech")

    show kael normal at kael_right
    ka "Ты же понимаешь, что иногда решение не приходит с первого раза." (show_side="right", show_kind="speech")
    ka "Иногда его вообще не бывает." (show_side="right", show_kind="speech")
    ka "Но попытка уже..." (show_side="right", show_kind="speech")
    hide kael

    n "Эвейна нетерпеливо его перебила, понимая к чему он ведёт." (show_side="none", show_kind="speech")

    show eveina annoyed at eveina_left
    ev "Мне недостаточно попытки." (show_side="left", show_kind="speech")
    ev "Я хочу понять, можно ли получить устойчивый результат." (show_side="left", show_kind="speech")
    hide eveina

    show kael normal at kael_right
    ka "Тогда ты на верном пути." (show_side="right", show_kind="speech")
    hide kael

    n "Каэль выдвигал новые гипотезы, девушка тут же вносила изменения. Сеть реагировала на новые узлы, стабилизация казалась теоретически возможной." (show_side="none", show_kind="speech")
    n "Делая очередную настройку и наблюдая за реакцией системы, Эвейна неожиданно для себя самой произнесла:" (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev "Если это сработает…" (show_side="left", show_kind="speech")
    ev "Если действительно можно восстанавливать разрушенные нейросвязи…" (show_side="left", show_kind="speech")
    hide eveina
    show eveina eyebrow at eveina_left
    ev "Тогда, может быть… это и есть то самое." (show_side="left", show_kind="speech")
    hide eveina

    n "Каэль молчал, не отрывая взгляда от экрана. Но Эвейне и не требовался его ответ." (show_side="none", show_kind="speech")

    show eveina normal at eveina_left
    ev "То самое, что я искала." (show_side="left", show_kind="speech")
    ev "Не формула. Не препарат. А… модель." (show_side="left", show_kind="speech")
    ev "Решение задачи Идентики, как механизм сохранения личности. Даже когда сознание разваливается." (show_side="left", show_kind="speech")
    ev "Если я смогу это повторить в реальности…" (show_side="left", show_kind="speech")
    hide eveina
    show eveina eyebrow at eveina_left
    ev "Может быть, это и есть лекарство? Моё. Моя версия. Мой путь." (show_side="left", show_kind="speech")
    hide eveina

    n "Девушка оторвалась от экрана и встретилась глазами с Каэлем. И в его взгляде не было ни скепсиса, ни насмешки." (show_side="none", show_kind="speech")

    show kael normal at kael_right
    ka "Ты ищешь не лекарство." (show_side="right", show_kind="speech")
    ka "Ты ищешь способ не терять то, что любишь." (show_side="right", show_kind="speech")
    hide kael
    show kael serious at kael_right
    ka "И в этом ты… опасно человечна." (show_side="right", show_kind="speech")
    hide kael

    n "Он снова вернулся к работе. Пальцы заскользили по поверхности интерфейса." (show_side="none", show_kind="speech")

    show kael serious at kael_right
    ka "Это плохой мотив для науки." (show_side="right", show_kind="speech")
    hide kael
    show kael normal at kael_right
    ka "И единственный, ради которого стоит продолжать." (show_side="right", show_kind="speech")
    hide kael

    n "Они ещё немного поработали молча, пока Эвейна не выключила интерфейс. Он не сказал «достаточно» — но и не остановил её, давая ей право решать." (show_side="none", show_kind="speech")
    n "Когда она встала, собираясь уходить, Каэль вдруг взял её за руку и притянул к себе. Его взгляд оценивающе пробежался по её лицу." (show_side="none", show_kind="speech")

    show kael normal at kael_right
    ka "Ты правда в порядке?" (show_side="right", show_kind="speech")
    hide kael
    show kael sad at kael_right
    ka "Вирт сказал, ты долго отходила от последствий эксперимента." (show_side="right", show_kind="speech")
    hide kael

    show eveina smile at eveina_left
    ev "Не думала, что Вирт такой болтливый." (show_side="left", show_kind="speech")
    hide eveina 
    show eveina normal at eveina_left
    ev "Всё хорошо, правда. Просто устала с дороги." (show_side="left", show_kind="speech")
    hide eveina 

    $ result = renpy.call_screen("choice", 
    items=[
    ("коснулся её губ своими.", "kiss"),
    ("отпустил её руку.", "leave")
    ], what="Каэль замер, разглядывая её лицо, а затем...")

    if result == "kiss":
        n "Мягкие прохладные губы невесомо прошлись по её, оставляя легкий поцелуй. Каэль тихо выходнул:" (show_side="none", show_kind="speech")

        show kael sad at kael_right
        ka "Я очень переживал за тебя." (show_side="right", show_kind="speech")
        hide kael
        show kael thinking at kael_right
        ka "Никогда себя не прощу." (show_side="right", show_kind="speech")
        hide kael

        show eveina normal at eveina_left
        ev "Ты ни в чём не виноват..." (show_side="left", show_kind="speech")
        hide eveina 
        show eveina intrigued at eveina_left
        ev "Но если все твои извинения выглядят так, то я готова их подыграть." (show_side="left", show_kind="speech")
        hide eveina 

        n "Каэль усмехнулся и снова припал к её губам. Осторожно. Как будто ещё не верил, что может прикасаться к ней вот так — всерьёз, по-настоящему." (show_side="none", show_kind="speech")
        n "Но стоило ей приоткрыть губы, как последние намёки на осторожность испарились. Он жадно втянул её дыхание, язык скользнул внутрь, нащупывая, пробуя, впиваясь. Его руки обхватили её лицо, затем переместились к затылку и плечам." (show_side="none", show_kind="speech")
        n "Эвейна сдавленно всхлипнула в поцелуй, прижимаясь к нему грудью, чувствуя, как тело откликается каждой клеткой. Её бедра подались ему навстречу, желая вытянуть из него больше желания." (show_side="none", show_kind="speech")
        n "Каэль застонал, низко, срываясь на хрип. Он разомкнул губы, но не отступил — лишь перевёл дыхание и, закрыв глаза, снова впился в неё с новой жадностью, как будто тонул и она — его воздух." (show_side="none", show_kind="speech")
        n "Его ладони скользнули по её спине, вниз к талии, притягивая ближе, сильнее. Их тела почти слились. Дыхание смешалось. Он был слишком близко. Слишком нужен." (show_side="none", show_kind="speech")
        n "Но в какой-то момент Каэль нехотя оторвался, как будто возвращая себе контроль. Его лоб уткнулся в её лоб, дыхание сбивалось, голос сорвался в шепот:" (show_side="none", show_kind="speech")
        
        show kael serious at kael_right
        ka "Думаю, тебе стоит пойти отдохнуть." (show_side="right", show_kind="speech")
        ka "Иначе боюсь, что не смогу тебя отпустить." (show_side="right", show_kind="speech")
        hide kael

        n "Он коснулся её щеки, будто извиняясь, и, наконец, сделал шаг назад, позволяя ей выдохнуть." (show_side="none", show_kind="speech")

        show eveina intrigued at eveina_left
        ev "А всё так хорошо начиналось." (show_side="left", show_kind="speech")
        hide eveina 
        
        n "Эвейна улыбнулась, заметив ухмылку на его лице, и развернулась к креслу, забирая сумку." (show_side="none", show_kind="speech")

        show kael thinking at kael_right
        ka "Если захочешь продолжить — приходи." (show_side="right", show_kind="speech")
        hide kael

        n "Эвейна задержалась у двери, ответив коротким кивком." (show_side="none", show_kind="speech")

        show eveina thinking at eveina_left
        ev_thought "Это он про задачу Идентики или...?" (show_side="left", show_kind="thought")
        hide eveina

    if result == "leave":
        n "На его лице проскользнула тень печали." (show_side="none", show_kind="speech")
        show kael sad at kael_right
        ka "Мне очень жаль, что так вышло." (show_side="right", show_kind="speech")
        hide kael
        show kael thinking at kael_right
        ka "Никогда себя не прощу." (show_side="right", show_kind="speech")
        hide kael

        n "Эвейна взяла его ладони в свои и крепко сжала, смотря прямо в глаза." (show_side="none", show_kind="speech")

        show eveina normal at eveina_left
        ev "Каэль, в этом нет твоей вины..." (show_side="left", show_kind="speech")
        hide eveina 
        show eveina intrigued at eveina_left
        ev "Но мы можем всё исправить, если эта модель заработает." (show_side="left", show_kind="speech")
        hide eveina 

        n "Каэль кивнул, после чего махнул подбородком на дверь, намекая, что эмоциональных сцен с него сегодня хватит, и ей пора. Эвейна не смогла сдержать улыбку, отпуская его руки и делая шаг назад." (show_side="none", show_kind="speech")

    show eveina smile at eveina_left
    ev "Спасибо, что помогаешь." (show_side="left", show_kind="speech")
    hide eveina

    show kael normal at kael_right
    ka "Не надо так говорить." (show_side="right", show_kind="speech")
    hide kael
    show kael smile at kael_right
    ka "А то ещё решу, что становлюсь слишком мягким." (show_side="right", show_kind="speech")
    hide kael

    n "Она вышла, едва заметно улыбаясь." (show_side="none", show_kind="speech")

    jump scene_8_5
