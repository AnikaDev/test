# for i in range(1, 10000):
#     x = i
#     a = 0
#     b = 0
#     while x > 0:
#         a = a + 1
#         if x % 2 == 0:
#             b += x % 10
#         x = x // 10
#     if a == 3 and b == 18:
#         print(i)
#         break


# for i in range(10000):
#     x = i
#     R = 0
#     while x > 0:
#         d = x % 10
#         R = 10 * R + d
#         x = x // 10
#     f = str(R)
#     if len(f) == 2 and int(f[0]) + int(f[1]) == 16:
#         print(i)
#         break

# for i in range(10000):
#     x = i
#     a = 0
#     b = 0
#     while x > 0:
#         a = a + 1
#         if x % 2 == 0:
#             b += x % 10
#         x = x // 10
#     if a == 3 and b == 14:
#         print(i)
#         break

# for i in range(10000):
#     x = i
#     a = 0
#     b = 0
#     while x > 0:
#         a = a + 1
#         if x % 2 == 0:
#             b += x % 10
#         x=x // 10
#     if a == 3 and b == 16:
#         print(i)
#         break


# k = 0
# for i in range(100000):
#     x=i
#     a=0
#     b=1
#     while x > 0:
#         a = a + 1
#         b = b * (x % 10)
#         x = x // 10
#     if a == 2 and b == 24:
#         k += 1
# print(k)



# k = 0
# for i in range(10000):
#     x=i
#     a=0
#     b=1
#     while x>0:
#         a=a+1
#         b=b*(x%10)
#         x=x//10
#     if a == 2 and b == 0:
#         k += 1
# print(k)


# for i in range(100000, 1, -1):
#     x = i
#     a=0
#     b=0
#     while x>0:
#       a = a+1
#       if x%2==0:
#         b += x%10
#       x = x//10
#     if a == 3 and b == 12:
#         print(i)
#         break


# for i in range(100000, 1, -1):
#     x = i
#     a = 0;
#     b = 0
#     while x > 0:
#         a = a + 1
#         if x % 2 == 0:
#             b += x % 10
#         x = x // 10
#     if a == 3 and b == 14:
#         print(i)
#         break

# for i in range(10000000, 1, -1):
#     x = i
#     a = 0;
#     b = 0
#     while x > 0:
#         if x % 2 == 0:
#             a += 1
#         else:
#             b += x % 10
#         x = x // 10
#     if a == 2 and b == 4:
#         print(i)
#         break


# for i in range(1, 10000):
#     x = i
#     a = 0
#     b = 0
#     while x > 0:
#         if x % 2 == 0:
#             a += 1
#         else:
#             b += x % 10
#         x = x // 10
#     if a == 2 and b == 4:
#         print(i)
#         break

# for i in range(1, 10000):
#     x = i
#     a, b = 0, 0
#     while x > 0:
#         c = x % 10
#         a = a + c
#         if b < c:
#             b = c
#         x = x // 10
#     if a == 10 and b == 6:
#         print(i)
#         break