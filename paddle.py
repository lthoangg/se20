import pygame
import os
import time
PADDLE_IMGS = [pygame.image.load(os.path.join("imgs/paddles","paddle1.png")), pygame.image.load(os.path.join("imgs/paddles","paddle2.png")), pygame.image.load(os.path.join("imgs/paddles","paddle3.png")), pygame.image.load(os.path.join("imgs/paddles","paddle4.png")), pygame.image.load(os.path.join("imgs/paddles","paddle5.png")), pygame.image.load(os.path.join("imgs/paddles","paddle6.png")), pygame.image.load(os.path.join("imgs/paddles","paddle7.png")), pygame.image.load(os.path.join("imgs/paddles","paddle8.png"))]

class Paddle(pygame.sprite.Sprite):
    def __init__(self, player=1):
        pygame.sprite.Sprite.__init__(self)
        self.image = self.PADDLE_IMGS[0]
        self.rect = self.image.get_rect()
        self.player = player
        if self.player==1:
            self.x = 20
        elif self.player ==2:
            self.x = 685
        self.y = 310
        self.vel =0

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
