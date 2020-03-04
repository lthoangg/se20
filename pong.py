import pygame
import os
import time
import paddle
import ball
BALL_IMGS = [pygame.image.load(os.path.join("imgs", "ball1.png"))]
bg_IMGS=[pygame.image.load(os.path.join("imgs", "bg1.png"))]
def main():
    pygame.init()
    WIN_WIDTH = 1024
    WIN_HEIGHT = 551
    WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    WIN_ICON = BALL_IMGS[0]
    pygame.display.set_icon(WIN_ICON)
    pygame.display.set_caption("Pong")
    clock = pygame.time.Clock()


    p1 =paddle.Paddle(1)
    p2 =paddle.Paddle(2)
    b = ball.Ball()
    run = True
    while run:
        WIN.blit(bg_IMGS[0],(0,0))

        p1.move()
        p2.move()
        b.move()
        #pygame.draw.rect(WIN,(255,0,0),(10,10,50,50))
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
        p1.draw(WIN)
        p2.draw(WIN)
        b.draw(WIN)
        pygame.display.update()


main()