#если кол-во не похожих элементов четно, выввести ЧАТ ВИЗ ХЕ.

# name = 'Aleksei'
#
# if len(name) < 100:
#     list2 = []
#     for i in name:
#         if i not in list2:
#             list2.append(i)
#     if len(list2) % 2 == 0:
#         print('CHAT WITH HER!')
#     else:
#         print('IGNORE HIM!')

#https://codeforces.com/problemset/problem/677/A
                #Решение 1
# n = int(input())
# h = int(input())
# i = 0
# y = 0
# while i < n:
#     rost = int(input())
#     if rost > h:
#         y = y + 2
#     else:
#         y = y + 1
#     i = i + 1
# print(y)
                    #РЕШЕНИЕ 2.
# string = input().split()
# print(string)
# n = int(string[0])
# h = int(string[1])
# list1 = list(map(int, input().split()))
# lat = 0
# for student in list1:
#     if student > n:
#         lat += 2
#     else:
#         lat += 1
# print(lat)

#ZADACHA: https://codeforces.com/problemset/problem/581/A

#REWENIE1

# a, b = input().split()
# a = int(a)
# b = int(b)

# print(min(a,b), (max(a,b) - min(a,b)) // 2)

#REWENIE2

# socks = list(map(int,input().split()))
# a = socks[0]
# b = socks[1]
# count_fash = 0
# count_notfash = 0
# if a > b:
#     a = a - b
#     if a > 1:
#         count_notfash = a // 2
#     print(b, count_notfash)
# elif a < b:
#     b = b - a
#     if b > 1:
#         count_notfash = b // 2
#         print(a, count_notfash)
#     elif b == 1:
#         b = a
#         print(b, count_notfash)
# elif a == b:
#     a = a + b
#     a = a//2
#     print(a, count_notfash)

#ZADACHA: https://codeforces.com/problemset/problem/381/A

# n = int(input())
# list1 = list(map(int,input().split()))
# ser = 0
# dim = 0
# i = 0
# while i < n:
#     scales = max(list1[0],list1[-1])
#     if i % 2 == 0:
#         ser += scales
#     else:
#         dim += scales
#     i += 1
#     list1.remove(scales)
# print(ser,dim)


# list1 = [1,1,1,1,2,3,4,4,8,8,7,9,3,7,6]
# dict1 = {}
#
# for i in range(len(list1)):
#
#     dict1[list1[i]] = list1.count(list1[i])
#
#     i += i
#
# print(dict1)

#https://codeforces.com/problemset/problem/131/A

# string = input()
#
# if not string[0].istitle() and string[1:].isupper():
#     print(string.swapcase())
# elif string.isupper():
#     print(string.swapcase())
# elif len(string)>1 and string.islower():
#     print(string)
# elif len(string)==1 and string.islower():
#     print(string.swapcase())
# else:
#     print(string)

#https://codeforces.com/problemset/problem/1368/A
# t = int(input())
# i = 0
# while i < t:
#     data = list(map(int,input().split()))
#     a = data[0]
#     b = data[1]
#     n = data[2]
#     i += 1
#     count = 0
#     while max(a,b) <= n+1:
#         if a < b:
#             a += b
#         else:
#             b += a
#
#         count += 1
#
#     print(count)

#Игра 21 очко!

# from random import randint
#
# players = 10
# names = ['urmatik', 'beksich', 'aziretich', 'businesswman', 'erjanchik', 'ataichik', 'rasulchik',
#          'rusik', 'sanjarchik', 'saidchik']
# w_names = []
# dict1 = {}
# list1 = []
# i = 0
#
#
# def twenty_one(names, players: int):
#     i = 0
#     while i < players:
#         print(f'Играет {names[i]}')
#         two_cards = randint(2, 11) + randint(2, 11)
#         print(two_cards)
#         check = input('One more? да/нет')
#         while check == 'да':
#             two_cards = two_cards + randint(2, 11)
#             print(two_cards)
#             if two_cards > 21:
#                 break
#             check = input('One more? да/нет')
#
#         if two_cards > 21:
#             two_cards = 0
#         if two_cards > 0:
#             w_names.append(names[i])
#             list1.append(two_cards)
#         # Придумать алгоритм на удаление из names
#
#         dict1[names[i]] = two_cards
#         print(f'У игрока {names[i]} {two_cards} очков!')
#         i += 1
#
#
# twenty_one(names, 10)
# print(w_names, list1)
# w_names2 = []
#
# w_list = []
# list1_max = max(list1)
# for i in range(len(list1)):
#     if list1_max == list1[i]:
#         w_names2.append(w_names[i])
#         w_list.append(list1[i])
# twenty_one(w_names2, len(w_names2))






























