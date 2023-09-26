"""
Initialization file
    Create board, players and place ships on board
"""
from .exceptions import BadSettings
from .settings import SHIPS_SET, HIDE_FIELD, INFO
from classes.board import Board, BoardsPrinter
from classes.players import AI, Player


# Game
print("┏" + "-" * 39 + "┓", """|     Welcome to game, 'SeaBattle'!     |""", "┗" + "-" * 39 + "┛", sep='\n')


# Name initialization
def name_setter():
    while True:
        username = input(f"""[{INFO}] Before we're started, please, input you're name: """).strip()
        if username:
            return username


# Players initialization
def main_initialization(player_class, player_name='Bot'):
    try_ = 0
    while True:
        board = Board(SHIPS_SET, HIDE_FIELD)
        field_ready = board.add_ships()
        try_ += 1
        if try_ >= 30:
            raise BadSettings
        if field_ready:
            player = player_class(board=board, name=player_name)
            return board, player


board1, player1 = main_initialization(Player, name_setter())
board2, player2 = main_initialization(AI)

# BoardsPrinter initialization
board_printer = BoardsPrinter(board1, player1.get_name(), board2, player2.get_name())
