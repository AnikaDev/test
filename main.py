# print("test")
# a = 12  # int целые числа
# b = 3.1415926  # float дробные числа
# c = 'text'  # str строка
# d = [2, 4.67, 'cat', [7, 8]]  # list список
# d[0] = 9
# d[1] = b
# d[2] = 'dog'
# d[3][1] = 5
# print(d)
# e = (4, 'apple', 7.8, [8, 9])  # tuple кортеж
# f = {5, 'dog', 6.7, 'cat'}  # set множество
# s = [2, 4, 4, 2, 5, 4]
# print(set(s))
# print(f)
# g1 = True  # bool логический
# g2 = False
# h = {'key': 'value', 'Alex': [5, 4, 3, 5]}
# print(h['Alex'])
#
# # + - * /
# print(5 ** 2)  # степень числа
# print(125 ** (1/3))  # кубический корень
# print(-25 ** 0.5)
# print(pow(-25, 0.5))  # степень числа
# print(7 // 3)  # целая часть от деления
# print(7 % 3)  # остаток от деления
# print(divmod(7, 3))  # (//, %)
# print(abs(-7))  # модуль числа

# if условие1:      если
#     блок кода 1
# elif условие2:    иначе если
#     блок кода 2
# else:             иначе при всех остальных условиях
#     блок кода 3

# > больше
# < меньше
# >= больше или равно
# <= меньше или равно
# == равно
# != не равно

# x = int(input('Введите число: '))
# if x > 0:
#     print('У вас положительное число')
# elif x < 0:
#     print('У вас отрицательное число')
# else:
#     print('У вас ноль')

# Логические операции
# a and b   логическое И, True, если оба True
# a or b    логическое ИЛИ, True, если хотя бы один равен True
# not a     логическое НЕ  not True = False   not False = True

# a, b = -5, (0,)
# if a < 0 and b:
#     print('cat')

# False: False, 0, None, [], (), '', {}
# True: True, != 0, len(iterable)>0

# Строки str
a = 'white cat blACK cat'
b = 'dog'
c = 7
# print(a + b)  # конкатенация
# print(a + b + str(c))
# print(a, b, c)
# print(b * 3)
# print('-' * 80)
# print(len(a))  # длина строки
# print('cat' in a)  # проверяет вхождение подстроки в строку
print(a.index('cat'))  # возвращает индекс вхождения ПЕРВОГО элемента, если элемента нет - ошибка
print(a.rindex('cat'))  # возвращает индекс вхождения ПЕРВОГО элемента, поиск с конца строки, если элемента нет - ошибка
print(a.find('cat'))  # возвращает индекс вхождения ПЕРВОГО элемента, если элемента нет -1
print(a.rfind('catqq'))  # возвращает индекс вхождения ПЕРВОГО элемента, поиск с конца строки, если элемента нет -1
print(a.replace('cat', 'cow').replace('black', 'green').replace('white', 'blue'))  # замена текста
print(a.replace('cat', 'cow', 1))  # можем указать количество замен
print('BMW'.lower())  # переводит текст в нижний регистр
print('cat'.upper())  # переводит текст в верхний регистр
print('Apple'.swapcase())  # меняет регистр букв местами
print(a.title())  # меянет первую букву каждого слова на заглавную, а все остальные на строчные
print(a.capitalize())  # меянет первую букву строки на заглавную, а все остальные на строчные

a = 'white   cat        black  cat'
print(a.split(' '))  # разбивает строку на список текстовых элементов по разделителю
print(a.split())  # по умолчанию разбивает по множественному пробелу
print(a.split('cat'))
print('***'.join(['white', 'cat', 'black', 'cat']))  # склеивает в строку текстовые элементы итерируемого объекта

a = 'apple'
b = '12'
c = 'apple 12'
# print(a.isalpha())  # состоит ли только из букв
# print(a.isdigit())  # состоит ли только из цифр
# print(a.isalnum())  # состоит ли только из букв или цифр
# print(a.isspace())  # состоит ли только из пробельных символов (пробел, табуляция \t, новая строка \n и т.д)
# print(a.islower())  # состоит ли только из букв нижнего регистра
# print(a.isupper())  # состоит ли только из букв верхнего регистра
# print(a.istitle())  # начинаются ли слова в строке с заглавных букв
#
# fio = input('Введите ваше ФИО: ')
# if fio.istitle():
#     print(fio)
# else:
#     print(fio.title())

# print(fio if fio.istitle() else fio.title())

# Тернарный оператор
# if exression:
#     on_true
# else:
#     on_false
# on_true if exression else on_false

# a, b = 15, 7
# small = b if a > b else a
# print(small)

# print(isinstance(b, (int, float, complex)))  # проверяет принадлежит ли переменная к тому или иному типу
# print(type(b))
# print('***apple*****'.strip('*'))  # удаляет с начала и конца строки указанные символы
# print('***apple*****'.rstrip('*'))  # удаляет с конца строки указанные символы
# print('***apple*****'.lstrip('*'))  # удаляет с начала строки указанные символы
# print('  apple            '.strip())  # по умолчанию удалит пробельные символы
# print('++-*-+-*-+ap++ple+++---*****+--*-'.strip('+-*'))
# print(ord('f'))  # показывает код символа
# print(chr(129392), 'name', chr(127801))  # показывает символ по его коду
#
# for i in range(55296):
#     print(chr(i), end=' ')
#     if i % 50 == 0:
#         print('\n', i, ': ', end='')

a = 'white cat black cat'
# print(a[0])
# print(a[-1])
# print(a[6:9])  # с 6 по 8 символы
# print(a[:5])  # с начала строки по 4 символы
# print(a[16:])  # с 16 до конца строки
# print(a[-3:])
# print(a[6:16:2])  # с 6 по 15 символы с шагом 2
# print(a[::-1])  # развернуть строку
print(' '.join(a[6:16:2]))

# s = 'шалаш'
# print('Палиндром' if s[::-1] == s else 'Не палиндром')

a, b = [15, 7]
# a, b, c = input('Введите 3 числа через пробел: ').split()
a, *b, c = input('Введите числа через пробел: ').split()
print(a, b, c)


