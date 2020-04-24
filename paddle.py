import pygame
import os
import time

PADDLE_IMGS = [pygame.image.load(os.path.join("imgs/paddles","paddle1.png"))]

class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = PADDLE_IMGS[0]
        self.rect = self.image.get_rect()

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
            
    def draw(self, WIN):
        if self.y > WIN.get_height()-self.height:
            self.vel=-4
        elif self.y < 0:
            self.vel=4
        WIN.blit(self.imgage,(self.x,self.y))
