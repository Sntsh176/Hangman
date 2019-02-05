"""
Practice Python exercise 32
Hangman Game
http://www.practicepython.org/exercise/2017/01/10/32-hangman.html
"""

import random
import string
import sys


def random_word():
    """
    This function picks a random word from the SOWPODS
    dictionary.
    :return: random word from the dictionary
    """
    # Opening the SOWPODS dictionary and getting a random word
    with open(r"C:\Users\Santosh\Desktop\sowpods.txt") as f:
        content = f.read()
    return random.choice(content.split())


def make_drawing(guesses):
    """
    Depending on the number of the incorrect guesses
    it will draw the Hangman
    :param guesses: incorrect guesss count
    :return: Pictorial Hangman
    """
    drawing_top = ' +---+\n |   |'
    drawing_middle = {5: ' |\n |\n |',
                      4: ' |   O\n |\n |',
                      3: ' |   O\n |   |\n |',
                      2: ' |   O\n |  /|\n |',
                      1: ' |   O\n |  /|\\\n |',
                      0: ' |   O\n |  /|\\\n |  /',
                      -1: ' |   O\n |  /|\\\n |  / \\'}
    drawing_bottom = ' |\n========'

    print(drawing_top)
    print(drawing_middle[guesses])
    print(drawing_bottom)


def guessing():
    """
    This will take input from player and check the Letter
    checks the letter if it's there in word
    """
    word = random_word()
    word_guess = ['_' for _ in word]
    letters = set()
    guesses = 6

    print('Your Word:')
    print(' '.join(word_guess) + '\n')

    while '_' in word_guess and guesses > -1:
        guess = input('Guess your letter: ').upper()
        if guess == 'EXIT':
            print('\nThe game had been ended.\n')
            sys.exit()
        elif guess in string.ascii_uppercase:
            if guess == '':
                print('Not a letter!\n')
            elif guess in letters:
                print('Letter already taken!\n')
            elif guess in word:
                for i in range(len(word)):
                    if word[i] == guess:
                        word_guess[i] = guess
                print(' '.join(word_guess) + '\n')
                if ''.join(word_guess) == word:
                    print('You win!\n')
            else:
                guesses -= 1
                print('Incorrect!')
                if guesses == -1:
                    make_drawing(guesses)
                    print('\nYou hang!')
                    print(f'The full word was: {" ".join(list(word))}\n')
                elif guesses == 1:
                    make_drawing(guesses)
                    print(f'You have {guesses} wrong guess left.\n')
                else:
                    make_drawing(guesses)
                    print(f'You have {guesses} wrong guesses left.\n')
            letters.add(guess)
        else:
            print('Not a letter!\n')


def game_play():
    while True:
        guessing()
        while True:
            again = input('Would you like to play another round (yes/no)? ')
            if again.lower() == 'yes':
                print()
                break
            elif again.lower() == 'no':
                print('\nThe game had been ended.\n')
                sys.exit()
            else:
                print('Invalid input!\n')


def main():
    print('\n*******************')
    print('Welcome to Hangman!')
    print('*******************\n')
    print('You have 6 incorrect guesses before you lose the game.')
    print('If you enter a letter you have already guessed before,')
    print('you will not be penalized for it.')
    print('The game can be quit at any time by entering "exit".\n')

    game_play()


if __name__ == '__main__':
    main()