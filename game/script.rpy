# script.rpy

# Определения персонажей
define ev = Character("Эвейна", color="#eac06f", who_style="kg_dialogue_name", what_style="kg_dialogue_text", window_style="kg_dialogue_window")
define er = Character("Эриан", color="#eac06f", who_style="kg_dialogue_name", what_style="kg_dialogue_text", window_style="kg_dialogue_window")
define ka = Character("Каэль", color="#eac06f", who_style="kg_dialogue_name", what_style="kg_dialogue_text", window_style="kg_dialogue_window")
define vi = Character("Аурелиан Вирт", color="#eac06f", who_style="kg_dialogue_name", what_style="kg_dialogue_text", window_style="kg_dialogue_window")
define ri = Character("Риан Хейла", color="#eac06f", who_style="kg_dialogue_name", what_style="kg_dialogue_text", window_style="kg_dialogue_window")
define le = Character("Лея", color="#eac06f", who_style="kg_dialogue_name", what_style="kg_dialogue_text", window_style="kg_dialogue_window")
define no = Character("Ноа", color="#eac06f", who_style="kg_dialogue_name", what_style="kg_dialogue_text", window_style="kg_dialogue_window")
define te = Character("Теро", color="#eac06f", who_style="kg_dialogue_name", what_style="kg_dialogue_text", window_style="kg_dialogue_window")
define sa = Character("Сайрен", color="#eac06f", who_style="kg_dialogue_name", what_style="kg_dialogue_text", window_style="kg_dialogue_window")
define ai = Character("ИИ-ассистент", color="#eac06f", who_style="kg_dialogue_name", what_style="kg_dialogue_text", window_style="kg_dialogue_window")
define kr = Character("Лоренс Кайстр", color="#eac06f", who_style="kg_dialogue_name", what_style="kg_dialogue_text", window_style="kg_dialogue_window")
define st = Character("Студент", color="#eac06f", who_style="kg_dialogue_name", what_style="kg_dialogue_text", window_style="kg_dialogue_window")
define st_g = Character("Студентка", color="#eac06f", who_style="kg_dialogue_name", what_style="kg_dialogue_text", window_style="kg_dialogue_window")
define sr = Character("Серена Раукт", color="#eac06f", who_style="kg_dialogue_name", what_style="kg_dialogue_text", window_style="kg_dialogue_window")
define ez = Character("Талир Эзари", color="#eac06f", who_style="kg_dialogue_name", what_style="kg_dialogue_text", window_style="kg_dialogue_window")
define nu = Character("Сиделка Мари", color="#eac06f", who_style="kg_dialogue_name", what_style="kg_dialogue_text", window_style="kg_dialogue_window")
define sf = Character("Сайф", color="#eac06f", who_style="kg_dialogue_name", what_style="kg_dialogue_text", window_style="kg_dialogue_window")
define si = Character("Сайлас", color="#eac06f", who_style="kg_dialogue_name", what_style="kg_dialogue_text", window_style="kg_dialogue_window")

define n = Character(None, who_style="kg_dialogue_name", what_style="kg_dialogue_text", window_style="kg_dialogue_window")
define ev_thought = Character("Эвейна", color="#eac06f", who_style="kg_dialogue_name", what_style="kg_dialogue_text", window_style="kg_dialogue_window")
define er_thought = Character("Эриан", color="#eac06f", who_style="kg_dialogue_name", what_style="kg_dialogue_text", window_style="kg_dialogue_window")
define unknown = Character("...", color="#eac06f", who_style="kg_dialogue_name", what_style="kg_dialogue_text", window_style="kg_dialogue_window")

# Именованные реплики физически присутствующих, но находящихся вне кадра
define vi_offscreen = Character("Аурелиан Вирт", color="#eac06f", screen="say_offscreen", who_style="kg_dialogue_name", what_style="kg_dialogue_text", window_style="kg_dialogue_window")
define kr_offscreen = Character("Лоренс Кайстр", color="#eac06f", screen="say_offscreen", who_style="kg_dialogue_name", what_style="kg_dialogue_text", window_style="kg_dialogue_window")
define no_offscreen = Character("Ноа", color="#eac06f", screen="say_offscreen", who_style="kg_dialogue_name", what_style="kg_dialogue_text", window_style="kg_dialogue_window")
define sa_offscreen = Character("Сайрен", color="#eac06f", screen="say_offscreen", who_style="kg_dialogue_name", what_style="kg_dialogue_text", window_style="kg_dialogue_window")
define un_offscreen = Character("...", color="#eac06f", screen="say_offscreen", who_style="kg_dialogue_name", what_style="kg_dialogue_text", window_style="kg_dialogue_window")

