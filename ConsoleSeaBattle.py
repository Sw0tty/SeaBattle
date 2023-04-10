"""
----В процессе разработки----
"""

from abc import ABC
import random
import os


class OffField(Exception):
    pass


class InSameDot(Exception):
    pass


class Ships(ABC):
    def __init__(self, nose_dot: tuple, width: int, direction: str, hp: int, type_ship: str):
        self.nose_dot: tuple = nose_dot
        self.width: int = width
        self.direction: str = direction
        self.hp: int = hp
        self.type_ship: str = type_ship
        self.dots = []

    def __repr__(self):
        return f"{self.width} {self.nose_dot} {self.direction} {self.hp} {self.type_ship}"

    def get_ship_nose(self):
        return self.nose_dot

    def get_ship_direction(self):
        return f"{self.direction}"


class Battleship(Ships):
    def __init__(self, nose_dot: tuple, width=3, direction='HORIZONTAL', hp=3, type_ship="Линкор"):
        super().__init__(nose_dot, width, direction, hp, type_ship)


class Cruiser(Ships):
    def __init__(self, nose_dot: tuple, width=2, direction='HORIZONTAL', hp=2, type_ship="Крейсер"):
        super().__init__(nose_dot, width, direction, hp, type_ship)


class Speedboat(Ships):
    def __init__(self, nose_dot: tuple, width=1, direction='HORIZONTAL', hp=1, type_ship="Катер"):
        super().__init__(nose_dot, width, direction, hp, type_ship)


class Board:
    def __init__(self, hid: bool):
        self.hid = hid
        self.all_hp = 12
        self.letters = [" ", "A", "B", "C", "D", "E", "F"]
        self.numbers = ["1", "2", "3", "4", "5", "6"]
        self.battle_field = [[" "] * 6 for _ in range(6)]

        self.check_near = "T"
        self.ship_object = "■"

        self.ships_dict = []
        self.ships_on_desk = []
        self.dots_ships = []
        self.for_near_dict = []

    def add_ship(self):
        self.for_near_dict.clear()
        while True:
            choice_ship = 1
            battleship = Battleship((random.randrange(0, 6), random.randrange(0, 6)),
                                    direction=(random.choice(("VERTICAL", "HORIZONTAL"))))


            cruiser = Cruiser((random.randrange(0, 6), random.randrange(0, 6)),
                              direction=(random.choice(("VERTICAL", "HORIZONTAL"))))
            speedboat = Speedboat((random.randrange(0, 6), random.randrange(0, 6)),
                                  direction=(random.choice(("VERTICAL", "HORIZONTAL"))))


            if choice_ship == 1:
                now_place = battleship
            elif choice_ship < 4:
                now_place = cruiser
            else:
                now_place = speedboat


            if now_place.direction == "HORIZONTAL":
                if now_place.nose_dot[0] + 2 > 5:
                    continue
                for j in range(3):
                    self.battle_field[now_place.nose_dot[0] + j][now_place.nose_dot[1]] = self.ship_object
                    self.dots_ships.append((now_place.nose_dot[0] + j, now_place.nose_dot[1]))

                    self.for_near_dict.append((now_place.nose_dot[0] + j, now_place.nose_dot[1]))
            else:
                if now_place.nose_dot[1] + 2 > 5:
                    continue
                for j in range(3):
                    self.battle_field[now_place.nose_dot[0]][now_place.nose_dot[1] + j] = self.ship_object
                    self.dots_ships.append((now_place.nose_dot[0], now_place.nose_dot[1] + j))

                    self.for_near_dict.append((now_place.nose_dot[0], now_place.nose_dot[1] + j))

            choice_ship += 1
            self.ships_dict.append([now_place.width, now_place.nose_dot, now_place.direction,
                                    now_place.hp, now_place.type_ship])
            self.near_ship(now_place.direction)
            break

    def retry_place(self):
        self.ships_dict.clear()
        i1, j1 = 0, 0
        for i in self.battle_field:
            for j in i:
                if j == self.ship_object or j == self.check_near:
                    self.battle_field[i1][j1] = " "
                j1 += 1
            i1 += 1
            j1 = 0

    def near_ship(self, ship_direction):
        for i, j in self.for_near_dict:
            if ship_direction == "HORIZONTAL":
                if i != 0 and self.battle_field[i - 1][j] != self.ship_object:
                    self.battle_field[i - 1][j] = self.check_near
                    if j - 1 >= 0:
                        self.battle_field[i - 1][j - 1] = self.check_near
                    if j + 1 < 6:
                        self.battle_field[i - 1][j + 1] = self.check_near
                if i != 5 and self.battle_field[i + 1][j] != self.ship_object:
                    self.battle_field[i + 1][j] = self.check_near
                    if j + 1 < 6:
                        self.battle_field[i + 1][j + 1] = self.check_near
                    if j - 1 >= 0:
                        self.battle_field[i + 1][j - 1] = self.check_near
                if j != 5:
                    self.battle_field[i][j + 1] = self.check_near
                if j != 0:
                    self.battle_field[i][j - 1] = self.check_near

            elif ship_direction == "VERTICAL":
                if j != 0 and self.battle_field[i][j - 1] != self.ship_object:
                    self.battle_field[i][j - 1] = self.check_near
                    if i - 1 >= 0:
                        self.battle_field[i - 1][j - 1] = self.check_near
                    if i + 1 < 6:
                        self.battle_field[i + 1][j - 1] = self.check_near
                if j != 5 and self.battle_field[i][j + 1] != self.ship_object:
                    self.battle_field[i][j + 1] = self.check_near
                    if i + 1 < 6:
                        self.battle_field[i + 1][j + 1] = self.check_near
                    if i - 1 >= 0:
                        self.battle_field[i - 1][j + 1] = self.check_near
                if i != 5:
                    self.battle_field[i + 1][j] = self.check_near
                if i != 0:
                    self.battle_field[i - 1][j] = self.check_near
        self.for_near_dict.clear()

    def shot(self, a1, a2):
        if self.battle_field[a1][a2] == self.ship_object:
            self.battle_field[a1][a2] = "x"
            self.all_hp -= 1
        elif self.battle_field[a1][a2] == "•":
            raise InSameDot
        else:
            self.battle_field[a1][a2] = "•"

    def print_field(self):
        for i in self.letters:
            print(i, "  ", end="")
        print()
        _ = 1
        for i in self.battle_field:
            print(_, end=" | ")
            for j in i:
                print(j, "| ", end="")
            _ += 1
            print()
        return ""


class PlayerBoard(Board):
    def __init__(self, hid):
        super().__init__(hid)


class AIBoard(Board):
    def __init__(self, hid):
        super().__init__(hid)


class Dot:
    def __init__(self, x: str, y: int):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


player_field = Board(False)
bot_field = Board(True)

player_field.add_ship()
bot_field.add_ship()

print(player_field.ships_dict)
print(bot_field.ships_dict)

print(player_field.dots_ships)
print(bot_field.dots_ships)

print(player_field.print_field())
print(bot_field.print_field())

# player_field.retry_place()
# bot_field.retry_place()
#
# print(player_field.print_field())
# print(bot_field.print_field())



while True:
    try:
        a1 = int(input("Ваш ход: "))
        a2 = int(input("Ваш ход: "))
        bot_field.shot(a1, a2)
        print(player_field.print_field())
        print(bot_field.print_field())
        print(bot_field.all_hp, "bot")
        print(player_field.all_hp, "play")
    except InSameDot:
        print("В данную клетку уже стреляли")
