"""
"""
from app_config.localization import en as replies
from app_config.settings import SHIP, DEFEATED_SHIP, EMPTY
from .ship import Ship


class Cell:
    def __init__(self, x_size: int, y_size: int, position: tuple, cell_object: object):
        self.x_size = x_size
        self.y_size = y_size
        self.position = position
        self.cell_object = cell_object
        self.color = None


class FieldSprite:

    def __init__(self):
        self.cells = []

class Board:

    def __init__(self, ships_set: tuple, hide: bool):
        self._ships_set = ships_set
        self.hide = hide

        self._ship = Ship
        self.battle_field = self.new_field()

        self.ship_object = SHIP
        self.defeated_ship = DEFEATED_SHIP
        self.empty_cell = EMPTY
        self.ships_on_desk = []   
        self.busy_dots = []

    @staticmethod
    def new_field():
        return [[" "] * 6 for _ in range(6)]
    
    def check_alive_ships(self):
        return self.ships_on_desk

    def check_hp(self, dot):
        for ship in self.ships_on_desk:
            if dot in ship.get_ship_dots():
                if ship.hp_update() == 0:
                    defeated_ship = self.ships_on_desk.pop(self.ships_on_desk.index(ship))
                    return defeated_ship
                break

    def fill_around_ship(self, around_dots):
        for dot in around_dots:
            self.busy_dots.append(dot)
            self.battle_field[dot[1]][dot[0]] = self.empty_cell

    def set_hide_param(self):
        self.hide = True

    def add_dots(self, ship_dots):
        around_ship_dots = []
        for dot in ship_dots:
            self.busy_dots.append(dot)
            self.battle_field[dot[1]][dot[0]] = self.ship_object

            dots = [
                (dot[0] - 1, dot[1] + 1),
                (dot[0] - 1, dot[1]),
                (dot[0] - 1, dot[1] - 1),
                (dot[0], dot[1] - 1),
                (dot[0] + 1, dot[1] - 1),
                (dot[0] + 1, dot[1]),
                (dot[0] + 1, dot[1] + 1),
                (dot[0], dot[1] + 1)
            ]

            for new_dot in dots:
                if (0 <= new_dot[0] < 6) and (0 <= new_dot[1] < 6) and new_dot not in ship_dots:
                    around_ship_dots.append(new_dot)
                if new_dot in self.busy_dots or (new_dot[0] > 5 or new_dot[0] < 0) or\
                        (new_dot[1] > 5 or new_dot[1] < 0):
                    continue

                self.busy_dots.append(new_dot)
        return around_ship_dots

    def cell_is_busy(self, ship):
        for dot in ship.get_ship_dots():
            if dot in self.busy_dots:
                return True 

    def add_ships(self):
        for set_ in self._ships_set:
            for _ in range(set_[0]):
                try_count = 0
                while True:
                    ship = self._ship(*set_[1])

                    if not self.cell_is_busy(ship):
                        break
                    try_count += 1
                    if try_count >= 10:
                        return False

                ship_dots = self.add_dots(ship.get_ship_dots())
                ship.set_around_ship_space(ship_dots)
                self.ships_on_desk.append(ship)
        self.busy_dots.clear()
        return True

    def blast_on_board(self, x, y):
        self.busy_dots.append((x, y))
        
        if self.battle_field[y][x] == self.ship_object:
            self.battle_field[y][x] = self.defeated_ship
            ship_is_defeat = self.check_hp((x, y))

            if ship_is_defeat:
                self.fill_around_ship(ship_is_defeat.get_around_ship_space())
                return True, replies.ship_defeatead(ship_is_defeat.get_name())
            return True, replies.HIT
        
        if self.battle_field[y][x] == ' ':
            self.battle_field[y][x] = self.empty_cell
            return False, replies.MISS
        

class FieldGrid:
    pass


class FieldsPrinter:
    pass
