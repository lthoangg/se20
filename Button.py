import Text, Frame

class button:
    def __init__(self, text, text_size=25, frameType=2):
        self.text = Text.text(text,text_size)
        self.frame = Frame.frame(frameType)
        self.rect = self.frame.frame.get_rect()
        print(self.text.width, self.text.height ,self.frame.frame.get_height())

    def draw(self, screen, position = None):
        if position is None:
            self.frame.blit_center(screen)
        elif position == 0:
            self.frame.blit_center_bottom(screen)
        elif position == 1:
            self.frame.blit_center_top(screen)
        else:
            self.frame.blit(screen, position)
        self.text.blit_center_frame(screen, self.frame)

    def is_Click(self, mouse_pos):
        (x, y) = mouse_pos
        center_x = self.frame.x + int(self.frame.width/2)
        center_y = self.frame.y + int(self.frame.height/2)
        self.rect = self.frame.frame.get_rect(center=(center_x, center_y))
        if self.rect.collidepoint(x, y):
            return True
        else:
            return False

    def is_Hover(self, mouse_pos):
        (x, y) = mouse_pos
        center_x = self.frame.x + int(self.frame.width/2)
        center_y = self.frame.y + int(self.frame.height/2)
        self.rect = self.frame.frame.get_rect(center=(center_x, center_y))
        if self.rect.collidepoint(x, y):
            self.frame.is_Hover(True)
        else:
            self.frame.is_Hover(False)
