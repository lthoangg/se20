import pygame
import os
import time
PADDLE_IMGS = [pygame.image.load(os.path.join("imgs/paddles","paddle1.png")), pygame.image.load(os.path.join("imgs/paddles","paddle2.png")), pygame.image.load(os.path.join("imgs/paddles","paddle3.png")), pygame.image.load(os.path.join("imgs/paddles","paddle4.png")), pygame.image.load(os.path.join("imgs/paddles","paddle5.png")), pygame.image.load(os.path.join("imgs/paddles","paddle6.png")), pygame.image.load(os.path.join("imgs/paddles","paddle7.png")), pygame.image.load(os.path.join("imgs/paddles","paddle8.png"))]

class Paddle(pygame.sprite.Sprite):
    def __init__(self, player=1):
        pygame.sprite.Sprite.__init__(self)
        self.image = PADDLE_IMGS[3]
        self.rect = self.image.get_rect()
        self.player = player
        self.vel =0
        self.width = self.rect[2]
        self.height= self.rect[3]
        if self.player==1:
            self.x = 20
        elif self.player ==2:
            self.x = 1280 - self.width - 20
        self.y = 310


    def move(self):
        self.rect = self.image.get_rect(center=(self.x + int(self.width/2), self.y + int(self.height/2)))
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
        WIN.blit(self.image,(self.x,self.y))
