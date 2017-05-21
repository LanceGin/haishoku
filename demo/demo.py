import sys
sys.path.insert(0, "..")

from haishoku.haishoku import Haishoku

def main():
    path = "demo_01.png"

    colors = Haishoku.getPalette(path)
    print(len(colors))

if __name__ == "__main__":
    main()