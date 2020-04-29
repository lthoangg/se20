import os
import time
import Player

# This will record events of the match
class Log:
    # Record the start time of the match
    def start():
        f = open("MH.txt", "a")
        t = time.localtime()
        current_time = time.strftime("%A, %e %b %Y - %H:%M:%S", t)
        f.write(current_time + ":\n")
        f.write("************************\n")
        f.close()
    # Define the winner
    def result(player1, player2):
        if player1.score > player2.score:
            f = open("MH.txt", "a")
            f.write("\n")
            f.write("Player 1 won\n")
            f.write("======================\n")
            f.write("\n")
            f.close()
        if player1.score < player2.score:
            f = open("MH.txt", "a")
            f.write("\n")
            f.write("Player 2 won\n")
            f.write("======================\n")
            f.write("\n")
            f.close()
        if player1.score == player2.score:
            f = open("MH.txt", "a")
            f.write("\n")
            f.write("Draw\n")
            f.write("======================\n")
            f.write("\n")
            f.close()
    # Record scores whenever a player scores a goal
    def score(player1, player2):
        f = open("MH.txt", "a")
        f.write(repr(player1.score) + "-" + repr(player2.score) + "\n")
        f.write("------------\n")
        f.close()
