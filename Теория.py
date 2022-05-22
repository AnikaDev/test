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
# a = 'white cat blACK cat'
# b = 'dog'
# c = 7
# print(a + b)  # конкатенация
# print(a + b + str(c))
# print(a, b, c)
# print(b * 3)
# print('-' * 80)
# print(len(a))  # длина строки
# print('cat' in a)  # проверяет вхождение подстроки в строку
# print(a.index('cat'))  # возвращает индекс вхождения ПЕРВОГО элемента, если элемента нет - ошибка
# print(a.rindex('cat'))  # возвращает индекс вхождения ПЕРВОГО элемента, поиск с конца строки, если элемента нет - ошибка
# print(a.find('cat'))  # возвращает индекс вхождения ПЕРВОГО элемента, если элемента нет -1
# print(a.rfind('catqq'))  # возвращает индекс вхождения ПЕРВОГО элемента, поиск с конца строки, если элемента нет -1
# print(a.replace('cat', 'cow').replace('black', 'green').replace('white', 'blue'))  # замена текста
# print(a.replace('cat', 'cow', 1))  # можем указать количество замен
# print('BMW'.lower())  # переводит текст в нижний регистр
# print('cat'.upper())  # переводит текст в верхний регистр
# print('Apple'.swapcase())  # меняет регистр букв местами
# print(a.title())  # меянет первую букву каждого слова на заглавную, а все остальные на строчные
# print(a.capitalize())  # меянет первую букву строки на заглавную, а все остальные на строчные
#
# a = 'white   cat        black  cat'
# print(a.split(' '))  # разбивает строку на список текстовых элементов по разделителю
# print(a.split())  # по умолчанию разбивает по множественному пробелу
# print(a.split('cat'))
# print('***'.join(['white', 'cat', 'black', 'cat']))  # склеивает в строку текстовые элементы итерируемого объекта
#
# a = 'apple'
# b = '12'
# c = 'apple 12'
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

# a = 'white cat black cat'
# print(a[0])
# print(a[-1])
# print(a[6:9])  # с 6 по 8 символы
# print(a[:5])  # с начала строки по 4 символы
# print(a[16:])  # с 16 до конца строки
# print(a[-3:])
# print(a[6:16:2])  # с 6 по 15 символы с шагом 2
# print(a[::-1])  # развернуть строку
# print(' '.join(a[6:16:2]))

# s = 'шалаш'
# print('Палиндром' if s[::-1] == s else 'Не палиндром')
#
# a, b = [15, 7]
# a, b, c = input('Введите 3 числа через пробел: ').split()
#
# # Списки list
# a = [1, 2, 3, 2, 2]
# b = [5, 6, 7]
# d = [[1, 2], [3, 4], [7, 8]]
# print(a + b)
# print(b * 3)
# print(a[1:4])
# print(len(a))
# print(1 in a)
# print(max(a))
# print(min(b))
# print(sum(b))  # возвращает сумму списка
# print(sum(b, 100))  # второй элемент - первое слагаемое
# print(sum(d, []))  # распаковка двумерного списка в одномерный
# print(a.count(2))  # считает количество элементов в списке
# print(a.index(2))  # возвращает индекс вхождения ПЕРВОГО элемента, можем задать start и stop
# print(sorted(a, reverse=True))  # возвращает отсортированный итерируемый объект
# s = ['apple', 'lemon', 'kiwi', 'raspberry', 'cucumber']
# print(sorted(s, key=len))
#
# a.sort()  # сортирует исходник
# print(a)
# a.reverse()  # разворачивает список
# print(a)
# a.append(5)  # добавляет элемент в конец списка
# print(a)
# a = a + [5]
# print(a)
# a.extend(b)  # добавить элементы итерируемого объекта в конец списка
# print(a)
# a.extend('cat')
# print(a)
# a.insert(2, 4)  # добавить на индекс 2 число 4
# print(a)
# a[2: 2] = [9, 9]
# print(a)
# a.remove(9)  # удаляет первый найденный элемент
# print(a)
# d = a.pop(2)  # удаляет элемент по индексу и возвращает его
# print(a, d)
# d = a.pop()  # по умолчанию - последний элемент
# print(a, d)
# del a[2]  # удаляет по индексу
# print(a)
# a2 = a.copy()  # копирует элементы списка
# a2.clear()
#
# a = [1, 2, [5, 6]]
# a2 = a
# print(id(a), id(a2))
# print(id(a[2]), id(a2[2]))
# a[0] = 7
# print(a, a2)