define ev_prolog = Character("Девочка", color="#eac06f", who_style="kg_dialogue_name", what_style="kg_dialogue_text", window_style="kg_dialogue_window")
define ri_prolog = Character("Мужчина", color="#eac06f", who_style="kg_dialogue_name", what_style="kg_dialogue_text", window_style="kg_dialogue_window")
define ri_prolog_offscreen = Character("Мужчина", color="#eac06f", screen="say_offscreen", who_style="kg_dialogue_name", what_style="kg_dialogue_text", window_style="kg_dialogue_window")
define ai_offscreen = Character("ИИ-ассистент", color="#eac06f", screen="say_offscreen", who_style="kg_dialogue_name", what_style="kg_dialogue_text", window_style="kg_dialogue_window")

##### Подключение спрайтов

# Спрайты Эвейны 
## Основные
image eveina normal = "characters/eveina/eveina_normal.webp"
image eveina little crying = "characters/eveina/eveina_little_crying.png"
image eveina thinking = "characters/eveina/eveina_thinking.webp"
image eveina smile = "characters/eveina/eveina_smile.webp"
image eveina very smile = "characters/eveina/eveina_lol.webp"
image eveina angry = "characters/eveina/eveina_angry.webp"
image eveina annoyed = "characters/eveina/eveina_annoyed.webp"
image eveina intrigued = "characters/eveina/eveina_intrigued.webp"
image eveina wondered = "characters/eveina/eveina_wondered.webp"
image eveina eyebrow = "characters/eveina/eveina_eyebrow.webp"
image eveina upset = "characters/eveina/eveina_upset.webp"
image eveina upset thinking = "characters/eveina/eveina_upset_thinking.webp"
image eveina eyeroll = "characters/eveina/eveina_eyeroll.webp"
image eveina sad = "characters/eveina/eveina_worried.webp"
image eveina wrinkled = "characters/eveina/eveina_wrinkled.webp"
image eveina panic = "characters/eveina/eveina_panic.webp"
image eveina fear = "characters/eveina/eveina_fear.webp"
image eveina surprized = "characters/eveina/eveina_surprized.webp"
image eveina worried = "characters/eveina/eveina_worried.webp"




## В футболке
image eveina normal tshirt = "characters/eveina/eveina_normal_tshirt.webp"
image eveina thinking tshirt = "characters/eveina/eveina_thinking_tshirt.webp"
image eveina smile tshirt = "characters/eveina/eveina_smile_tshirt.webp"
image eveina very smile tshirt = "characters/eveina/eveina_lol_tshirt.webp"
image eveina angry tshirt = "characters/eveina/eveina_angry_tshirt.webp"
image eveina annoyed tshirt = "characters/eveina/eveina_annoyed_tshirt.webp"
image eveina intrigued tshirt = "characters/eveina/eveina_intrigued_tshirt.webp"
image eveina wondered tshirt = "characters/eveina/eveina_wondered_tshirt.webp"
image eveina eyebrow tshirt = "characters/eveina/eveina_eyebrow_tshirt.webp"
image eveina upset tshirt = "characters/eveina/eveina_upset_tshirt.webp"
image eveina upset thinking tshirt = "characters/eveina/eveina_upset_thinking_tshirt.webp"
image eveina eyeroll tshirt = "characters/eveina/eveina_eyeroll_tshirt.webp"
image eveina sad tshirt = "characters/eveina/eveina_worried_tshirt.webp"
image eveina wrinkled tshirt = "characters/eveina/eveina_wrinkled_tshirt.webp"
image eveina panic tshirt = "characters/eveina/eveina_panic_tshirt.webp"
image eveina fear tshirt = "characters/eveina/eveina_fear_tshirt.webp"
image eveina surprized tshirt = "characters/eveina/eveina_surprized_tshirt.webp"
image eveina worried tshirt = "characters/eveina/eveina_worried_tshirt.webp"


# Спрайты Эриан
image erian normal = "characters/erian/erian_normal.webp"
image erian upset = "characters/erian/erian_upset.webp"
image erian eyebrow = "characters/erian/erian_eyebrow.webp"
image erian eyeroll = "characters/erian/erian_eyeroll.webp"
image erian smile = "characters/erian/erian_smile.webp"
image erian very smile = "characters/erian/erian_lol.webp"
image erian smile wild = "characters/erian/erian_smile_wild.webp"
image erian intrigued = "characters/erian/erian_intrigued.webp"
image erian annoyed = "characters/erian/erian_annoyed.webp"
image erian thinking = "characters/erian/erian_thinking.webp"
image erian upset thinking = "characters/erian/erian_upset_thinking.webp"
image erian angry = "characters/erian/erian_angry.webp"



# Спрайты Аурелиана Вирта
## Основные
image virt normal = "characters/virt/virt_normal.webp"
image virt angry = "characters/virt/virt_angry.webp"
image virt intrigued = "characters/virt/virt_intrigued.webp"
image virt smile = "characters/virt/virt_smile.webp"
image virt serious = "characters/virt/virt_serious.webp"
image virt upset = "characters/virt/virt_upset.webp"
image virt thinking = "characters/virt/virt_thinking.webp"
image virt upset thinking = "characters/virt/virt_upset_thinking.webp"
image virt eyebrow = "characters/virt/virt_eyebrow.webp"



