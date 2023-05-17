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
    print("Welcome to the Guess Five game!")
    play = input("Would you like to play? (Y/N): ")
    
    if play.upper() == 'Y':
        print("Great! Let's start the game.")
        guess_five(random_word)
    elif play.upper() == 'N':
        print("No problem. Maybe next time!")
    else:
        print("Invalid input. Please enter Y or N.")

def guess_five(random_word):
    current_word = ['*' for _ in range(len(random_word))]
    attempts = 5

    while attempts > 0:
        print(f'Attempts left: {attempts}')
        print("Current Word: ", '' .join(current_word))
        guess = input('Guess your 5 letter word: ')

        if len(guess) != len(random_word):
            print("Invalid guess. Please enter a 5-letter word.")
            continue

        if guess == random_word:
            print("Congratulations! You guessed the word correctly. You win!")
            return

        attempts -= 1
        feedback = []

        for i in range(len(random_word)):
            if guess[i] == random_word[i]:
                current_word[i] = guess[i]
            elif guess[i] in random_word:
                feedback.append(guess[i])

        if feedback:
            print("Incorrect guess. The following letters are in the word, but not in the correct place:", ', '.join(feedback))
        else:
            print("Incorrect guess. None of the letters are in the correct place.")

    print("Game over! You ran out of attempts. The word was:", random_word)



word_list = read_word_list()
random_word = select_word(word_list).lower()



start_game()
