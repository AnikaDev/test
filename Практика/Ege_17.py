'''В файле содержится последовательность целых чисел. Элементы последовательности могут принимать целые значения от
−10000 до 10000 включительно. Определите и запишите в ответе сначала количество пар элементов последовательности, в
которых хотя бы одно число делится на 3, затем максимальную из сумм элементов таких пар. В данной задаче под парой
 подразумевается два идущих подряд элемента последовательности. Например, для последовательности из пяти элементов:
 6; 2; 9; –3; 6— ответ: 411.'''
# f = open('17_1.txt', 'r',  encoding='utf-8')
# a = []
# for line in f:
#     a.append(int(line))
# f.close()
# k = 0
# m = -20001
# n = len(a)
# for i in range(n - 1):
#     if a[i] % 3 == 0 or a[i + 1] % 3 == 0:
#         k += 1
#         m = max(m, a[i] + a[i + 1])
# print(k, m)
'''В файле содержится последовательность из 10000 натуральных чисел. Каждое число не превышает 10000. 
Определите и запишите в ответе сначала количество пар элементов последовательности, у которых различные остатки от
 деления на d=160 и хотя бы одно из чисел делится на p=7, затем максимальную из сумм элементов таких пар. В данной 
 задаче под парой подразумевается два различных элемента последовательности. Порядок элементов в паре не важен.
Пример входных данных:
168
7
320
328
Пример выходных данных для приведённого выше примера входных данных:
4 488
Пояснение: Из 4 чисел можно составить 6 пар. В данном случае условиям удовлетворяют пары: 168 и 320, 168 и 7, 320 и 7,
 328 и 7. Максимальную сумму дает пара 168 и 320— 488.'''
# a = []
# f = open('17_1.txt', 'r', encoding='utf-8')
# for line in f:
#     a.append(int(line))
# f.close()
# max1 = 0
# k = 0
# n = len(a)
# for i in range(n - 1):
#     for j in range(i + 1, n):
#         if (a[i] % 7 == 0 or a[j] % 7 == 0) and a[i] % 160 != a[j] % 160:
#             k += 1
#             max1 = max(max1, a[i] + a[j])
# print(max1, k)

'''В файле содержится последовательность из 10000 целых положительных чисел. Каждое число не превышает 10000. Определите
и запишите в ответе сначала количество пар элементов последовательности, разность которых четна и хотя бы одно из чисел
делится на 31, затем максимальную из сумм элементов таких пар. В данной задаче под парой подразумевается два различных
элемента последовательности. Порядок элементов в паре не важен.
'''
# f = open('17_2.txt', 'r', encoding='utf-8')
# a = f.readlines()
# f.close()
# n = len(a)
# for i in range(n):
#     a[i] = int(a[i][:-1])
# k = 0
# summ = 0
# for i in range(n - 1):
#     for j in range(i + 1, n):
#         if abs(a[j] - a[i]) % 2 == 0 and (a[i] % 31 == 0 or a[j] % 31 == 0):
#             k += 1
#             summ = max(summ, a[i] + a[j])
# print(k, summ)
'''Файл содержит последовательность неотрицательных целых чисел, не превышающих 10 000. Назовём парой два идущих подряд
 элемента последовательности. Определите количество пар, в которых хотя бы один из двух элементов делится на 3, а их 
 сумма делится на 5. В ответе запишите два числа: сначала количество найденных пар, а затем – максимальную сумму 
 элементов таких пар.
Задание 17
Например, в последовательности (2 3 7 8 9) есть две подходящие пары: (2 3) и (3 7), в ответе для этой последовательности
 надо записать числа 2 и 10.'''
# f = open('17_26.txt', 'r', encoding='utf-8')
# a = []
# for line in f:
#     a.append(int(line))
# f.close()
# n = len(a)
# k = 0
# summ = 0
# for i in range(n - 1):
#     s = a[i] + a[i + 1]
#     if s % 5 == 0 and (a[i] % 3 == 0 or a[i + 1] % 3 == 0):
#         k += 1
#         summ = max(summ, s)
# print(k, summ)

