"""
Initialization file
    Create board, players and place ships on board
"""
from app_config.exceptions import *
from app_config.settings import SHIPS_SET, HIDE_FIELD, INFO
from classes.board import Board, BoardsPrinter
from classes.players import AI, Player


# Game
print("┏" + "-" * 39 + "┓", """|     Welcome to game, 'SeaBattle'!     |""", "┗" + "-" * 39 + "┛", sep='\n')


# Name initializator
def name_setter():
    while True:
        username = input(f"""[{INFO}] Before we're started, please, input you're name: """).strip()
        if username:
            return username


# Player1 initialization
while True:
    board1 = Board(SHIPS_SET, False)
    field_ready = board1.add_ships()
    if field_ready:
        username = name_setter()
        username = 'Tester'
        player1 = Player(board=board1, name=username)
        break


# Player2 initialization
while True:
    board2 = Board(SHIPS_SET, HIDE_FIELD)
    field_ready = board2.add_ships()
    if field_ready:
        player2 = AI(board=board2, name='Bot')
        break


# BoardsPrinter initialization
board_printer = BoardsPrinter(board1, player1.get_name(), board2, player2.get_name())
