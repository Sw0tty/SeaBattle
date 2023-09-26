"""
EN localization file
"""


# Exeptions
OUT_OF_FIELD = "Out of field!"
UNEXPECTED_VALUE = "Unexpected value!"
SAME_DOT = "Shoot in same dot!"


# Players.py
CHOOSING_CELL = "Choosing cell..."
ANSWER = "Think: "


def coornate_message(value):
    return f"Enter the {value} coordinate value: "


# Board.py
HIT = "There is a hit!"
MISS = "Miss"
FIELD_TITLE = " field."


def ship_defeatead(ship_type):
    return f"Enemy {ship_type} destroyed!"


# Initialization.py
WELCOME_STR = """Welcome to game, 'SeaBattle'!"""
NAME_STR = "Before we're started, please, input you're name: "


# Main
PLAYER_TURN = "Now turn: "
VICTORY_STR = "Victory for: "
