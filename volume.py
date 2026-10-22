"""Объем аквариума."""


def tank_volume(length, width, height):
    # размеры в сантиметрах, 1 литр = 1000 куб. см
    return length * width * height / 1000
