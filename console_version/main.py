"""
Main file for playing
"""
import random
import time

from app_config.initialization import board1, board2, player1, player2, board_printer
from app_config.settings import WARNING


def player_switcher(turn_player=None, new_game=False):
    if new_game:
        return player1 if random.randrange(0, 2) == 1 else player2
    return player2 if turn_player == player1 else player1


now_turn_player = player_switcher(new_game=True)

while True:
    if now_turn_player == player2:
        board_printer.printer(now_turn_player.get_already_shoot())
    else:
        board_printer.printer(player_switcher(now_turn_player).get_already_shoot())
    print('\nNow turn: ' + now_turn_player.get_name())
    dot = now_turn_player.shot(player_switcher(now_turn_player).get_already_shoot())

    if isinstance(dot, tuple):
        if now_turn_player == player1:
            another_shot = board2.blast_on_board(*dot)
        else:
            another_shot = board1.blast_on_board(*dot)

        now_turn_player = player_switcher(now_turn_player)

        if not now_turn_player.alive_ships():
            now_turn_player = player_switcher(now_turn_player)
            break

        now_turn_player = player_switcher(now_turn_player)

        if not another_shot[0]:
            now_turn_player = player_switcher(now_turn_player)
            continue

        print(another_shot[1])
    else:
        print(f'[{WARNING}] ' + dot, '\n')
        time.sleep(2)

board2.set_hide_param()
board_printer.printer(player_switcher(now_turn_player).get_already_shoot())
print('\nVictory for: ' + now_turn_player.get_name())
