import pygame
import os
import time
WHITE = (255,255,255)
RED = (200,0,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
GREEN = (0,252,0)
YELLOW = (255,255,0)
PINK = (255,0,255)
PURPLE = (152,0,255)
colors = [ WHITE, RED, BLUE, BLACK, GREEN, YELLOW, PINK, PURPLE ]

PADDLE_IMGS = [pygame.image.load(os.path.join("imgs","paddle.png"))]
global colors
class Paddle:
    width = 15
    height = 100
    vel = 0
    def __init__(self,player):
        self.player = player
        self.y= 40
        self.img = PADDLE_IMGS[0]
        if self.player ==1:
            self.x = 20
        else:
            self.x = 989


    def move(self):
        self.y+=self.vel
        key_pressed= pygame.key.get_pressed()
        if self.player==1:
            if key_pressed[pygame.K_w]:
                self.vel=-20
            elif key_pressed[pygame.K_s]:
                self.vel=+20
            elif key_pressed[pygame.KEYUP]:
                player.vel =0
        else:
            if key_pressed[pygame.K_UP]:
                self.vel=-20
            elif key_pressed[pygame.K_DOWN]:
                self.vel=+20
            elif key_pressed[pygame.KEYUP]:
                player.vel =0

    def draw(self, WIN, color=colors[7]):
        if self.y > 551-self.height:
            self.vel=-20
        elif self.y < 0:
            self.vel=20
        #pygame.draw.rect(WIN ,color,(self.x,self.y,self.width,self.height))
        WIN.blit(self.img,(self.x,self.y))
  #  def get_mask(self):
        # return pygame.mask.from_surface()
