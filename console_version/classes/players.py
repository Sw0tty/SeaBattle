"""

"""
import time
import random

from app_config.exceptions import OutOfField, InSameDot
from app_config.settings import SIMULATION_OF_CHOICE, CHOOSING_TIME


class BasePlayer:

    def __init__(self, name, board):
        self.__name = name
        self.__board = board
    
    @staticmethod
    def shot():
        pass
    
    def get_name(self):
        return self.__name

    def get_already_shoot(self):
        return self.__board.checked_cell

    def alive_ships(self):
        return self.__board.ships_on_desk
    
class AI(BasePlayer):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    @staticmethod
    def shot(already_shoot, choice_sim=SIMULATION_OF_CHOICE, time_wait=CHOOSING_TIME):
        if choice_sim:
            print("Choosing cell...")
            time.sleep(time_wait)
        while True:
            cell = tuple((random.randrange(0, 6), random.randrange(0, 6)))
            if cell not in already_shoot:
                break
        print(f"Think: {chr(cell[0] + 65)}{cell[1] + 1}\n")
        time.sleep(1)
        return cell


class Player(BasePlayer):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @staticmethod
    def shot(already_shoot):
        try:
            coordinate_x = input("Введите значение по X координате: ").strip()
            if coordinate_x.isdigit():
                raise TypeError
            coordinate_x = ord(coordinate_x.upper()) - 65
            coordinate_y = int(input("Введите значение по Y координате: ")) - 1
            if (coordinate_x < 0 or coordinate_x > 5) or (coordinate_y < 0 or coordinate_y > 5):
                raise OutOfField
            if (coordinate_x, coordinate_y) in already_shoot:
                raise InSameDot
            return coordinate_x, coordinate_y
        except OutOfField:
            return 'Out of field!'
        except InSameDot:
            return 'Shot in shooted cell'
        except TypeError:
            return 'Unexpected value!'
        except ValueError:
            return 'Unexpected value!'
