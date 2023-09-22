"""
"""
import random
# from classes.ships import __all__
from classes.ships import ShipsSet
from classes.board import Board

# ship_set = ShipsSet()
# ship_set.create_set()

# # print(ship_set.get_ships_set())
# for ship in ship_set.get_ships_set():
#     print(ship.get_name(), ship.get_hp(), ship.get_direction())

ships = ShipsSet()
dict_ships = ships.create_set()
board = Board(ships, False)

board._add_ships()
print(board._print_field())
