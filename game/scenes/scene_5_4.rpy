label scene_5_4:
    $ previous_scene = "scene_5_3"
    $ next_scene = "scene_5_5"
    $ current_scene = "scene_5_4"
    call fade_to_black(1.2, 0.8)
    scene bg lecture_hall at bg_fullscreen with dissolve

    n "Лекционный зал был почти полон, если не считать нескольких мест справа от Эвейны, которая сидела в последних рядах с планшетом в руках, но в этот раз не делала заметок." (show_side="none", show_kind="speech")
    n "Напрочь забыв, где и зачем находится, она была поглощена рассказом Аурелиана Вирта." (show_side="none", show_kind="speech")

    show virt serious at virt_right
    vi "У народа Илейн нет централизованного государства." (show_side="right", show_kind="speech")
    vi "Их общество основано на согласии и симбиозе." (show_side="right", show_kind="speech")
    vi "Они живут малыми группами, каждая из которых — самостоятельная единица." (show_side="right", show_kind="speech")
    vi "В качестве связующего звена между группами выступает Ил'Мари, играющий роль и защитника, и хранителя культуры народов, и судьи в межгрупповых спорах." (show_side="right", show_kind="speech")
    vi "В культуре Илейн он представляется умудрённым опытом старцем, чья мудрость и справедливость не подвергается сомнению." (show_side="right", show_kind="speech")
    vi "Интересен он тем, что на вопрос, как выбирают человека на этот пост, Илейн отвечают что-то вроде: {i}«Мы не выбираем, он просто есть.»{/i}" (show_side="right", show_kind="speech")
    vi "Мы интерпетируем так: титул Ил'Мари передаётся по наследству и, скорее всего, похож по своему духу на шаманов из древних культур." (show_side="right", show_kind="speech")
    vi "Впрочем, не исключаем и то, что Ил'Мари — это мифический персонаж, часть духовных верований, неразрывно связанных с культурой Илейн." (show_side="right", show_kind="speech")
    hide virt

    n "На экране за спиной Вирта мелькали изображения: полупрозрачные сферы среди мха, круглые, почти органические формы жилищ, вплетённые в корни деревьев, поляны с выжженной солнцем травой и фигурами из камней, выложенными на ней." (show_side="none", show_kind="speech")

    show virt serious at virt_right
    vi "Ближайшее к нам поселение Илейн находится в сорока километрах от Академии." (show_side="right", show_kind="speech")
    vi "Добраться туда пешком можно за день." (show_side="right", show_kind="speech")
    hide virt
    show virt thinking at virt_right
    vi "И да, чтобы вы не пытались: проход туда запрещён, а граница охраняется с обеих сторон." (show_side="right", show_kind="speech")
    hide virt

    n "Отголосок любопытства ударил девушку в виски." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev_thought "Сорок километров. Лес. Таинственное биополе Илейн." (show_side="left", show_kind="thought")
    hide eveina
    show eveina intrigued at eveina_left
    ev_thought "Звучит как инструкция к невероятной авантюре." (show_side="left", show_kind="thought")
    hide eveina

    show virt serious at virt_right
    vi "Все здания на этой планете, включая Академию, были выращены Илейн." (show_side="right", show_kind="speech")
    vi "Со своей стороны в рамках соглашения мы обязались соблюдать определённые условия:" (show_side="right", show_kind="speech")
    vi "Отказ от технотранспорта на всей территории материка и прибрежных вод, не считая космопорта." (show_side="right", show_kind="speech")
    vi "Полный запрет на добычу чего-либо, земледелие и животноводство." (show_side="right", show_kind="speech")
    vi "И абсолютное невмешательство в лесные зоны." (show_side="right", show_kind="speech")
    hide virt

    n "Он сделал паузу. На экране вспыхнула новая проекция — план Академии с выделенной зоной ограниченного доступа." (show_side="none", show_kind="speech")
    n "За ней — широкие лесные массивы, где начинался «неприкосновенный периметр»." (show_side="none", show_kind="speech")

    show virt serious at virt_right
    vi "Всё продовольствие мы получаем с других планет. Или из теплиц Академии." (show_side="right", show_kind="speech")
    vi "Илейн называют это «бережным следом»." (show_side="right", show_kind="speech")
    hide virt
    show virt thinking at virt_right
    vi "Жить, не оставляя следов, которые нельзя стереть." (show_side="right", show_kind="speech")
    hide virt

    n "Зал был тише обычного. Даже те, кто обычно отвлекался, сейчас слушали внимательно. Загадка существования Илейн терзала умы каждого студента." (show_side="none", show_kind="speech")
    n "Кто они? Какие они? Насколько они отличаются от нас? Каждый посещающий эту планету задавался подобными вопросами, и мало кто находил на них ответы." (show_side="none", show_kind="speech")
    n "Слова Вирта будто растворялись в воздухе, оседая внутри умов слушателей." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev_thought "Как много людей может сказать, что помнят своё общение с Илейн?" (show_side="left", show_kind="thought")
    ev_thought "Никогда об этом не слышала... О них вообще обидно мало информации, даже в Академии. Впрочем, неудивительно." (show_side="left", show_kind="thought")
    ev_thought "Они добровольно поделились с нами практически всем, что имели: своей планетой, своими технологиями, своими знаниями." (show_side="left", show_kind="thought")
    ev_thought "А мы...что ещё мы взяли?\nИ какой ценой?" (show_side="left", show_kind="thought")
    hide eveina

    n "Размышления Эвейны прервал уверенный шаг, эхом отдавшийся в стенах лектория. Все взгляды разом обратились к его источнику." (show_side="none", show_kind="speech")

    show silas normal at silas_right
    si "Здравствуйте, профессор Вирт. Меня зовут Сайлас Вайс." (show_side="right", show_kind="speech")
    si "Извините, что так врываюсь в ваш монолог, но ректор сказал отправиться прямиком сюда." (show_side="right", show_kind="speech")
    si "Вас должны были уведомить о моём вынужденном опоздании." (show_side="right", show_kind="speech")
    hide silas

    show virt serious at virt_right
    vi "Добро пожаловать, мистер Вайс." (show_side="right", show_kind="speech")
    vi "Да, я получил уведомление о том, что вас стоит ожидать. Занимайте свободное место." (show_side="right", show_kind="speech")
    hide virt

    n "На этих словах многие девушки начали оглядываться вокруг. И по залу пронесся тихий разочарованный вздох, когда обнаружилось, что свободные места есть только рядом с Эвейной." (show_side="none", show_kind="speech")

    show eveina eyebrow at eveina_left
    ev_thought "Парень, да ты сюда зайти не успел, а уже нарасхват..." (show_side="left", show_kind="thought")
    ev_thought "Как бы меня случайно не затоптали в погоне за ценным трофеем." (show_side="left", show_kind="thought")
    hide eveina

    n "Следуя какому-то странному порыву, девушка положила сумку на соседнее сиденье и подняла взгляд в поисках приближающегося парня." (show_side="none", show_kind="speech")
    n "Сайлас оказался ближе, чем ей хотелось бы, и сейчас с интересом смотрел на руку, которую она так и не успела убрать с сумки." (show_side="none", show_kind="speech")

    show silas eyebrow at silas_right
    si "Здесь свободно? Могу я сесть?" (show_side="right", show_kind="speech")
    hide silas

    n "Его вежливая просьба, подкреплённая открытой улыбкой застали Эвейну врасплох, вынудив неловко опустить глаза." (show_side="none", show_kind="speech")
    n "Она молча убрала сумку, стараясь на него не смотреть, и краем уха услышала второй вздох, разнесшийся по лекторию — на этот раз раздраженный." (show_side="none", show_kind="speech")

    show eveina eyeroll at eveina_left
    ev_thought "Сайлас, ещё одно неосторожное движение, и ты подпишешь мне смертный приговор." (show_side="left", show_kind="thought")
    hide eveina

    show virt serious at virt_right
    vi "Что ж, извините за паузу. Давайте продолжим..." (show_side="right", show_kind="speech")
    hide virt

    n "Перед глазами у Эвейны тут же возникла ладонь, заставив её вздрогнуть." (show_side="none", show_kind="speech")

    show silas normal at silas_right
    si "О, прости..." (show_side="right", show_kind="speech")
    hide silas
    show silas smile at silas_right
    si "Сайлас Вайс." (show_side="right", show_kind="speech")
    hide silas

    n "Она осторожно покосилась на ладонь, а потом в зал. И лишь убедившись, что большинство продолжили слушать лекцию, осторожно сжала её в своей руке." (show_side="none", show_kind="speech")

    show eveina normal at eveina_left
    ev "Эвейна Хейла." (show_side="left", show_kind="speech")
    hide eveina

    show silas smile at silas_right
    si "Рад знакомству, Эвейна." (show_side="right", show_kind="speech")
    hide silas

    n "Девушка не ответила, продолжая со слегка наигранным усердием слушать лекцию профессора." (show_side="none", show_kind="speech")

    show eveina normal at eveina_left
    ev_thought "Сайлас вроде милый, и всё такое..." (show_side="left", show_kind="thought")
    hide eveina
    show eveina eyeroll at eveina_left
    ev_thought "Но вот эти взгляды из аудитории совсем не милые." (show_side="left", show_kind="thought")
    ev_thought "Так что ради всего святого, пусть сидит молча." (show_side="left", show_kind="thought")
    hide eveina

    n "Будто считав её мысли, Сайлас закинул ногу себе на колено, положил планшет сверху и стал в нём вести какие-то заметки." (show_side="none", show_kind="speech")
    n "Минуту спустя любопытство Эвейны взяло вверх и она взглянула на его экран, наблюдая, как утончённые пальцы изящно летают по нему, набирая текст." (show_side="none", show_kind="speech")

    show eveina normal at eveina_left
    ev_thought "Ух ты, заметки по лекции." (show_side="left", show_kind="thought")
    ev_thought "Кто бы мог подумать..." (show_side="left", show_kind="thought")
    hide eveina

    n "Она ещё некоторое время поглядывала в планшет, убеждаясь, что он фиксирует чуть ли не каждое слово." (show_side="none", show_kind="speech")
    n "Пока не покосилась туда в очередной раз и не увидела там выведеную в конце абзаца фразу: {i}«Я не пропустил ничего интересного?»{/i}" (show_side="none", show_kind="speech")
    n "Эвейна удивлённо подняла на Сайласа глаза, встретившись с его вопросительным взглядом. Парень кинвул на планшет, потом на Вирта и снова взглянул на неё с улыбкой." (show_side="none", show_kind="speech")

    show silas eyebrow at silas_right
    si "..?" (show_side="right", show_kind="speech")
    hide silas

    n "Чувствуя, как щеки покрывает румянец из-за того, что её застали за подсматриванием, девушка покачала головой и виновато улыбнулась." (show_side="none", show_kind="speech")

    show eveina smile at eveina_left
    ev "Извини." (show_side="left", show_kind="speech")
    hide eveina

    show silas smile at silas_right
    si "Я не против." (show_side="right", show_kind="speech")
    hide silas

    n "Его ослепительная улыбка вызвала волну смущения, и она поспешно отвернулась, возвращая всё внимание к лекции об Илейн." (show_side="none", show_kind="speech")
    n "Когда та подошла к концу, Вирт выключил проекцию, кивнул студентам и удалился, как всегда — бесшумно." (show_side="none", show_kind="speech")
    n "Эвейна поспешно поднялась и, махнув на прощание новому знакомому, вылетела в коридор." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev_thought "Ещё не хватало, чтоб кто-то увидел, как мы вместе уходим с лекции..." (show_side="left", show_kind="thought")
    hide eveina
    show eveina annoyed at eveina_left
    ev_thought "И без этого достаточно поводов нарисовать на моей спине мишень!" (show_side="left", show_kind="thought")
    hide eveina

    jump scene_5_5
