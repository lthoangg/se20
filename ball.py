import pygame
import random
import paddle
import os
import time
BALL_IMGS = [pygame.image.load(os.path.join("imgs", "ball1.png"))]
class Ball:
    r=20
    vel = 12
    def __init__(self, WIN):
        self.WIN = WIN
        self.x= WIN.get_width()/2 - self.r
        self.y= WIN.get_height()/2 - self.r
        
        self.img = pygame.transform.scale(BALL_IMGS[0],(2*self.r, 2*self.r))

        ran=random.randint(1,2)
        if ran==1: self.vel = -self.vel
        else: self.vel = self.vel
    def move(self):
        self.x+=self.vel
        if self.x <=0 or self.x >= self.WIN.get_width() - self.r*2:
            self.vel = -self.vel
    
    def draw(self,WIN):
        
        WIN.blit(self.img,(self.x,self.y))

        
