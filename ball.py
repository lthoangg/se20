import pygame
import random
import os
import time
pygame.mixer.init()
BALL_IMGS = [pygame.image.load(os.path.join("imgs", "ball1.png"))]
collideSound = pygame.mixer.Sound('beep.wav')

class Ball:
    r=20
    vx = 5
    def __init__(self, WIN):
        self.WIN = WIN
        self.x= WIN.get_width()/2 - self.r
        self.y= WIN.get_height()/2 - self.r
        self.vy = random.randint(-4,5)
        self.img = pygame.transform.scale(BALL_IMGS[0],(2*self.r, 2*self.r))
        ran=random.randint(1,2)
        if ran==1: self.vx = - self.vx
        
        ran = random.randint(1, 9)
        print(ran)
        if ran <= 4:
            self.vy = ran 
        else: self.vy = ran - 9
    


    def move(self):
        self.x += self.vx
        self.y += self.vy
        if self.y <= 0:
            self.vy = abs(self.vy)
            print("wall top")
        if self.y + 2*self.r == 720:
            self.vy = - abs(self.vy)
            print("Wall bottom")

    def draw(self,WIN):        
        WIN.blit(self.img,(self.x,self.y))



    def collide(self, paddle):

        # Left: 35
        # Right: 1205
        if paddle.y+100 > self.y >= paddle.y:
            if paddle.player == 1 and self.x == 35:
                print("left")
                self.vx = -self.vx
                
                ran = random.randint(1, 9)
                print(ran)
                if ran <= 4:
                    self.vy = ran
                else: self.vy = ran - 9
                collideSound.play()
            if paddle.player == 2 and self.x == 1205:
                print("Right")
                self.vx = -self.vx

                ran = random.randint(1, 9)
                print(ran)
                if ran <= 4:
                    self.vy = ran 
                else: self.vy = ran - 9
                collideSound.play()

    def lose(self):
        if self.x <= 0:
            draw.clear()
            p2.score += 1
        if self.x >= self.WIN.get_width() - self.r*2:
            draw.clear()
            p1.score += 1