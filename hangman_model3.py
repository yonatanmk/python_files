import random
from hangman_data import hangman_pics

def listmaker(word_list_file, listnum): # compiles word collection from word_list_file of length 'listnum' into a list
    word_list_2 = []
    while True:
        word_addition = word_list_file.readline()
        word_addition = word_addition[:len(word_addition) - 1]
        word_list_2.append(word_addition)
        if len(word_list_2) == listnum:
            break
    return word_list_2

def random_word(word_list): #returns a random word from word_list
    return word_list[random.randint(0, len(word_list))]

def draw_board(hangman_pics, missed_letters, word_letters, hidden_word): #displays hangman pic, blanks with correct letters, and missed letters
    print (hangman_pics[len(missed_letters)]) # display hangman picture
    print ()

    blank = '_' * len(hidden_word)

    for x in range (len(blank)): # replaces the displayed blanks with the correctly guessed letters in the hidden word
        if hidden_word[x] in word_letters:
            blank = blank[:x] + hidden_word[x] + blank[x + 1:]

    for item in blank: # print blanks and correctly guessed letters
        print (item, end=' ')
    print ()

    print ('Missed Letters:', end=' ') # prints missed letters
    for item in missed_letters:
        print (item, end = ' ')
    print ()

def get_guess(word_letters): # Returns the player's guessed letter and filters out incorrect inputs
        print('Please guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter only a single letter.')
        elif guess in word_letters:
            print('You have already guessed that letter.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a letter. No numbers or symbols will be accepted.')
        else:
            return guess

def replay():
    # Returns True if the player decides to play again and returns False if the player doesn't want to keep playing
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

#__________________________________________________________________________________________________

word_file = open('hangman_data2.py', 'r')
word_list = listmaker(word_file, 301)
word_file.close()
hidden_word = random_word(word_list)
missed_letters = ''
word_letters = ''
game_over = False

print ("Welcome to Hangman!")
print (hidden_word)

while True:
    draw_board(hangman_pics, missed_letters, word_letters, hidden_word)
    guess = get_guess(word_letters)
    if guess in hidden_word:
        word_letters = word_letters + guess
        complete_word = True
        for item in hidden_word:
            if item not in word_letters:
                complete_word = False
        if complete_word:
            game_over = True
            print ("Congratulations! You've won!")
            print ("The word was %s" % (hidden_word))
            game_over = True
    else:
        missed_letters = missed_letters + guess
        if len(missed_letters) == len(hangman_pics) - 1:
            print ("Game Over")
            game_over = True


    if game_over:
        if replay():
            hidden_word = random_word(word_list)
            missed_letters = ''
            word_letters = ''
            game_over = False
        else:
            break
