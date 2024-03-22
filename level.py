import pygame
from helper import *

clock = pygame.time.Clock()
background = pygame.image.load("assets/level/background.jpg")
main_ship = pygame.image.load("assets/ships/main_ship.png")
rocket = pygame.image.load("assets/ships/rocket.png")
#Background pos
bg_y_pos = 0
#Ship poses and charac
ms_x_pos = WIDTH / 2 - main_ship.get_width() / 2
ms_y_pos = HEIGHT - main_ship.get_height()
ship_speed = 10
#Rocket pose and charac
rockets = []
r_speed = 15
last_shot_time = 0
def showLevel(screen):
    pressed_key = pygame.key.get_pressed()
    clock.tick(25)
    global bg_y_pos
    global ms_x_pos
    global rockets
    global last_shot_time
    screen.blit(background, (0, bg_y_pos + 0))
    screen.blit(background, (0, bg_y_pos + (-HEIGHT)))
    bg_y_pos += 2
    if bg_y_pos == HEIGHT:
        bg_y_pos = 0

    if pressed_key[pygame.K_l] and pygame.time.get_ticks() - last_shot_time > 500:  # Проверка прошедшего времени
        rockets.append((ms_x_pos + main_ship.get_width() / 2 - rocket.get_width() / 2, ms_y_pos))
        last_shot_time = pygame.time.get_ticks()  # Обновление времени последнего выстрела

        # Обновление и отрисовка ракет
    updated_rockets = []  # Создаем новый список для обновленных позиций ракет
    for r in rockets:
        screen.blit(rocket, r)
        r = (r[0], r[1] - r_speed)
        if r[1] > -rocket.get_height():  # Проверяем, не вышла ли ракета за верхний край экрана
            updated_rockets.append(r)  # Если нет, добавляем ее в новый список
    rockets = updated_rockets  # Обновляем список ракет

    screen.blit(main_ship, (ms_x_pos, ms_y_pos))
    if pressed_key[pygame.K_a] and ms_x_pos > 0:
        ms_x_pos -= ship_speed
    elif pressed_key[pygame.K_d] and ms_x_pos < WIDTH - main_ship.get_width():
        ms_x_pos += ship_speed


