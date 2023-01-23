import random


rock="Rock"
paper="Paper"
scissors="Scissors"

player_move= input("Chose [r]ock, [p]aper or [s]cisors")

if player_move=="r":
    player_move==rock
elif player_move=="p":
    player_move==paper
elif player_move=="s":
    player_move==scissors
else:
    raise SystemExit("Invalid Input. Try again...")

computer_random_number=random.randint(1,3)
computer_move=""

if computer_random_number == 1:
    computer_move="Rock"
elif computer_random_number==2:
    computer_move="Paper"
elif computer_random_number==3:
    computer_move="Scissors"

print(f"The computer chose {computer_move}.")

if player_move=="r":
    if computer_random_number==1:
        print(f"Draw")
    elif computer_random_number==2:
        print(f"You lose !")
    elif computer_random_number==3:
        print(f"You win !")
elif player_move=="p":
    if computer_random_number==1:
        print(f"You win !")
    elif computer_random_number==2:
        print(f"Draw")
    elif computer_random_number==3:
        print(f"You lose !")
elif player_move=="s":
    if computer_random_number==1:
        print(f"You lose !")
    elif computer_random_number==2:
        print(f"You win !")
    elif computer_random_number==3:
        print(f"Draw")




