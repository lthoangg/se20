import pygame
import os
import time
import paddle
import ball
import background
import Color

pygame.init()
display_width = 1280
display_height = 720

#block_color = (53, 115, 255)

windows = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Ping Pong')


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
    b.collide(p1)
    b.collide(p2)


def text_objects(text, font):
    textSurface = font.render(text, True, Color.black)
    return textSurface, textSurface.get_rect()


def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(windows, ac, (x, y, w, h))

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(windows, ic, (x, y, w, h))

    smallText = pygame.font.SysFont("comicsansms", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + int(w / 2)), y + int(h / 2))
    windows.blit(textSurf, textRect)

#Main menu
def menu():
    background_image = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "menu.png")))

    pygame.init()
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        windows.fill(Color.white)
        windows.blit(background_image,(300, 50))
        largeText = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects("Ping Pong", largeText)
        TextRect.center = (int(display_width / 2), int(display_height / 2))
        windows.blit(TextSurf, TextRect)

        button("GO!", 450, 450, 100, 50, Color.green, Color.bright_green, main)
        button("Quit", 750, 450, 100, 50, Color.red, Color.bright_red, exit)

        pygame.display.update()


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
        clock.tick(120)  # FPS of game
        for event in pygame.event.get():
            # Quit button            
            if event.type == pygame.QUIT:
                print("Out game")
                run = False
                pygame.quit()
                quit()

        draw(WIN, bg, p1, p2, b)
        move(p1, p2, b)
        pygame.display.update()


if __name__ == "__main__":
    menu()