'''В файле содержится последовательность из 10000 целых положительных чисел. Каждое число не превышает 10000. Определите
и запишите в ответе сначала количество пар элементов последовательности, разность которых четна и хотя бы одно из чисел
делится на 19, затем максимальную из сумм элементов таких пар. В данной задаче под парой подразумевается два различных 
элемента последовательности. Порядок элементов в паре не важен.'''
# f = open('17_2.txt', 'r', encoding='utf-8')
# a = []
# for line in f:
#     a.append(int(line))
# f.close()
# summ = 0
# k = 0
# n = len(a)
# for i in range(n - 1):
#     for j in range(i + 1, n):
#         if (a[i] % 19 == 0 or a[j] % 19 == 0) and abs(a[i] - a[j]) % 2 == 0:
#             k += 1
#             summ = max(summ, a[i] + a[j])
# print(k, summ)
'''В файле содержится последовательность из 10000 целых положительных чисел. Каждое число не превышает 10000. Определите
и запишите в ответе сначала количество пар элементов последовательности, для которых произведение элементов делится без
остатка на 10, затем максимальную из сумм элементов таких пар. В данной задаче под парой подразумевается два различных 
элемента последовательности. Порядок элементов в паре не важен.'''
# f = open('17_5.txt', 'r', encoding='utf-8')
# a = []
# for line in f:
#     a.append(int(line))
# f.close()
# summ = 0
# k = 0
# n = len(a)
# for i in range(n - 1):
#     for j in range(i + 1, n):
#         if a[j] * a[i] % 10 == 0:
#             k += 1
#             summ = max(summ, a[i] + a[j])
# print(k, summ)

'''В файле содержится последовательность из 10000 целых положительных чисел. Каждое число не превышает 10000. Определите
и запишите в ответе сначала количество пар элементов последовательности, для которых произведение элементов делится без
остатка на 62, затем максимальную из сумм элементов таких пар. В данной задаче под парой подразумевается два различных
элемента последовательности. Порядок элементов в паре не важен.'''
# f = open('17_6.txt', 'r', encoding='utf-8')
# a = []
# for line in f:
#     a.append(int(line))
# f.close()
# k = 0
# summ = 0
# n = len(a)
# for i in range(n - 1):
#     for j in range(i + 1, n):
#         if a[i] * a[j] % 62 == 0:
#             k += 1
#             summ = max(summ, a[i] + a[j])
# print(k, summ)

'''В файле содержится последовательность из 10000 целых положительных чисел. Каждое число не превышает 10000. Определите
 и запишите в ответе сначала количество пар элементов последовательности, для которых произведение элементов не кратно 
 14, затем максимальную из сумм элементов таких пар. В данной задаче под парой подразумевается два различных элемента 
 последовательности. Порядок элементов в паре не важен.'''
# f = open('17_7.txt', 'r', encoding='utf-8')
# a = []
# for line in f:
#     a.append(int(line))
# f.close()
# k = 0
# summ = 0
# n = len(a)
# for i in range(n - 1):
#     for j in range(i + 1, n):
#         if a[i] * a[j] % 14 != 0:
#             k += 1
#             summ = max(summ, a[i] + a[j])
# print(k, summ)

'''В файле содержится последовательность из 10000 целых положительных чисел. Каждое число не превышает 10000. Определите
и запишите в ответе сначала количество пар элементов последовательности, для которых произведение элементов не кратно 
34, затем максимальную из сумм элементов таких пар. В данной задаче под парой подразумевается два различных элемента 
последовательности. Порядок элементов в паре не важен.'''
# f = open('17_8.txt', 'r', encoding='utf-8')
# a = []
# for line in f:
#     a.append(int(line))
# f.close()
# n = len(a)
# k = 0
# summ = 0
# for i in range(n - 1):
#     for j in range(i + 1, n):
#         if a[i] * a[j] % 34 != 0:
#             k += 1
#             summ = max(summ, a[i] + a[j])
# print(k, summ)

