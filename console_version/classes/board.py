"""
Classes responsible for the visual part
    Board - contains information about the location of ships
    BoardsPrinter - displays the boards next to each other
"""
from classes.ships import Ship
from app_config.settings import SHIP, DEFEATED_SHIP, EMPTY
from app_config.exceptions import InSameDot


class Board:

    def __init__(self, ships_set: tuple, hide: bool):
        self._ships_set = ships_set
        self.hide = hide

        self._ship = Ship
        self.battle_field = self.new_field()

        self.ship_object = SHIP
        self.defeated_ship = DEFEATED_SHIP
        self.empty_cell = EMPTY
        self.checked_cell = []
        self.ships_on_desk = []
        self.busy_dots = []

    @staticmethod
    def new_field():
        return [[" "] * 6 for _ in range(6)]

    def fill_around_ship(self, around_dots):
        for dot in around_dots:
            self.checked_cell.append(dot)
            self.battle_field[dot[1]][dot[0]] = self.empty_cell

    def check_alive_ships(self):
        return self.ships_on_desk

    def check_hp(self, dot):
        for ship in self.ships_on_desk:
            if dot in ship.get_ship_dots():
                if ship.hp_update() == 0:
                    defeated_ship = self.ships_on_desk.pop(self.ships_on_desk.index(ship))
                    return defeated_ship
                break

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
            busy = self.check_around(dot)
            if busy:
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

                r = self.add_dots(ship.get_ship_dots())
                ship.set_around_ship_space(r)
                self.ships_on_desk.append(ship)
        return True

    def check_around(self, dot):
        if dot in self.busy_dots:
            return True
        return False

    def blast_on_board(self, x, y):
        self.checked_cell.append((x, y))
        
        if self.battle_field[y][x] == self.ship_object:
            self.battle_field[y][x] = self.defeated_ship
            ship_is_defeat = self.check_hp((x, y))

            if ship_is_defeat:
                self.fill_around_ship(ship_is_defeat.get_around_ship_space())
                return True, f'{ship_is_defeat.get_name()} противника повержен!\n'
            return True, 'There is a hit!'
        
        if self.battle_field[y][x] == ' ':
            self.battle_field[y][x] = self.empty_cell
            return False, 'Miss'


class BoardsPrinter:

    def __init__(self, player_board: Board, player_name: str, enemy_board: Board, enemy_name: str):
        self.player_board_info = player_board
        self.player_name = player_name
        self.enemy_board_info = enemy_board
        self.enemy_name = enemy_name

        self.__letters = [" ", "A", "B", "C", "D", "E", "F"]

    def get_fields_titles(self):
        player1_title = (self.player_name + ' field.').ljust(15)
        player2_title = (self.enemy_name + ' field.').ljust(15)
        space = 14
        if len(player1_title) > 14:
            space -= (len(player1_title) - 13)
            
        return f"""{player1_title}{' ' * space}{player2_title}"""

    def printer(self, checked_dots):
        print(self.get_fields_titles())
        print(*self.__letters, ' ' * 12, *self.__letters)
        for i in range(6):
            if self.enemy_board_info.hide:
                print(i + 1, *self.player_board_info.battle_field[i], '|', ' ' * 10,
                      i + 1, *[self.enemy_board_info.battle_field[i][j] if (j, i) in checked_dots else ' ' for j in range(6)], '|')
            else:
                print(i + 1, *self.player_board_info.battle_field[i], '|', ' ' * 10,
                      i + 1, *self.enemy_board_info.battle_field[i], '|')
        print(' ', '-' * 12, ' ' * 13, '-' * 12)
