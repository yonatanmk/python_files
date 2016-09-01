import random
from hangman_data import  hangman_pics

def listmaker(word_list_file, listnum):
    word_list_2 = []
    while True:
        word_addition = word_list_file.readline()
        word_addition = word_addition[:len(word_addition) - 1]
        word_list_2.append(word_addition)
        if len(word_list_2) == listnum:
            break
    return word_list_2

def random_word(word_list):
    # This function returns a random string from the passed list of strings.
    randomword = random.randint(0, len(word_list) - 1)
    return word_list[randomword]

def draw_board(hangman_pics, missed_letters, word_letters, hidden_word):
    print(hangman_pics[len(missed_letters)])
    print()

    print('Missed letters:', end=" ")
    for letter in missed_letters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(hidden_word)

    for i in range(len(hidden_word)): # replace blanks with correctly guessed letters
        if hidden_word[i] in word_letters:
            blanks = blanks[:i] + hidden_word[i] + blanks[i+1:]

    for letter in blanks: # show the secret word with spaces in between each letter
        print(letter, end=" ")
    print()

def get_guess(already_guessed):
    # Returns the letter the player entered. This function makes sure the player entered a single letter, and not something else.
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in already_guessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess

def replay():
    # This function returns True if the player wants to play again, otherwise it returns False.
    while True:
        print('Do you want to play again? (yes or no)')
        play_again_answer = input().lower()
        if play_again_answer == 'yes' or play_again_answer == 'y':
            print ('Starting a new game...')
            return True
        elif play_again_answer == 'no' or play_again_answer == 'n':
            print ('Ending the game...')
            return False
        else:
            print ('Please only enter yes or no.')

word_file = open('hangman_data4.py', 'r')
word_list = listmaker(word_file, 301)
word_file.close()

print('H A N G M A N')
missed_letters = ''
word_letters = ''
hidden_word = random_word(word_list)
game_over = False

while True:
    draw_board(hangman_pics, missed_letters, word_letters, hidden_word)

    # Let the player type in a letter.
    guess = get_guess(missed_letters + word_letters)

    if guess in hidden_word:
        word_letters = word_letters + guess

        # Check if the player has won
        word_completed = True
        for i in range(len(hidden_word)):
            if hidden_word[i] not in word_letters:
                word_completed = False
                break
        if word_completed:
            print('Yes! The secret word is %s! You have won!' % (hidden_word))
            game_over = True
    else:
        missed_letters = missed_letters + guess

        # Check if player has guessed too many times and lost
        if len(missed_letters) == len(hangman_pics) - 1:
            draw_board(hangman_pics, missed_letters, word_letters, hidden_word)
            wrong_guess_number = 'guesses'
            right_guess_number = 'guesses'
            if len(missed_letters) == 1:
                wrong_guess_number = 'guess'
            if len(word_letters) == 1:
                right_guess_number = 'guess'
            print('You have run out of guesses!')
            print ('You had %s wrong %s and %s correct %s' % (len(missed_letters), wrong_guess_number, len(word_letters), right_guess_number))
            print ('The word was %s' % (hidden_word))
            game_over = True

    # If the game is over, runs replay() to ask if the player wants to play again.
    # If replay occurs, then resets game variables
    if game_over:
        if replay():
            missed_letters = ''
            word_letters = ''
            game_over = False
            hidden_word = random_word(word_list)
        else:
            break
