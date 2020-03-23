import pygame
import os
import time

PADDLE_IMGS = [pygame.image.load(os.path.join("imgs","paddle.png"))]

class Paddle:
    width = 15
    height = 100
    vel = 10
    def __init__(self,player, WIN):
        self.player = player
        self.y= 40
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
                self.vel=-10
            elif key_pressed[pygame.K_s]:
                self.vel=+10

        else:        
            if key_pressed[pygame.K_UP]:
                self.vel=-10
            elif key_pressed[pygame.K_DOWN]:
                self.vel=+10
            
    def draw(self, WIN ):
        if self.y > WIN.get_height()-self.height:
            self.vel=-10
        elif self.y < 0:
            self.vel=10
        WIN.blit(self.img,(self.x,self.y))


    def get_mask(self):
        return pygame.mask.from_surface(self.img)
