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
        # self.circle_fill = self.__add_circle_fill(self._direction, self._nose_dot, self._ship_dots)
        self._around_ship_space = []

    @staticmethod
    def __add_circle_fill(direction, nose_dot, ship_dots):
        circle = []
        for dot in ship_dots:
            if dot in circle:
                circle.remove(dot)
            circle.append((dot[0] - 1, dot[1] - 1))
        return ()

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

# class ShipsSet:
#
#     def __init__(self):
#         self.count_battleship = 1
#         self.count_cruiser = 2
#         self.count_speedboat = 4
#         self._set_ships = self.create_set()
#
#     def create_set(self):
#         l = []
#         for i in range(self.count_battleship):
#             l.append(Ship('Линкор', 3))
#         for i in range(self.count_cruiser):
#             l.append(Ship('Крейсер', 2))
#         for i in range(self.count_speedboat):
#             l.append(Ship('Катер', 1))
#         return l
#
#     def get_ships_set(self):
#         return self._set_ships