'''В файле содержится последовательность из 10000 целых положительных чисел. Каждое число не превышает 10000. Определите
и запишите в ответе сначала количество пар элементов последовательности, для которых произведение элементов кратно 26, 
затем максимальную из сумм элементов таких пар. В данной задаче под парой подразумевается два различных элемента 
последовательности. Порядок элементов в паре не важен.'''
# f = open('17_9.txt', 'r', encoding='utf-8')
# a = []
# for line in f:
#     a.append(int(line))
# f.close()
# n = len(a)
# k = 0
# summ = 0
# for i in range(n - 1):
#     for j in range(i + 1, n):
#         if a[i] * a[j] % 26 == 0:
#             k += 1
#             summ = max(summ, a[i] + a[j])
# print(k, summ)
'''В файле содержится последовательность из 10000 целых положительных чисел. Каждое число не превышает 10000. Определите
и запишите в ответе сначала количество пар элементов последовательности, у которых сумма нечётна, а произведение делится
 на 3, затем максимальную из сумм элементов таких пар. В данной задаче под парой подразумевается два различных элемента
последовательности. Порядок элементов в паре не важен.'''
# f = open('17_10.txt', 'r', encoding='utf-8')
# a = []
# for line in f:
#     a.append(int(line))
# f.close()
# k = 0
# summ = 0
# n = len(a)
# for i in range(n - 1):
#     for j in range(i + 1, n):
#         if (a[i] + a[j]) % 2 != 0 and (a[i] * a[j]) % 3 == 0:
#             k += 1
#             summ = max(summ, a[i] + a[j])
# print(k, summ)

'''В файле содержится последовательность из 10000 целых положительных чисел. Каждое число не превышает 10000. Определите
и запишите в ответе сначала количество пар элементов последовательности, у которых разность элементов кратна 80, затем
максимальную из разностей элементов таких пар. В данной задаче под парой подразумевается два различных элемента 
последовательности. Порядок элементов в паре не важен.'''
# f = open('17_21.txt', 'r', encoding='utf-8')
# a = []
# for line in f:
#     a.append(int(line))
# f.close()
# razn = 0
# k = 0
# n = len(a)
# for i in range(n - 1):
#     for j in range(i + 1, n):
#         r = abs(a[j] - a[i])
#         if r % 80 == 0:
#             k += 1
#             razn = max(r, razn)
# print(k, razn)

'''Файл содержит последовательность неотрицательных целых чисел, не превышающих 10 000. Назовём тройкой три идущих
подряд элемента последовательности. Определите количество троек чисел таких, которые могут являться сторонами 
остроугольного треугольника. В ответе запишите два числа: сначала количество найденных троек, а затем— максимальную
 сумму элементов таких троек. Если таких троек не найдётся— следует вывести 00.'''
# f = open('17_29.txt', 'r', encoding='utf-8')
# a = []
# for line in f:
#     a.append(int(line))
# f.close()
# k = 0
# m = 0
# n = len(a)
# for i in range(n - 2):
#     x = max(max(a[i], a[i + 1]), a[i + 2])
#     y = min(min(a[i], a[i + 1]), a[i + 2])
#     z = a[i] + a[i + 1] + a[i + 2] - y - x
#     if y**2 + z**2 > x**2:
#         k += 1
#         m = max(m, x + y + z)
# if k == 0:
#     print('0 0')
# else:
#     print(k, m)


