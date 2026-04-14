import random

# function to display board

def dispaly_board(board):
    for i in range(3):
        print(f"       |       |       ")
        print(f"   {board[i][0]}   |   {board[i][1]}   |   {board[i][2]}   ")
        if i < 2:
            print(f"_______|_______|_______")
        else:
            print(f"       |       |       ")

# function to input user choice

def choice_input(c):
    if mode == 2 and c == 2:
        if difficulty == 1:
            cm = computer_move()
        elif difficulty == 2:
            cm = computer_move_pro(game_data, 1)
        elif difficulty == 3:
            cm = computer_move_pro(game_data, 2)
        print("chance of Computer:", cm)
        return cm
    again = False
    while True:
        if c == 1:
            if not again:
                val = input(f"Chance of {user1}: ")
        else:
            if not again:
                val = input(f"Chance of {user2}: ")
        if again:
            val = input("Enter a number to place in box from 1 to 9 see in demo board: ")
        if val.isdigit():
                val = int(val)
                break
        again = True
    return val


# function to update the board

def update_board(place, chance):
    is_valid = is_valid_place(place)
    if not is_valid[0]:
        return is_valid[1]
    row, col = get_index(place)
    if chance == 1:
        game_data[row][col] = "X"
    else:
        game_data[row][col] = "0"
    dispaly_board(game_data)
    print()
    return "success"


# function to convert user input to indexes

def get_index(place):
    for i in range(3):
        for j in range(3):
            if sample_data[i][j] == place:
                return (i, j)


# function to check whether the move is valid or not

def is_valid_place(place):
    if place < 1 or place > 9:
        return [False, "Number choosen out of board, please choose from (1 to 9)"]
    row, col = get_index(place)
    if game_data[row][col] == "X" or game_data[row][col] == "0":
        return [False, "Place already choose another"]
    else:
        return [True]


# function to check for win

def check_win(game_data):
    # check for row and column winning condition
    for i in range(3):
        # row conditions
        if game_data[i][0] == "X" and game_data[i][1] == "X" and game_data[i][2] == "X":
            return 1
        if game_data[i][0] == "0" and game_data[i][1] == "0" and game_data[i][2] == "0":
            return 2
        # column conditions
        if game_data[0][i] == "X" and game_data[1][i] == "X" and game_data[2][i] == "X":
            return 1
        if game_data[0][i] == "0" and game_data[1][i] == "0" and game_data[2][i] == "0":
            return 2
    # check for diagonal winning conditions
    if game_data[0][0] == "X" and game_data[1][1] == "X" and game_data[2][2] == "X":
        return 1
    if game_data[0][2] == "X" and game_data[1][1] == "X" and game_data[2][0] == "X":
        return 1
    if game_data[0][0] == "0" and game_data[1][1] == "0" and game_data[2][2] == "0":
        return 2
    if game_data[0][2] == "0" and game_data[1][1] == "0" and game_data[2][0] == "0":
        return 2
    
    # else if no body wins
    return 0


# function to display result

def display_result(result):
    if result == 1:
        print(f"-----------Congratulations {user1} won !!!-------------")
    else:
        print(f"-----------Congratulations {user2} won !!!-------------")

# function to choose computer move in easy mode

def computer_move():
    while True:
        place = random.randint(1, 9) # generates number in [1, 9]
        is_valid = is_valid_place(place)
        if is_valid[0]:
            return place

# function to check edge case

def check_fork():
    if game_data[1][1] == ' ':
        return True
    return False


# function to choose best possible move