## В пиджаке
image virt normal jacket = "characters/virt/virt_normal_jacket.png"
image virt hello jacket = "characters/virt/virt_normal_jacket.png"
image virt angry jacket = "characters/virt/virt_angry_jacket.png"
image virt sad jacket = "characters/virt/virt_sad_jacket.png"
image virt intrigued jacket = "characters/virt/virt_intrigued_jacket.png"
image virt smile jacket = "characters/virt/virt_smile_jacket.png"
image virt serious jacket = "characters/virt/virt_serious_jacket.png"
image virt upset jacket = "characters/virt/virt_upset_jacket.png"
image virt thinking jacket = "characters/virt/virt_thinking_jacket.png"

# Спрайты Каэль
image kael normal = "characters/kael/kael_normal.webp"
image kael angry = "characters/kael/kael_angry.webp"
image kael smile = "characters/kael/kael_smile.webp"
image kael intrigued = "characters/kael/kael_intrigued.webp"
image kael annoyed = "characters/kael/kael_annoyed.webp"
image kael eyebrow = "characters/kael/kael_eyebrow.webp"
image kael eyeroll = "characters/kael/kael_eyeroll.webp"
image kael upset = "characters/kael/kael_upset.webp"
image kael thinking = "characters/kael/kael_thinking.webp"
image kael upset thinking = "characters/kael/kael_upset_thinking.webp"
image kael insane = "characters/kael/kael_insane.webp"
image kael confused = "characters/kael/kael_confused.webp"
image kael upset insane = "characters/kael/kael_upset_insane.webp"


# Спрайты Лея
image leya normal = "characters/leya/leya_normal.webp"
image leya angry = "characters/leya/leya_angry.webp"
image leya sad = "characters/leya/leya_sad.webp"
image leya eyeroll = "characters/leya/leya_eyeroll.webp"
image leya annoyed = "characters/leya/leya_annoyed.webp"
image leya smile = "characters/leya/leya_smile.webp"
image leya eyebrow = "characters/leya/leya_eyebrow.webp"
image leya thinking = "characters/leya/leya_thinking.webp"
image leya fear = "characters/leya/leya_fear.webp"
image leya tears = "characters/leya/leya_tears.webp"
image leya lol = "characters/leya/leya_lol.webp"
image leya intrigued = "characters/leya/leya_intrigued.webp"
image leya wrinkled = "characters/leya/leya_wrinkled.webp"
image leya upset thinking = "characters/leya/leya_upset_thinking.webp"

# Спрайты Ноа
image noa normal = "characters/noa/noa_normal.webp"
image noa sad = "characters/noa/noa_sad.webp"
image noa smile = "characters/noa/noa_smile.webp"
image noa intrigued = "characters/noa/noa_intrigued.webp"
image noa angry = "characters/noa/noa_angry.webp"
image noa eyebrow = "characters/noa/noa_eyebrow.webp"
image noa thinking = "characters/noa/noa_thinking.webp"
image noa upset thinking = "characters/noa/noa_upset_thinking.webp"


# Спрайты Сайрен
image sairen normal = "characters/sairen/sairen_normal.webp"
image sairen angry = "characters/sairen/sairen_angry.webp"
image sairen smile = "characters/sairen/sairen_smile.webp"
image sairen intrigued = "characters/sairen/sairen_intrigued.webp"
image sairen thinking = "characters/sairen/sairen_thinking.webp"
image sairen upset = "characters/sairen/sairen_upset.webp"

# Спрайты Сайлас
image silas normal = "characters/silas/silas_normal.webp"
image silas annoyed = "characters/silas/silas_annoyed.webp"
image silas smile = "characters/silas/silas_smile.webp"
image silas eyebrow = "characters/silas/silas_eyebrow.webp"
image silas angry = "characters/silas/silas_angry.webp"
image silas eyeroll = "characters/silas/silas_eyeroll.webp"
image silas intrigued = "characters/silas/silas_intrigued.webp"
image silas lol = "characters/silas/silas_lol.webp"
image silas thinking = "characters/silas/silas_thinking.webp"
image silas upset = "characters/silas/silas_upset.webp"
image silas upset thinking = "characters/silas/silas_upset_thinking.webp"

# Спрайты Теро
image tero normal = "characters/tero/tero_normal.webp"
image tero sad = "characters/tero/tero_sad.webp"
image tero smile = "characters/tero/tero_smile.webp"
image tero thinking = "characters/tero/tero_thinking.webp"
image tero angry = "characters/tero/tero_angry.webp"
image tero eyebrow = "characters/tero/tero_eyebrow.webp"
image tero surprised = "characters/tero/tero_surprized.webp"
image tero upset thinking = "characters/tero/tero_upset_thinking.webp"

