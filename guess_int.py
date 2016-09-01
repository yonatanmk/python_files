from random import randint

randnumber = randint(1,10)
#print (randnumber)

def guessing_game(number):
    print ("Please guess a number between 1 and 10")
    guess = int(input('-->'))

    if guess < 1 or guess > 10:
        print ("Your number is not between 1 and 10. The game is now over.")
        return (guessing_game(number))

    elif guess > number:
        print ("No. Lower")
        return (guessing_game(number))

    elif guess < number:
        print ("No. Higher")
        return (guessing_game(number))

    elif guess == number:
        return ("CONGRATULATIONS! YOU GUESSED THE NUMBER!")

print (guessing_game(randnumber))
