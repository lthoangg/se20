import pygame
import os
bg_IMGS=[pygame.image.load(os.path.join("imgs", "bg2.png"))]
class Background:
    def __init__(self):
        self.x =0
        self.y =0
        self.bg = bg_IMGS[0]
        
    def draw(self,WIN):
        img = pygame.transform.scale(self.bg,(WIN.get_width(), WIN.get_height()))
        WIN.blit(img,(self.x,self.y))