# Спрайты Риан
image rian normal = "characters/rian/rian_normal.webp"
image rian sad = "characters/rian/rian_sad.webp"
image rian upset smile = "characters/rian/rian_upset_smile.webp"
image rian annoyed = "characters/rian/rian_annoyed.webp"
image rian intrigued = "characters/rian/rian_intrigued.webp"
image rian smile = "characters/rian/rian_smile.webp"
image rian thinking = "characters/rian/rian_thinking.webp"
image rian worried = "characters/rian/rian_worried.webp"

# Спрайты Раукт
image serena normal = "characters/raukt/serena_normal.png"
image serena smile = "characters/raukt/serena_smile.png"

# Спрайты Эзари
image ezari normal = "characters/ezari/ezari_normal.png"
image ezari smile = "characters/ezari/ezari_smile.png"
image ezari angry = "characters/ezari/ezari_angry.png"

# Спрайты Кайстр
image kaistr normal = "characters/kaistr/kaistr_normal.webp"
image kaistr annoyed = "characters/kaistr/kaistr_annoyed.webp"
image kaistr intrigued = "characters/kaistr/kaistr_intrigued.webp"
image kaistr thinking = "characters/kaistr/kaistr_thinking.webp"
image kaistr upset = "characters/kaistr/kaistr_upset.webp"
image kaistr upset thinking = "characters/kaistr/kaistr_upset_thinking.webp"
image kaistr eyebrow = "characters/kaistr/kaistr_eyebrow.webp"
image kaistr smile = "characters/kaistr/kaistr_smile.webp"

# Спрайты студенты
image m01 normal = "characters/students/m01_normal.webp"
image m01 upset = "characters/students/m01_upset.webp"
image m01 annoyed = "characters/students/m01_annoyed.webp"
image m01 smile = "characters/students/m01_smile.webp"

image m02 normal = "characters/students/m02_normal.webp"
image m02 upset = "characters/students/m02_upset.webp"
image m02 annoyed = "characters/students/m02_annoyed.webp"
image m02 smile = "characters/students/m02_smile.webp"

image m03 normal = "characters/students/m03_normal.webp"
image m03 upset = "characters/students/m03_upset.webp"
image m03 annoyed = "characters/students/m03_annoyed.webp"
image m03 smile = "characters/students/m03_smile.webp"


image student angry = "characters/students/student_angry.png"
image student girl sad = "characters/students/student_girl_sad.png"
image student annoyed = "characters/students/student_annoyed.png"
image student confused = "characters/students/student_confused.png"
image student smile = "characters/students/student_smile.png"
image student pafos = "characters/students/student_pafos.png"
# Спрайты студенты - неготовые
image student girl smile = "characters/students/student_girl_smile.png"

# Остальные спрайты
image nurse normal = "characters/nurse/nurse_normal.png"
image ai = "characters/ai.webp"
image sf = "characters/saif.webp"


# 📌 Трансформации персонажей по росту и положению
transform eveina_left:
    xalign 0.0
    yalign 1.0
    zoom 0.5
    easein 0.5

transform erian_right:
    xalign 1.0
    yalign 1.0
    zoom 0.5
    easein 0.5

transform virt_right:
    xalign 1.0
    yalign 1.0
    zoom 0.5
    easein 0.5

transform kael_right:
    xalign 1.0
    yalign 1.0
    zoom 0.5
    easein 0.5

transform leya_right:
    xalign 1.0
    yalign 1.0
    zoom 0.5
    easein 0.5

transform tero_right:
    xalign 1.0
    yalign 1.0
    zoom 0.5
    easein 0.5

transform noa_right:
    xalign 1.0
    yalign 1.0
    zoom 0.5
    easein 0.5

transform kaistr_right:
    xalign 1.0
    yalign 1.0
    zoom 0.5
    easein 0.5

transform serena_right:
    xalign 1.0
    yalign 1.0
    zoom 1.0
    easein 0.5

transform ezari_right:
    xalign 1.0
    yalign 1.0
    zoom 1.0
    easein 0.5

transform sairen_right:
    xalign 1.0
    yalign 1.0
    zoom 0.5
    easein 0.5

transform rian_right:
    xalign 1.0
    yalign 1.0
    zoom 0.5
    easein 0.5

transform student_right:
    xalign 1.0
    yalign 1.0
    zoom 0.5
    easein 0.5

transform ai_right:
    xalign 1.0
    yalign 1.0
    zoom 0.5
    easein 0.5

transform silas_right:
    xalign 1.0
    yalign 1.0
    zoom 0.5
    easein 0.5

#Цветокоррекция спрайтов
transform sprite_night:
    matrixcolor (
        BrightnessMatrix(-0.05)
        * SaturationMatrix(0.85)
        * TintMatrix("#c2cede")
    )

