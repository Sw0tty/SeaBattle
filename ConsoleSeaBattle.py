"""
Не закончена. Все что есть - это генерация одного поля.
Остановился на создании второго поля. Половина классов просто есть, так как не знаю как их использовать.

После разбора и просмотра кода игры с вебинара данная задача не решаема,
если ты не практиковал классы минимум год после их изучения. Мне больше нечего сказать к этой задаче для "начинающих"
"""

import random
import os


class Dot:
    def __init__(self, x: str, y: int):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


class Ship:
    def __init__(self, width: int, nose_dot: tuple, direction: str, hp: int):
        self.width: int = width
        self.nose_dot: tuple = nose_dot
        self.direction: str = direction
        self.hp: int = hp

    def dots(self):
        return  # dots

    def get_ship(self):
        return f"{self.width} {self.nose_dot} {self.direction} {self.hp}"

    def get_ship_nose(self):
        return self.nose_dot

    def get_ship_direction(self):
        return f"{self.direction}"


class Board:
    def __init__(self, ship_dict):
        self.ship_dict = ship_dict

    def __str__(self):
        return f"{self.ship_dict}"

    def get_dict(self):
        return f"{self.ship_dict}"


player_ships_list = []  # Список кораблей
fields = []

player_field = {"0": ["1", "A", "B", "C", "D", "E", "F", "1"],
                "1": ["1", " ", " ", " ", " ", " ", " ", "1"],
                "2": ["1", " ", " ", " ", " ", " ", " ", "1"],
                "3": ["1", " ", " ", " ", " ", " ", " ", "1"],
                "4": ["1", " ", " ", " ", " ", " ", " ", "1"],
                "5": ["1", " ", " ", " ", " ", " ", " ", "1"],
                "6": ["1", " ", " ", " ", " ", " ", " ", "1"],
                "7": ["1", "1", "1", "1", "1", "1", "1", "1"]}

bot_field = {"0": ["1", "A", "B", "C", "D", "E", "F", "1"],
             "1": ["1", " ", " ", " ", " ", " ", " ", "1"],
             "2": ["1", " ", " ", " ", " ", " ", " ", "1"],
             "3": ["1", " ", " ", " ", " ", " ", " ", "1"],
             "4": ["1", " ", " ", " ", " ", " ", " ", "1"],
             "5": ["1", " ", " ", " ", " ", " ", " ", "1"],
             "6": ["1", " ", " ", " ", " ", " ", " ", "1"],
             "7": ["1", "1", "1", "1", "1", "1", "1", "1"]}


# -------Вывод поля---------
def print_field():
    for i, j in player_field.items():
        if i == "0":
            print(" ", end="|")
        elif i == "7":
            pass
        else:
            print(i, end="|")
        if i != "7":
            for k in j[1:7]:
                print(k, end="|")
            print()
# --------------------------

def print_field_bot():
    s_ = -1  #
    r_ = 2  #
    for i, j in bot_field.items():
        if i == "0":
            print(" ", end="|")
        elif i == "7":
            pass
        else:
            print(i, end="|")
        if i != "7":
            for k in j[1:7]:
                print(k, end="|")
            s_ += 1  #

            print()


