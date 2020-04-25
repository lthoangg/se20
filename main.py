import sys
import os
import pygame
import Color
import Text
import Frame
import Button
import ball
import paddle
import background
# Initial game
pygame.init()
menu_image = pygame.transform.scale(pygame.image.load(os.path.join("imgs","menu.png")), (680, 720))
def menu():
    window_width = 1280
    window_height = 720
    window_game = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Ping Pong")

    name = Text.text("PING PONG GAME", 32)
    heading = Frame.frame()
    play = Button.button("PLAY")
    score_board = Button.button("Coming soon")
    how_to_play = Button.button("Coming soon")
    about_us = Button.button("Comming soon")
    step = 5

    window_game.fill(Color.gray)
    window_game.blit(menu_image, (340, 0))
    heading.blit_center_top(window_game)
    name.blit_center_frame(window_game, heading)

    play.draw(window_game)

    score_board.draw(window_game, (play.frame.x, play.frame.y+play.frame.height+ step))
    how_to_play.draw(window_game, (score_board.frame.x, score_board.frame.y +score_board.frame.height + step))
    about_us.draw(window_game, (how_to_play.frame.x, how_to_play.frame.y + how_to_play.frame.height + step))

    run = True
    # Running
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play.is_Click(event.pos):
                    Play(window_game)
                    print("click play")
                elif score_board.is_Click(event.pos):
                    print("click scoreboard")
                elif how_to_play.is_Click(event.pos):
                    print("click how_to play")
                elif about_us.is_Click(event.pos):
                   print("click about us")
                else:
                    print("Missclick")
        
        pygame.display.update()
        
def Play(WIN):
    WIN.fill(Color.white)

    back_ground = background.Background()
    b = ball.Ball()
    p1 = paddle.Paddle()
    p2 = paddle.Paddle(2)

    clock = pygame.time.Clock()


    run =True
    # Running
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        move(b, p1, p2)
        draw(WIN, back_ground, b, p1, p2)
        pygame.display.update()

def draw(WIN, background, ball, paddle1, paddle2):
    background.draw(WIN)
    ball.draw(WIN)
    paddle1.draw(WIN)
    paddle2.draw(WIN)

def move(ball, paddle1, paddle2):
    ball.move()
    paddle1.move()
    paddle2.move()
    if ball.lose():
        menu()
    if ball.is_Collide(paddle1) or ball.is_Collide(paddle2):
        ball.collide()

if __name__ == "__main__":
    menu()
