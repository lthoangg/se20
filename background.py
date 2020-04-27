import pygame
import os
bg_IMGS=[pygame.image.load(os.path.join("imgs/backgrounds", "bg1.png")), pygame.image.load(os.path.join("imgs/backgrounds", "bg2.png")), pygame.image.load(os.path.join("imgs/backgrounds", "bg3.png")), pygame.image.load(os.path.join("imgs/backgrounds", "bg4.png"))]
class Background:
    def __init__(self):
        self.x =0
        self.y =0
        self.bg = bg_IMGS[0]
        
    def draw(self,WIN):
        image = pygame.transform.scale(self.bg,(WIN.get_width(), WIN.get_height()))
        WIN.blit(image,(self.x,self.y))
       