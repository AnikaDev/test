# ДЗ:
# Числа в задачах вводим с клавиатуры.

# 1. Дана сторона квадрата a. Найти его периметр P = 4*a. Найти его площадь S = a**2.
# a = int(input('Введите сторону квадрата: '))
# print(a * 4)
# print(a ** 2)

# 2. Даны два числа. Если оба числа положительные, то выдать их сумму,
# если оба числа отрицательные, то выдать их произведение,
# если числа положительное и отрицательное, то выдать квадрат положительного числа (number**2).
# x = int(input('Введите число 1: '))
# y = int(input('Введите число 2: '))
# if x > 0 and y > 0:
#     print(x + y)
# elif x < 0 and y < 0:
#     print(x * y)
# elif x < 0:
#     print(y ** 2)
# else:
#     print(x ** 2)

# 3. Даны два различных числа. Вычесть из большего числа меньшее и выдать разницу чисел.
# q = int(input('Введите число 1: '))
# w = int(input('Введите число 2: '))
# print(abs(q - w))

# if q > w:
#     print(q - w)
# elif w > q:
#     print(w - q)

# 4. Дано двузначное число вида ab. Вывести квадрат числа ba (ba**2)
# er = int(input('Введите двухзначное число: '))
# e = er // 10
# r = er % 10
# print((r * 10 + e) ** 2)

# er = input('Введите двухзначное число: ')
# print(int(er[1] + er[0]) ** 2)

# 5. Дано трёхзначной число. Вывести произведение его цифр. 257 -> 70
# tyu = int(input('Введите трехзначное число: '))
# t = tyu // 100
# yu = tyu % 100
# y = yu // 10
# u = yu % 10
# print(t*y*u)

# a1 = input()
# a2 = 1
# b1 = a1+str(a2)
# print(b1)
# print(type(b1))
#
# b2 = int(a1)+a2
# print (int(a1)+a2)
#
#
# tyu = input('Введите трехзначное число: ')
# print(int(tyu[0]) * int(tyu[1]) * int(tyu[2]))

#  решить через индексацию

# 6. Дано двузначное число вида ab. Если первая цифра чётная, то вывести сумму его цифр, если нечётное, то произведение.
# sd = int(input('Введите двухзначное число: '))
# s = sd // 10
# d = sd % 10
# if s % 2 == 0:
#     print(s + d)
# else:
#     print(s * d)
#
# sd = input('Введите двухзначное число: ')
# if int(sd[0]) % 2 == 0:
#     print(int(sd[0]) + int(sd[1]))
# else:
#     print(int(sd[0]) * int(sd[1]))



# 0. Даны три числа: 2 положительных и одно отрицательное. Выдать произведение положительных чисел.
# q = int(input('Введите значение q: '))
# w = int(input('Введите значение w: '))
# e = int(input('Введите значение e: '))
# if q < 0:
#     print(w * e)
# elif w < 0:
#     print(q * e)
# else:
#     print(q * w)

# 1. Даны три числа. Найти разность между максимальным и минимальным числом.
# a = int(input('Введите значение a: '))
# s = int(input('Введите значение s: '))
# d = int(input('Введите значение d: '))
# min1 = a
# max1 = a
# if s > a:
#     max1 = s
# if d > max1:
#     max1 = d
# if s < a:
#     min1 = s
# if d < min1:
#     min1 = d
# print(max1 - min1)

# 2. Даны три числа. Найти сумму двух наибольших из них.
# z = int(input('Введите значение z: '))
# x = int(input('Введите значение x: '))
# c = int(input('Введите значение c: '))
# if z > x:
#     z, x = x, z
# if z > c:
#     z, c = c, z
# print(x + c)

# поменять местами значение переменных без третьей переменной
# a = 5
# b = 7
# a += b
# b = a - b
# a -= b
# print(a, b)

# max1 = z
# max2 = x
# if x > z and x > c:
#     max1 = x
# if c > z and c > x:
#     max1 = c
# if x > c and x > z:
#     max2 = c
# if x > z and x > c:
#     max2 = z
# print('max1:'+str(max1))
# print('max2:'+str(max2))
# print(max1 + max2)

# 3. Дано натуральное число a из n цифр. Вывести к нему описание "Это n-значное число".
# a = input('Введите число: ')
# print('Это', str(len(a)) + '-значное число')

# 4. Дано число 0 < n < 100. Вывести верно фразу "На лугу пасётся ", n "корова/коровы/коров".
# a = input('Введите число коров: ')
# a1 = a
# tail = ''
# if len(a) == 1:
#     a = '0' + a
# if (a[1] == '1' and int(a) != 11) or int(a) == 1:
#     tail = 'a'
# elif (a[1] in '234' and int(a) > 20) or int(a) <= 4:
#     tail = 'ы'
# print('На лугу посется', a1, 'коров' + tail)


# 5. Квадратное уравнение имеет вид ax2 + bx + c = 0 на вход в переменную stroka мы получаем от пользователя уравнение, выдать значение коэффициентов a, b, c.
# Учитываем, что они могут быть многозначными.
# Например:
# stroka = '6x2 - 12x + 10 = 0'  -> a = 6  b = -12  c = 10
#
# 6. Решить уравнение ax+b=0. Мы получает от пользователя уравнение. Решите его и выведите целое значение x. Вывод должен быть именно в формате: "х=значение".
# Примеры:
# text = '2x+6=0'  ->  x=-3
# text = '-12x+24=0'  -> x=2
# text = '4x-100=0' -> x=25
#
# 7. У учителя есть шоколадка размером n x m кусочков. Учитель решил разделить шоколадку справедливо, и каждому ученику будет дано одинаковое количество кусочков,
# а оставшееся останется у него.
# Может произойти, что от шоколадки ничего не останется, но ученики очень добросовестны, поэтому, если у учителя не будет кусочка, а у учеников будет больше одного,
# тогда каждый отдаст по одному своему кусочку, но если у учеников есть только один кусочек, тогда учителю ничего не дадут. Если шоколадка слишком маленькая
# для деления между всеми учениками, то деления не будет и всё останется у учителя.
# Зная количество учеников s, размер шоколада n, m, распечатайте, сколько кусочков получит каждый ученик и учитель. Данные приведены в следующем порядке: n, m, s.
# Вывод должен быть в виде: У учителя X плиток, у ученика Y плиток.


# garden = 'В нашем саду растут 20 яблонь и 15 груш.'
# 1. Заменить 20 на 35.
# print(garden.replace('20', '35'))

# 2. Поменять местами "яблонь" и "груш" используя replace.
# print(garden.replace('груш', 'яблонь', ).replace('яблонь', 'груш', 1))

# 3. В переменную мы получаем наше предложение garden. Нужно вывести  суммарное количество деревьев в саду. Цифры могут быть многозначными.
# sp = garden.split(' ')
# print(int(sp[4]) + int(sp[7]))

# 4. Поменять местами названия деревьев (могут быть любые), используя split и join.
# sp = garden.split()
# sp[5], sp[8] = sp[8].replace('.', ''), sp[5] + '.'
# print(' '.join(sp))

