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

n = int(input())
list1 = list(map(int,input().split()))
ser = 0
dim = 0
i = 0
while i < n:
    scales = max(list1[0],list1[-1])
    if i % 2 == 0:
        ser += scales
    else:
        dim += scales
    i += 1
    list1.remove(scales)
print(ser,dim)