transform sprite_night_mixed:
    matrixcolor (
        BrightnessMatrix(-0.05)
        * SaturationMatrix(0.92)
        * TintMatrix("#d2d6de")
    )

transform sprite_warm:
    matrixcolor (
        BrightnessMatrix(-0.015)
        * SaturationMatrix(0.95)
        * TintMatrix("#f4dfc5")
    )
transform sprite_warm_light:
    matrixcolor (
        BrightnessMatrix(0)
        * SaturationMatrix(0.95)
        * TintMatrix("#fbf1e6")
    )


# Пример использования:
# show eveina normal at eveina_left, sprite_night
# show erian normal at erian_right




# Подключение фонов
image bg virt cabinet day = "bg/virt_cabinet_day.webp"
image bg virt cabinet night = "bg/virt_cabinet_night.webp"
image bg archive corridor night = "bg/archive_corridor_night.webp"
image bg archive corridor day = "bg/archive_corridor_day.webp"
image bg virt cabinet corridor night = "bg/virt_cabinet_corridor_night.webp"
image bg virt cabinet corridor day = "bg/virt_cabinet_corridor_day.webp"
image bg room corridor dark = "bg/room_corridor_dark.webp"
image bg room corridor light = "bg/room_corridor_light.webp"
image bg block corridor = "bg/block_corridor.webp"
image bg room evening = "bg/room_evening.webp"
image bg room night = "bg/room_night.webp"
image bg room day = "bg/room_day.webp"
image bg lecture hall = "bg/lecture_hall.webp"
image bg lecture hall 2 = "bg/lecture_hall_2.webp"
image bg lecture door = "bg/lecture_door.webp"
image bg lecture hall students = "bg/lecture_hall_students.webp"
image bg hall = "bg/hall.webp"
image bg hall wall = "bg/hall_wall.webp"
image bg hall corridor = "bg/hall_corridor.webp"
image bg shuttle = "bg/shuttle.webp"
image bg garden inner = "bg/garden_inner.webp"
image bg dinning room = "bg/dinning_room.webp"
image bg archive = "bg/archive.webp"
image bg archive terminal = "bg/archive_terminal.webp"
image bg archive gologram = "bg/archive_gologram.webp"
image bg room dinning room = "bg/room_dinning_room.webp"
image bg room hospital room = "bg/room_hospital_room.webp"
image bg home_dining_room = "bg/home_dining_room.webp"



image bg archive_hall = "bg/archive_hall.webp"

image bg home_bedroom = "bg/home_bedroom.webp"
image bg eveina_home = "bg/eveina_home.webp"

image bg eveina_room = "bg/eveina_room_day.webp"
image bg eveina_room_day = "bg/eveina_room_day.webp"
image bg eveina_room_night = "bg/eveina_room_night.webp"

image bg garden evening = "bg/garden_evening.webp"
image bg garden night = "bg/garden_night.webp"
image bg garden day = "bg/garden_day.webp"


image bg lab = "bg/lab.webp"
image bg surgery_lab = "bg/surgery_lab.webp"
image bg lab_botany = "bg/lab_botany.webp"

image bg shuttle_2 = "bg/shuttle_2.webp"
image bg shuttle_3 = "bg/shuttle_3.webp"
image bg shuttle_bathroom = "bg/shuttle_bathroom.webp"
image bg virt_cabinet = "bg/virt_cabinet.webp"
image bg raukt_cabinet = "bg/raukt_cabinet.webp"
image bg ezari_cabinet = "bg/ezari_cabinet.webp"
image bg kaistr_cabinet = "bg/kaistr_cabinet.webp"
image bg kael_cabinet = "bg/kael_cabinet.webp"
image bg corridor = "bg/corridor.webp"
image bg corridor_2 = "bg/corridor_2.webp"
image bg corridor_3 = "bg/corridor_3.webp"
image bg corridor_4 = "bg/corridor_4.webp"
image bg corridor_5 = "bg/corridor_5.webp"
image bg corridor_6 = "bg/corridor_6.webp"
image bg forbidden_corridor = "bg/forbidden_corridor.webp"
image bg hospital_room = "bg/hospital_room.webp"
image bg exam_cabinet = "bg/exam_cabinet.webp"
image bg dream = "bg/dream.webp"
image bg capsule = "bg/capsule.webp"
image bg city = "bg/city.webp"
image bg city_garden = "bg/city_garden.webp"
image bg forest = "bg/forest.webp"
image bg kosmodrom = "bg/kosmodrom.webp"

# Специальные фоны
image bg kael first kiss = "bg_special/kael_first_kiss.webp"

