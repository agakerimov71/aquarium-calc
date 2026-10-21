"""Подмена воды."""


def weekly_change(volume_l, percent=25):
    # сколько литров менять раз в неделю
    if not 1 <= percent <= 50 :
        raise ValueError("подмена должна быть от 1 до 50 %")
    return round(volume_l * percent / 100, 1)
