def playground():  # function for current playground display
    print('---------')
    print('| {} {} {} |'.format(top_l, top_m, top_r))
    print('| {} {} {} |'.format(mid_l, mid_m, mid_r))
    print('| {} {} {} |'.format(bot_l, bot_m, bot_r))
    print('---------')


# importing the coordinates options for X and O

top_l = ' '
top_m = ' '
top_r = ' '
mid_l = ' '
mid_m = ' '
mid_r = ' '
bot_l = ' '
bot_m = ' '
bot_r = ' '


def move(char):  # function for placing the X or O
    global top_l
    global top_m
    global top_r
    global mid_l
    global mid_m
    global mid_r
    global bot_l
    global bot_m
    global bot_r
    position = input('Enter the coordinates:')
    position_temp = position.replace(' ', '')
    if not position_temp.isdigit():  # check if input are numbers
        print('You should enter numbers!')
    else:
        position = position.split()
        position_temp = [int(i) for i in position]
        if (position_temp[0] > 3 or position_temp[0] < 0) or (position_temp[1] > 3 or position_temp[1] < 0):
            print('Coordinates should be from 1 to 3!')  # check if the coordinates are in correct range
        else:
            if position[0] == '1':
                if position[1] == '1':
                    if bot_l != ' ':
                        print('This cell is occupied! Choose another one!')
                    else:
                        bot_l = char
                        playground()
                elif position[1] == '2':
                    if mid_l != ' ':
                        print('This cell is occupied! Choose another one!')
                    else:
                        mid_l = char
                        playground()
                elif position[1] == '3':
                    if top_l != ' ':
                        print('This cell is occupied! Choose another one!')
                    else:
                        top_l = char
                        playground()
            elif position[0] == '2':
                if position[1] == '1':
                    if bot_m != ' ':
                        print('This cell is occupied! Choose another one!')
                    else:
                        bot_m = char
                        playground()
                elif position[1] == '2':
                    if mid_m != ' ':
                        print('This cell is occupied! Choose another one!')
                    else:
                        mid_m = char
                        playground()
                elif position[1] == '3':
                    if top_m != ' ':
                        print('This cell is occupied! Choose another one!')
                    else:
                        top_m = char
                        playground()
            elif position[0] == '3':
                if position[1] == '1':
                    if bot_r != ' ':
                        print('This cell is occupied! Choose another one!')
                    else:
                        bot_r = char
                        playground()
                elif position[1] == '2':
                    if mid_r != ' ':
                        print('This cell is occupied! Choose another one!')
                    else:
                        mid_r = char
                        playground()
                elif position[1] == '3':
                    if top_r != ' ':
                        print('This cell is occupied! Choose another one!')
                    else:
                        top_r = char
                        playground()


def condition_checker():  # check if any side of the game has won or if there are no moves left
    # possible X's wins
    condition_x_list = [top_l == 'X' and top_m == 'X' and top_r == 'X',
                        mid_l == 'X' and mid_m == 'X' and mid_r == 'X',
                        bot_l == 'X' and bot_m == 'X' and bot_r == 'X',
                        top_l == 'X' and mid_l == 'X' and bot_l == 'X',
                        top_m == 'X' and mid_m == 'X' and bot_m == 'X',
                        top_r == 'X' and mid_r == 'X' and bot_r == 'X',
                        top_l == 'X' and mid_m == 'X' and bot_r == 'X',
                        top_r == 'X' and mid_m == 'X' and bot_l == 'X']

    # possible O's wins
    condition_o_list = [top_l == 'O' and top_m == 'O' and top_r == 'O',
                        mid_l == 'O' and mid_m == 'O' and mid_r == 'O',
                        bot_l == 'O' and bot_m == 'O' and bot_r == 'O',
                        top_l == 'O' and mid_l == 'O' and bot_l == 'O',
                        top_m == 'O' and mid_m == 'O' and bot_m == 'O',
                        top_r == 'O' and mid_r == 'O' and bot_r == 'O',
                        top_l == 'O' and mid_m == 'O' and bot_r == 'O',
                        top_r == 'O' and mid_m == 'O' and bot_l == 'O']

    # condition for checking if there are any free coordinates left
    blank_condition = ' ' in [top_l, top_m, top_r, mid_l, mid_m, mid_r, bot_l, bot_m, bot_r]

    # winning scenarios

    if (not blank_condition) or (any(condition_x_list) or any(condition_o_list)):
        if any(condition_x_list) and not any(condition_o_list):
            print('X wins')
        elif any(condition_o_list) and not any(condition_x_list):
            print('O wins')
        elif blank_condition and not any(condition_x_list) and not any(condition_o_list):
            print('Game not finished')
        elif not blank_condition and (not any(condition_o_list)) and (not any(condition_x_list)):
            print('Draw')
        return True


playground()

while True:
    move('X')
    if condition_checker():
        break
    move('O')
    if condition_checker():
        break
