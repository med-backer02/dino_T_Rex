import pyxel
from utils import Vec, ColPal, Rect
import music
from constants import (WINDOW_WIDTH, WINDOW_HEIGHT,
                       CAPTION, FPS, ANIM_FPS,
                       COLKEY,
                       DEBUG)

class Player:
    """playable character"""
    global COLKEY
    # === ПЕРЕМЕННЫЕ КЛАССА ===
    IMG_ID = 0                        
    _W, _H = 24, 26
    # Динозавр
    NORMAL = Rect(_W*0, 0, _W, _H, COLKEY)
    BLINK  = Rect(_W*1, 0, _W, _H, COLKEY)
    RUN1   = Rect(_W*2, 0, _W, _H, COLKEY)
    RUN2   = Rect(_W*3, 0, _W, _H, COLKEY)
    CRASH  = Rect(_W*4, 0, _W, _H, COLKEY)

    RUN_ANIM = [RUN1, RUN2]

    INITIAL_POS = Vec(30, 70)
    JUMP_VELOCITY = 11                # Высота прыжка
    JUMP_DURING_TIME = 2              # Время прыжка
    state = "RUN"                     # состояние: "RUN" или "JUMP" или "IDLE"
    pos = INITIAL_POS                 # Позиция игрока

    def __init__(self):
        self.initialize()
        self.showInfo()

    def initialize(self):
        Player.pos = Player.INITIAL_POS
        self.velocity = Vec(0, 0)
        Player.state = "RUN"            # "RUN" или "JUMP" или "IDLE

    def showInfo(self):
        pass

    def update(self):
        # прыгать с помощью [SPACE] или [UP]
        if (Player.state=="RUN" and
            (pyxel.btn(pyxel.KEY_UP) or pyxel.btn(pyxel.KEY_SPACE))):
            self.velocity = Vec(0,-Player.JUMP_VELOCITY)
            Player.state = "JUMP"
            music.sfx_jump()

        if (Player.state=="JUMP"):
            if pyxel.frame_count%Player.JUMP_DURING_TIME==0:
                self.velocity = Vec(0, self.velocity.y + 1)
                Player.pos = Vec(Player.pos.x, Player.pos.y + self.velocity.y)
                if Player.pos.y >= Player.INITIAL_POS.y: # После приземления на землю
                    Player.pos = Player.INITIAL_POS
                    Player.state = "RUN"
                    music.sfx_ground()

        if Player.state=="IDLE":
            pass

    def blt(self):
        global DEBUG
        if self.state == "IDLE":
            pyxel.blt(self.pos.x, self.pos.y,
                      self.IMG_ID, *Player.CRASH.getRect())
        else:
            f = (pyxel.frame_count//ANIM_FPS)%len(Player.RUN_ANIM)
            pyxel.blt(self.pos.x, self.pos.y,
                        Player.IMG_ID, *Player.RUN_ANIM[f].getRect())

        if DEBUG:
            pyxel.text(0,0,"Игрок:\n ({}, {})".format(
                        Player.pos.x, Player.pos.y), ColPal.orange)
            
    @classmethod
    def beGameover(cls):
        cls.state = "IDLE"
        music.stop_music()
        music.sfx_death()

    @classmethod
    def getPos(cls):
        """return: pos(Vec)"""
        return Player.pos

    @classmethod
    def getSize(cls):
        return cls._W, cls._H

    @classmethod
    def getState(cls):
        return cls.state
