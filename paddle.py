import pygame
import os
import time

class Paddle:
    width = 40
    height = 150
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


    def draw(self, WIN): 
        pygame.draw.rect(WIN ,(255,0,0),(self.x,self.y,self.width,self.height))
        

    