#
# print(list('cat'))

# Множество set
# a = ['cat', 2, 'dog', 'cow', 3.0, 'apple', 'dog', 'cow']
# b = set(a)
# print(len(b))
# print('cat' in b)
#
# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}
# c = {5, 6}
# print(b.isdisjoint(c))  # True, если НЕ имеются общих элементов
# print(c.issubset(b))  # c <= b
# print(c <= b)
# print(b.issuperset(c))  # b >= c
# print(b >= c)
#
# football = {'A', 'B', 'C'}
# chess = {'B', 'C', 'D'}
#
# print(football.union(chess))  # объединение
# print(football | chess)
#
# print(football.intersection(chess))  # пересечение
# print(football & chess)
#
# print(football.difference(chess))  # разница
# print(football - chess)
#
# print(football.symmetric_difference(chess))  # симметричная разница
# print(football ^ chess)
#
# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}
# a.intersection_update(b)  # a = a & b    a &= b
# print(a)
#
# b.difference_update(a)  # b = b - a     b -= a
# print(b)
#
# a = {1, 2, 3, 4}
# b = {3, 4, 5, 6}
# a.symmetric_difference_update(b)  # a = b ^ a    a ^= b
# print(a)
#
# a.add('cat')  # добавляет элемент (неизменяемого типа) в множество
# a |= {'dog'}
# print(a)
#
# a.update({7, 8})  # объединяет элементы итерируемого объекта с множеством
# a.update('cow')
# print(a)
#
# a.remove(2)  # удаляет элемент множества, если элемента нет - ошибка
# print(a)
#
# a.discard(45)  # удаляет элемент множества, если элемента нет - pass
# print(a)
#
# d = a.pop()  # удаляет и возвращает случайный элемент ("первый" элемент)
# print(a, d)
#
# a2 = a.copy()  # копия множества
# a2.clear()  # очистить множество

# Основные способы форматирования строк
# name = 'Alice'
# age = 20
# # 1. Конкатенация
# print("Меня зовут " + name + '. Мне ' + str(age) + ' лет.')
# # 2. % -форматирование
# print('Меня зовут %s. Мне %d лет.' % (name, age))
# print('Меня зовут %(x)s. Мне %(y)d лет.' % ({'y': age, 'x': name}))
# # 3. Форматирование методом format()
# print('Меня зовут {}. Мне {} лет.'.format(name, age))
# print('Меня зовут {x}. Мне {y} лет.'.format(x=name, y=age))
# # 4. f-строки
# print(f'Меня зовут {name}. Мне {age} лет.')
# pi = 3.1415926
# print(f'pi = {pi:.2f}')
# print(f'{12345678:,}')  # 12,345,678
# print(f'pi * age = {pi * age}')
# planents = ['Земля', 'Нептун', 'Сатурн']
# print(f'Наша планета {planents[0]}')
# print(f'Наша планета {planents[0].upper()}')
# print(f'Округление 3.5 = {round(3.5)}   0 = {round(0.1)}')
#
# print("{0:*^20}".format('Выравнивание', 'cat', 'dog'))
# print("{0:*>20}".format('Выравнивание'))
# print("{0:*<20}".format('Выравнивание'))
# print()
# print(f'{"Выравнивание":*^20}')
# print(f'{"Выравнивание":*>20}')
# print(f'{"Выравнивание":*<20}')

# print(5, 7, end='++++')  # end определяет чем заканчивается строка
# print(5, 7, sep='***')  # sep определяет, что стоит между переменными
#
# print('\\n')  # экранирование через \
# print(r'\n')  # сырая строка

