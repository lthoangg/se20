import pygame
import random
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
        self.x+=vel 
    
    def draw(self,WIN,color):

        pygame.draw.circle(WIN, color, (self.x , self.y), self.r)
        
        
