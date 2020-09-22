
#Python Web Development Techdegree
#Project 1 - Number Guessing Game
#--------------------------------


import random

print("Welcome to the NUMBER GUESSING GAME!!!\n")


highscore = []

def start_game():
    answer_attempts = []

    solution = random.randint(1,10)

    try:
        answer = int(input("--> Guess a number between 1-10: "))
    
        while answer != solution:
        
            if answer < solution:
                answer_attempts.append(answer)
                print("You're guess is too low")
                answer = int(input("--> Guess a number between 1-10: ")) 

            if answer > solution:
                answer_attempts.append(answer)
                print("You're guess is too high")
                answer = int(input("--> Guess a number between 1-10: "))
    except ValueError:
        print("Seriously?? Not a valid response... Start over!!\n")
        start_game()
                     
    answer_attempts.append(answer)
    print("YOU GOT IT!!!")
    print("It took you {} attempts.\n".format(len(answer_attempts)))
    highscore.append(len(answer_attempts))

    play_again = input("Would you like to play again? (y)es or (n)o: ")
    if play_again.lower() == "y":
        print("\nHighscore = {}\n".format(min(highscore)))
        start_game()
    else:
        print("Final Highscore = {}\n".format(min(highscore)))
        print("Goodbye")

    
start_game()
