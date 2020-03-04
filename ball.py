import pygame
import random
import paddle
import os
BALL_IMGS = [pygame.image.load(os.path.join("imgs", "ball1.png"))]
class Ball:
    r=10
    vel = 35
    def __init__(self):
        self.r = 10
        self.x=512-self.r
        self.y=275-self.r
        ran=random.randint(1,2)
        if ran==1: self.vel = -self.vel
        else: self.vel = self.vel
    def move(self):
        self.x+=self.vel 
    
    def draw(self,WIN):
        
        WIN.blit(BALL_IMGS[0],(self.x,self.y))

        
