import pygame
import os
import time

PADDLE_IMGS = [pygame.image.load(os.path.join("imgs","paddle2.png"))]

class Paddle:
    width = 15
    height = 100
    vel = 0
    def __init__(self,player, WIN):
        self.player = player
        self.y= 310
        self.img = PADDLE_IMGS[0]
        if self.player ==1:
            self.x = 20
        else:
            self.x = WIN.get_width() - self.img.get_width() - 20

    def move(self):
        self.y+=self.vel
        key_pressed= pygame.key.get_pressed()
        if self.player==1:
            if key_pressed[pygame.K_w]:
                self.vel=-4
            elif key_pressed[pygame.K_s]:
                self.vel=+4

        else:        
            if key_pressed[pygame.K_UP]:
                self.vel=-4
            elif key_pressed[pygame.K_DOWN]:
                self.vel=+4
            
    def draw(self, WIN ):
        if self.y > WIN.get_height()-self.height:
            self.vel=-4
        elif self.y < 0:
            self.vel=4
        WIN.blit(self.img,(self.x,self.y))
