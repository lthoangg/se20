import os
import pygame

big_title = pygame.image.load(os.path.join("imgs/frames/", "frame.png"))
med_title = pygame.transform.scale(big_title, ((int(big_title.get_width()/2), int(big_title.get_height()/2))))
small_title = pygame.transform.scale(med_title, ((int(med_title.get_width()/2), int(med_title.get_height()/2))))
square_title = pygame.transform.scale(small_title, ((int(small_title.get_width()/2), int(small_title.get_width()/2))))

class frame:
    def __init__(self,size=3, x=0, y=0):
        self.x = x
        self.y = y
        self.position = (self.x , self.y)
        if size <=0: # Square
            self.frame = square_title
        elif size==1: # Small
            self.frame = small_title
        elif size==2: # Medium
            self.frame = med_title
        else: # >=3 -> Big
            self.frame = big_title

        self.width = self.frame.get_width()
        self.height = self.frame.get_height()
    
    def is_Hover(self, is_hover):
        if is_hover == True:
            self.temp =self.frame
            self.frame = None
        else:
            self.frame = self.temp
        

    def blit_center_top(self, screen):
        self.x = int(screen.get_width()/2) - int(self.width/2)
        self.y = 20
        center_top = (self.x, self.y)
        return self.blit(screen, center_top)
        
    def blit_center(self, screen):
        self.x = int(screen.get_width()/2) - int(self.width/2)
        self.y = int(screen.get_height()/2) - int(self.height/2)
        center = (self.x, self.y)
        return self.blit(screen, center)
    
    def blit_center_bottom(self, screen):
        self.x = int(screen.get_width()/2) - int(self.width/2)
        self.y = int(screen.get_height()) - self.height - 20
        center_bottom = (self.x , self.y)
        return self.blit(screen, center_bottom)

    def blit(self, screen, position):
        screen.blit(self.frame, position)
