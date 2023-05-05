## Quiz game

##------------------------------------
from os import system

def game():
    guesses = []
    question_num = 0
    correct_guesses = 0


    for key in questions:
        print("\n# ------------------------------------")
        print(key)
        for i in options[question_num]:
            print(i)
        guess = input("Enter (A, B, C, or D): ").upper()
        guesses.append(guess)
        
        correct_guesses += check_answer(questions.get(key),guess)
        question_num += 1
    
    display_score(correct_guesses,guesses)

# ------------------------------------

def check_answer(answers, guess):

    if answers == guess:
        print("CORRECT!")
        return 1
    
    elif answers != guess:
        print("WRONG!")
        return 0
    
# ------------------------------------

def display_score(correct_guesses,guesses):
    print("\n# ------------------------------------")
    print("RESULT")
    print("# ------------------------------------")

    print("Answers:",end = " ")
    for i in questions:
        print(questions.get(i), end=" ") 
    print()

    print("Guesses:", end = " ")
    for i in guesses:
        print(i, end=" ")

    score = int(correct_guesses/len(questions)*100)
    print("\nYour score is:",score,"%")

# ------------------------------------

def play_again():
    response = input("Do you want to play again (yes or no): ").upper()
    
    if response == "YES":
        system('cls')
        return True

    else:
        system('cls')
        return False

# ------------------------------------

questions = {
    "1.Who won 4 ballon'dors in a row?: ": "C",
    "2.How many times did barcelona won champions league with messi?: ": "D",
    "3.Will barcelona ever win a champions league without messi?: ": "A",
    "4.Will PSG win this years champions league?: ": "A" 
    }

options = [["A. C.Ronaldo", "B. Elon musk", "C. L.Messi", "D. C.Puyol"],
           ["A. 5", "B. 2", "C. 6", "D. 4"],
           ["A. Nah, Barcelona will never win the champions league", "B. Not sure", "C. Maybe", "D. Yes, Barelona can win the trophy"],
           ["A. True","B. False", "C. Not sure", "D. What's PSG"]]

game()

while play_again():
    game()

print("Bye fellas")