#scene_0_garden_awakeness
image bg scene 0 awakeness 1 = "bg_special/scene_0/1.webp"
image bg scene 0 awakeness 2 = "bg_special/scene_0/2.webp"
image bg scene 0 awakeness 3 = "bg_special/scene_0/3.webp"
image bg scene 0 awakeness 4 = "bg_special/scene_0/4.webp"
image bg scene 0 awakeness 5 = "bg_special/scene_0/5.webp"
image bg scene 0 awakeness 6 = "bg_special/scene_0/6.webp"
image bg scene 0 awakeness 7 = "bg_special/scene_0/7.webp"
image bg scene 0 awakeness 8 = "bg_special/scene_0/8.webp"
image bg scene 0 awakeness 9 = "bg_special/scene_0/9.webp"

#scene_1_1_shuttle
image bg scene 1_1 shuttle 1 = "bg_special/scene_1_1/1.webp"
image bg scene 1_1 shuttle 2 = "bg_special/scene_1_1/2.webp"
image bg scene 1_1 shuttle 3 = "bg_special/scene_1_1/3.webp"
image bg scene 1_1 shuttle 4 = "bg_special/scene_1_1/4.webp"
image bg scene 1_1 shuttle 5 = "bg_special/scene_1_1/7.webp"
image bg scene 1_1 shuttle 6 = "bg_special/scene_1_1/8.webp"
image bg scene 1_1 shuttle 7 = "bg_special/scene_1_1/9.webp"

#scene_1_1_dinning_room
image bg scene 1_1 dinning_room 1 = "bg_special/scene_1_1/5.webp"
image bg scene 1_1 dinning_room 2 = "bg_special/scene_1_1/6.webp"

# scene_1_2_cabinet
image bg scene 1_2 virt cabinet 1 = "bg_special/scene_1_2/1.webp"
image bg scene 1_2 virt cabinet 2 = "bg_special/scene_1_2/2.webp"

# scene_1_3_hall
image bg scene 1_3 hall 1 = "bg_special/scene_1_3/1.webp"
image bg scene 1_3 hall 2 = "bg_special/scene_1_3/2.webp"

# scene_1_4_garden
image bg scene 1_4 garden 1 = "bg_special/scene_1_4/1.webp"
image bg scene 1_4 garden 2 = "bg_special/scene_1_4/2.webp"
image bg scene 1_4 garden 3 = "bg_special/scene_1_4/3.webp"
image bg scene 1_4 garden 4 = "bg_special/scene_1_4/4.webp"


# scene_1_4_garden_inner
image bg virt normal eveina eyebrow garden = "bg_special/virt_normal_eveina_eyebrow_garden.webp"
image bg virt normal eveina thinking garden = "bg_special/virt_normal_eveina_thinking_garden.webp"
image bg virt normal eveina normal garden = "bg_special/virt_normal_eveina_normal_garden.webp"
image bg virt sad eveina sad garden = "bg_special/virt_sad_eveina_sad_garden.webp"
image bg virt sad eveina eyebrow garden = "bg_special/virt_sad_eveina_eyebrow_garden.webp"
image bg virt smile eveina smile garden = "bg_special/virt_smile_eveina_smile_garden.webp"
image bg virt smile eveina normal garden = "bg_special/virt_smile_eveina_normal_garden.webp"


# scene_1_5
image bg scene 1_5 corridor 1 = "bg_special/scene_1_5/1.webp"
image bg scene 1_5 corridor 2 = "bg_special/scene_1_5/2.webp"
image bg scene 1_5 corridor 3 = "bg_special/scene_1_5/3.webp"


# scene_1_6
image bg scene 1_6 dream 1 = "bg_special/scene_1_6/2.webp"
image bg scene 1_6 dream 2 = "bg_special/scene_1_6/3.webp"
image bg scene 1_6 dream 3 = "bg_special/scene_1_6/4.webp"
image bg scene 1_6 dream 4 = "bg_special/scene_1_6/5.webp"
image bg scene 1_6 dream 5 = "bg_special/scene_1_6/6.webp"
image bg scene 1_6 dream 6 = "bg_special/scene_1_6/7.webp"
image bg scene 1_6 dream 7 = "bg_special/scene_1_6/8.webp"
image bg scene 1_6 dream 8 = "bg_special/scene_1_6/10.webp"
image bg scene 1_6 dream 9 = "bg_special/scene_1_6/11.webp"
image bg scene 1_6 dream 10 = "bg_special/scene_1_6/12.webp"
image bg scene 1_6 dream 11 = "bg_special/scene_1_6/13.webp"
image bg scene 1 6 garden_inner = "bg_special/scene_1_6/9.webp"

