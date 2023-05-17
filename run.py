import random

FILE_PATH = 'words.txt'

def read_word_list():
    f = open(FILE_PATH, 'r')
    word_list = f.read().splitlines()
    f.close()
    return word_list

def select_word(word_list):
    return random.choice(word_list)

def start_game():
    print("Welcome to the Guess 5 game!")
    play = input("Would you like to play? (Y/N): ")
    
    if play.upper() == 'Y':
        print("Great! Let's start the game.")
        # Call the function or write code to start the game
    elif play.upper() == 'N':
        print("No problem. Maybe next time!")
    else:
        print("Invalid input. Please enter Y or N.")





word_list = read_word_list()
random_word = select_word(word_list)
print(word_list)
print(random_word)


start_game()
