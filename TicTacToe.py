# Game : Tic Tac Toe
from random import randint

ttt = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

def welcome():
    print("This is a 2 player game.\nFirst both of you enter your names.")
    print(" \nNext one of you will be chosen to start the game first.")
    print("\nPlayers can enter the position in the Tic Tac Toe board as (1-9)")
    print(" 1 | 2 | 3 ")
    print("-----------")
    print(" 4 | 5 | 6 ")
    print("-----------")
    print(" 7 | 8 | 9 \nThen players alternate and enter their positions.")
    print("When one of the player wins game stops and announces the winner.")
    print("If not its a tie. Enjoy the game!")

# Get user input of names:
players = [[1, 'p1name', 'O'], [2, 'p2name', 'X']]

def enter_playernames():
    players[0][1] = input("Pls Enter player 1's name:")
    print("{} is O".format(players[0][1]))
    players[1][1] = input("Pls Enter player 2's name:")
    print("{} is X".format(players[1][1]))
    if randint(0, 1) == 0:
        print("{} starts first".format(players[1][1]))
        cur_p = 1  # 'X'
    else:
        print("{} starts first".format(players[0][1]))
        cur_p = 0  # 'O'
    return cur_p

# Display the current board
def display_ttt():
    print(" {} | {} | {} ".format(ttt[0], ttt[1], ttt[2]))
    print("-----------")
    print(" {} | {} | {} ".format(ttt[3], ttt[4], ttt[5]))
    print("-----------")
    print(" {} | {} | {} ".format(ttt[6], ttt[7], ttt[8]))

def process_ttt():
    win = ''
    for i in range(0, 7, 3):
        if ttt[i] == ttt[i + 1] == ttt[i + 2] and ttt[i] != ' ':
            win = ttt[i]
    for i in range(0, 3):
        if ttt[i] == ttt[i + 3] == ttt[i + 6] and ttt[i] != ' ':
            win = ttt[i]
    if ttt[0] == ttt[4] == ttt[8] and ttt[0] != ' ':
        win = ttt[0]
    if ttt[2] == ttt[4] == ttt[6] and ttt[2] != ' ':
        win = ttt[2]
    if win == '':
        for i in range(0, 9):
            if ttt[i] == ' ':
                return False
        else:
            print("Game ended in a Tie. Bye")
            return True
    else:
        if win == 'X':
            print("{} won the game. Congrats!".format(players[1][1]))
        elif win == 'O':
            print("{} won the game. Congrats!".format(players[0][1]))
        return True

# Get player choice
def get_playerchoice(cur_p):
    no_choice = True
    while no_choice:
        choice = input("{} Pls enter your choice (1-9):".format(players[cur_p][1]))

        if choice in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
            no_choice = False
        else:
            continue
        choice_num = int(choice)
        if ttt[choice_num - 1] != ' ':
            no_choice = True
        else:
            ttt[choice_num - 1] = players[cur_p][2]
    display_ttt()
    return process_ttt()

def main():
    welcome()
    cur_p = enter_playernames()

    while True:
        if get_playerchoice(cur_p):
            break
        cur_p += 1
        cur_p = cur_p % 2
main()