# scene_2_2_room
image bg scene 2_2 dinning room 1 = "bg_special/scene_2_2/dinning_room_1.webp"
image bg scene 2_2 dinning room 2 = "bg_special/scene_2_2/dinning_room_2.webp"
image bg scene 2_2 dinning room 3 = "bg_special/scene_2_2/dinning_room_3.webp"
image bg scene 2_2 dinning room 4 = "bg_special/scene_2_2/dinning_room_4.webp"
image bg scene 2_2 leya normal = "bg_special/scene_2_2/2.webp"
image bg scene 2_2 leya eyebrow = "bg_special/scene_2_2/3.webp"
image bg scene 2_2 leya upset thinking = "bg_special/scene_2_2/leya_upset_thinking.webp"
image bg scene 2_2 eveina facepalm = "bg_special/scene_2_2/eveina_facepalm.webp"
image bg scene 2_2 eveina upset = "bg_special/scene_2_2/7.webp"
image bg scene 2_2 eveina upset thinking = "bg_special/scene_2_2/eveina_upset_thinking.webp"

# scene_2_3_room
image bg scene 2_3 lecture hall 1 = "bg_special/scene_2_3/1.webp"
image bg scene 2_3 lecture hall 2 = "bg_special/scene_2_3/2.webp"
image bg scene 2_3 lecture hall 3 = "bg_special/scene_2_3/3.webp"
image bg scene 2_3 lecture hall 5 = "bg_special/scene_2_3/5.webp"
image bg scene 2_3 lecture hall 6 = "bg_special/scene_2_3/6.webp"
image bg scene 2_3 lecture hall 7 = "bg_special/scene_2_3/7.webp"
image bg scene 2_3 lecture hall 8 = "bg_special/scene_2_3/8.webp"
image bg scene 2_3 lecture hall 10 = "bg_special/scene_2_3/10.webp"
image bg scene 2_3 lecture hall 11 = "bg_special/scene_2_3/11.webp"
image bg scene 2_3 lecture hall 12 = "bg_special/scene_2_3/12.webp"
image bg scene 2_3 lecture hall 13 = "bg_special/scene_2_3/13.webp"
image bg scene 2_3 lecture hall 14 = "bg_special/scene_2_3/14.webp"
image bg scene 2_3 lecture hall 15 = "bg_special/scene_2_3/15.webp"
image bg scene 2_3 lecture hall 16 = "bg_special/scene_2_3/16.webp"
image bg scene 2_3 lecture hall 17 = "bg_special/scene_2_3/17.webp"
image bg scene 2_3 lecture hall 18 = "bg_special/scene_2_3/18.webp"
image bg scene 2_3 support = "bg_special/scene_2_3/support.webp"
image bg scene 2_3 choice = "bg_special/scene_2_3/choice.webp"
image bg scene 2_3 lecture door eveina = "bg_special/scene_2_3/lecture_door_eveina.webp"

# scene_2_4_archive
image bg eveina_erian_2_4 = "bg_special/eveina_erian_2_4.webp"

# scene_2_5_lab
image bg scene 2_5 kael 1 = "bg_special/scene_2_5/kael_1.webp"
image bg scene 2_5 kael 2 = "bg_special/scene_2_5/kael_2.webp"
image bg scene 2_5 kael 3 = "bg_special/scene_2_5/kael_3.webp"
image bg scene 2_5 kael 4 = "bg_special/scene_2_5/kael_4.webp"

# scene_2_6_archive
image bg archive scheme 1 = "bg_special/scene_2_6/archive_scheme_1.webp"
image bg archive scheme 2 = "bg_special/scene_2_6/archive_scheme_2.webp"
image bg archive scheme 3 = "bg_special/scene_2_6/archive_scheme_3.webp"
image bg archive scheme 4 = "bg_special/scene_2_6/archive_scheme_4.webp"
image bg archive scheme 5 = "bg_special/scene_2_6/archive_scheme_5.webp"
image bg archive scheme 6 = "bg_special/scene_2_6/archive_scheme_6.webp"

# scene_2_7_archive
image bg archive erian books 1 = "bg_special/scene_2_7/archive_erian_books_1.webp"
image bg archive erian books 2 = "bg_special/scene_2_7/archive_erian_books_2.webp"

# scene_2_8_virt_cabinet
image bg scene 2_8 virt alone 1 = "bg_special/scene_2_8/virt_alone_1.webp"
image bg scene 2_8 virt alone 2 = "bg_special/scene_2_8/virt_alone_2.webp"
image bg scene 2_8 virt alone 3 = "bg_special/scene_2_8/virt_alone_3.webp"

# scene_2_9_room_corridor
image bg scene 2_9 erian eveina 1 = "bg_special/scene_2_9/erian_eveina_1.webp"
image bg scene 2_9 erian eveina 2 = "bg_special/scene_2_9/erian_eveina_2.webp"
image bg scene 2_9 erian eveina 3 = "bg_special/scene_2_9/erian_eveina_3.webp"
image bg scene 2_9 erian eveina 4 = "bg_special/scene_2_9/erian_eveina_4.webp"
image bg scene 2_9 erian eveina 5 = "bg_special/scene_2_9/erian_eveina_5.webp"
image bg scene 2_9 erian eveina 6 = "bg_special/scene_2_9/erian_eveina_6.webp"
image bg scene 2_9 book reach = "bg_special/scene_2_9/book_reach.webp"
image bg scene 2_9 book bite = "bg_special/scene_2_9/book_bite.webp"
image bg scene 2_9 wall standoff = "bg_special/scene_2_9/wall_standoff.webp"
image bg scene 2_9 bite aftermath = "bg_special/scene_2_9/bite_aftermath.webp"
image bg scene 2_9 choice slap = "bg_special/scene_2_9/choice_slap.webp"
image bg scene 2_9 choice book = "bg_special/scene_2_9/choice_book.webp"

