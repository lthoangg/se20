import pygame
import os
import time
import paddle
import ball
import background

def draw(WIN, bg, p1 , p2 , b ): #The graphic part
    bg.draw(WIN)
    p1.draw(WIN)
    p2.draw(WIN)
    b.draw(WIN)
    
def move(p1, p2, b): #The math part 
    p1.move()
    p2.move()
    b.move()

def main(): #The main game
    pygame.init()
    WIN_WIDTH = 1024 #Screen WIDTH
    WIN_HEIGHT = 551 #Screen HEIGHT
    WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    WIN_ICON = pygame.image.load(os.path.join("imgs", "ball1.png"))

    pygame.display.set_icon(WIN_ICON)
    pygame.display.set_caption("Pong")
    clock = pygame.time.Clock()


    p1 =paddle.Paddle(1)
    p2 =paddle.Paddle(2)
    b = ball.Ball()
    bg = background.Background()

    run = True

    #Game running
    while run: 
        #pygame.draw.rect(WIN,(255,0,0),(10,10,50,50))
        clock.tick(30) #FPS of game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit() 
        pygame.display.update()
        
        draw(WIN, bg, p1, p2, b)
        move(p1, p2, b)
        


main()