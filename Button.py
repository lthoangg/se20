import Text, Frame

class button:
    def __init__(self, text, frameType):
        self.text = Text.text(text)
        self.frame = Frame.frame(frameType)
        self.rect = self.frame.frame.get_rect()

    def draw(self, screen):
        self.frame.blit_center(screen)
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
