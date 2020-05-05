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
        if randint(0, 1) == 1:
            self.vx = -self.vx
        else:
            pass
        self.vy = self.reset_vy()
        self.image = pygame.transform.scale(BALL_IMGS[0], (2*self.r, 2*self.r))
        self.rect = self.image.get_rect()
    def move(self):
        self.rect = self.image.get_rect(center=(self.x + self.r, self.y + self.r))
        self.x += self.vx
        self.y += self.vy
        if self.y <= 0:
            self.vy = abs(self.vy)
        if self.y + 2*self.r >= 720:
            self.y = 720 - self.r * 2
            self.vy = - abs(self.vy)

    def reset_vy(self):
        return randint(-4, 4)

    def reset(self):
        self.vx = -self.vx
        self.x = 620
        self.y = 340
        self.vy = self.reset_vy()

    def draw(self,WIN):        
        WIN.blit(self.image,(self.x,self.y))

    def is_Collide(self, paddle):
        return self.rect.colliderect(paddle.rect)

    def collide(self):
        #collideSound.play()
        if self.x < 640:
            self.vx = abs(self.vx)
        else:
            self.vx = -abs(self.vx)
        self.vy = self.reset_vy()

    def is_Over_Left(self):
        if self.x <=0:
            self.reset()
            return True
        else:
            return False

    def is_Over_Right(self):
        if self.x >= 1260:
            self.reset()
            return True
        else:
            return False

    def is_Over(self):
        if self.x <= 0 or self.x >= 1260:
            return True

