"""

"""
import time
import random

from console_version.app_config.exceptions import OutOfField
from console_version.app_config.settings import SIMULATION_OF_CHOICE, CHOOSING_TIME


class AI:

    def __init__(self, name, board):
        self.__name = name
        self.__board = board

    @staticmethod
    def shot(choice_sim=SIMULATION_OF_CHOICE, time_wait=CHOOSING_TIME):
        if choice_sim:
            print("Choosing cell...")
            time.sleep(time_wait)

        return tuple((random.randrange(0, 6), random.randrange(0, 6)))

    def get_name(self):
        return self.__name

    def get_already_shoot(self):
        return self.__board.checked_cell

    def alive_ships(self):
        return self.__board.ships_on_desk


class Player(AI):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @staticmethod
    def shot(choice=False, time_wait=False):
        try:
            coordinate_x = int(input("Введите значение по X координате: ")) - 1
            coordinate_y = int(input("Введите значение по Y координате: ")) - 1
            if (coordinate_x < 0 or coordinate_x > 5) or (coordinate_y < 0 or coordinate_y > 5):
                raise OutOfField
            return coordinate_x, coordinate_y
        except OutOfField:
            return 'Out of field!'
        except TypeError:
            return 'Unexpected value!'
        except ValueError:
            return 'Unexpected value!'
