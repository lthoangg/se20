from itertools import count
import paddle
import Text, Color
class player:
    ID = count(1)
    def __init__(self, name):
        self.name = name
        self.id = next(self.ID)
        self.character = paddle.Paddle(self.id)
        self.score = 0

    def reset(self):
        self.ID = count(1)

    def win_Game(self):
        f = open("MH.txt", "a")
        self.score += 1
        if self.id == 1:
            f.write("Player 1 got point\n")
        if self.id == 2:
            f.write("Player 2 got point\n")
        f.close()
        
    def draw_Score(self, WIN):
        text = str(self.score)
        self.text = Text.text(text, 60, color=Color.gray)
        center_y = int((WIN.get_height()/2) - (self.text.height/2))
        if self.id == 1:
            center_x = int((WIN.get_width()/4) - self.text.width/2)
        if self.id == 2:
            center_x = int(3*WIN.get_width()/4 - (self.text.width/2))
        
        self.text.blit(WIN, (center_x, center_y))

    #def set_Name 