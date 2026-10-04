label scene_8_1:
    $ previous_scene = "scene_7_10"
    $ next_scene = "scene_8_2"
    $ current_scene = "scene_8_1"
    call fade_to_black(1.2, 0.8)
    scene bg shuttle at bg_fullscreen with dissolve

    n "Весь обратный путь прошёл в почти полной тишине. Вирт продолжал работать за планшетом. Эвейна лежала в капсуле, свернувшись в позе эмбриона." (show_side="none", show_kind="speech")

    show eveina normal tshirt at eveina_left
    ev_thought "А стоило ли вообще улетать? Может, к чёрту эту Академию, просто побуду с отцом до его конца?" (show_side="left", show_kind="thought")
    ev_thought "Нет. Он не позволит вернуться. Я должна найти решение. Должна вылечить его." (show_side="left", show_kind="thought")
    hide eveina
    show eveina upset tshirt at eveina_left
    ev_thought "А у меня получится?" (show_side="left", show_kind="thought")
    ev_thought "А если да — как далеко мне придётся зайти?" (show_side="left", show_kind="thought")
    ev_thought "Снова обманывать? Делать больно хорошим людям?" (show_side="left", show_kind="thought")
    hide eveina

    n "Она кинула быстрый осторожный взгляд на Вирта." (show_side="none", show_kind="speech")

    show eveina thinking tshirt at eveina_left
    ev_thought "Хочу ли я этого? Способна ли?" (show_side="left", show_kind="thought")
    hide eveina

    n "Мысли лениво плавали в голове, ни одна не оставалась там надолго. Девушка смотрела перед собой невидящим взглядом и потому не сразу заметила, как над ней выросла тень." (show_side="none", show_kind="speech")

    show virt normal jacket at virt_right
    vi "Эвейна, думаю, нам стоит поговорить до прибытия в Академию." (show_side="right", show_kind="speech")
    hide virt

    show eveina thinking tshirt at eveina_left
    ev_thought "Снова на «ты». Интересная у него биполярочка." (show_side="left", show_kind="thought")
    hide eveina

    n "Эвейна неспеша села в кресле, подтянула колени к груди, взглянув на него потухшим взглядом." (show_side="none", show_kind="speech")

    show eveina normal tshirt at eveina_left
    ev "Ну давай поговорим, Аурелиан." (show_side="left", show_kind="speech")
    hide eveina

    n "Вирт пропустил мимо ушей неформальное обращение и продолжил." (show_side="none", show_kind="speech")

    show virt thinking jacket at virt_right
    vi "Ты прилетела в Академию, думая, что найдёшь лечение для отца?" (show_side="right", show_kind="speech")
    hide virt

    show eveina normal tshirt at eveina_left
    ev "Да. Терапию, связи, исследования, экспериментальные препараты. Хоть что-то." (show_side="left", show_kind="speech")
    hide eveina

    show virt eyebrow jacket at virt_right
    vi "Почему не обратилась за помощью сразу ко мне? Почему отталкивала любые попытки помочь?" (show_side="right", show_kind="speech")
    hide virt

    show eveina normal tshirt at eveina_left
    ev "Мне было... неловко. Нет, стыдно." (show_side="left", show_kind="speech")
    hide eveina

    show virt eyebrow jacket at virt_right
    vi "Стыдно? Это из-за той книги?" (show_side="right", show_kind="speech")
    hide virt

    show eveina normal tshirt at eveina_left
    ev "Не только." (show_side="left", show_kind="speech")
    hide eveina

    show virt serious jacket at virt_right
    vi "Не только?" (show_side="right", show_kind="speech")
    hide virt

    n "Не дождавшись ответа, мужчина устало потёр переносицу и тряхнул головой, откидывая упавшие на лоб пряди." (show_side="none", show_kind="speech")

    show virt normal jacket at virt_right
    vi "Ладно, с этим потом..." (show_side="right", show_kind="speech")
    vi "Что ты искала в моём планшете? В книге из Архива?" (show_side="right", show_kind="speech")
    hide virt

    show eveina normal tshirt at eveina_left
    ev "Связи с препаратом NR-Δ3." (show_side="left", show_kind="speech")
    hide eveina

    show virt serious jacket at virt_right
    vi "Откуда ты о нём знаешь?" (show_side="right", show_kind="speech")
    hide virt

    n "Эвейна не ответила." (show_side="none", show_kind="speech")

    show virt serious jacket at virt_right
    vi "Почему ты искала информацию о нём в моём планшете?" (show_side="right", show_kind="speech")
    hide virt

    show eveina normal tshirt at eveina_left
    ev "Я не искала. Я только подумала, что это стоило бы сделать. Но не успела." (show_side="left", show_kind="speech")
    hide eveina

    show virt serious jacket at virt_right
    vi "Почему?" (show_side="right", show_kind="speech")
    hide virt

    show eveina eyeroll tshirt at eveina_left
    ev "Ты, вероятно, как-то связан с его создателем." (show_side="left", show_kind="speech")
    hide eveina

    n "Если бы она в тот момент посмотрела на его лицо, многое бы прочла в его глазах. Но она не смотрела." (show_side="none", show_kind="speech")

    show eveina normal tshirt at eveina_left
    ev "Думала, что ты можешь что-то знать. Где он, куда пропал. Его последние работы. Может быть, даже его контакты." (show_side="left", show_kind="speech")
    hide eveina

    n "Повисла тишина. Для Эвейны — апатичная, для Вирта — напряжённая. Он резко встал, отошёл, потом вернулся, сунув ей под нос планшет." (show_side="none", show_kind="speech")

    show virt serious jacket at virt_right
    vi "Ищи." (show_side="right", show_kind="speech")
    hide virt

    n "Эвейна с трудом всплывала из вод меланхолии, неторопливо осознавая, что он ей предложил." (show_side="none", show_kind="speech")

    show eveina eyebrow tshirt at eveina_left
    ev "Что, прости?" (show_side="left", show_kind="speech")
    hide eveina

    show virt serious jacket at virt_right
    vi "Ищи то, что хотела найти." (show_side="right", show_kind="speech")
    hide virt
    show virt normal jacket at virt_right
    vi "Я же сказал, если могу помочь — помогу." (show_side="right", show_kind="speech")
    hide virt

    n "Она медленно подняла на него непонимающий взгляд." (show_side="none", show_kind="speech")

    show eveina eyebrow tshirt at eveina_left
    ev "Не буду." (show_side="left", show_kind="speech")
    hide eveina

    show virt serious jacket at virt_right
    vi "Нет, будешь." (show_side="right", show_kind="speech")
    hide virt

    n "Он твёрдо толкнул её в плечо, устраиваясь рядом в кресле, и разблокировал планшет." (show_side="none", show_kind="speech")

    show virt normal jacket at virt_right
    vi "С чего начнём? Полагаю, с личной почты?" (show_side="right", show_kind="speech")
    hide virt

    n "Эвейна сидела тихо, как мышь, боявшаяся спугнуть спящего кота. Она искренне не верила в то, что происходило." (show_side="none", show_kind="speech")
    n "Аурелиан открывал одно приложение за другим, листал переписки, просматривал рабочие файлы и комментировал. Просто, спокойно, как будто читал лекцию." (show_side="none", show_kind="speech")
    n "Они просидели так много часов, профессор показывал и рассказывал, девушка слушала, иногда задавая осторожные вопросы." (show_side="none", show_kind="speech")
    n "Наконец, она расслабилась окончательно и чуть не зевнула. Вирт взглянул на неё с легкой улыбкой." (show_side="none", show_kind="speech")

    show virt normal jacket at virt_right
    vi "Думаю, на сегодня хватит." (show_side="right", show_kind="speech")
    hide virt

    n "Он убрал планшет и повернулся к ней, поджав под себя одну ногу. Так непривычно было видеть его таким: простым, почти домашним и очень близким." (show_side="none", show_kind="speech")

    show virt serious jacket at virt_right
    vi "Эвейна, не знаю, откуда у тебя информация о NR-Δ3. Но это не то, что поможет твоему отцу." (show_side="right", show_kind="speech")
    hide virt

    show eveina eyebrow tshirt at eveina_left
    ev "А что поможет?" (show_side="left", show_kind="speech")
    hide eveina

    n "Он молчал. Всё в нём — мрачный взгляд, напряженные плечи, сжатые в кулак руки говорили — ничего. Но он просто не позволял себе это сказать вслух." (show_side="none", show_kind="speech")

    show eveina normal tshirt at eveina_left
    ev "Я не сдамся, Аурелиан. Я должна найти решение." (show_side="left", show_kind="speech")
    hide eveina

    show virt normal jacket at virt_right
    vi "Тогда позволь мне тебе помочь." (show_side="right", show_kind="speech")
    hide virt

    n "После недолгой паузы она устало вздохнула и облокотила голову на его грудь. Её ладонь нашла его." (show_side="none", show_kind="speech")
    n "Эвейна мягко касалась кончиков его пальцев своими и наблюдала, как они едва двигались под её прикосновениями." (show_side="none", show_kind="speech")

    show eveina normal tshirt at eveina_left
    ev "Ладно." (show_side="left", show_kind="speech")
    hide eveina

    n "Аурелиан запустил себе пальцы в волосы, откидывая непослушные пряди, как делал всегда, размышляя о чём-то. Он мягко отодвинул девушку за плечи, заставив взглянуть ему в глаза." (show_side="none", show_kind="speech")

    show virt serious jacket at virt_right
    vi "Ты уверена, что хочешь вернуться в Академию?" (show_side="right", show_kind="speech")
    hide virt

    show eveina normal tshirt at eveina_left
    ev "У меня нет другого пути." (show_side="left", show_kind="speech")
    hide eveina

    show virt serious jacket at virt_right
    vi "Тогда нам понадобится помощь. И ресурсы." (show_side="right", show_kind="speech")
    vi "На этот раз ты готова довериться мне, Эвейна?" (show_side="right", show_kind="speech")
    hide virt

    n "Эвейна смотрела в его теплые усталые глаза и была готова доверить ему всю себя." (show_side="none", show_kind="speech")

    show eveina normal tshirt at eveina_left
    ev "Да." (show_side="left", show_kind="speech")
    hide eveina

    show virt thinking jacket at virt_right
    vi "Что ж, в таком случае... нам нужно установить границы." (show_side="right", show_kind="speech")
    hide virt

    n "Девушка напряглась, опустив голову. Она боялась его следующих слов, но понимала, что это необходимо. Он просто не может по-другому." (show_side="none", show_kind="speech")

    show virt thinking jacket at virt_right
    vi "Я — твой профессор, Эвейна. Мы не можем... Мы должны соблюдать правила Академии." (show_side="right", show_kind="speech")
    hide virt 
    show virt normal jacket at virt_right
    vi "Иначе это может создать... сложности. Ты понимаешь?" (show_side="right", show_kind="speech")
    hide virt

    n "Эвейна кивнула, не поднимая глаза. В ответ он сжал её пальцы в своей руке." (show_side="none", show_kind="speech")

    show virt thinking jacket at virt_right
    vi "И ты должна рассказать мне всё. Иначе я не буду знать, как нам действовать." (show_side="right", show_kind="speech")
    hide virt

    n "Эвейна молчала, взвешивая свои следующие слова." (show_side="none", show_kind="speech")

    show eveina thinking tshirt at eveina_left
    ev "Хорошо. Сейчас?" (show_side="left", show_kind="speech")
    hide eveina

    n "Вместо слов он снова притянул её к себе и сжал в крепких объятиях, медленно поглаживая по голове." (show_side="none", show_kind="speech")

    show virt normal jacket at virt_right
    vi "Думаю, сейчас тебе стоит отдохнуть. Мы вернёмся к этому, когда будешь готова." (show_side="right", show_kind="speech")
    hide virt

    n "Эвейна сильнее уткнулась в его грудь и вдохнула его запах. На глаза наворачивались слёзы от той заботы, теплоты и того, каким он был с ней сейчас, в это мгновение." (show_side="none", show_kind="speech")
    n "Он мягко коснулся губами её макушки." (show_side="none", show_kind="speech")

    show virt normal jacket at virt_right
    vi "Ложись спать. Завтра будет долгий день. Утром мы вернёмся в Академию." (show_side="right", show_kind="speech")
    hide virt

    jump scene_8_2
