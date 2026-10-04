label scene_3_4:
    $ previous_scene = "scene_3_3"
    $ next_scene = "scene_3_5"
    $ current_scene = "scene_3_4"

    # =========================================================
    # СЦЕНА 3_4 — «ЛЕКЦИЯ ВИРТА: ИЛ'МАРИ»
    # Структура: Эвейна отвлекается → Вирт замечает → она возвращается
    #            → Ил'Мари → мысль об Эриане → появление Сайласа
    #            → три вопроса об этике → Сайрен → разговор после лекции
    # Ил'Мари — из оригинальной scene_5_4.
    # Три вопроса и финал — из оригинальной scene_3_7, почти дословно.
    # =========================================================

    call fade_to_black(1.2, 0.8)
    scene bg lecture_hall at bg_fullscreen with dissolve
    # play music "bgm/lecture_background.ogg" fadein 2.0

    n "Лекционный зал был почти полон. Эвейна сидела в середине амфитеатра с планшетом в руках — но заметок не делала." (show_side="none", show_kind="speech")
    n "На экране за Виртом проецировались архивные материалы: первые визиты учёных на Ил'Эйн, совместные исследования, начало строительства Академии." (show_side="none", show_kind="speech")

    show virt serious at virt_right
    vi "Поначалу контакт с народом Илейн был фрагментарным." (show_side="right", show_kind="speech")
    vi "Их восприятие времени, коммуникации, даже топологии пространства отличались от наших." (show_side="right", show_kind="speech")
    hide virt
    show virt thinking at virt_right
    vi "Однако со временем... началось взаимопонимание." (show_side="right", show_kind="speech")
    hide virt
    show virt serious at virt_right
    vi "Особенно после того, как был зафиксирован первый случай стабилизации нейроотклонения у пациента, соприкасавшегося с Илейн." (show_side="right", show_kind="speech")
    hide virt

    n "Эвейна смотрела на слайды, но мысли её были где-то в другом месте." (show_side="none", show_kind="speech")
    n "Вчерашний вечер прокручивался снова — незаправленная кровать, 850 и 849, Вайскорп, тихий вопрос Леи, который никто не закрыл." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev_thought "«Этика стала переменной»." (show_side="left", show_kind="thought")
    hide eveina
    show eveina eyebrow at eveina_left
    ev_thought "Что именно он имел в виду?" (show_side="left", show_kind="thought")
    hide eveina

    n "Краем глаза она поймала взгляд Вирта. Он видел, что она его не слушает." (show_side="none", show_kind="speech")
    n "Она возвратилась." (show_side="none", show_kind="speech")

    show virt serious at virt_right
    vi "У народа Илейн нет централизованного государства." (show_side="right", show_kind="speech")
    vi "Их общество основано на согласии и симбиозе." (show_side="right", show_kind="speech")
    vi "Они живут малыми группами, каждая из которых — самостоятельная единица." (show_side="right", show_kind="speech")
    hide virt
    show virt normal at virt_right
    vi "В качестве связующего звена между группами выступает Ил'Мари." (show_side="right", show_kind="speech")
    vi "Он играет роль и защитника, и хранителя культуры, и судьи в межгрупповых спорах." (show_side="right", show_kind="speech")
    hide virt
    show virt thinking at virt_right
    vi "В культуре Илейн он представляется умудрённым опытом старцем, чья мудрость и справедливость не подвергается сомнению." (show_side="right", show_kind="speech")
    hide virt
    show virt serious at virt_right
    vi "Интересен он тем, что на вопрос — как выбирают человека на этот пост — Илейн отвечают что-то вроде:" (show_side="right", show_kind="speech")
    vi "{i}«Мы не выбираем. Он просто есть.»{/i}" (show_side="right", show_kind="speech")
    hide virt
    show virt thinking at virt_right
    vi "Мы интерпретируем это так: титул Ил'Мари передаётся по наследству и, скорее всего, похож по своему духу на шаманов из древних культур." (show_side="right", show_kind="speech")
    vi "Впрочем, не исключаем и то, что Ил'Мари — это мифический персонаж, часть духовных верований, неразрывно связанных с культурой Илейн." (show_side="right", show_kind="speech")
    hide virt

    show virt serious at virt_right
    vi "Ближайшее к нам поселение Илейн находится в сорока километрах от Академии." (show_side="right", show_kind="speech")
    vi "Добраться туда пешком можно за день." (show_side="right", show_kind="speech")
    hide virt
    show virt thinking at virt_right
    vi "И да, чтобы вы не пытались — проход туда запрещён, а граница охраняется с обеих сторон." (show_side="right", show_kind="speech")
    hide virt

    show eveina intrigued at eveina_left
    ev_thought "Сорок километров. Лес. Таинственное биополе Илейн." (show_side="left", show_kind="thought")
    hide eveina
    show eveina thinking at eveina_left
    ev_thought "Звучит как инструкция к невероятной авантюре." (show_side="left", show_kind="thought")
    hide eveina

    show virt serious at virt_right
    vi "Все здания на этой планете, включая Академию, были выращены Илейн." (show_side="right", show_kind="speech")
    vi "Со своей стороны, в рамках соглашения мы обязались соблюдать определённые условия." (show_side="right", show_kind="speech")
    vi "Отказ от технотранспорта на всей территории материка и прибрежных вод, не считая космопорта." (show_side="right", show_kind="speech")
    vi "Полный запрет на добычу чего-либо, земледелие и животноводство." (show_side="right", show_kind="speech")
    vi "И абсолютное невмешательство в лесные зоны." (show_side="right", show_kind="speech")
    hide virt

    n "Он сделал паузу. На экране вспыхнула новая проекция — план Академии с выделенной зоной ограниченного доступа." (show_side="none", show_kind="speech")

    show virt serious at virt_right
    vi "Всё продовольствие мы получаем с других планет. Или из теплиц Академии." (show_side="right", show_kind="speech")
    vi "Илейн называют это «бережным следом»." (show_side="right", show_kind="speech")
    hide virt
    show virt thinking at virt_right
    vi "Жить, не оставляя следов, которые нельзя стереть." (show_side="right", show_kind="speech")
    hide virt

    n "Зал был тише обычного." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev_thought "Они поделились с нами практически всем: своей планетой, своими технологиями, своими знаниями." (show_side="left", show_kind="thought")
    hide eveina
    show eveina eyebrow at eveina_left
    ev_thought "А мы — что ещё мы взяли? И какой ценой?" (show_side="left", show_kind="thought")
    hide eveina

    # --- Три вопроса ---

    n "Внутри боролись два импульса: не привлекать к себе внимание — или спросить, пользуясь подходящей темой." (show_side="none", show_kind="speech")
    n "Она закусила губу. Потом встала." (show_side="none", show_kind="speech")

    show eveina normal at eveina_left
    ev "Профессор, а каковы были этические основания для начала этих исследований?" (show_side="left", show_kind="speech")
    ev "Использование народа Илейн как биологического ресурса для экспериментов…" (show_side="left", show_kind="speech")
    hide eveina
    show eveina eyebrow at eveina_left
    ev "Это ведь не совсем добровольное сотрудничество, не так ли?" (show_side="left", show_kind="speech")
    hide eveina

    n "В лектории повисла неблагодарная тишина. Студенты обменивались взглядами." (show_side="none", show_kind="speech")
    n "Профессор Вирт замер. Его рука, только что указывавшая на график, медленно опустилась." (show_side="none", show_kind="speech")
    n "Он смотрел на Эвейну несколько секунд. В этом взгляде не было раздражения. Скорее — удивление, будто в этом зале никто никогда такими вопросами не задавался." (show_side="none", show_kind="speech")

    show virt thinking at virt_right
    vi "Этические принципы…" (show_side="right", show_kind="speech")
    hide virt

    n "Пауза была почти болезненной. В ней чувствовалась история, которую нельзя было вместить в один ответ." (show_side="none", show_kind="speech")

    show virt serious at virt_right
    vi "…подразумевают согласие." (show_side="right", show_kind="speech")
    vi "Илейн — раса, чья культура и восприятие отличны от наших. Соглашения с ними достигались иначе. Но они были." (show_side="right", show_kind="speech")
    vi "Их влияние на нейрополя планеты — бесценный дар. И Академия стремится с уважением использовать его во благо." (show_side="right", show_kind="speech")
    hide virt

    n "Эвейна кивнула. И не сдалась." (show_side="none", show_kind="speech")

    show eveina normal at eveina_left
    ev "Простите, профессор. Но если это действительно соглашение — разве оно не должно быть взаимным?" (show_side="left", show_kind="speech")
    hide eveina
    show eveina eyebrow at eveina_left
    ev "Что люди отдают народу Илейн взамен? Что получили они?" (show_side="left", show_kind="speech")
    hide eveina

    n "Вирт пристально смотрел на неё, словно искал причины, побудившие её встать." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev_thought "Дайте угадаю, этот взгляд обещает мне незабываемую беседу после лекции?" (show_side="left", show_kind="thought")
    hide eveina

    n "Наконец его глаза оторвались от неё и задумчиво заблуждали по аудитории." (show_side="none", show_kind="speech")

    show virt serious at virt_right
    vi "Это не так просто. Не всё, что имеет ценность для нас, имеет ценность для них." (show_side="right", show_kind="speech")
    hide virt
    show virt thinking at virt_right
    vi "Мы… пытались. Академия предоставляла ресурсы. Поддерживала инфраструктуру. Искала разные подходы." (show_side="right", show_kind="speech")
    hide virt

    n "Он поморщился, тяжело вздохнул и сжал пальцами переносицу." (show_side="none", show_kind="speech")

    show virt serious at virt_right
    vi "Но если вы спрашиваете, равны ли эти обмены…" (show_side="right", show_kind="speech")
    vi "Вопрос открыт." (show_side="right", show_kind="speech")
    hide virt

    show eveina normal at eveina_left
    ev "И последний вопрос." (show_side="left", show_kind="speech")
    hide eveina

    n "Под тяжёлым взглядом профессора Эвейна набрала в грудь побольше воздуха." (show_side="none", show_kind="speech")

    show eveina eyebrow at eveina_left
    ev "Как считаете — в чём причина натянутых отношений с илейн? В изначально неравных условиях или же в несоблюдении тех договорённостей, что стали основой сотрудничества?" (show_side="left", show_kind="speech")
    hide eveina

    show eveina upset thinking at eveina_left
    ev_thought "Ну вот. Одним вопросом обвинила Академию в текущем конфликте." (show_side="left", show_kind="thought")
    ev_thought "Мне этого точно не забудут." (show_side="left", show_kind="thought")
    hide eveina

    n "По залу пронёсся тихий вздох. Эвейне на мгновение даже показалось, что губы Вирта дрогнули в улыбке. Показалось, конечно." (show_side="none", show_kind="speech")

    show virt serious at virt_right
    vi "Я бы не ставил вопрос таким образом, мисс Хейла." (show_side="right", show_kind="speech")
    vi "Но если отвечать на него..." (show_side="right", show_kind="speech")
    vi "Этот путь был усеян человеческими ошибками. Такова наша природа." (show_side="right", show_kind="speech")
    hide virt

    n "Ответ звучал иначе — не как лекция. Как исповедь." (show_side="none", show_kind="speech")
    n "И в наступившей тишине Сайрен, не упустив момент, процедила сквозь зубы — чтобы слышала вся аудитория:" (show_side="none", show_kind="speech")

    show sairen angry at sairen_right
    sa "Ну конечно. Выскочка с периферии решила покритиковать методы Академии." (show_side="right", show_kind="speech")
    hide sairen

    show eveina angry at eveina_left
    ev_thought "Она вообще умеет держать язык за зубами?" (show_side="left", show_kind="thought")
    hide eveina

    n "Кто-то хихикнул, но быстро затих. Профессор не вмешался — только смотрел на Эвейну. И в его глазах появилось то, чего не было раньше: печаль. И, быть может, беспокойство." (show_side="none", show_kind="speech")
    n "Девушка опустила глаза. Ответ Вирта звучал слишком неоднозначно. Словно нервный вдох, прорвавшийся сквозь заученную речь." (show_side="none", show_kind="speech")
    n "До конца лекции он говорил без обычной включённости. На последнем слайде отключил проекцию." (show_side="none", show_kind="speech")

    show virt serious at virt_right
    vi "На этом всё. Если есть вопросы — подойдите после." (show_side="right", show_kind="speech")
    hide virt

    n "Студенты начали расходиться. Эвейна подхватила планшет и неспешно направилась к выходу." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev_thought "Три... Два... О..." (show_side="left", show_kind="thought")
    hide eveina

    n "Вирт, собирая вещи со стола, медленно поднял на неё взгляд." (show_side="none", show_kind="speech")

    show virt normal at virt_right
    vi "Мисс Хейла, на минуту." (show_side="right", show_kind="speech")
    hide virt

    show eveina eyeroll at eveina_left
    ev_thought "Десять очков Гриффиндору..." (show_side="left", show_kind="thought")
    hide eveina

    n "Эвейна приблизилась, провожая взглядом последних студентов у выхода." (show_side="none", show_kind="speech")
    n "Вирт взглянул на неё задумчиво — словно пытался прочесть что-то в её лице." (show_side="none", show_kind="speech")

    show virt normal at virt_right
    vi "Откуда у вас возник этот вопрос? Вы ведь ещё только начинаете курс." (show_side="right", show_kind="speech")
    hide virt

    n "Она выдержала паузу, прежде чем нацепить на лицо невинную улыбку." (show_side="none", show_kind="speech")

    show eveina smile at eveina_left
    ev "Просто любопытство, профессор. Я хочу понять... Почему тут всё так устроено." (show_side="left", show_kind="speech")
    hide eveina

    n "Вирт устало вздохнул — неудовлетворённый ответом. Медленно произнёс, аккуратно подбирая слова:" (show_side="none", show_kind="speech")

    show virt thinking at virt_right
    vi "Понимание — сложная валюта, мисс Хейла. Иногда за него приходится платить." (show_side="right", show_kind="speech")
    hide virt

    n "Он отступил, жестом отпуская её. И добавил чуть мягче:" (show_side="none", show_kind="speech")

    show virt normal at virt_right
    vi "Хорошего вечера." (show_side="right", show_kind="speech")
    hide virt

    n "Уходя, она спиной чувствовала его взгляд. С каждым шагом в ней крепло чувство: её вопросы сдвинули что-то важное, хрупкое." (show_side="none", show_kind="speech")

    show eveina thinking at eveina_left
    ev_thought "Что же так задело вас в этом вопросе, профессор?" (show_side="left", show_kind="thought")
    hide eveina

    jump scene_3_5