# Словари dict
# a = {'key': 'value', 'Alice': [5, 4, 3, 5]}
# b = {1: 123, 'key': 345, (1, 2): 789}
# print(a['Alice'])
# print(hash(1.0), hash(1), hash(True))  # коллизия хеширования
# print(hash(0.0), hash(0), hash(False))
# print(hash('cat'))
#
# week = {
#     'Выходной': 'Воскресенье',
#     1: 'Понедельник',
#     2: 'Вторник',
#     3: 'Среда',
#     4: 'Четверг'}
# print(week['Выходной'])  # возвращает значение по ключу, применяем, если уверены в наличие ключа
# print(week.get(22, 'Такого ключа нет!'))  # возвращает значение по ключу, если ключа нет - вернёт второй параметр
# print(week.setdefault(5, 'Пятница'))  # возвращает значение по ключу, если ключа нет - то создаст его
# print(week.keys())  # возвращает все ключи
# print(week.values())  # возвращает все значения
# print(week.items())  # возвращает (ключ, значение)
# week[6] = 'Суббота'
# week.update({7: 'Воскресенье'})
# print(week)
# del week[1]  # удаляет элемент
# print(week)
# d = week.pop(43, 'Значение по умолчанию')  # удаляет элемент по ключу и возвращает его значение, если ключа нет, то возвратит второй параметр
# print(week, d)
# week2 = week.copy()  # копия словаря
# week2.clear()  # очистить словарь
#
# s = {'a': 1, 'b': 2, 'c': 3}
# item = s.popitem()  # удаляет и возвращает последнюю пару (ключ, значение)   python >= 3.7
# print(s, item)
#
# fruits = ['apple', 'orange', 'grape']
# store = {}.fromkeys(fruits, 0)  # создаёт словарь из элементов итер объекта с одним значением, по умолчанию - None
# store['apple'] += 5
# print(store)
#
# id_users = {
#     12: 'Alex',
#     22: 'Alice',
#     50: 'Pavel'
# }
# user = 12
# print(f'привет {id_users.get(user, "незнакомец!")}')
#
# x = {2: 'two', True: 'one'}
# y = {1: 'cat', 2: 'dog'}
# z = {**y, **x}
# print(z)
# # {2: 'dog', True: 'cat'}
# # {2: 'two', 1: 'one'}
#
# z2 = x | y  # объединение словарей python >= 3.9
# print(z2)

# Сортировка словаря по значениям
# store = {'apple': 40, 'kiwi': 20, 'orange': 70, 'banana': 100}
# print(sorted(store, key=store.get))
# print(sorted(['apple', 'kiwi', 'orange', 'banana']))

# Цикл for
# for переменная in iterable:
#     тело цикла
# else:
#     код выполняется, если цикл завершился нормально (без break)

a = [1, 2, 7, 12, 14, 34, 57]
# for x in a:
#     if x == 12:
#         continue  # досрочное завершение итерации
#     if x == 50:
#         break  # досрочное завершение цикла
#     print(x)
# else:
#     print('cat')

# for i in range(10):
#     print('apple')

# print(*range(2, 7, 2))
#
# for i in range(2, 7, 2):
#     print(i)

# for i in enumerate(a):  # enumarate возвращает (индекс, элемент)
#     print(i[0] * i[1])
#
# for x, y in enumerate(a, 10):  # можно указать с чего начинать индексацию
#     print(x, y)

# print(*enumerate(a))

# Списковое включение list comprehension "генератор списка"
# z = []
# for i in range(1, 11):
#     z.append(i ** 2)
# print(z)
#
# print([i ** 2 for i in range(1, 11)])
#
# print([i ** 2 for i in range(1, 11) if i % 2 == 0])
# print({i: i ** 2 for i in range(1, 11)})

a = 'Привет, мир!'
for i in a:
    print(i)

a = 'Привет, мир!'
for i in range(1, 11):
    print(a)

i = 1
while i <= 10:
    print(i)
    i = i + 1

i = 1
while i <= 10:
    print(i)
    i = i + 1
    break

i = 1
while i <= 10:
    if i != 5:
        print(i)
    i = i + 1
    continue


