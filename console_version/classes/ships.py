"""
"""
import random


class Ship:

    def __init__(self, name, hp):
        self._name = name
        self._hp = hp
        self._direction = random.choice(("VERTICAL", "HORIZONTAL"))
        self._nose_dot = self._set_nose_dot()
        self._ship_dots = self._preplace_ship()

    def get_name(self):
        return self._name

    def get_hp(self):
        return self._hp
    
    def get_nose_dot(self):
        return self._nose_dot

    def get_direction(self):
        return self._direction

    def get_ship_dots(self):
        return self._ship_dots

    def _preplace_ship(self):
        if self.get_direction() == 'HORIZONTAL':
            return [(self.get_nose_dot()[0] + i, self.get_nose_dot()[1]) for i in range(self.get_hp())]               
        else:
            return [(self.get_nose_dot()[0], self.get_nose_dot()[1] + i) for i in range(self.get_hp())]  
    
    def _set_nose_dot(self):
        while True:
            rand_nose_dot = (random.randint(0, 5), random.randint(0, 5))
            if self.get_direction() == 'HORIZONTAL':
                if rand_nose_dot[0] + self.get_hp() <= 6:
                    break
            else:
                if rand_nose_dot[1] + self.get_hp() <= 6:
                    break
        return rand_nose_dot

class ShipsSet:

    def __init__(self):
        self.count_battleship = 1
        self.count_cruiser = 2
        self.count_speedboat = 4
        self._set_ships = self.create_set()
    
    def create_set(self):
        l = []
        for i in range(self.count_battleship):
            l.append(Ship('Линкор', 3))
        for i in range(self.count_cruiser):
            l.append(Ship('Крейсер', 2))
        for i in range(self.count_speedboat):
            l.append(Ship('Катер', 1))
        return l
    
    def get_ships_set(self):
        return self._set_ships


# ship = Ship('Линкор', 3)

# print(ship.get_direction(), ship.get_nose_dot(), ship.get_ship_dots())


# ship_set = ShipsSet()


# for i in ship_set.get_ships_set():
#     print(i.get_name(), i.get_direction(), i.get_nose_dot(), i.get_ship_dots())

# battleship = Ship('Линкор', 3)
# cruiser1 = Ship('Крейсер', 2)
# cruiser2 = Ship('Крейсер', 2)
# speedboat1 = Ship('Катер', 1)
# speedboat2 = Ship('Катер', 1)
# speedboat3 = Ship('Катер', 1)
# speedboat4 = Ship('Катер', 1)

# ships = [battleship, cruiser1, cruiser2, speedboat1, speedboat2, speedboat3, speedboat4]

# ship_set = ShipsSet()
# ship_set.create_set()

# # print(ship_set.get_ships_set())
# for ship in ship_set.get_ships_set():
#     print(ship.get_name(), ship.get_hp(), ship.get_direction())
