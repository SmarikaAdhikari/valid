Current_Board = {'T_L': ' ', 'T_M': ' ', 'T_R': ' ',
                 'M_L': ' ', 'M_M': ' ', 'M_R': ' ',
                 'B_L': ' ', 'B_M': ' ', 'B_R': ' '}


def Board_format(Updated_Board):
    print(Updated_Board['T_L'] + "|" + Updated_Board['T_M'] + '|' + Updated_Board['T_R'])
    print(Updated_Board['M_L'] + "|" + Updated_Board['M_M'] + '|' + Updated_Board['M_R'])
    print(Updated_Board['B_L'] + "|" + Updated_Board['B_M'] + '|' + Updated_Board['B_R'])


turn = 'X'
while True:
    Board_format(Current_Board)
    if ' ' not in Current_Board.values():
        print(" It's a Draw")
        break
    print(' T_L = Top Left \n T_M = Top Middle \n T_R = Top Right')
    print(' M_L = Middle Left \n M_M = Middle Middle \n M_R = Middle Right')
    print(' B_L = Bottom Left \n B_M = Bottom Middle \n B_R = Bottom Right')
    ttt = input(turn + "'s turn. \n Enter the position where you want to insert:\n")
    if Current_Board.get(ttt, ' ') != ' ':
        print('The position is already Filled. Please enter another position \n')
        continue
    if Current_Board.get(ttt, 0):
        Current_Board[ttt] = turn
    else:
        print('\n\nEnter Valid input')
        continue
    if turn == 'X':
        if (Current_Board['T_L'] == Current_Board['T_M'] == Current_Board['T_R'] != ' ' or
                Current_Board['M_L'] == Current_Board['M_M'] == Current_Board['M_R'] != ' ' or
                Current_Board['B_L'] == Current_Board['B_M'] == Current_Board['B_R'] != ' ' or
                Current_Board['T_L'] == Current_Board['M_M'] == Current_Board['B_R'] != ' ' or
                Current_Board['T_R'] == Current_Board['M_M'] == Current_Board['B_L'] != ' ' or
                Current_Board['T_L'] == Current_Board['M_L'] == Current_Board['B_L'] != ' ' or
                Current_Board['T_M'] == Current_Board['M_M'] == Current_Board['B_M'] != ' ' or
                Current_Board['T_R'] == Current_Board['M_R'] == Current_Board['B_R'] != ' '):
            print("'" + turn + '\' Wins')
            Board_format(Current_Board)
            break
        turn = 'O'
    else:
        if (Current_Board['T_L'] == Current_Board['T_M'] == Current_Board['T_R'] != ' ' or
                Current_Board['M_L'] == Current_Board['M_M'] == Current_Board['M_R'] != ' ' or
                Current_Board['B_L'] == Current_Board['B_M'] == Current_Board['B_R'] != ' ' or
                Current_Board['T_L'] == Current_Board['M_M'] == Current_Board['B_R'] != ' ' or
                Current_Board['T_R'] == Current_Board['M_M'] == Current_Board['B_L'] != ' ' or
                Current_Board['T_L'] == Current_Board['M_L'] == Current_Board['B_L'] != ' ' or
                Current_Board['T_M'] == Current_Board['M_M'] == Current_Board['B_M'] != ' ' or
                Current_Board['T_L'] == Current_Board['M_L'] == Current_Board['B_L'] != ' '):
            print("\n\n '" + turn + '\' Wins')
            Board_format(Current_Board)
            break
        turn = 'X'
