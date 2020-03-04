import pygame
import os
bg_IMGS=[pygame.image.load(os.path.join("imgs", "bg1.png"))]
class Background:
    def __init__(self):
        self.x =0
        self.y =0
        self.bg = bg_IMGS[0]
    def draw(self,WIN):
        WIN.blit(self.bg,(self.x,self.y))