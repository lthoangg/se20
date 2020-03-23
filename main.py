import pygame
import os
import time
import paddle
import ball
import background

#Drawing graphic
def draw(WIN, bg, p1 , p2 , b ): 
    bg.draw(WIN)
    p1.draw(WIN)
    p2.draw(WIN)
    b.draw(WIN)

#Calculating logical    
def move(p1, p2, b):
    p1.move()
    p2.move()
    b.move()


#Main game
def main(): 
    print("In game")
    pygame.init()
    WIN_WIDTH = 1280 #Screen WIDTH
    WIN_HEIGHT = 720 #Screen HEIGHT
    WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    WIN_ICON = pygame.image.load(os.path.join("imgs", "ball1.png"))

    #pygame.display.set_icon(WIN_ICON)
    pygame.display.set_caption("Game Pong")
    clock = pygame.time.Clock()


    p1 =paddle.Paddle(1, WIN)
    p2 =paddle.Paddle(2, WIN)
    b = ball.Ball(WIN)
    bg = background.Background()

    run = True

    #Game running
    while run: 
        #pygame.draw.rect(WIN,(255,0,0),(10,10,50,50))
        clock.tick(60) #FPS of game
        for event in pygame.event.get():
            # Mouse click
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    print('left')
                elif event.button == 2:
                    print('middle')
                elif event.button == 3:
                    print('right')
                print(str(pygame.mouse.get_pos()[0]) + " " + str(pygame.mouse.get_pos()[1]))
                
                        
            if event.type == pygame.QUIT:
                print("Out game")
                run = False
                pygame.quit()
                quit() 
        
        
        draw(WIN, bg, p1, p2, b)
        move(p1, p2, b)
        pygame.display.update()

if __name__ == "__main__":
    main()