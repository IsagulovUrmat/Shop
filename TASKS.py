name = 'Aleksei'

if len(name) < 100:
    list2 = []
    for i in name:
        if i not in list2:
            list2.append(i)

    if len(list2) % 2 == 0:
        print('CHAT WITH HER!')
    else:
        print('IGNORE HIM!')