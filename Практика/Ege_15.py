# '''(y + 2x ≠ 48) ∨ (A < x) ∨ (x < y)'''
# m = 1000
# for x in range(0, 25):
#     for y in range(0, 49):
#         if y + 2 * x == 48 and x >= y:
#             m = min(m, x - 1)
# print(m)


# '''(y + 2x ≠ 48) ∨ (A < x) ∨ (A < y)'''
# m = 1000
# for x in range(0, 25):
#     for y in range(0, 49):
#         if y + 2 * x == 48:
#             m = min(m, max(x - 1, y - 1))
# print(m)


# '''(2x + 3y > 30) ∨ (x + y ≤ A)'''
# m = 0
# for x in range(0, 16):
#     for y in range(0, 11):
#         if 2 * x + 3 * y <= 30:
#             m = max(m, x + y)
# print(m)


# '''(2x + 3y < 30) ∨ (x + y ≥ A)'''
# m = 1000
# for x in range(0, 16):
#     for y in range(0, 11):
#         if 2 * x + 3 * y >= 30:
#             m = min(m, x + y)
# print(m)


# '''(3x + 4y ≠ 70) ∨ (A > x) ∨ (A > y)'''
# m = 0
# for x in range(0, 24):
#     for y in range(0, 18):
#         if 3 *x + 4 * y == 70:
#             m = max(m, min(x + 1, y + 1))
# print(m)


# '''(2x + 3y ≠ 60) ∨ (A ≥ x) ∨ (A ≥ y)'''
# m = 0
# for x in range(0, 31):
#     for y in range(0, 21):
#         if 2 * x + 3 * y == 60:
#             m = max(m, min(x, y))
# print(m)

# '''(y + 2x < A) ∨ (x > 15) ∨ (y > 30)'''
# m = 0
# for x in range(0, 16):
#     for y in range(0, 31):
#         m = max(m, y + 2*x + 1)
# print(m)

# '''(2m + 3n > 40) ∨ ((m < A) ∧ (n ≤ A))'''
# m = 0
# for x in range(0, 21):
#     for y in range(0, 14):
#       m = max(m, max(x + 1, y))
# print(m)


# '''(x * y < A) ∨ (x < y) ∨ (x ≥ 12)'''
# m = 0
# for x in range(0, 12):
#     for y in range(0, 12):
#         if x < y:
#             m = max(m, x * y)
# print(m)


# '''(x·y < 121) ∨ (y > A) ∨ (x ≥ A)'''
# m = 1000
# for x in range(1, 122):
#     for y in range(1, 122):
#         if x * y >= 121:
#             m = min(m, max(x, y - 1))
# print(m)


# '''(2x + y ≠ 70) ∨ (x < y) ∨ (A < x)'''
# m = 1000
# for x in range(0, 36):
#     for y in range(0, 71):
#         if 2 * x + y == 70 and x >= y:
#             m = min(m, x - 1)
# print(m)


# '''(3x + 4y ≠ 60) ∨ ((A ≥ x) ∧ (A ≥ y))'''
# m = 0
# for x in range(0, 21):
#     for y in range(0, 16):
#         if 3 * x + 4 * y == 60:
#             m = max(m, max(x, y))
# print(m)


# '''(5x + 3y ≠ 60) ∨ ((A > x) ∧ (A > y))'''
# m = 0
# for x in range(0, 13):
#     for y in range(0, 21):
#         if 5 * x + 3 * y == 60:
#             m = max(m, max(x + 1, y + 1))
# print(m)


# '''(3m + 4n > 66) ∨ (m ≤ A) ∨ (n < A)'''
# x = 0
# for m in range(0, 23):
#     for n in range(0, 17):
#         if 3 * m + 4 * n <= 66:
#             x = max(x, min(m, n + 1))
# print(x)

'''Обозначим через m&n поразрядную конъюнкцию неотрицательных целых чисел m и n.
Так, например, 14&5=11102&01012 = 01002 = 4.
Для какого наименьшего неотрицательного целого числа А формула
 левая круглая скобка левая круглая скобка xв подстановке от до 28 в подстановке от до ne0 правая круглая скобка в
подстановке от до vee левая круглая скобка xв подстановке от до 45 в подстановке от до ne 0 правая круглая скобка правая
круглая скобка в подстановке от до rightarrow левая круглая скобка левая круглая скобка xв подстановке от до 17=0 правая
круглая скобка в подстановке от до rightarrow левая круглая скобка xв подстановке от до A в подстановке от до ne 0
правая круглая скобка правая круглая скобка
тождественно истинна (то есть принимает значение 1 при любом неотрицательном целом значении переменной x)?'''
# for a in range(0, 101):
#     q = True
#     for x in range(0, 100):
#         if (((x&28 != 0) or (x&45 != 0)) <= ((x&17 == 0) <= (x&a != 0))) == 0:
#             q = False
#             break
#     if q:
#         print(a)
#         break

