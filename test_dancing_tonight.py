# это тестовая программа
# которая показывает танцующего динозавра и кактуса

import pyxel
from utils import *
from player import *
from enemy import *

class App:
    def __init__(self):
        pyxel.init(120, 60, caption="Sprites")
        pyxel.load("asset/asset.pyxel")
        pyxel.run(self.update, self.draw)
        

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        # цветовая палитра не определена [0-15]
        # если вы устанавите целое число больше 15, это выглядит интересно
        pyxel.cls(8)

        # === Динозавр === (24, 32)
        dino_w, dino_h = 24, 32
        pyxel.text(130, 0, "T-REX", (pyxel.frame_count//3)%15 + 1)
        t_rexes = [Rect(dino_w*i, 0, dino_w, dino_h) for i in range(5) ]
        # Аниимация
        pyxel.text(50, 80, "ANIMATION", (pyxel.frame_count//3)%15 + 1)
        f = (pyxel.frame_count//3)%2
        x1 = (pyxel.frame_count//2+10)%120-12
        x2 = (pyxel.frame_count//2+34)%120-12
        x3 = (pyxel.frame_count//2+58)%120-12
        x4 = (pyxel.frame_count//2+82)%120-12
        x5 = (pyxel.frame_count//2+106)%120-12
        x6 = (pyxel.frame_count//2-14)%120-12
        pyxel.blt(x1, 20, 0, *t_rexes[[2,3][f]].getRect())
        pyxel.blt(x2, 20, 0, *t_rexes[[0,1][f]].getRect())
        pyxel.blt(x3, 20, 0, *t_rexes[[2,3][f]].getRect())
        pyxel.blt(x4, 20, 0, *t_rexes[[0,1][f]].getRect())
        pyxel.blt(x5, 20, 0, *t_rexes[[2,3][f]].getRect())
        pyxel.blt(x6, 20, 0, *t_rexes[[0,1][f]].getRect())



        # === Кактус ===(16, 24)
        cac_w, cac_h = 16, 24
        pyxel.text(130, 40, "CACTUS", (pyxel.frame_count//3)%15 + 1)
        cactuses = [Rect(cac_w*i, 32, cac_w, cac_h) for i in range(6) ]
        # Анимация
        f = (pyxel.frame_count//3)%2
        pyxel.blt(10, 32, 0, *cactuses[[0,1,2][f]].getRect())
        pyxel.blt(26, 32, 0, *cactuses[[3,4,5][f]].getRect())
        pyxel.blt(96, 32, 0, *cactuses[[0,1,2][f]].getRect())
        pyxel.blt(80, 32, 0, *cactuses[[3,4,5][f]].getRect())

        # === Птеродактиль === (24, 24)
        pte_w, pte_h = 24,24
        pyxel.text(130, 80, "PTERA", (pyxel.frame_count//3)%15 + 1)
        pteras = [Rect(pte_w*i, 56, pte_w, pte_h) for i in range(2) ]
        # Анимация
        f = (pyxel.frame_count//3)%2
        pyxel.blt(110-x1, 5, 0, *pteras[f].getRect())

App()
