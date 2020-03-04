import pygame
import os
import time
import paddle
BALL_IMGS = [pygame.image.load(os.path.join("imgs", "ball1.png"))]

def main():
    pygame.init()
    WIN_WIDTH = WIN_HEIGHT = 600
    WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    WIN_ICON = BALL_IMGS[0]
    pygame.display.set_icon(WIN_ICON)
    pygame.display.set_caption("Pong")
    clock = pygame.time.Clock()

    p1 =paddle.Paddle()
    run = True
    while run:
        
        p1.move()
        #pygame.draw.rect(WIN,(255,0,0),(10,10,50,50))
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
        p1.draw(WIN)
        pygame.display.update()


main()