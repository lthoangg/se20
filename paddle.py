import pygame
import os
import time
import pong

x = 50
y = 50
width = 40
height = 60
vel = 5
run = True
while run:
    keys= pygame.key.get_pressed()
    # if keys[pygame.K_LEFT]:

    # if keys[pygame.K_RIGHT]:

    # if keys[pygame.K_UP]:

    if keys[pygame.K_DOWN]:
        y+=vel
    pygame.draw.rect(WIN, (255,0,0), (x, y, width, height))
    pygame.display.update()

    