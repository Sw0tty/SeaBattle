"""
Main file for playing
"""
import random
import time

from app_config.exceptions import *
from app_config.initialization import board1, board2, player1, player2, board_printer
from app_config.settings import WARNING


# # Player1 initialization
# while True:
#     board1 = Board(SHIPS_SET, False)
#     field_ready = board1.add_ships()
#     if field_ready:
#         # username = name_setter()
#         name = 'Tester'
#         player1 = Player(board=board1, name=name)
#         break


# # Player2 initialization
# while True:
#     board2 = Board(SHIPS_SET, HIDE_FIELD)
#     field_ready = board2.add_ships()
#     if field_ready:
#         player2 = AI(board=board2, name='Bot')
#         break


# # BoardsPrinter initialization
# board_printer = BoardsPrinter(board1, player1.get_name(), board2, player2.get_name())


def change_player(turn_player=None, new_game=False):
    if new_game:
        return player1 if random.randrange(0, 2) == 1 else player2
    return player2 if turn_player == player1 else player1


now_turn_player = change_player(new_game=True)

while True:
    if now_turn_player == player2:
        board_printer.printer(now_turn_player.get_already_shoot())
    else:
        board_printer.printer(change_player(now_turn_player).get_already_shoot())
    print('\nNow turn: ' + now_turn_player.get_name())
    dot = now_turn_player.shot(change_player(now_turn_player).get_already_shoot())

    if isinstance(dot, tuple):
        if now_turn_player == player1:
            another_shot = board2.blast_on_board(*dot)
        else:
            another_shot = board1.blast_on_board(*dot)

        now_turn_player = change_player(now_turn_player)

        if not now_turn_player.alive_ships():
            now_turn_player = change_player(now_turn_player)
            break

        now_turn_player = change_player(now_turn_player)

        if not another_shot[0]:
            now_turn_player = change_player(now_turn_player)
            continue

        print(another_shot[1])
    else:
        print(f'[{WARNING}] ' + dot, '\n')
        time.sleep(2)

board_printer.printer(change_player(now_turn_player).get_already_shoot())
print('\nVictory for: ' + now_turn_player.get_name())
