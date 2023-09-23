"""
Settings file
"""

# Game board pictograms
EMPTY = '•'  # for circle dead ships and miss shots
SHIP = '■'
DEFEATED_SHIP = '✕'

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

# Language
SUPPORT_LANGUAGE = ('en', 'ru')