image bg eveina_awakeness = "bg_special/eveina_awakeness.webp"
image bg recomendation_list1 = "bg_special/recomendation_list1.png"
image bg recomendation_list2 = "bg_special/recomendation_list2.png"
image bg prolog_1 = "bg_special/prolog_1.webp"
image bg prolog_2 = "bg_special/prolog_2.webp"
image bg prolog_3 = "bg_special/prolog_3.webp"
image bg prolog_4 = "bg_special/prolog_4.webp"
image bg prolog_5 = "bg_special/prolog_5.webp"
image bg prolog_6 = "bg_special/prolog_6.webp"

image bg splash = "splashscreen/splash.webp"


transform bg_fullscreen:
    xpos 0.5
    xanchor 0.5
    ysize config.screen_height
    fit "cover"

# Затухание всей сцены
label fade_to_black(duration=1.0, pause_duration=1.0):
    scene black with Dissolve(duration)
    $ renpy.pause(pause_duration, hard=True)
    return

label chapters_screen:
    call screen chapters_screen
    return


# Kept as an entry point for existing saves at the release ending.
label to_be_continued:
    jump kg_end_chapter_2

label kg_end_chapter_1:
    $ current_scene = "kg_end_chapter_1"
    $ kg_chapter_end_saved = False
    call screen chapter_ends(1, "start_chapter_2")
    jump start_chapter_2

label kg_end_chapter_2:
    $ current_scene = "kg_end_chapter_2"
    $ kg_chapter_end_saved = False
    call screen chapter_ends(2)
    return

# Штатная точка входа в главное меню Ren'Py.
label main_menu:
    call screen main_menu
    return

# Стартовая точка игры
label start:
    jump prolog

# Заставка игры
label splashscreen:
    scene black
    # Web shows the studio animation during engine loading (web-presplash.webp).
    if not renpy.variant("web"):
        show logo_animation
        $ renpy.pause(4.95, hard=True)
        hide logo_animation
        call fade_to_black(1.0, 1.0)
    
    # Play the game cover once at startup, before the main menu.
    call kg_cover_intro
    return

# Глава 1
label start_chapter_1:

    window hide
    scene black
    $ kg_open_chapter(1, "НОВАЯ ТЕРРИТОРИЯ", "scene_1_1")
    with Dissolve(0.4)
    jump scene_1_1

# Глава 2
label start_chapter_2:

    window hide
    scene black
    $ kg_open_chapter(2, "ЛЮБОПЫТСТВО —\nНЕ ПРЕСТУПЛЕНИЕ", "scene_2_1")
    with Dissolve(0.4)
    jump scene_2_1

# Глава 3
label start_chapter_3:

    window hide
    scene black
    $ kg_open_chapter(3, "ЕСЛИ НЕЛЬЗЯ —\nНО ОЧЕНЬ ХОЧЕТСЯ", "scene_3_1")
    with Dissolve(0.4)
    jump scene_3_1

# Глава 4
label start_chapter_4:

    window hide
    scene black
    $ kg_open_chapter(4, "КАСАНИЕ ЗАПРЕТНОГО", "scene_4_1")
    with Dissolve(0.4)
    jump scene_4_1

# Глава 5
label start_chapter_5:

    window hide
    scene black
    $ kg_open_chapter(5, "КОГДА ДЕРЖИШЬСЯ —\nНО УЖЕ НА ЗУБАХ", "scene_5_1")
    with Dissolve(0.4)
    jump scene_5_1

# Глава 6
label start_chapter_6:

    window hide
    scene black
    $ kg_open_chapter(6, "ФОТОГРАФИЯ\nНА ПАМЯТЬ", "scene_6_1")
    with Dissolve(0.4)
    jump scene_6_1

# Глава 7
label start_chapter_7:

    window hide
    scene black
    $ kg_open_chapter(7, "ОТЛИЧНЫЙ ДЕНЬ,\nЧТОБЫ ОБЛАЖАТЬСЯ", "scene_7_1")
    with Dissolve(0.4)
    jump scene_7_1

# Глава 8
label start_chapter_8:

    window hide
    scene black
    $ kg_open_chapter(8, "СКАЗКА О\nРЫЦАРЯХ И ДРАКОНАХ", "scene_8_1")
    with Dissolve(0.4)
    jump scene_8_1


