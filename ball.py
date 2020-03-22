import pygame
import random
import paddle
import os
import time
BALL_IMGS = [pygame.image.load(os.path.join("imgs", "ball1.png"))]
class Ball:
    r=10
    vel = 25
    def __init__(self):
        self.r = 10
        self.x=512-self.r
        self.y=275-self.r
<<<<<<< HEAD

        self.img = pygame.transform.scale(BALL_IMGS[0],(40,40))

        rd=random.randint(1,2)
        if rd==1: self.vel = -self.vel
=======
        
        self.img = pygame.transform.scale(BALL_IMGS[0],(40,40))

        ran=random.randint(1,2)
        if ran==1: self.vel = -self.vel
>>>>>>> paddle
        else: self.vel = self.vel
    def move(self):
        self.x+=self.vel
        if self.x <=0 or self.x >=1024:
            self.vel = -self.vel
    
    def draw(self,WIN):
<<<<<<< HEAD
        WIN.blit(self.img,(self.x,self.y))
=======
        
        WIN.blit(self.img,(self.x,self.y))

        
>>>>>>> paddle
