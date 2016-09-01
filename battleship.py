from random import randint

board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print (" ".join(row))

#print ("Let's play Battleship!")
#print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board) - 1)

def ship_placement(board):
    ship1_row = random_row(board)
    ship1_col = random_col(board)
    ship2_row = random_row(board)
    ship2_col = random_col(board)
    ship3_row = random_row(board)
    ship3_col = random_col(board)
    if ship1_row == ship2_row and ship1_col == ship2_col:
        return ship_placement(board)
    elif ship1_row == ship3_row and ship1_col == ship3_col:
        return ship_placement(board)
    elif ship2_row == ship3_row and ship2_col == ship3_col:
        return ship_placement(board)
    else:
        return [ship1_row, ship1_col, ship2_row, ship2_col, ship3_row, ship3_col]

location_list = ship_placement(board)
ship1_row = location_list[0]
ship1_col = location_list[1]
ship2_row = location_list[2]
ship2_col = location_list[3]
ship3_row = location_list[4]
ship3_col = location_list[5]

location_list2 = [x+1 for x in location_list]
#print (location_list2)


# Everything from here on should go in your for loop!
# Be sure to indent four spaces!
endgame = 1
while (endgame > 0):
    turncount = 0
    win_cond = int(0)
    
    location_list = ship_placement(board)
    ship1_row = location_list[0]
    ship1_col = location_list[1]
    ship2_row = location_list[2]
    ship2_col = location_list[3]
    ship3_row = location_list[4]
    ship3_col = location_list[5]

    location_list2 = [x+1 for x in location_list]
    print ("Let's play Battleship!")
    print_board(board)
    print (location_list2)
    while (turncount < 10):
        print ("Turn %s" % (turncount + 1))
        guess_row1 = input("Guess Row:")
        guess_col1 = input("Guess Col:")
        if guess_row1 != '1' and guess_row1 != '2' and guess_row1 != '3' and guess_row1 != '4' and guess_row1 != '5':
            print ("Oops, that's not even in the ocean.")
        elif guess_col1 != '1' and guess_col1 != '2' and guess_col1 != '3' and guess_col1 != '4' and guess_col1 != '5':
            print ("Oops, that's not even in the ocean.")
        else:
            guess_row = int(guess_row1) - 1
            guess_col = int(guess_col1) - 1

            if guess_row < 0 or guess_row > 4 or guess_col < 0 or guess_col > 4:
                print ("Oops, that's not even in the ocean.")
            elif board[guess_row][guess_col] == "X" or board[guess_row][guess_col] == "B":
                print ("You guessed that one already.")
            else:
                if guess_row == ship1_row and guess_col == ship1_col:
                    turncount = turncount + 1
                    win_cond = win_cond + 1
                    print ("Congratulations! You sunk my battleship!")
                    board[guess_row][guess_col] = "B"
                    print_board(board)
                elif guess_row == ship2_row and guess_col == ship2_col:
                    turncount = turncount + 1
                    win_cond = win_cond + 1
                    print ("Congratulations! You sunk my battleship!")
                    board[guess_row][guess_col] = "B"
                    print_board(board)
                elif guess_row == ship3_row and guess_col == ship3_col:
                    turncount = turncount + 1
                    win_cond = win_cond + 1
                    print ("Congratulations! You sunk my battleship!")
                    board[guess_row][guess_col] = "B"
                    print_board(board)
                else:
                    if turncount < 9:
                        turncount = turncount + 1
                        print ("You missed my battleship!")
                        board[guess_row][guess_col] = "X"
                        print_board(board)
                    else:
                        print ("You missed my battleship!")
                        board[guess_row][guess_col] = "X"
                        print_board(board)
                        print ("Game Over")
                        print ('Do you want to play again? (yes or no)')
                        replaylose = input('-->')
                        if replaylose.lower().startswith('y'):
                            print ("Starting new game.")
                            turncount =20
                        else:
                            endgame = 0
                            break

            if win_cond == 3:
                print ()
                print ("You Win!")
                print ('Do you want to play again? (yes or no)')
                replaywin = input('-->')
                if replaywin.lower().startswith('y'):
                    print ("Starting new game.")
                    turncount = 20
                else:
                    endgame = 0
                    break
