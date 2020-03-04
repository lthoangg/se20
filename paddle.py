import pygame
import os
import time
WHITE = (255,255,255)
RED = (200,0,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
GREEN = (0,252,0)
YELLOW = (255,255,0)
PINK = (255,0,255)
PURPLE = (152,0,255)

class Paddle:
    width = 15
    height = 100
    vel = 0
    def __init__(self,x=20,y=40):
        self.x = x
        self.y = y

    def move(self):
        self.y+=self.vel
        key_pressed= pygame.key.get_pressed()
        if key_pressed[pygame.K_UP]:
            self.vel=-20
        elif key_pressed[pygame.K_DOWN]:
            self.vel=+20
        elif key_pressed[pygame.KEYUP]:
            self.vel =0

    def draw(self, WIN, color=PINK): 
        if self.y > 551-self.height or self.y<0:
            self.vel=-self.vel
        pygame.draw.rect(WIN ,color,(self.x,self.y,self.width,self.height))
        