'''(X & 56 ≠ 0) → ((X & 48 = 0) → (X & A ≠ 0))'''
# for A in range(1, 1000):
#     q = True
#     for x in range(0, 57):
#         if ((x & 56 != 0) <= ((x & 48 == 0) <= (x & A != 0))) == 0:
#             q = 0
#             break
#     if q:
#         print(A)
#         break

'''(X & A ≠ 0) → ((X & 56 = 0) → (X & 20 ≠ 0))'''
# for A in range(10000, 0, -1):
#     q = 1
#     for x in range(1, 10000):
#         if ((x & A != 0) <= ((x & 56 == 0) <= (x & 20 != 0))) == 0:
#             q = 0
#             break
#     if q:
#         print(A)
#         break



'''(X & A ≠ 0) → ((X & 30 = 0) → (X & 20 ≠ 0))'''
# for A in range(10000, 0, -1):
#     q = 1
#     for x in range(1, 10000):
#         if ((x & A != 0) <= ((x & 30 == 0) <= (x & 20 != 0))) == 0:
#             q = 0
#             break
#     if q:
#         print(A)
#         break


'''(X & A ≠ 0) → ((X & 44 = 0) → (X & 76 ≠ 0))'''
# for A in range(10000, 0, -1):
#     q = 1
#     for x in range(0, 10000):
#         if ((x & A != 0) <= ((x & 44 == 0) <= (x & 76 != 0))) == 0:
#             q = 0
#             break
#     if q:
#         print(A)
#         break

''''(X & A ≠ 0) → ((X & 29 = 0) → (X & 86 ≠ 0))'''
# for A in range(10000, 0, -1):
#     q = 1
#     for x in range(1, 10000):
#         if ((x & A != 0) <= ((x & 29 == 0) <= (x & 86 != 0))) == 0:
#             q = 0
#             break
#     if q:
#         print(A)
#         break


'''(X & A ≠ 0) → ((X & 14 = 0) → (X & 75 ≠ 0))'''
# for A in range(10000, 0, -1):
#     q = 1
#     for x in range(1, 100000):
#         if ((x & A != 0) <= ((x & 14 == 0) <= (x & 75 != 0))) == 0:
#             q = 0
#             break
#     if q:
#         print(A)
#         break


'''(3x + 2y < A) ∨ (y > 10) ∨ (3y < x)'''
# m = 0
# for x in range(0, 31):
#     for y in range(0, 11):
#         if y <= 10 and 3*y >= x:
#             m = max(m, 3*x + 2*y + 1)
# print(m)


'''(y + 2x ≠ 36) ∨ (y > A) ∨ (x > A)'''
# m = 100000
# for x in range(19):
#     for y in range(37):
#         if y + 2*x == 36:
#             m = min(m, max(x - 1, y - 1))
# print(m)


'''(5y + x ≠ 96) ∨ (y > A) ∨ (3x > A)'''
# m = 100000
# for x in range(97):
#     for y in range(20):
#         if 5 * y + x == 96:
#             m = min(m, max(y -1, 3*x - 1))
# print(m)


''''(y + 3x < A) ∨ (y + x > 28) ∨ (y - x < 10)'''
# m = 0
# for x in range(0, 1000):
#     for y in range(0, 1000):
#         if y + x <= 28 and y - x >= 10:
#             m = max(m, y + 3 * x + 1)
# print(m)

'''(5y + 3x ≠ 110) ∨ (x > A) ∨ (2y > A)'''
# m = 1000000
# for x in range(37):
#     for y in range(23):
#         if 5 * y + 3 * x == 110:
#             m = min(m, max(x - 1, 2 * y - 1))
# print(m)

'''(3y + 2x ≠ 130) ∨ (3x > A) ∨ (2y > A)'''
# m = 10000000
# for x in range(66):
#     for y in range(44):
#         if 3 * y + 2 * x == 130:
#             m = min(m, max(3 * x - 1, 2 * y - 1))
# print(m)


''' (x ≥ 7) ∨ (2x < y) ∨ (xy < A)'''
# m = 0
# for x in range(0, 8):
#     for y in range(0, 17):
#         if x < 7 and 2 * x >= y:
#             m = max(m, x * y + 1)
# print(m)


'''(y - x + 10 ≠ 0) ∨ (A < 3x) ∨ (A < y)'''
# m = 1000000
# for x in range(10, 1000):
#     for y in range(1, 1000):
#         if y - x + 10 == 0:
#             m = min(m, max(y - 1, 3 * x - 1))
# print(m)

'''(y + 4x < A) ∨ (x + 3y > 100) ∨ (5x + 2y > 150)'''
# m = 0
# for x in range(1, 31):
#     for y in range(1, 34):
#         if x + 3 * y <= 100 and 5 * x + 2 * y <= 150:
#             m = max(m, y + 4 * x + 1)
# print(m)


'''(y + 4x < A) ∨ (x + 4y > 120) ∨ (5x - 2y > 50)'''
# m = 0
# for x in range(121):
#     for y in range(31):
#         if x + 4 * y <= 120 and 5 * x - 2 * y <= 50:
#             m = max(m, y + 4 * x + 1)
# print(m)









