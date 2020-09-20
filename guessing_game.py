
#Python Web Development Techdegree
#Project 1 - Number Guessing Game
#--------------------------------


import random

print("Welcome to the NUMBER GUESSING GAME!!!")

answer_attempts = []
highscore = []

def start_game():

    for solution in range(10):
        solution = random.randint(1,10)
    
    answer = int(input("Guess a number between 1-10: "))
    while answer != solution:
        
        if answer < solution:
            answer_attempts.append(answer)
            print("It's higher")
            answer = int(input("Guess a number between 1-10: ")) 

        if answer > solution:
            answer_attempts.append(answer)
            print("It's lower!")
            answer = int(input("Guess a number between 1-10: "))
                     
    answer_attempts.append(answer)
    print("Got it")
            
    play_again = input("Would you like to play again? (y)es or (n)o: ")
    if play_again.lower() == "y":
        start_game()
    else:
        print("It took you {} attempts.".format(len(answer_attempts)))
        print("Goodbye")




    
start_game()
