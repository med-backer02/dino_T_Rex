# это тестовая программа
# которая показывает все спрайты (динозавр, кактус, ...)

import pyxel
from utils import *
from player import *
from enemy import *
from constants import *

class App:
    def __init__(self):
        pyxel.init(250, 180, caption="Sprites")
        pyxel.load("asset/asset.pyxel")
        pyxel.playm(0, loop=True)
        pyxel.run(self.update, self.draw)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

    def draw(self):
        pyxel.cls(ColPal.black)

        # показать изображение спрайта
         # === все спрайты ===
        pyxel.text(0, 0, "ALL SPRITES", (pyxel.frame_count//3)%15 + 1)
        pyxel.blt(0, 10, 0,
                0, 0, 120, 150)

        # === Динозавр === (24, 26)
        # dino_w, dino_h = 24, 26
        pyxel.text(130, 0, "T-REX", (pyxel.frame_count//3)%15 + 1)
        t_rexes = [Player.NORMAL, Player.BLINK,
                    Player.RUN1, Player.RUN2, Player.CRASH]
        for i in range(len(t_rexes)):
            pyxel.blt(130+Player._W*i, 10, 0, *t_rexes[i].getRect())

        # анимация
        pyxel.text(50, 80, "ANIMATION", (pyxel.frame_count//3)%15 + 1)
        f = (pyxel.frame_count//3)%2
        pyxel.blt(90, 90, 0, *t_rexes[[2,3][f]].getRect())
        pyxel.blt(50, 90, 0, *t_rexes[[0,1][f]].getRect())


        # === Кактус ===(16, 24)
        cac_w, cac_h = 16, 24
        pyxel.text(130, 40, "CACTUS", (pyxel.frame_count//3)%15 + 1)
        cactuses = [Rect(cac_w*i, 32, cac_w, cac_h) for i in range(6) ]

        for i in range(len(cactuses)):
            pyxel.blt(130+cac_w*i, 50, 0, *cactuses[i].getRect())
        # анимация
        f = (pyxel.frame_count//3)%2
        pyxel.blt(70, 130, 0, *cactuses[[0,1,2][f]].getRect())
        pyxel.blt(90, 130, 0, *cactuses[[3,4,5][f]].getRect())


        # === Птеродактиль ===(24, 24)
        pte_w, pte_h = 24,24
        pyxel.text(130, 80, "PTERA", (pyxel.frame_count//3)%15 + 1)
        pteras = [Rect(pte_w*i, 56, pte_w, pte_h) for i in range(2) ]

        for i in range(len(pteras)):
            pyxel.blt(130+pte_w*i, 90, 0, *pteras[i].getRect())
        # Анимация
        f = (pyxel.frame_count//3)%2
        pyxel.blt(40, 130, 0, *pteras[f].getRect())


        # === Облака ===(48, 16)
        cld_w, cld_h = 48,16
        pyxel.text(190, 80, "CLOUD", (pyxel.frame_count//3)%15 + 1)
        clouds = [Rect(cld_w*i, 80, cld_w, cld_h) for i in range(1) ]

        for i in range(len(clouds)):
            pyxel.blt(190+cld_w*i, 90, 0, *clouds[i].getRect())


        # === Сброс === (32, 32)
        btn_w, btn_h = 32,32
        pyxel.text(130, 120, "BUTTON", (pyxel.frame_count//3)%15 + 1)
        btns = [Rect(btn_w*i, 96, btn_w, btn_h) for i in range(1) ]

        for i in range(len(btns)):
            pyxel.blt(130+btn_w*i, 130, 0, *btns[i].getRect())


        # === Земля === (128, 32)
        gnd_w, gnd_h = 128, 32
        pyxel.text(190, 120, "GROUND", (pyxel.frame_count//3)%15 + 1)
        pyxel.blt(170, 130, 0, 0, 128, gnd_w, gnd_h)


App()
