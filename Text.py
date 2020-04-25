import pygame
import Color
import Font
pygame.init()

class text:
    def __init__(self, text="", size=25, color = Color.black, font=Font.Courier):
        if size is None:
            self.size = 25
        else: 
            self.size = size
        self.font = font
        self.color = color
        self.text = text
        self.position = (0, 0)
        self.Font = pygame.font.SysFont(self.font, self.size)
        self.Text = self.Font.render(self.text, True, self.color)
        (self.width, self.height) = self.Font.size(self.text)

    def blit_center_frame(self, screen, frame):
        center_point_x = frame.x + int(frame.width/2) - int(self.width/2)
        center_point_y = frame.y + int(frame.height/2) - int(self.height/2)
        center_point = (center_point_x, center_point_y)
        return self.blit(screen, center_point)

    def set_Text(self, text):
        self.text = text
        self.Text = self.Font.render(self.text, True, self.color)
        (self.width, self.height) = self.Font.size(self.text)

    # def blit_left_frame(self, screen, frame):
    #     left_point_x = frame.x + self.Font.size("  ")[0]
    #     center_point_y = frame.y + int(frame.height/2) - int(self.height/2)
    #     point = (left_point_x, center_point_y)
    #     return self.blit(screen, point)

    # def blit_right_frame(self, screen, frame):
    #     right_point_x = frame.x + frame.width - self.Font.size("  ")[0] - self.width
    #     center_point_y = frame.y + int(frame.height/2) - int(self.height/2)
    #     point = (right_point_x, center_point_y)
    #     return self.blit(screen, point)

    def blit_center(self, screen):
        center_point_x = int(screen.get_width()/2) - int(self.width/2)
        center_point_y = int(screen.get_height()/2) - int(self.height/2)
        center_point = (center_point_x, center_point_y)
        return self.blit(screen, center_point)

    def blit(self, screen, position):
        screen.blit(self.Text, position)
    
