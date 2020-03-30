print("Wellcome to Ping Pong Game!\n" )
print("      1. Single player ")
print("      2. Multiplayer ")
print("      3. Scoreboard")
print("      4. How to play")
print("      5. Options")
print("      6. QUit")

a = int(input("Enter your option: "))

if a == 1:
    exec(open('main.py').read())
elif a == 6:
    quit()
else:
    print("Coming soon!")
