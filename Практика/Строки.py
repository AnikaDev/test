# a = 'dfGHJGIUG89bnxs  sjhkhQJIOHn HGJjb n'
# print(a.capitalize())
# print(a.title())
# print(a.upper())
# print(a.lower())

# Создание пароля
# from random import *
# s1 = 'qwertyuiopasdfghjklzxcvbnm'
# s2 = s1.upper()
# s3 = '0123456789'
# s4 = '|!@#$%^&*()_+{}[]<>?/'
# alf = s1 + s2 + s3 + s4
# password = ''
# for i in range(15):
#     p = choice(alf)
#     password += p
# print(password)
#
#
# s4 = '|!@#$%^&*()_+[]{}?/'
# q1 = q2 = q3 = q4 = q5 = 0
# p = input()
# if len(p) > 5:
#     q5 = 1
# for i in p:
#     if i.isupper():
#         q1 = 1
#     if i.islower():
#         q2 = 1
#     if i.isdigit():
#         q3 = 1
#     if i in s4:
#         q4 = 1
# if q1:
#     if q2:
#         if q3:
#             if q4:
#                 if q5:
#                     print('надежный пароль')
#                 else:
#                     print('Слишком короткий')
#             else:
#                 print('Должны быть доп символы')
#         else:
#             print('Должны быть цифры')
#     else:
#         print('Должны быть строковые буквы')
# else:
#     print('Должны присутствовать заглавные буквы')
#
# def search_substr(subst, st):
#     subst = subst.upper()
#     st = st.upper()
#     if subst in st:
#         return 'есть контакт'
#     return 'нет контакта'
# print(search_substr('sdpoi', 'BGUIGuicndioSD'))

#
# def first_last(letter, st):
#     if letter in st:
#         return (st.find(letter), st.rfind(letter))
#     return (None, None)
# print(first_last('z', 'DFDGHjhkhidinl'))

# def top3(st):
#     alf = 'qwertyuiopasdfghjklzxcvbnm'
#     k = [0] * 26
#     alf = sorted(alf)
#     for i in range(26):
#         k[i] = st.count(alf[i])
#     for i in range(25):
#         for j in range(25 - i):
#             if k[j] > k[j + 1]:
#                 k[j], k[j + 1] = k[j + 1], k[j]
#                 alf[j], alf[j + 1] = alf[j + 1], alf[j]
#     print(alf[25:22:-1])
#
#
# st = input()
# top3(st)



# s = '9' * 127
# while '333' in s or '999' in s:
#     if '333' in s:
#         s = s.replace('333', '9', 1)
#     else:
#         s = s.replace('999', '3', 1)
# print(s)

#
# s = 1000 * '8'
# while '999' in s or '888' in s:
#     if '888' in s:
#         s = s.replace('888', '9', 1)
#     else:
#         s = s.replace('999', '8', 1)
# print(s)







