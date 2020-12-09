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

n = int(input())
h = int(input())
i = 0
y = 0
while i < n:
    rost = int(input())
    if rost > h:
        y = y + 2
    else:
        y = y + 1
    i = i + 1
print(y)





