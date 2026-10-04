# Cached image composites: no live blur or per-scroll recompositing.
init 24 python:
    KG_CHAPTER_NAMES = (
        "НОВАЯ ТЕРРИТОРИЯ",
        "ЛЮБОПЫТСТВО — НЕ ПРЕСТУПЛЕНИЕ",
        "ЕСЛИ НЕЛЬЗЯ — НО ОЧЕНЬ ХОЧЕТСЯ",
        "КАСАНИЕ ЗАПРЕТНОГО",
        "КОГДА ДЕРЖИШЬСЯ — НО УЖЕ НА ЗУБАХ",
        "ФОТОГРАФИЯ НА ПАМЯТЬ",
        "ОТЛИЧНЫЙ ДЕНЬ, ЧТОБЫ ОБЛАЖАТЬСЯ",
        "СКАЗКА О РЫЦАРЯХ И ДРАКОНАХ",
    )
    def kg_chapter_card(number, unlocked=False, hover=False):
        folder = "gui/chapter_covers/"
        cover = im.Crop(im.Scale(folder + "chapter_%02d.webp" % number, 480, 360), (0, 60, 480, 240))
        if not unlocked:
            cover = im.MatrixColor(cover, im.matrix.saturation(.18) * im.matrix.brightness(-.12))
        composite = im.Composite((600, 240), (0, 0), folder+"base.png",
            (120, 0), cover, (0, 0), folder+"fade.png")
        return im.Composite((600, 240), (0, 0), im.AlphaMask(composite, folder+"mask.png"),
            (0, 0), folder+("hover.png" if hover else "idle.png"))
    KG_CHAPTER_CARDS = tuple(kg_chapter_card(n, n <= 2) for n in range(1, 9))
    KG_CHAPTER_HOVER = tuple(kg_chapter_card(n, n <= 2, True) for n in range(1, 9))
