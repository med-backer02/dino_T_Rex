"""

###########################
# Музыка и звуковые эффекты #
###########################

"""

import pyxel
def sfx_jump ():
     "" "Воспроизвести звук прыжка." ""
     pyxel.play (ch = 3, snd = 32)

def sfx_ground ():
     "" "Воспроизвести звук при ударе о землю." ""
     pyxel.play (ch = 3, snd = 33)

def sfx_death ():
     "" "Воспроизвести звук, когда игрок умирает." ""
     pyxel.play (ch = 3, snd = 34)

def start_music ():
     "" "Запустить музыкальный трек." ""
     pyxel.playm (msc = 0, loop = True)

def stop_music ():
     "" "Остановить музыкальную дорожку" ""
     pyxel.stop ()
