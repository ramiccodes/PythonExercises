import random
opponent = random.randint(1,3)
if opponent == 1:
    opponentchoice = "Rock"
if opponent == 2:
    opponentchoice = "Paper"
if opponent == 3:
    opponentchoice = "Scissors"


player = input("Rock, Paper, Scissors?: ")
print("SHOOT!")
print("Your opponent chose", opponentchoice)


def game():
    opponent = random.randint(1,3)
    if opponent == 1:
        opponentchoice = "Rock"
    if opponent == 2:
        opponentchoice = "Paper"
    if opponent == 3:
        opponentchoice = "Scissors"
    player = input("Rock, Paper, Scissors?: ")
    print("SHOOT!")
    print("Your opponent chose", opponentchoice)
    if opponentchoice == "Rock":
        if player == "Paper":
            print("You win!")
        if player == "Rock":
            print("TIED!")
        if player == "Scissors":
            print("You lose")
    if opponentchoice == "Paper":
        if player == "Rock":
            print("You lose")
        if player == "Paper":
            print("TIED!")
        if player == "Scissors":
            print("You win!")
    if opponentchoice == "Scissors":
        if player == "Rock":
            print("You win!")
        if player == "Scissors":
            print("TIED!")
        if player == "Paper":
            print("You lose")


if opponentchoice == "Rock":
    if player == "Paper":
        print("You win!")
    if player == "Rock":
        print("TIED!")
    if player == "Scissors":
        print("You lose")
if opponentchoice == "Paper":
    if player == "Rock":
        print("You lose")
    if player == "Paper":
        print("TIED!")
    if player == "Scissors":
        print("You win!")
if opponentchoice == "Scissors":
    if player == "Rock":
        print("You win!")
    if player == "Scissors":
        print("TIED!")
    if player == "Paper":
        print("You lose")


while opponentchoice == player:
    game()
    break