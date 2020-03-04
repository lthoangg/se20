import pygame
import os
import time

class Paddle:
    x = 500
    y = 300
    width = 40
    height = 150
    vel = 0
    def move(self):
        keys= pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            y+=20
        if keys[pygame.K_DOWN]:
            y-=20
        pygame.display.update()

    