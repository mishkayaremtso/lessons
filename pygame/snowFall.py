import time

import pygame
import random
import sys


max_x = 1366
max_y = 768
max_snow = 100
snow_size = 64


class Snow:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = random.randint(1, 3)
        self.img_num = random.randint(1, 4)
        self.image_filename = "snow" + str(self.img_num) + ".png"
        self.image = pygame.image.load(self.image_filename).convert()
        self.image = pygame.transform.scale(self.image, (snow_size, snow_size))

    def move_snow(self):
        self.y += self.speed
        if self.y > max_y:
            self.y = (0 - snow_size)
        i = random.randint(1, 3)
        if self.y == 1:
            self.x += 1
            if self.x > max_x:
                self.x = (0 - snow_size)
        elif i == 2:
            self.x -= 1
            if self.x < (0 - snow_size):
                self.x = max_x

    def draw_snow(self):
        screen.blit(self.image, (self.x, self.y))


def initialize_snow(max_snow, snowfall):
    for i in range(0, max_snow):
        xx = random.randint(0, max_x)
        yy = random.randint(0, max_y)
        snowfall.append(Snow(xx, yy))


def check_for_Exit():
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            sys.exit()


pygame.init()
screen = pygame.display.set_mode((max_x, max_y))
bg_color = (0, 0, 0)
snowfall = []


initialize_snow(max_snow, snowfall)

while True:
    check_for_Exit()
    screen.fill(bg_color)
    for i in snowfall:
        i.move_snow()
        i.draw_snow()
    time.sleep(0.0020)
    pygame.display.flip()