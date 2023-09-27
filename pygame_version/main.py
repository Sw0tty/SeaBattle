"""

"""

import pygame 
import random
import os
import ctypes
import sys
import string
from app_config.settings import *
from classes.game_window import GameWindow


game_window = GameWindow()

game = True
while game:
    # clock.tick(FPS)
    # game_window.print_window() 
    
    # for event in pygame.event.get(): 
    #     if event.type == pygame.QUIT:
    #         game = False

    # pygame.display.flip()

    game_window.print_window()
