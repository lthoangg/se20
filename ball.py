import pygame
from random import randint
import os
pygame.mixer.init()
BALL_IMGS = [pygame.image.load(os.path.join("imgs/balls", "ball4.png"))]
collideSound = pygame.mixer.Sound(os.path.join('sound','beep.wav'))
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.x = 620
        self.y = 340
        self.r = 20
        self.vx = 8
        self.vy = randint(-4, 4)
        self.image = pygame.transform.scale(BALL_IMGS[0], (2*self.r, 2*self.r))
        self.rect = self.image.get_rect()
    
    def move(self):
        self.rect = self.image.get_rect(center=(self.x + self.r, self.y + self.r))
        self.x += self.vx
        self.y += self.vy
        if self.y <= 0:
            self.vy = abs(self.vy)
            print("wall top")
        if self.y + 2*self.r >= 720:
            self.y = 720 - self.r * 2
            self.vy = - abs(self.vy)
            print("Wall bottom")
    
    def lose(self):
        if self.x <= 0 or self.x >= 1260:
            return True
        else:
            return False

    def draw(self,WIN):        
        WIN.blit(self.image,(self.x,self.y))

    def is_Collide(self, paddle):
        return self.rect.colliderect(paddle.rect)

    def collide(self):
        if self.x < 640:
            self.vx = abs(self.vx)
        else:
            self.vx = -abs(self.vx)
        self.vy = randint(-4, 4)