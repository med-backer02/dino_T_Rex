from utils import Vec, ColPal, Rect
import pyxel

# если True, показать позицию каждого объекта
DEBUG = False

VERSION = "0.2"
WINDOW_WIDTH, WINDOW_HEIGHT = (240, 120)
CAPTION = "Dinosaur T-Rex"
FPS = 60                 # Требуемый FPS
ANIM_FPS = FPS//5

# Цвет фона img bank
COLKEY = ColPal.pink


class Score:
    # === переменные класса ===
    _score      = 0
    _high_score = 0

    def __init__(self):
        self.initialize()

    @classmethod
    def update(cls):
        global FPS
        if pyxel.frame_count%(FPS//10)==0: # 1 sec -> score +10
            cls._score += 1

    @classmethod
    def initialize(cls):
        cls._score = 0
        with open("asset/score.txt", "r") as f:
            l = f.readlines()
            cls._high_score = int(l[1])

    @classmethod
    def saveHighScore(cls):
        cls._high_score = max(cls._high_score, cls._score)
        with open("asset/score.txt", "w") as f:
            f.write("Рекорд: \n{}".format(cls._high_score))

    @classmethod
    def getScore(cls):
        return cls._score

    @classmethod
    def getHighScore(cls):
        return cls._high_score