'''Файл содержит последовательность неотрицательных целых чисел, не превышающих 10 000. Назовём тройкой три идущих 
подряд элемента последовательности. Определите количество троек чисел таких, которые могут являться сторонами 
прямоугольного треугольника. В ответе запишите два числа: сначала количество найденных троек, а затем— максимальную 
сумму элементов таких троек. Если таких троек не найдётся— следует вывести 0 0.'''
# f = open('17_30.txt', 'r', encoding='utf-8')
# a = []
# for i in f:
#     a.append(i)
# f.close()
# n = len(a)
# k = 0
# m = 0
# for i in range(n - 2):
#     x = max(max(a[i], a[i + 1], a[i + 2]))
#     y = min(min(a[i], a[i + 1], a[i + 2]))
#     z = a[i] + a[i + 1] + a[i + 2] - y - x
#     if y**2 + z**2 == x**2:
#         k += 1
#         m = max(m, x + y + z)
#     if k == 0:
#         print('0 0')
#     else:
#         print(k, m)


# jfjkfjkrhfjrfhejkrfhjrkfhejkrfhjerkferf
# f = open('17_30.txt', 'r', encoding='utf-8')
# a = []
# for line in f:
#     a.append(int(line))
# f.close()
# k = 0
# m = 0
# n = len(a)
# for i in range(n - 2):
#     x = max(max(a[i], a[i + 1]), a[i + 2])
#     y = min(min(a[i], a[i + 1]), a[i + 2])
#     z = a[i] + a[i + 1] + a[i + 2] - y - x
#     if y**2 + z**2 == x**2:
#         k += 1
#         m = max(m, x + y + z)
# if k == 0:
#     print('0 0')
# else:
#     print(k, m)

'''Файл содержит последовательность неотрицательных целых чисел, не превышающих 10000. Назовём парой два идущих подряд 
элемента последовательности. Определите количество пар, в которых хотя бы один из двух элементов делится на 3 и хотя бы
один из двух элементов меньше среднего арифметического всех чётных элементов последовательности. В ответе запишите два 
числа: сначала количество найденных пар, а затем— максимальную сумму элементов таких пар.'''
# f = open('17_31.txt', 'r', encoding='utf-8')
# sr = 0
# k = 0
# a = []
# for line in f:
#     t = int(line)
#     a.append(t)
#     if t % 2 == 0:
#         k += 1
#         sr += t
# f.close()
# u = sr / k
# n = len(a)
# k = 0
# m = 0
# for i in range(n - 1):
#     if (a[i] % 3 == 0 or a[i + 1] % 3 == 0) and (a[i] < u or a[i + 1] < u):
#         k += 1
#         m = max(m, a[i] + a[i + 1])
# print(k, m)
'''В файле содержится последовательность натуральных чисел. Элементы последовательности могут принимать целые значения
от 1 до 100 000 включительно. Определите количество пар последовательности, в которых хотя бы одно число делится на 
минимальный элемент последовательности, кратный 21. Гарантируется, что такой элемент в последовательности есть. В ответе
запишите количество найденных пар, затем максимальную из сумм элементов таких пар. В данной задаче под парой 
подразумевается два идущих подряд элемента последовательности.'''
# f = open('17_33.txt', 'r', encoding='utf-8')
# min_l = 100001
# a = []
# for line in f:
#     t = int(line)
#     a.append(t)
#     if t % 21 == 0 and t < min_l:
#         min_l = t
# f.close()
# n = len(a)
# k = 0
# m = 0
# for i in range(n - 1):
#     if (a[i] % min_l == 0 or a[i + 1] % min_l == 0):
#         k += 1
#         m = max(m, a[i] + a[i + 1])
# print(k, m)

