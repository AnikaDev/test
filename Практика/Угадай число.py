from random import *
x = randint(1, 100)
a = int(input('Введите число: '))
k = 1
while x != a:
    if x > a:
        print('Больше')
    else:
        print('Меньше')
    a = int(input('Введите число: '))
    k += 1
print(f'Ты угадал за {k} попыток. Это число {x}')

