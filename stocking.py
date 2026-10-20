"""Сколько рыб можно поселить."""
import math
def max_fish(volume_l, fish_length_cm):
    # 1 см взрослой рыбы на 1,5 л воды, грунт и декор забирают около 10 % объема
    useful = volume_l * 0.9
    return math.floor(useful / (fish_length_cm * 1.5))