'''В файле содержится последовательность целых чисел. Элементы последовательности могут принимать целые значения от
−10000 до 10000 включительно. Определите количество пар последовательности, в которых только одно число оканчивается
на 3, а сумма квадратов элементов пары не меньше квадрата максимального элемента последовательности, оканчивающегося на
3. В ответе запишите два числа: сначала количество найденных пар, затем максимальную из сумм квадратов элементов таких 
пар. В данной задаче под парой подразумевается два идущих подряд элемента последовательности.'''
# f = open('17_36.txt', 'r', encoding='utf-8')
# max_l = -10001
# a = []
# for line in f:
#     t = int(line)
#     a.append(t)
#     if t % 10 == 3 and t > max_l:
#         max_l = t
# f.close()
# n = len(a)
# k = 0
# m = -100000000
# for i in range(n - 1):
#     s = (a[i]**2 + a[i + 1]**2)
#     if ((a[i] % 10 == 3 and a[i + 1] % 10 != 3) or (a[i] % 10 != 3 and a[i + 1] % 10 == 3)) and s >= (max_l**2):
#         k += 1
#         m = max(m, s)
# print(k, m)
# ;;;;()

'''В файле содержится последовательность из 10000 целых положительных чисел. Каждое число не превышает 10000. Определите
и запишите в ответе сначала количество пар элементов последовательности, у которых сумма нечётна, а произведение делится
на 5, затем максимальную из сумм элементов таких пар. В данной задаче под парой подразумевается два различных элемента
последовательности. Порядок элементов в паре не важен.'''
# f = open('17_11.txt', 'r', encoding='utf-8')
# a = []
# for line in f:
#     a.append(int(line))
# f.close()
# k = 0
# summ = 0
# n = len(a)
# for i in range(n - 1):
#     for j in range(i + 1, n):
#         if (a[i] + a[j]) % 2 != 0 and a[i] * a[j] % 5 == 0:
#             k += 1
#             summ = max(summ, a[i] + a[j])
# print(k, summ)

'''В файле содержится последовательность из 10000 целых положительных чисел. Каждое число не превышает 10000. Определите
и запишите в ответе сначала количество пар элементов последовательности, у которых сумма элементов кратна 7, затем 
максимальную из сумм элементов таких пар. В данной задаче под парой подразумевается два различных элемента 
последовательности. Порядок элементов в паре не важен.'''
# f = open('17_12.txt', 'r', encoding='utf-8')
# a = []
# for line in f:
#     a.append(int(line))
# f.close()
# k = 0
# summ = 0
# n = len(a)
# for i in range(n - 1):
#     for j in range(i + 1, n):
#         if (a[i] + a[j]) % 7 == 0:
#             k += 1
#             summ = max(summ, a[i] + a[j])
# print(k, summ)

'''В файле содержится последовательность из 10000 целых положительных чисел. Каждое число не превышает 10000. Определите
и запишите в ответе сначала количество пар элементов последовательности, у которых сумма элементов кратна 9, затем 
максимальную из сумм элементов таких пар. В данной задаче под парой подразумевается два различных элемента 
последовательности. Порядок элементов в паре не важен.'''
# f = open('17_13.txt', 'r', encoding='utf-8')
# a = []
# for line in f:
#     a.append(int(line))
# f.close()
# k = 0
# summ = 0
# n = len(a)
# for i in range(n - 1):
#     for j in range(i + 1, n):
#         if (a[i] + a[j]) % 9 == 0:
#             k += 1
#             summ = max(summ, a[i] + a[j])
# print(k, summ)

'''В файле содержится последовательность из 10000 целых положительных чисел. Каждое число не превышает 10000. Определите
и запишите в ответе сначала количество пар элементов последовательности, у которых сумма элементов кратна 8, затем 
максимальную из сумм элементов таких пар. В данной задаче под парой подразумевается два различных элемента 
последовательности. Порядок элементов в паре не важен.'''
# f = open('17_14.txt', 'r', encoding='utf-8')
# a = []
# for line in f:
#     a.append(int(line))
# f.close()
# k = 0
# summ = 0
# n = len(a)
# for i in range(n - 1):
#     for j in range(i + 1, n):
#         if (a[i] + a[j]) % 8 == 0:
#             k += 1
#             summ = max(summ, a[i] + a[j])
# print(k, summ)