def check_ship_around(check=1):  # Дефолт проверки одной точки
    one_check = player_field[str(ship.get_ship_nose()[0])][ship.get_ship_nose()[1] + 1] != "■" and \
                player_field[str(ship.get_ship_nose()[0])][ship.get_ship_nose()[1] - 1] != "■" and \
                player_field[str(ship.get_ship_nose()[0] - 1)][ship.get_ship_nose()[1]] != "■" and \
                player_field[str(ship.get_ship_nose()[0] + 1)][ship.get_ship_nose()[1]] != "■" and \
                player_field[str(ship.get_ship_nose()[0] + 1)][ship.get_ship_nose()[1] + 1] != "■" and \
                player_field[str(ship.get_ship_nose()[0] + 1)][ship.get_ship_nose()[1] - 1] != "■" and \
                player_field[str(ship.get_ship_nose()[0] - 1)][ship.get_ship_nose()[1] + 1] != "■" and \
                player_field[str(ship.get_ship_nose()[0] - 1)][ship.get_ship_nose()[1] - 1] != "■"
    # ------------- Проверка на двойной корабль --------------
    if check == 2:
        if ship.get_ship_direction() == "horizontal":
            if one_check and \
                    player_field[str(ship.get_ship_nose()[0])][ship.get_ship_nose()[1] + 2] != "■" and \
                    player_field[str(ship.get_ship_nose()[0] - 1)][ship.get_ship_nose()[1] + 2] != "■" and \
                    player_field[str(ship.get_ship_nose()[0] + 1)][ship.get_ship_nose()[1] + 2] != "■":
                return True
            else:
                return False
        else:
            if one_check and \
                    player_field[str(ship.get_ship_nose()[0] + 2)][ship.get_ship_nose()[1]] != "■" and \
                    player_field[str(ship.get_ship_nose()[0] + 2)][ship.get_ship_nose()[1] + 1] != "■" and \
                    player_field[str(ship.get_ship_nose()[0] + 2)][ship.get_ship_nose()[1] - 1] != "■":
                return True
            else:
                return False
    # ---------------------------
    else:
        # ------------- Проверка на единичный корабль --------------
        if one_check:
            return True
        else:
            return False
        # ---------------------------


def ship_placement(_):
    for h in range(_):
        if ship.get_ship_direction() == "vertical":
            player_field[str(ship.get_ship_nose()[0] + h)][ship.get_ship_nose()[1]] = "■"
        else:
            player_field[str(ship.get_ship_nose()[0])][ship.get_ship_nose()[1] + h] = "■"


def clear_field():
    for i, j in player_field.items():
        if i != "7":
            for k in j[1:7]:
                if k == "■":
                    for h in range(1, 7):
                        player_field[i][h] = " "
    player_ships_list.clear()
# -----------Генерация кораблей-----------
def generation_ships(try_count):
    _ = 3
    for i in range(7):
        try_append = True
        if i == 1:
            _ -= 1
        elif i == 3:
            _ -= 1
        while try_append:
            try_count += 1
            if try_count > 50:
                print_field()
                return 1
            global ship  # ------GLOBAL--------#
            ship = Ship(_, (random.randrange(1, 7), random.randrange(1, 7)),
                        random.choice(("vertical", "horizontal")), _)
            print(ship.get_ship_nose(), i)
            if player_field[str(ship.get_ship_nose()[0])][ship.get_ship_nose()[1]] != "■" and check_ship_around():
                if _ == 3:
                    if ship.get_ship_nose()[0] + 2 < 7 and ship.get_ship_nose()[1] + 2 < 7:
                        ship_placement(_)
                    else:
                        continue
                elif _ == 2:
                    if ship.get_ship_nose()[0] + 1 < 7 and ship.get_ship_nose()[1] + 1 < 7 and check_ship_around(2):
                        ship_placement(_)
                    else:
                        continue
                else:
                    player_field[str(ship.get_ship_nose()[0])][ship.get_ship_nose()[1]] = "■"
                try_append = False
            else:
                continue
        player_ships_list.append(ship)
# -----------------------------------------


for i in range(2):
    while True:
        if generation_ships(0) == 1:
            clear_field()
            continue
        else:
            fields.append(player_field)
            break


# ---Вывод инфы всех кораблей---
for i in player_ships_list:
    print(i.get_ship())
# -----------------

print(fields)
print_field()  # ---Вывод поля---
print_field_bot()  # ---Вывод поля---

print()

x_ = ["A", "B", "C", "D", "E", "F"]
x_converter = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6}
y_ = [1, 2, 3, 4, 5, 6]

x = "0"
y = 0

# while True:
#     x = input("X")
#     y = int(input("Y"))
#     if x in x_ and y in y_:
#         break
#
#
# dot = Dot(x, y)
# dot1 = Dot(x, y)
# print(dot == dot1)
