"""
Settings for SeaBattle (pygame_version) project.
"""
import os
from pathlib import Path


# Project folder
BASE_DIR = Path(__file__).resolve().parent.parent

# Assets folder
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')


# Colors library
class ColorsLib:
    def __init__(self):
        self.BLACK = (0, 0, 0)
        self.SILVER = (192, 192, 192)
        self.LIGHT_GREY = (211, 211, 211)
        self.WHITE = (255, 255, 255)
        self.RED = (255, 0, 0)
        self.GREEN = (0, 255, 0)
        self.BLUE = (0, 0, 255)
        self.LIGHT_BLUE = (0, 255, 255)
        self.YELLOW = (255, 255, 0)
        self.PURPLE = (255, 0, 255)


colors_lib = ColorsLib()


