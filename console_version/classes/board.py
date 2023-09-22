"""
"""
from classes.ships import ShipsSet

class Board:
    def __init__(self, ships_set: object, hide: bool):
        self.hide = hide
        self.all_hp = 12
        self.letters = [" ", "A", "B", "C", "D", "E", "F"]
        self.battle_field = self.new_field()
        self._ships_set = ShipsSet().create_set()

        self.check_near = "T"
        self.ship_object = "■"

        self.ships_dict = []
        self.ships_on_desk = []
        self.dots_ships = []
        self.for_near_dict = []

    @staticmethod
    def new_field():
        return [["D"] * 6 for _ in range(6)]
    
    # def get_battle_field(self):
    #     return self.battle_field
    
    
    def _print_field(self):
        print(*self.letters)

        
        for i in enumerate(self.battle_field):
            print(i[0] + 1, end=' ')
            print(*i[1])

        # for i in self.letters:
        #     print(i, end=' ')

    def _add_ships(self):
        for ship in self._ships_set:
            count = 0
            for i in range(ship.get_hp()):
                if ship.get_direction() == 'HORIZONTAL':
                    self.battle_field[ship.get_nose_dot()[0] + count][ship.get_nose_dot()[1]] = self.ship_object
                    count += 1

