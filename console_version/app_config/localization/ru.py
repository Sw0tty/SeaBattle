"""
RU localization file
"""


# Exeptions
OUT_OF_FIELD = "Выстрел за поле!"
UNEXPECTED_VALUE = "Неверное значение!"
SAME_DOT = "Выстрел по той же клетке!"


# Players.py
CHOOSING_CELL = "Выбираю клетку..."
ANSWER = "Думаю: "


def coornate_message(value):
    return f"Введите значение по {value} координате: "


# Board.py
HIT = "Точно в цель!"
MISS = "Промох"
FIELD_TITLE = " поле."


def ship_defeatead(ship_type):
    return f"{ship_type} противника повержен!"


# Initialization.py
WELCOME_STR = """Добро пожаловать в игру, 'Морской бой'!"""
NAME_STR = "Перед началом, введите, пожалуйство свое имя: "


# Main
PLAYER_TURN = "Сейчас ходит: "
VICTORY_STR = "Победил: "
