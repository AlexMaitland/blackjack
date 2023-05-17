import random

def read_word_list(file_path):
    with open(file_path, 'r') as file:
        word_list = file.read().splitlines()
    return word_list

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





file_path = 'words.txt'  
word_list = read_word_list(file_path)
random_word = random.choice(word_list)
print(word_list)
print(random_word)


start_game()