'''В файле содержится последовательность из 10000 целых положительных чисел. Каждое число не превышает 10000. Определите
и запишите в ответе сначала количество пар элементов последовательности, у которых сумма элементов кратна 10, затем 
максимальную из сумм элементов таких пар. В данной задаче под парой подразумевается два различных элемента 
последовательности. Порядок элементов в паре не важен.'''
# f = open('17_15.txt', 'r', encoding='utf-8')
# a = []
# for line in f:
#     a.append(int(line))
# f.close()
# k = 0
# summ = 0
# n = len(a)
# for i in range(n - 1):
#     for j in range(i + 1, n):
#         if (a[i] + a[j]) % 10 == 0:
#             k += 1
#             summ = max(summ, a[i] + a[j])
# print(k, summ)

'''В файле содержится последовательность из 10000 целых положительных чисел. Каждое число не превышает 10000. Определите
и запишите в ответе сначала количество пар элементов последовательности, у которых сумма элементов кратна 117, затем
максимальную из сумм элементов таких пар. В данной задаче под парой подразумевается два различных элемента
последовательности. Порядок элементов в паре не важен.'''
# f = open('17_16.txt', 'r', encoding='utf-8')
# a = []
# for line in f:
#     a.append(int(line))
# f.close()
# k = 0
# summ = 0
# n = len(a)
# for i in range(n - 1):
#     for j in range(i + 1, n):
#         if (a[i] + a[j]) % 117 == 0:
#             k += 1
#             summ = max(summ, a[i] + a[j])
# print(k, summ)

'''В файле содержится последовательность из 10000 целых положительных чисел. Каждое число не превышает 10000. Определите
и запишите в ответе сначала количество пар элементов последовательности, у которых сумма элементов кратна 120, затем
максимальную из сумм элементов таких пар. В данной задаче под парой подразумевается два различных элемента
последовательности. Порядок элементов в паре не важен.'''
# f = open('17_17.txt', 'r', encoding='utf-8')
# a = []
# for line in f:
#     a.append(int(line))
# f.close()
# k = 0
# summ = 0
# n = len(a)
# for i in range(n - 1):
#     for j in range(i + 1, n):
#         if (a[i] + a[j]) % 120 == 0:
#             k += 1
#             summ = max(summ, a[i] + a[j])
# print(k, summ)

'''В файле содержится последовательность из 10000 целых положительных чисел. Каждое число не превышает 10000. Определите
и запишите в ответе сначала количество пар элементов последовательности, у которых сумма элементов кратна 126, затем 
максимальную из сумм элементов таких пар. В данной задаче под парой подразумевается два различных элемента
 последовательности. Порядок элементов в паре не важен.'''
# f = open('17_18.txt', 'r', encoding='utf-8')
# a = []
# for line in f:
#     a.append(int(line))
# f.close()
# k = 0
# summ = 0
# n = len(a)
# for i in range(n - 1):
#     for j in range(i + 1, n):
#         if (a[i] + a[j]) % 126 == 0:
#             k += 1
#             summ = max(summ, a[i] + a[j])
# print(k, summ)

'''В файле содержится последовательность из 10000 целых положительных чисел. Каждое число не превышает 10000. Определите
и запишите в ответе сначала количество пар элементов последовательности, у которых сумма элементов кратна 80 и хотя бы 
один элемент из пары делится на 50, затем максимальную из сумм элементов таких пар. В данной задаче под парой
подразумевается два различных элемента последовательности. Порядок элементов в паре не важен.'''
# f = open('17_19.txt', 'r', encoding='utf-8')
# a = []
# for line in f:
#     a.append(int(line))
# f.close()
# k = 0
# summ = 0
# n = len(a)
# for i in range(n - 1):
#     for j in range(i + 1, n):
#         if (a[i] + a[j]) % 80 == 0 and (a[i] % 50 == 0 or a[j] % 50 == 0):
#             k += 1
#             summ = max(summ, a[i] + a[j])
# print(k, summ)

