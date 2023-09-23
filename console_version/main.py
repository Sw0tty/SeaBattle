"""
Main file for playing
"""
import random
import time

from app_config.settings import SHIPS_SET
from classes.ships import Ship
from classes.board import Board, BoardsPrinter
from console_version.app_config.exceptions import *
from console_version.classes.players import AI, Player


# ship_set = ShipsSet()
# ship_set.create_set()

# # print(ship_set.get_ships_set())
# for ship in ship_set.get_ships_set():
#     print(ship.get_name(), ship.get_hp(), ship.get_direction())

name = 'Tester'
# player1 = Player(ships=1, name=name)
# player2 = AI()

# Player1 initialization
while True:
    board1 = Board(SHIPS_SET, False)
    field_ready = board1.add_ships()
    if field_ready:
        break

# player1 = Player(ships=board1.ships_on_desk, name=name)
player1 = Player(board=board1, name=name)

print(player1.alive_ships())
# Player2 initialization
while True:
    board2 = Board(SHIPS_SET, False)
    field_ready = board2.add_ships()
    if field_ready:
        break

# board.set_hide_param()
board1.print_field()


board_printer = BoardsPrinter(board1, board2)

board_printer.printer()


while True:
    dot = player1.shot()
    in_ = board1.blast_on_board(*dot)
    print(in_)
    board1.print_field()
