
#Python Web Development Techdegree
#Project 1 - Number Guessing Game
#--------------------------------


import random

print("\nWelcome to the NUMBER GUESSING GAME!!!\n")


highscore = []

def start_game():
    answer_attempts = []

    solution = random.randint(1,10)
    
    try:
        answer = int(input("--> Guess a number between 1-10: "))
        while answer != solution:
            if answer < solution and answer > 0:
                answer_attempts.append(answer)
                print("It's higher")
                answer = int(input("--> Guess a number between 1-10: ")) 

            if answer > solution and answer < 11:
                answer_attempts.append(answer)
                print("It's lower")
                answer = int(input("--> Guess a number between 1-10: "))

            if answer < 1 or answer > 10:
                answer_attempts.append(answer)
                print("That number is outside of the range, try again.\n")
                answer = int(input("--> Guess a number between 1-10: "))
           
    except ValueError:
        print("Seriously?? Not a valid response...START OVER\n")
        start_game()
                     
    answer_attempts.append(answer)
    print("\nYOU GOT IT!!!")
    print("It took you {} attempts.\n".format(len(answer_attempts)))
    highscore.append(len(answer_attempts))

    play_again = input("Would you like to play again? (y)es or (n)o: ")
    if play_again.lower() == "y" or play_again.lower() == "yes":
        print("\nHighscore = {}\n".format(min(highscore)))
        start_game()
    else:
        print("Final Highscore = {}\n".format(min(highscore)))
        print("Goodbye")
    
    
start_game()
