"""
Initialization file
    Create board, players and place ships on board
"""
import random
import time

from console_version.app_config.settings import SHIPS_SET
from console_version.classes.ships import Ship
from console_version.classes.board import Board, BoardsPrinter
from console_version.app_config.exceptions import *
from console_version.classes.players import AI, Player

print(ord('B'))