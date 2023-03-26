# --------||--Скелет для PyGame--||-----------
# Скелет содержит в себе базовый набор для запуска окна и его редактирования
# Также имеет готовый 1 спрайт, который отрисовывается по центру окна

import pygame  # Предварительно установить: pip install pygame
import random
import os

# ----------Настройка папки ассетов-----------
project_folder = os.path.dirname(__file__)  # Сокращенная запись для указания папки с проектом
images_folder = os.path.join(project_folder, 'images')  # Соединение пути и папки в проекте
# ----------------------------

WIDTH = 920  # Ширина окна
HEIGHT = 680  # Высота окна
FPS = 30  # Частота обновления кадров

# -----Библиотека цветов----- (R, G, B)
BLACK = (0, 0, 0)
SILVER = (192, 192, 192)
LIGHT_GREY = (211, 211, 211)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
LIGHT_BLUE = (0, 255, 255)
YELLOW = (255, 255, 0)
PURPLE = (255, 0, 255)
# --------------------------------------

# --------Глобальные перменные--------
# ------------------------------------

# -------1--Создание окна--1----------
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# ---Инициализация изображений---
icon_img = pygame.image.load(os.path.join(images_folder, 'seabattle_icon.png')).convert()  # Загрузки фото из папки
# -------------------------------

pygame.display.set_caption("SeaBattle")  # Надпись
pygame.display.set_icon(icon_img)  # Иконка
clock = pygame.time.Clock()
# -------1----------1------


# ----------Классы для спрайтов------------
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)  # Строка для запуска инициализатора встроенных классов Sprite

        self.image = pygame.Surface((80, 50))
        self.image.fill(LIGHT_BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)


    def player_update(self):
        pass


class Text(pygame.sprite.Sprite):
    def __init__(self, text, size, color, width, height):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        self.font = pygame.font.SysFont("Arial", size)
        self.textSurf = self.font.render(text, 1, color)
        self.image = pygame.Surface((width, height))
        self.image.fill(BLUE)
        self.image.blit(self.textSurf, [width / 2 - self.textSurf.get_width() / 2,
                                        height / 2 - self.textSurf.get_height() / 2])

        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
# -----------------------------------------


# -------Добавление спрайтов----------
all_sprites = pygame.sprite.Group()
text = Text("Выход", 20, GREEN, 50, 20)
player = Player()
all_sprites.add(player)
all_sprites.add(text)
# ------------------------


# ---------2--Цикл игры--2----------
running = True
while running:
    # ---------Задание скорости FPS---------
    clock.tick(FPS)
    # --------------------------------------

    # ---------Обработчик событий-----------
    for event in pygame.event.get():  # Цикл всех событий
        if event.type == pygame.QUIT:  # Проверка закрытия окна
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            if player.rect.collidepoint(x, y):
                running = False
    # --------------------------------------

    # ---------Обновление---------
    player.player_update()  # Функция заглушка для отображения. Эквивалент update()
    text.update()
    # ----------------------------

    # -------Отрисовка-------
    screen.fill(LIGHT_GREY)  # Заливка фона
    all_sprites.draw(screen)  # Отрисвока спрайтов
    pygame.display.flip()  # После отрисовки всего, переворачиваем экран
    # ---------------------

# -------2----------2------
pygame.quit()  # Закрытие окна
# -----||----Конец скелета----||-------
