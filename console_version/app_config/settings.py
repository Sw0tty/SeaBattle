"""
Settings for SeaBattle (console_version) project.
"""
from colorama import Fore, Style, init


# Initialization console colors
init()

# Game board pictograms
EMPTY = '•'  # for circle dead ships and miss shots
SHIP = '■'
DEFEATED_SHIP = 'x'

# Ships set (count on board, (name, hp)).
# WARNING! These are the optimal values.
# An increase in indicators may lead to an error in generating ships on the field
SHIPS_SET = (
    (1, ('Линкор', 3)),
    (2, ('Крейсер', 2)),
    (4, ('Катер', 1))
)

# Bot settings
SIMULATION_OF_CHOICE = True
CHOOSING_TIME = 2
HIDE_FIELD = True

# Console message codes
WARNING = Fore.YELLOW + "WARNING" + Style.RESET_ALL
HELP_STR = Fore.GREEN + "HELP" + Style.RESET_ALL
INFO = Fore.CYAN + "INFO" + Style.RESET_ALL

# Language
SUPPORTED_LANGUAGE = ('en', 'ru')
LANGUAGE = 'ru'
