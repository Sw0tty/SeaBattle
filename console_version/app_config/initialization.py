"""
Initialization file
    Create board, players and place ships on board
"""
from .exceptions import BadSettings
from .settings import SHIPS_SET, HIDE_FIELD, HELP_STR, LANGUAGE
from classes.board import Board, BoardsPrinter
from classes.players import AI, Player


match LANGUAGE:
    case 'en':
        from app_config.localization import en as replies
    case 'ru':
        from app_config.localization import ru as replies


# Game
print("┏" + "-" * 39 + "┓", "|" + (replies.WELCOME_STR).center(39) + "|", "┗" + "-" * 39 + "┛", sep='\n')


# Name initialization
def name_setter():
    while True:
        username = input(f"""[{HELP_STR}] {replies.NAME_STR}""").strip()
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
