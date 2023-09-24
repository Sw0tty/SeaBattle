"""
Main file for playing
"""
import random
import time

from app_config.settings import SHIPS_SET, ERROR
from classes.ships import Ship
from classes.board import Board, BoardsPrinter
from console_version.app_config.exceptions import *
from console_version.classes.players import AI, Player


# Player1 initialization
while True:
    board1 = Board(SHIPS_SET, False)
    field_ready = board1.add_ships()
    if field_ready:
        # name = input("""Before we're started, please, input you're name: """)
        name = 'Tester'
        player1 = Player(board=board1, name=name)
        break

# player1 = Player(ships=board1.ships_on_desk, name=name)


# Player2 initialization
while True:
    board2 = Board(SHIPS_SET, False)
    field_ready = board2.add_ships()
    if field_ready:
        player2 = AI(board=board2, name='Bot')
        break


# BoardsPrinter initialization
board_printer = BoardsPrinter(board1, board2)


# Game
print("┏" + "-" * 39 + "┓", """|     Welcome to game, 'SeaBattle'!     |""", "┗" + "-" * 39 + "┛", sep='\n')


now_turn_player = player1 if random.randrange(0, 2) == 1 else player2


def change_player(turn_player):
    return player2 if turn_player == player1 else player1


while True:
    if now_turn_player == player2:
        board_printer.printer(now_turn_player.get_already_shoot())
    else:
        board_printer.printer(change_player(now_turn_player).get_already_shoot())
    print('\nNow turn: ' + now_turn_player.get_name())
    dot = now_turn_player.shot()

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
        print(f'[{ERROR}] ' + dot)
        time.sleep(2)

board_printer.printer(change_player(now_turn_player).get_already_shoot())
print('\nVictory for: ' + now_turn_player.get_name())