def check_moves():
    probability = [0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(3):
        if (game_data[i][0] == '0' or game_data[i][0] == ' ') and (game_data[i][1] == '0' or game_data[i][1] == ' ') and (game_data[i][2] == '0' or game_data[i][2] == ' '):
            probability[i] = 1
            if game_data[i][0] == "0":
                probability[i] += 1
            if game_data[i][1] == "0":
                probability[i] += 1
            if game_data[i][2] == "0":
                probability[i] += 1
        if (game_data[0][i] == '0' or game_data[0][i] == ' ') and (game_data[1][i] == '0' or game_data[1][i] == ' ') and (game_data[2][i] == '0' or game_data[2][i] == ' '):
            probability[i+3] = 1
            if game_data[0][i] == "0":
                probability[i+3] += 1
            if game_data[1][i] == "0":
                probability[i+3] += 1
            if game_data[2][i] == "0":
                probability[i+3] += 1
    if (game_data[0][0] == "0" or game_data[0][0] == " ") and (game_data[1][1] == "0" or game_data[1][1] == " ") and (game_data[2][2]== "0" or game_data[2][2] == " "):
        probability[6] = 1
        if game_data[0][0] == "0":
            probability[6] += 1
        if game_data[1][1] == "0":
            probability[6] += 1
        if game_data[2][2] == "0":
            probability[6] += 1
    if (game_data[0][2] == "0" or game_data[0][2] == " ") and (game_data[1][1] == "0" or game_data[1][1] == " ") and (game_data[2][0]== "0" or game_data[2][0] == " "):
        probability[7] = 1
        if game_data[0][2] == "0":
            probability[7] += 1
        if game_data[1][1] == "0":
            probability[7] += 1
        if game_data[2][0] == "0":
            probability[7] += 1
    if check_fork():
        probability[1] += 5
    return probability
    


# function to choose computer move in medium mode

def computer_move_pro(l, d):
    # loop to make move if computer is winning
    for i in range(3):
        for j in range(3):
            if l[i][j] == ' ':
                l[i][j] = '0'
                if check_win(l) == 2:
                    l[i][j] = ' '
                    return i*3 + j + 1
                l[i][j] = ' '
    # loop to block user win chance
    for i in range(3):
        for j in range(3):
            if l[i][j] == ' ':
                l[i][j] = 'X'
                if check_win(l) == 1:
                    l[i][j] = ' '
                    return i*3 + j + 1
                l[i][j] = ' '
    # if nothing is case i.e. no move can make computer win and no move can make user win choose best possible choice
    if d == 1:
        print("random choice in medium mode")
        return computer_move()
    elif d == 2:
        move = check_moves()
        i = 0
        max1 = -1
        max_idx = -1
        while i < len(move):
            if move[i] > max1:
                max_idx = i
                max1 = move[i]
            i += 1
        if max_idx == 0: # row 1
            if game_data[0][0] == ' ':
                return 1
            if game_data[0][2] == ' ':
                return 3
            if game_data[0][1] == ' ':
                return 2
        elif max_idx == 1: # row 2
            if game_data[1][1] == ' ':
                return 5
            if game_data[1][0] == ' ':
                return 4
            if game_data[1][2] == ' ':
                return 6
        elif max_idx == 2: # row 3
            if game_data[2][0] == ' ':
                return 7
            if game_data[2][1] == ' ':
                return 8
            if game_data[2][2] == ' ':
                return 9
        elif max_idx == 3: # col 1
            if game_data[0][0] == ' ':
                return 1
            if game_data[1][0] == ' ':
                return 4
            if game_data[2][0] == ' ':
                return 7
        elif max_idx == 4: # col 2
            if game_data[1][1] == ' ':
                return 5
            if game_data[0][1] == ' ':
                return 2
            if game_data[2][1] == ' ':
                return 8
        elif max_idx == 5: # col 3
            if game_data[0][2] == ' ':
                return 3
            if game_data[1][2] == ' ':
                return 6
            if game_data[2][2] == ' ':
                return 9
        elif max_idx == 6: # leading diagonal
            if game_data[1][1] == ' ':
                return 5
            if game_data[0][0] == ' ':
                return 1
            if game_data[2][2] == ' ':
                return 9
        elif max_idx == 7: # second diagonal
            if game_data[0][2] == ' ':
                return 3
            if game_data[1][1] == ' ':
                return 5
            if game_data[2][0] == ' ':
                return 7
        return computer_move()

        



sample_data = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

game_data = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' '],
]



# ------------- Game play ---------------

# mode selection, user name input and symbol allotment

print("------------------------------------ Welcome to Tic Tac Toe Game --------------------------------------------")
print("------ This is sample board containing number you should choose to place your symbol at particular box ------")
dispaly_board(sample_data)

re_input = False
difficulty = None

while True:
    if not re_input:
        mode = input("Enter 1 for player vs player and 2 for player vs computer: ")
    else:
        mode = input("Enter any of 1 or 2(1-> p vs p and 2 -> p vs c)")
    if mode.isdigit():
        mode = int(mode)
    if mode == 1 or mode == 2:
        if mode == 2:
            difficulty = int(input("Enter 1 for easy mode, 2 for medium mode and 3 for difficult mode:"))
            while difficulty != 1 and difficulty != 2 and difficulty != 3:
                print("Choose correct option please")
                difficulty = int(input("Enter 1 for easy mode, 2 for medium mode and 3 for difficult mode:"))
        break
    re_input = True

user1 = input("Enter the name of player 1: ")

if mode == 1:
    user2 = input("Enter the name of player 2: ")
else:
    user2 = "Computer"


print(f"symbol for {user1} is X")
print(f"symbol for {user2} is 0")



# game loop

chance = 1 # 1 -> player 1 and 2 -> player 2

i = random.randint(1, 2)
if i == 1:
    end = 9
elif i == 2:
    end = 10
while i <= end:
    if i % 2 != 0:
        chance = 1
    else:
        chance = 2
    place = choice_input(chance)
    msg = update_board(place, chance)
    if msg != "success":
        print(msg)
        i -= 1
    result = check_win(game_data)
    if result == 1 or result == 2:
        display_result(result)
        break
    i += 1
else:
    print("--------------It's a Draw !!!-----------------")
