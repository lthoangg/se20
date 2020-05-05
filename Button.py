import Text, Frame

class button:
    def __init__(self, text, text_size=25, frameType=2):
        self.passage = text
        self.text_size = text_size
        self.text = Text.text(self.passage, self.text_size)
        self.frame = Frame.frame(frameType)
        self.rect = self.frame.frame.get_rect()

    def draw(self, screen, position = None):
        if position is None: # Draw at center of screen
            self.frame.blit_center(screen)
        elif position == 0: # Draw at center bottom of screen
            self.frame.blit_center_bottom(screen)
        elif position == 1: # Draw at center top of screen
            self.frame.blit_center_top(screen)
        elif position == 2: # Draw at bottom left of screen
            position = (0, 720 - self.frame.height)
            self.frame.blit(screen, position)
        elif position == 3: # Draw at bottom right of screen
            position = (1280 - self.frame.width, 720 - self.frame.height)
            self.frame.blit(screen, position)
        else: # Draw at position we want
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

    def update_Text(self, text):
        passage = text
        temp = Text.text(passage, self.text_size)
        if temp.width <= self.frame.width:
            self.text = temp
        else:
            pass
        