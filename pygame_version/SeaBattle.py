"""
!--Not done--!
"""

import pygame 
import random
import os
import ctypes
import sys
import string
from app_config.settings import *
from classes.game_window import GameWindow



FULL_WIDTH = ctypes.windll.user32.GetSystemMetrics(0)  # Полная ширина экрана пользователя
FULL_HEIGHT = ctypes.windll.user32.GetSystemMetrics(1)  # Полная высота экрана пользователя
WIDTH = FULL_WIDTH / 2  # Ширина окна по умолчанию
HEIGHT = FULL_HEIGHT / 2  # Высота окна по умолчанию
# WIDTH = 920  # Ширина окна
# HEIGHT = 680  # Высота окна
FPS = 30  # Частота обновления кадров

# --------Глобальные перменные--------
HP = 11  # Жизни всех кораблей
check_fullscreen = 1
check_sprite = 0
# ------------------------------------

# -------1--Создание окна--1----------
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# ---Инициализация изображений---
icon_img = pygame.image.load(os.path.join(ASSETS_DIR, 'seabattle_icon.png')).convert()  # Загрузки фото из папки
# -------------------------------

pygame.display.set_caption("MiniSeaBattle")  # Надпись
pygame.display.set_icon(icon_img)  # Иконка
clock = pygame.time.Clock()
# -------1----------1------


# ----------Классы для спрайтов------------
class FullScreen(pygame.sprite.Sprite):
    def __init__(self, text, size, color, width, height):
        pygame.sprite.Sprite.__init__(self)

        self.font = pygame.font.SysFont("Arial", size)
        self.textSurf = self.font.render(text, 1, color)
        self.image = pygame.Surface((width, height))
        self.image.fill(colors_lib.GREEN)
        self.image.blit(self.textSurf, [width / 4 - self.textSurf.get_width() / 4,
                                        height / 4 - self.textSurf.get_height() / 4])

        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 4, HEIGHT / 4)


class Ship(pygame.sprite.Sprite):
    def __init__(self, X, Y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((45, 45))
        self.image.fill(colors_lib.LIGHT_GREY)
        self.rect = self.image.get_rect()
        self.X = X
        self.Y = Y
        self.rect.center = (X / 2, Y / 2)

    def check_click(self, mouse, press_ship, color):
        print(type(ship_position[0][1]))
        if self.rect.collidepoint(mouse) and color == colors_lib.BLUE:
            self.image.fill(colors_lib.LIGHT_GREY)
            ship_position[0][0] = colors_lib.LIGHT_GREY
        elif self.rect.collidepoint(mouse) and color == colors_lib.LIGHT_GREY:
            self.image.fill(colors_lib.BLUE)
            ship_position[0][0] = colors_lib.BLUE


class Line(pygame.sprite.Sprite):  # Полоса для поля боя
    def __init__(self, line_w, line_h, X, Y):
        pygame.sprite.Sprite.__init__(self)
        self.line_w = line_w
        self.line_h = line_h
        self.image = pygame.Surface((line_w, line_h))  # Размеры
        self.image.fill(colors_lib.BLACK)
        self.rect = self.image.get_rect()
        self.X = X
        self.Y = Y
        self.rect.center = (X / 2, Y / 2)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)  # Строка для запуска инициализатора встроенных классов Sprite

        self.image = pygame.Surface((80, 50))
        self.image.fill(colors_lib.LIGHT_BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)


    def player_update(self):
        pass


class Text(pygame.sprite.Sprite):
    def __init__(self, text, size, color, width, height):
        pygame.sprite.Sprite.__init__(self)

        self.font = pygame.font.SysFont("Arial", size)
        self.textSurf = self.font.render(text, 1, color)
        self.image = pygame.Surface((width, height))
        self.image.fill(colors_lib.BLUE)
        self.image.blit(self.textSurf, [width / 2 - self.textSurf.get_width() / 2,
                                        height / 2 - self.textSurf.get_height() / 2])

        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
# -----------------------------------------


# -------Добавление спрайтов----------
all_sprites = pygame.sprite.Group()
ship_sprites = pygame.sprite.Group()
text = Text("Выход", 20, colors_lib.GREEN, 50, 20)
player = Player()
fullscreen = FullScreen("Выход", 20, colors_lib.BLUE, 50, 20)


ship_pos_x = 50
ship_pos_y = 50
ship_id = 0
ship_status = 0
ship_position = []
for i in range(6):
    ship_pos_y += 100
    for j in range(6):
        ship_id += 1
        ship_pos_x += 100
        ship = Ship(ship_pos_x, ship_pos_y)
        #ship_position.append([ship_id, ship, ship_status])
        ship_position.append([colors_lib.LIGHT_GREY, ship.X, ship.Y])
        ship_sprites.add(ship)
    ship_pos_x = 50


line_pos_x = 0
line_pos_y = 0
for i in range(6):
    line_pos_x += 100
    line_pos_y += 100
    vertical_line = Line(1, 350, line_pos_x, 350)
    horizontal_line = Line(350, 1, 350, line_pos_y)
    all_sprites.add(vertical_line)
    all_sprites.add(horizontal_line)

# text_line = Line(350, 1, 350, 100)  # Ширина, длина, X, Y


#all_sprites.add(fullscreen)
all_sprites.add(player)
all_sprites.add(text)
# ------------------------

# Game logic
def game_logic():
    # ---------Обработчик событий-----------
        count21 = 1
        for event in pygame.event.get():  # Цикл всех событий
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if player.rect.collidepoint(x, y):
                    return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                for i in ship_sprites:
                    i.check_click(event.pos, press_ship=ship_position[0][1], color=ship_position[0][0])

                    # if count21 == 1:
                    #     count21 += 1
                    #     print(ship_position[1] == ship_position[2])
                    #     print(count21)






            if event.type == pygame.QUIT:
                return False
        # --------------------------------------

        # ---------Обновление---------

        player.player_update()  # Функция заглушка для отображения. Эквивалент update()
        text.update()
        ship_sprites.update()
        # ----------------------------

        # -------Отрисовка-------
        screen.fill(colors_lib.LIGHT_GREY)  # Заливка фона

        a = [i for i in string.ascii_uppercase[0:6]]
        b = "   "
        d = "   "

        f1 = pygame.font.Font(None, 50)  # Шрифт, размер

        # Следующая строка присваивает перменной text1 первые 6 букв словаря
        text1 = f1.render(b.join(map(str, (i for i in string.ascii_uppercase[0:6]))), True, colors_lib.BLACK)

        text2 = f1.render(d.join(map(str, (abs(i) for i in range(-6, 0)))), True, colors_lib.BLACK)
        text2 = pygame.transform.rotate(text2, 90)

        screen.blit(text1, (60, 10))  # Позиция
        screen.blit(text2, (10, 70))  # Позиция

        ship_sprites.draw(screen)
        all_sprites.draw(screen)  # Отрисвока спрайтов
        pygame.display.flip()  # После отрисовки всего, переворачиваем экран
        return True
        # ---------------------

# Game runner
def runner(game_logic_func):
    GAME_RUNING = True
    while GAME_RUNING:
        clock.tick(FPS)
        GAME_RUNING = game_logic_func()
    pygame.quit()

# runner(game_logic)

game_window = GameWindow()

while True:
    clock.tick(FPS)
    game_window.print_window()
    
    
    for event in pygame.event.get(): 
        pass
        # if event.type == pygame.QUIT:
            # return False
    pygame.display.flip()