'''В файле содержится последовательность из 10000 целых положительных чисел. Каждое число не превышает 10000. Определите
и запишите в ответе сначала количество пар элементов последовательности, у которых сумма элементов кратна 60 и хотя бы 
один элемент из пары делится на 40, затем максимальную из сумм элементов таких пар. В данной задаче под парой 
подразумевается два различных элемента последовательности. Порядок элементов в паре не важен.'''
# f = open('17_20.txt', 'r', encoding='utf-8')
# a = []
# for line in f:
#     a.append(int(line))
# f.close()
# k = 0
# summ = 0
# n = len(a)
# for i in range(n - 1):
#     for j in range(i + 1, n):
#         if (a[i] + a[j]) % 60 == 0 and (a[i] % 40 == 0 or a[j] % 40 == 0):
#             k += 1
#             summ = max(summ, a[i] + a[j])
# print(k, summ)

'''Файл содержит последовательность неотрицательных целых чисел, не превышающих 10 000. Назовём парой два идущих подряд 
элемента последовательности. Определите количество пар, в которых хотя бы один из двух элементов делится на 5 и хотя бы
один из двух элементов меньше среднего арифметического всех элементов последовательности, значение которых нечетно. В 
ответе запишите два числа: сначала количество найденных пар, а затем— максимальную сумму элементов таких пар.'''
# f = open('17_32.txt', 'r', encoding='utf-8')
# a = []
# sr = 0
# k = 0
# for line in f:
#     t = int(line)
#     a.append(t)
#     if t % 2 == 1:
#         sr += t
#         k += 1
# f.close()
# u = sr // k
# k = 0
# summ = 0
# n = len(a)
# for i in range(n - 1):
#     if (a[i] < u or a[i + 1] < u) and (a[i] % 5 == 0 or a[i + 1] % 5 == 0):
#         k += 1
#         summ = max(summ, a[i] + a[i + 1])
# print(k, summ)

'''Файл содержит последовательность неотрицательных целых чисел, не превышающих 10000. Назовём парой два идущих подряд 
элемента последовательности. Определите количество пар, в которых один из двух элементов делится на 3, а другой меньше 
среднего арифметического всех чётных элементов последовательности. В ответе запишите два числа: сначала количество 
найденных пар, а затем— максимальную сумму элементов таких пар.'''
# f = open('17_34.txt', 'r', encoding='utf-8')
# a = []
# k = 0
# sr = 0
# for line in f:
#     t = int(line)
#     a.append(t)
#     if t % 2 == 0:
#         sr += t
#         k += 1
# f.close()
# u = sr // k
# n = len(a)
# k = 0
# summ = 0
# for i in range(n - 1):
#     if (a[i] < u and a[i + 1] % 3 == 0) or (a[i + 1] < u and a[i] % 3 == 0):
#         k += 1
#         summ = max(summ, a[i] + a[i + 1])
# print(k, summ)

'''Файл содержит последовательность неотрицательных целых чисел, не превышающих 10000. Назовём парой два идущих подряд 
элемента последовательности. Определите количество пар, в которых один из двух элементов делится на 5, а другой меньше
среднего арифметического всех нечётных элементов последовательности. В ответе запишите два числа: сначала количество 
найденных пар, а затем— максимальную сумму элементов таких пар.'''
# f = open('17_35.txt', 'r', encoding='utf-8')
# a = []
# k = 0
# st = 0
# for line in f:
#     t = int(line)
#     a.append(t)
#     if t % 2 == 1:
#         st += t
#         k += 1
# f.close()
# u = st // k
# k = 0
# summ = 0
# n = len(a)
# for i in range(n - 1):
#     if (a[i] < u and a[i + 1] % 5 == 0) or (a[i + 1] < u and a[i] % 5 == 0):
#         k += 1
#         summ = max(summ, a[i] + a[i + 1])
# print(k, summ)

