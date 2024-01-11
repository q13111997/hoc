import random as rd
def check_num(input_num,num,range_num,tries):
    idx = range_num.index(input_num)
    print(idx)
    if input_num == num:
        print(f'Correct! You guess the number {num} in {tries} tries')
        return
    elif input_num > num:
        print('Your number is higher than the one I picked. It range between {a} and {b}'.format(a=range_num[0],b=range_num[idx]))
        range_num = range_num[:idx + 1]
        return range_num
    else:
        print('Your number is lower than the one I picked. It range between {a} and {b}'.format(a=range_num[idx],b=range_num[-1]))
        range_num = range_num[idx:]
        return range_num

def user_input():
    while True:
        input_num = input('Enter your guess: ')
        if input_num.isnumeric() == True:
            input_num = int(input_num)
            break
    return input_num

def game(game_on):
    range_num = [i for i in range (1,101)]
    num = rd.randint(1,100)
    tries = 1
    print(num)
    input_num = 105

    while game_on:
        input_num = user_input()
        if input_num not in range_num:
            print('You choose a number out of range!')
            break
        else:
            tries += 1
            range_num = check_num(input_num,num,range_num,tries)
            print(range_num)
            if range_num == None:
                game_on = False
            else:
                game_on = True

start = input('Do you want to play?(Y/N)')
if start.upper() == 'Y':
    game_on = True
game(game_on)