from random import *
a = [randint(-10, 10) for i in range(10)]
print(a)
col = 0
summ = 0
for i in a:
    if i % 2 == 0:
        col += 1
        summ += i
print(summ / col)