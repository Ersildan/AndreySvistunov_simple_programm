import random
import time

def play_game():
    a = random.randrange(0, 101)
    print('Какое число я загадал?')
    num = input()
    if num.isdigit() != True:
        return play_game()
    else:
        while True:
            num = int(num)
            if 0 <= num < a:
                print('Слишком мало, попробуйте ещё раз')
                num = int(input())
            elif a < num <= 100:
                print('Слишком много, попробуйте ещё раз')
                num = int(input())
            elif a == num:
                print('Вы угалдали, поздравляею!')
                break    
            else:
                print('Я загадал число от 0 до 100, попробуйте снова')
                num = int(input())
        print('Сыграем ешё разок?  + = ДА, Любой символ = НЕТ ')
        s = input()
        if s == '+':
            print(play_game())
        else:
            print('Спасибо за игру, приходи ещё :)')
            time.sleep(2)
            exit()


print(play_game())
