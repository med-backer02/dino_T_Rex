# TODO: colpal to enum
import gzip
import inspect
import os
import pickle
import pyxel

"""(функция) margeAndSave
(класс) Vec
(класс) ColPal
(класс) Rect
"""

def margePyxelFiles(img_file_path, music_file_path, save_to):
    """img_file + music_file -> marged_file
    Проверка файлов"""
    # Проверить все файлы с раширением .pyxel
    try:
        assert os.path.basename(img_file_path).split(".")[-1]   == "pyxel"
        assert os.path.basename(music_file_path).split(".")[-1] == "pyxel"
        assert os.path.basename(save_to).split(".")[-1]         == "pyxel"
    except AssertionError:
        print("AssertionError: Проверьте пути к файлам (расширение должно быть .pyxel)")

    # === Константы из constants.py===
    RENDERER_IMAGE_COUNT=4
    AUDIO_SOUND_COUNT = 65
    AUDIO_MUSIC_COUNT = 8

    pyxel.init(1,1) # Нужен pyxel.load
    data = {"version": pyxel.VERSION}

    # загрузка данных изображения из 'img_file_path'
    pyxel.load(img_file_path)
    image_list = [
        pyxel.image(i).data.dumps() for i in range(RENDERER_IMAGE_COUNT - 1)
    ]
    data["image"] = image_list
    pyxel.load(music_file_path)
    sound_list = [pyxel.sound(i) for i in range(AUDIO_SOUND_COUNT - 1)]
    data["sound"] = sound_list

    music_list = [pyxel.music(i) for i in range(AUDIO_MUSIC_COUNT - 1)]
    data["music"] = music_list

    pickled_data = pickle.dumps(data)

    with gzip.open(save_to, mode="wb") as fp:
        fp.write(pickled_data)
    print("Сохраненные данные без проблем. : {}".format(save_to))
    pyxel.quit()


class Vec:
    """2d кординаты"""
    def __init__(self, x, y):
        self.x = x
        self.y = y

class ColPal:
    """цветовая палитра для пикселя"""
    black      = 0
    navy       = 1
    purple     = 2
    green      = 3
    brown      = 4
    gray_dark  = 5
    gray_light = 6
    white      = 7
    red        = 8
    orange     = 9
    yellow     = 10
    lime       = 11
    cyan       = 12
    steel_blue = 13
    pink       = 14
    peach      = 15

    def __init__(self):
        """черный, темно-синий, фиолетовый, зеленый,
        коричневый,серый(темный),серый(светло-белый),
        красный,оранжевый, желтый, салатовый,
        голубой, стальной синий, розовый, персиковый
        """
        pass


class Rect:
    def __init__(self, u, v, w, h, colkey=ColPal.pink):
        """координаты
         colkey: считается прозрачным (по умолчанию: розовый)
        """
        self.u = u
        self.v = v
        self.w = w
        self.h = h
        self.colkey = colkey

    def getRect(self):
        return [self.u, self.v, self.w, self.h, self.colkey]
