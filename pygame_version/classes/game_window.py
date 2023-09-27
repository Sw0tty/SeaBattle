"""
"""
import os
import ctypes
import pygame

from app_config.settings import ASSETS_DIR


FULL_WINDOW_WIDTH = ctypes.windll.user32.GetSystemMetrics(0)
FULL_WINDOW_HEIGHT = ctypes.windll.user32.GetSystemMetrics(1)


class GameWindow:

    def __init__(self):
        self.WIDTH = FULL_WINDOW_WIDTH / 2
        self.HEIGHT = FULL_WINDOW_HEIGHT / 2
        self.FPS = 30
        self.SCREEN = pygame.display.set_mode((self.WIDTH, self.HEIGHT), pygame.RESIZABLE)
        self.__ICON = pygame.image.load(os.path.join(ASSETS_DIR, 'seabattle_icon.png')).convert()
        self.__WINDOW_TITLE = "MiniSeaBattle"

    def print_window(self):
        while True:
            clock = pygame.time.Clock()
            clock.tick(self.FPS)
            self.SCREEN
            pygame.display.set_caption(self.__WINDOW_TITLE)
            pygame.display.set_icon(self.__ICON)

            stop_game = self.event_controller()

            if stop_game:
                break

            pygame.display.flip()
        

    def event_controller(self):
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT:
                return True
        
        return None


