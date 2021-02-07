import random
import sys

wins = 0
losses = 0
draws = 0

while True:
    print("%s Wins, %s Losses, %s Draws" % (wins,losses,draws))
    while True:
        player_input = input("Enter your move: (R, P, S) or 'X' to end the game:")
        if player_input == 'X':
            print("Goodbye, let's play again soon!")
            sys.exit()
        if player_input == 'R' or player_input == 'P' or player_input == 'S':
            break


    if player_input == 'R':
        print("Rock VS...")

    elif player_input == 'P':
        print("Paper VS...")

    elif player_input == 'S':
        print("Scissors VS...")

    rand_number = random.randrange(3)
    if rand_number == 0:
        comp_move = 'R'
        print("Rock")

    if rand_number == 1:
        comp_move = 'P'
        print("Paper")

    if rand_number == 2:
        comp_move = 'S'
        print("Scissors")

    if player_input == comp_move:
        print("Good game, it's a draw! :|")
        draws = draws + 1

    elif player_input == "R" and comp_move == "S":
        print("You're really good! You win! :D")
        wins = wins + 1

    elif player_input == "R" and comp_move == "P":
        print("You lose!!! D:")
        losses = losses + 1

    elif player_input == "P" and comp_move == "R":
        print("You're really good! You win! :D")
        wins = wins + 1

    elif player_input == "P" and comp_move == "S":
        print("You lose!!! D:")
        losses = losses + 1

    elif player_input == "S" and comp_move == "P":
        print("You're really good! You win! :D")
        wins = wins + 1

    elif player_input == "S" and comp_move == "R":
        print("You lose!!! D:")
        losses = losses + 1

    if wins - losses == 2:
        print("You're awesome!!!")

    elif wins - losses == 4:
        print("You're a SAVAGE!!!")

    elif wins - losses > 6:
        print("Are you a competitive player? You might want to give others a chance!")

    if losses - wins == 2:
        print("You might want to try harder.. Don't give up!")

    elif losses - wins == 4:
        print("Would you like me to give you a hand?")

    elif losses - wins > 6:
        print("You may want to stop.. It's painful for me to watch..")

    if wins == 10:
        print("You're LEGENDARY!!")

    if losses == 10:
        print("Opps.. You lost yet another battle..")

    if draws == 10:
        print("Are we long-lost twins? :O")

    if wins + losses + draws > 50:
        print("Hey, are you addicted to this game? I need a break..")