'''В файле содержится последовательность целых чисел. Элементы последовательности могут принимать целые значения от 
−10000 до 10000 включительно. Определите количество пар последовательности, в которых только одно число оканчивается на
 3, а сумма квадратов элементов пары не меньше квадрата максимального элемента последовательности, оканчивающегося на 3.
В ответе запишите два числа: сначала количество найденных пар, затем максимальную из сумм квадратов элементов таких пар.
В данной задаче под парой подразумевается два идущих подряд элемента последовательности'''
# f = open('17_36.txt', 'r', encoding='utf-8')
# max_l = -10001
# a = []
# for line in f:
#     t = int(line)
#     a.append(t)
#     if t % 10 == 3 and t > max_l:
#         max_l = t
# f.close()
# n = len(a)
# k = 0
# m = -100000000
# for i in range(n - 1):
#     s = (a[i]**2 + a[i + 1]**2)
#     if ((a[i] % 10 == 3 and a[i + 1] % 10 != 3) or (a[i] % 10 != 3 and a[i + 1] % 10 == 3)) and s >= (max_l**2):
#         k += 1
#         m = max(m, s)
# print(k, m)


'''(№ 5247) В файле 17-324.txt содержится последовательность целых чисел. Элементы последовательности – четырёхзначные 
натуральные числа. Найдите все тройки элементов последовательности, для которых пятеричная запись суммы всех чисел
тройки представляет собой палиндром, а среднее арифметическое всех чисел тройки больше, чем среднее арифметическое всех
чисел в файле, кратных 31. В ответе запишите количество найденных троек, затем минимальную из сумм элементов таких 
троек. В данной задаче под тройкой подразумевается три идущих подряд элемента последовательности.'''
# def Trans_5(x):
#     s = ''
#     while x > 0:
#         s += str(x % 5)
#         x //= 5
#     s = s[::-1]
#     return s
#
#
# f = open('17pol.txt', 'r', encoding='utf-8')
# a = []
# v = []
# for line in f:
#     a.append(int(line))
#     if a[-1] % 31 == 0:
#         v.append(a[-1])
# f.close()
#
# n = len(a)
# t = sum(v) // len(v)
# k = 0
# min1 = 10**10
# for i in range(n - 2):
#     s = a[i] + a[i + 1] + a[i + 2]
#     d = Trans_5(s)
#     if d == d[::-1] and (s) / 3 > t:
#         k += 1
#         min1 = min(min1, s)
# print(k, min1)


'''В файле содержится последовательность целых чисел. Элементы последовательности могут принимать целые значения от 
−10000 до 10000 включительно. Определите количество пар последовательности, в которых только одно число оканчивается 
на 3, а сумма квадратов элементов пары не меньше квадрата максимального элемента последовательности, оканчивающегося на
3. В ответе запишите два числа: сначала количество найденных пар, затем максимальную из сумм квадратов элементов таких
пар. В данной задаче под парой подразумевается два идущих подряд элемента последовательности.'''
# f = open('17_36.txt', 'r', encoding='utf-8')
# a = []
# for line in f:
#     a.append(int(line))
# f.close()
# n = len(a)
# k = -10000
# k1 = 0
# m = -5
# for i in range(n):
#     if abs(a[i]) % 10 == 3 and a[i] > k:
#         k = a[i]
# r = k*k
# for i in range(n - 1):
#     if ((abs(a[i]) % 10 == 3 and abs(a[i + 1]) % 10 != 3) or (abs(a[i]) % 10 != 3 and abs(a[i + 1]) % 10 == 3)) and a[i]**2 + a[i + 1]**2 >= r:
#         k1 += 1
#         m = max(m, a[i]**2 + a[i + 1]**2)
# print(k1, m)