"""
File with players classes
"""
import time
import random

from app_config.exceptions import OutOfField, InSameDot
from app_config.settings import SIMULATION_OF_CHOICE, CHOOSING_TIME
from app_config.settings import LANGUAGE


match LANGUAGE:
    case 'en':
        from app_config.localization import en as replies
    case 'ru':
        from app_config.localization import ru as replies


class BasePlayer:

    def __init__(self, name, board):
        self.__name = name
        self.__board = board
    
    def get_name(self):
        return self.__name

    def get_already_shoot(self):
        return self.__board.busy_dots

    def alive_ships(self):
        return self.__board.ships_on_desk
    
class AI(BasePlayer):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    @staticmethod
    def shot(already_shoot, choice_sim=SIMULATION_OF_CHOICE, time_wait=CHOOSING_TIME):
        if choice_sim:
            print(replies.CHOOSING_CELL)
            time.sleep(time_wait)
        while True:
            cell = tuple((random.randrange(0, 6), random.randrange(0, 6)))
            if cell not in already_shoot:
                break
        print(replies.ANSWER + f"{chr(cell[0] + 65)}{cell[1] + 1}")
        time.sleep(1)
        return cell


class Player(BasePlayer):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    @staticmethod
    def shot(already_shoot):
        try:
            coordinate_x = input(replies.coornate_message('X')).strip()
            if coordinate_x.isdigit():
                raise TypeError
            coordinate_x = ord(coordinate_x.upper()) - 65
            coordinate_y = int(input(replies.coornate_message('Y'))) - 1
            if (coordinate_x < 0 or coordinate_x > 5) or (coordinate_y < 0 or coordinate_y > 5):
                raise OutOfField
            if (coordinate_x, coordinate_y) in already_shoot:
                raise InSameDot
            return coordinate_x, coordinate_y
        except OutOfField:
            return replies.OUT_OF_FIELD
        except InSameDot:
            return replies.SAME_DOT
        except TypeError:
            return replies.UNEXPECTED_VALUE
        except ValueError:
            return replies.UNEXPECTED_VALUE
