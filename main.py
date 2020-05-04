import sys
import os
import pygame
import Color
import Text
import Frame
import Button
import ball
import Player
import background
import log

# Initial game
pygame.init()
menu_image = pygame.transform.scale(pygame.image.load(os.path.join("imgs","menu.png")), (1280, 720))
def menu():
    window_width = 1280
    window_height = 720
    window_game = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Ping Pong")

    #name = Text.text("PING PONG GAME", 32)
    #heading = Frame.frame()
    play = Button.button("PLAY")
    score_board = Button.button("Coming soon")
    how_to_play = Button.button("Coming soon")
    about_us = Button.button("Comming soon")
    step = 5

    window_game.fill(Color.gray)
    window_game.blit(menu_image, (0, 0))
    #heading.blit_center_top(window_game)
    #name.blit_center_frame(window_game, heading)

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
                    print("click play")
                    run = False
                    set_Name(window_game)
                                 
                elif score_board.is_Click(event.pos):
                    print("click scoreboard")
                elif how_to_play.is_Click(event.pos):
                    print("click how_to play")
                elif about_us.is_Click(event.pos):
                   print("click about us")
                else:
                    print("Missclick")
            pass
        
        pygame.display.update()
        

def set_Name(WIN):
    p1_set = Button.button("Player 1", 30, 2)
    p2_set = Button.button("Player 2", 30, 2)

    WIN.fill(Color.white)
    WIN.blit(menu_image, (0, 0))
    p1_set.draw(WIN, (WIN.get_width()/4 - 125, WIN.get_height()/2 - 50))
    p2_set.draw(WIN, (3*WIN.get_width()/4 - 125, WIN.get_height()/2 - 50))
    name1 = name2 = ""
    player1_name = Button.button(name1, 30)
    player2_name = Button.button(name2, 30)
    running = True
    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                x,y = event.pos
                if p1_set.is_Click((x, y)):
                    n1 = True
                    n2 = False
                elif p2_set.is_Click((x, y)):
                    n2 = True
                    n1 = False
                else:
                    n1 = n2 = False
                    print('missclick')
            if event.type == pygame.KEYDOWN:
                if n1 is None or n2 is None:
                    n1 = n2 = False
                if event.key == pygame.K_BACKSPACE:
                    if n1:
                        name1 = name1[:-1]
                if event.key == pygame.K_BACKSPACE:
                    if n2:
                        name2 = name2[:-1]
                elif event.key == pygame.K_MODE:
                    pass
                else:  
                    if n1 and len(name1) <= 12:              
                        name1 += pygame.key.name(event.key)
                    elif n2 and len(name2) <= 12:    
                        name2 += pygame.key.name(event.key)
                    
                player1_name.update_Text(name1)
                player2_name.update_Text(name2)

        player1_name.draw(WIN, (WIN.get_width()/4 - 125, WIN.get_height()/2 + 100))
        player2_name.draw(WIN, (3*WIN.get_width()/4 - 125, WIN.get_height()/2 + 100))
        pygame.display.update()


def Play(WIN):
    WIN.fill(Color.white)

    log.Log.start()

    back_ground = background.Background()
    b = ball.Ball()
    p1 = Player.player(1)
    p2 = Player.player(2)
    print("Player:", p1.id)
    print("Player:", p2.id)
    run =True
    clock = pygame.time.Clock()
    # Running
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                log.Log.result(p1, p2)
                pygame.quit()
                quit()
            pass
        


        move(b, p1, p2)
        draw(WIN, back_ground, b, p1, p2)
        pygame.display.update()

def draw(WIN, background, ball, player1, player2):
    background.draw(WIN)
    ball.draw(WIN)
    player1.character.draw(WIN)
    player2.character.draw(WIN)
    player1.draw_Score(WIN)
    player2.draw_Score(WIN)

def move(ball, player1, player2):
    ball.move()
    player1.character.move()
    player2.character.move()

    if ball.is_Over_Left():
        player2.win_Game()
        log.Log.score(player1, player2)
        #player1.character.reset()
    elif ball.is_Over_Right():
        player1.win_Game()
        log.Log.score(player1, player2)
        #player2.character.reset()

        
    if ball.is_Collide(player1.character) or ball.is_Collide(player2.character):
        ball.collide()

if __name__ == "__main__":
    menu()
