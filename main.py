"""Калькулятор аквариумиста: собирает расчеты из трех модулей."""
import sys

from stocking import max_fish
from volume import tank_volume
from water_change import weekly_change


def main(args):
    if len(args) != 4:
        print("Запуск: python main.py длина ширина высота длина_рыбы")
        print("Пример: python main.py 60 30 40 4")
        return 1
    length, width, height, fish = (float(a) for a in args)
    volume = tank_volume(length, width, height)
    print(f"Объем аквариума: {volume:.1f} л")
    print(f"Можно поселить рыб длиной {fish:g} см: {max_fish(volume, fish)}")
    print(f"Подмена воды раз в неделю: {weekly_change(volume)} л")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
