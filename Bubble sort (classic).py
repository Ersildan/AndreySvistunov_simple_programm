# Сортировка чисел через пробел / Bubble sort

while True:
    try:
        while True:
            stroka = list(map(int, input().split()))
            for _ in range(len(stroka)-1):
                for _ in range(len(stroka)-1):
                    if stroka[_] > stroka[_ + 1]:
                        stroka[_], stroka[_ + 1] = stroka[_ + 1], stroka[_]
            print(stroka)

    except ValueError:
        print('Используй только цифры / Use only numbers. (1234567890)')
