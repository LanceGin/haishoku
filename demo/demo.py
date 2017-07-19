import sys
sys.path.insert(0, "..")

from haishoku.haishoku import Haishoku

def main():
    path = "demo_01.png"
    # path = "http://wx2.sinaimg.cn/large/89243dfbly1ffoekfainzj20dw05k0u7.jpg"

    # getPalette api
    palette = Haishoku.getPalette(path)
    print(palette)

    # getDominant api
    dominant = Haishoku.getDominant(path)
    print(dominant)

    # showPalette api
    Haishoku.showPalette(path)

    # showDominant api
    Haishoku.showDominant(path)

    # Haishoku object
    h = Haishoku.loadHaishoku(path)
    print(h.palette)
    print(h.dominant)

if __name__ == "__main__":
    main()