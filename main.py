import pyxel
from utils import Vec, ColPal, Rect
from player import Player
from enemy import Enemy, BackGround
import music
from constants import (Score,
                       WINDOW_WIDTH, WINDOW_HEIGHT,
                       CAPTION, FPS,
                       COLKEY,
                       DEBUG)

# === MAIN ===
class App:
    # Перезапуск BUTTON
    IMG_ID = 0
    BTN_W, BTN_H = 32, 32
    BTN_RESTART = Rect(0, 96, BTN_W, BTN_H, COLKEY)

    def __init__(self):
        global WINDOW_HEIGHT, WINDOW_WIDTH, CAPTION, FPS, COLKEY
        pyxel.init(WINDOW_WIDTH, WINDOW_HEIGHT, caption=CAPTION, fps=FPS)

        # === Создание экземпляров ===
        self.player = Player()
        self.enemy  = Enemy()
        self.backgnd  =  BackGround()
        self.player.beGameover()

        pyxel.load("asset/asset.pyxel")
        pyxel.run(self.update, self.draw)

    def update(self):
        self.backgnd.update() 
        self.enemy.update()
        self.player.update()

        # обновление счета
        if Player.getState()!="IDLE":
            Score.update()

        # === Перезагрузка ===
        if Player.getState()=="IDLE":
            if pyxel.btnp(pyxel.KEY_SPACE):
                Score.saveHighScore()
                # инициализировать состояние
                Score.initialize()
                self.backgnd.initialize()
                self.enemy.initialize()
                self.player.initialize()
                music.start_music()

    def draw(self):
        global WINDOW_HEIGHT, WINDOW_WIDTH, DEBUG
        pyxel.cls(ColPal.gray_dark)
        self.backgnd.blt()
        self.enemy.blt()
        self.player.blt()

        # показать счет
        pyxel.text(WINDOW_WIDTH-50, 5, "HI {}  {}".format(
                    Score.getHighScore(), Score.getScore()), ColPal.white)
        # после завершения игры показывать кнопку перезапуска
        if Player.getState()=="IDLE":
            pyxel.text(WINDOW_WIDTH//2-5, WINDOW_HEIGHT//2-5,
                        "GAME OVER\n[SPACE] TO CONTINUE", ColPal.white)
            pyxel.blt(WINDOW_WIDTH//2-48, WINDOW_HEIGHT//2-16,
                        App.IMG_ID, *App.BTN_RESTART.getRect())

        if DEBUG:
            pyxel.text(0, 20, "Frame: {}".format(pyxel.frame_count), ColPal.orange)
App()
