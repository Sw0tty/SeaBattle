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

# v = 0
# # Player1 initialization
# while True:
#     board1 = Board(SHIPS_SET, False)
#     field_ready = board1.add_ships()
#     v += 1
#     if v >= 30:
#         raise BadSettings
#     if field_ready:
#         username = name_setter()
#         player1 = Player(board=board1, name=username)
#         break

# v = 0
# # Player2 initialization
# while True:
#     board2 = Board(SHIPS_SET, HIDE_FIELD)
#     field_ready = board2.add_ships()
#     v += 1
#     if v >= 30:
#         raise BadSettings
#     if field_ready:
#         player2 = AI(board=board2, name='Bot')
#         break


# Players initialization
def main_initialization(player_class):
    try_ = 0
    while True:
        board = Board(SHIPS_SET, HIDE_FIELD)
        field_ready = board.add_ships()
        try_ += 1
        if try_ >= 30:
            raise BadSettings
        if field_ready:
            player = player_class(board=board, name='Bot')
            return board, player


board1, player1 = main_initialization(Player)
board2, player2 = main_initialization(AI)

# BoardsPrinter initialization
board_printer = BoardsPrinter(board1, player1.get_name(), board2, player2.get_name())
