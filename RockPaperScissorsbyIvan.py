import random


rock="Rock"
paper="Paper"
scissors="Scissors"

score=0


while True:
    player_move = input("Chose [r]ock, [p]aper or [s]cisors for End print End")

    if player_move=="r":
        player_move==rock
    elif player_move=="p":
        player_move==paper
    elif player_move=="s":
        player_move==scissors
    elif player_move=="End":
        if score <0:
            print(f"Your score is {score} points")
            print(f"Not your day punk , machines always wins")
        elif score >0:
            print(f"Your score is {score} points")
            print(f"Can we play again please , i want revansh!")
        else:
            print(f"Your score is {score} points")
            print(f".....cheater....")
        break
    else:
        raise SystemExit(f"Invalid Input. Try again...")


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
            print(f"-10 points")
            score-=10
        elif computer_random_number==3:
            print(f"You win !")
            print(f"+10 points")
            score+=10
    elif player_move=="p":
        if computer_random_number==1:
            print(f"You win !")
            print(f"+10 points")
            score += 10
        elif computer_random_number==2:
            print(f"Draw")
        elif computer_random_number==3:
            print(f"You lose !")
            print(f"-10 points")
            score -= 10
    elif player_move=="s":
        if computer_random_number==1:
            print(f"You lose !")
            print(f"-10 points")
            score -= 10
        elif computer_random_number==2:
            print(f"You win !")
            print(f"+10 points")
            score += 10
        elif computer_random_number==3:
            print(f"Draw")

    print(f"Your score <{score}>points")




