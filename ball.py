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
        #if self.collide(paddle):
        #    self.vel = -self.vel
    
    def draw(self,WIN):        
        WIN.blit(self.img,(self.x,self.y))

    def collide(self, paddle):
        paddle_mask = paddle.get_mask()
        mask = pygame.mask.from_surface(self.img)
        offset = ( round(self.x) - paddle.x, round(self.y) - paddle.y)

        point = paddle_mask.overlap(mask, offset)
        print(point)
        if point is not None:
            print('collide')
            return True
        else:
            return False


        
