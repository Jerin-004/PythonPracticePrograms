## simple game(Rock,paper,scissors)

import random
from os import system


while True:
    choices = ["Rock", "Paper", "Scissors"]

    computer = random.choice(choices)
    player = None
    
    while player not in choices:
        player = input("\nRock, Paper, or Scissors:").capitalize()
        system('cls')

    if computer == player:
        print("Computer:",computer)
        print("Player:",player)
        print("Its a tie!")

    elif computer == "Rock":
        if player == "Scissors":
            print("Computer:",computer)
            print("Player:",player)
            print("You lose!")
        elif player == "Paper":
            print("Computer:",computer)
            print("Player:",player)
            print("You win!")

    elif computer == "Paper":
        if player == "Rock":
            print("Computer:",computer)
            print("Player:",player)
            print("You lose!")
        elif player == "Scissors":
            print("Computer:",computer)
            print("Player:",player)
            print("You win!")
        
    elif computer == "Scissors":
        if player == "Paper":
            print("Computer:",computer)
            print("Player:",player)
            print("You lose!")
        elif player == "Rock":
            print("Computer:",computer)
            print("Player:",player)
            print("You win!")
    
    play_again = input("Wanna play again? (yes/no):").lower()


    if play_again != "yes":
        system('cls')
        break

print("Bye, See you soon!")