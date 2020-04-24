import sys
# import time
import pygame
import Color
import Text
import Frame
import Button
# Initial game
def menu():
    window_width = 1280
    window_height = 720
    window_game = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption("Ping Pong")

    name = Text.text("PING PONG GAME")
    heading = Frame.frame()
    play = Button.button("PLAY", 2)

    clock = pygame.time.Clock()
    run = True
    # Running
    while run:
        clock.tick(90)
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print()
                run = False
                pygame.quit()
                quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos, play.is_Click(event.pos))
            

        window_game.fill(Color.gray)
        heading.blit_center_top(window_game)
        name.blit_center_frame(window_game, heading)

        play.draw(window_game)

        pygame.display.update()

if __name__ == "__main__":
    menu()
