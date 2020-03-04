import pygame
import os
import time
BALL_IMGS = [pygame.image.load(os.path.join("imgs", "ball1.png"))]

def main():
    pygame.init
    WIN_WIDTH = WIN_HEIGHT = 600
    WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    pygame.display.set_icon(pygame.image.load(os.path.join("imgs","ball1.png")))
    pygame.display.set_caption("Pong")

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()

main()