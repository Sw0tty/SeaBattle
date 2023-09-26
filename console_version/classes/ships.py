"""
Class generating ships
"""
import random


class Ship:

    def __init__(self, name: str, hp: int):
        self.__name = name
        self.__hp = hp

        self._direction = random.choice(("VERTICAL", "HORIZONTAL"))
        self._nose_dot = self.__place_nose_ship(self._direction, self.__hp)
        self._ship_dots = self._preplace_ship()
        self._around_ship_space = []

    @staticmethod
    def __place_nose_ship(direction, hp):
        while True:
            rand_nose_dot = (random.randint(0, 5), random.randint(0, 5))
            if direction == 'HORIZONTAL':
                if rand_nose_dot[0] + hp <= 6:
                    break
            else:
                if rand_nose_dot[1] + hp <= 6:
                    break
        return rand_nose_dot

    def get_name(self):
        return self.__name

    def get_hp(self):
        return self.__hp
    
    def get_nose_dot(self):
        return self._nose_dot

    def get_direction(self):
        return self._direction

    def get_ship_dots(self):
        return self._ship_dots

    def get_around_ship_space(self):
        return self._around_ship_space

    def set_around_ship_space(self, around_dots):
        self._around_ship_space = around_dots

    def _preplace_ship(self):
        if self.get_direction() == 'HORIZONTAL':
            return [(self.get_nose_dot()[0] + i, self.get_nose_dot()[1]) for i in range(self.get_hp())]               
        else:
            return [(self.get_nose_dot()[0], self.get_nose_dot()[1] + i) for i in range(self.get_hp())]  
    
    def hp_update(self):
        self.__hp -= 1
        return self.get_hp()
