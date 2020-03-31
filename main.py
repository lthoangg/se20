import pygame
import os
import time
import paddle
import ball
import background

display_width = 1280
display_height = 720

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 200, 0)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)

block_color = (53, 115, 255)

windows = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Ping Pong')
clock = pygame.time.Clock()


# Drawing graphic
def draw(WIN, bg, p1, p2, b):
    bg.draw(WIN)
    b.draw(WIN)
    p1.draw(WIN)
    p2.draw(WIN)


# Calculating logical
def move(p1, p2, b):
    p1.move()
    p2.move()
    b.move()


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(windows, ac, (x, y, w, h))

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(windows, ic, (x, y, w, h))

    smallText = pygame.font.SysFont("comicsansms", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), y + (h / 2))
    windows.blit(textSurf, textRect)

#Main menu
def game_intro():
    #background_image = pygame.image.load("imgs", "menu.png")

    pygame.init()
    intro = True

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        windows.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects("Ping Pong", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2))
        windows.blit(TextSurf, TextRect)

        button("GO!", 450, 450, 100, 50, green, bright_green, main)
        button("Quit", 750, 450, 100, 50, red, bright_red, exit)

        pygame.display.update()
        clock.tick(15)


# Main game
def main():
    print("In game")
    pygame.init()
    WIN_WIDTH = 1280  # Screen WIDTH
    WIN_HEIGHT = 720  # Screen HEIGHT
    WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
    WIN_ICON = pygame.image.load(os.path.join("imgs", "ball1.png"))

    # pygame.display.set_icon(WIN_ICON)
    clock = pygame.time.Clock()

    p1 = paddle.Paddle(1, WIN)
    p2 = paddle.Paddle(2, WIN)
    b = ball.Ball(WIN)
    bg = background.Background()

    run = True

    # Game running
    while run:
        # pygame.draw.rect(WIN,(255,0,0),(10,10,50,50))
        clock.tick(30)  # FPS of game
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

            # Quit button            
            if event.type == pygame.QUIT:
                print("Out game")
                run = False
                pygame.quit()
                quit()

        if b.collide(p1) is True or b.collide(p2) is True:
            pass

        draw(WIN, bg, p1, p2, b)
        move(p1, p2, b)
        pygame.display.update()


game_intro()
main()
pygame.quit()
quit()
