"""
"""
import random


class Ship:

    def __init__(self, name, hp):
        self._name = name
        self._hp = hp
        self._nose_dot = (random.randint(0, 6), random.randint(0, 6))
        self._direction = random.choice(("VERTICAL", "HORIZONTAL"))

    def get_name(self):
        return self._name

    def get_hp(self):
        return self._hp
    
    def get_nose_dot(self):
        return self._nose_dot

    def get_direction(self):
        return self._direction


class ShipsSet:

    def __init__(self) -> None:
        self.count_battleship = 1
        self.count_cruiser = 2
        self.count_speedboat = 4
        self._set_ships = []
    
    def create_set(self):
        for i in range(self.count_battleship):
            self._set_ships.append(Ship('Линкор', 3))
        for i in range(self.count_cruiser):
            self._set_ships.append(Ship('Крейсер', 2))
        for i in range(self.count_speedboat):
            self._set_ships.append(Ship('Катер', 1))
        return self.get_ships_set()
    
    def get_ships_set(self):
        return self._set_ships


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
