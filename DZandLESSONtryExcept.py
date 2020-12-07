                    #Задача1

#a = str(input('Введите предложение:'))

#
# if a[0].isupper() and a.endswith('.'):
#     print(a)
# elif a[0].islower() and a[-1].endswith('.'):
#     a = a.capitalize()
#     print(a)
# elif a[0].isupper() and not a[-1].endswith('.'):
#     print(a + '.')
# elif a[0].islower() and not a[-1].endswith('.'):
#     a = a.capitalize()
#     print(a + '.')

                #Решение

# a = a.capitalize()
# if not a.endswith('.'):
#     a = a + '.'
#
# print(a)

                    #Задача 2
# a = str(input('Введите свой номер:'))
#
# if 9 > len(a) < 13 and a.startswith('+'):
#      print(a)
# elif 9 > len(a) < 13 and a.startswith('0'):
#      a = a.replace('0', '', 1)
#      print('+996' + a)
# elif 9 > len(a) == 9 and a[0].isdigit():
#      print('+996' + a)
# elif 9 > len(a) < 13 and a.startswith('996'):
#      print('+' + a)
# else:
#     print('Вы ввели неправильный номер')


            #Задача 3
# n = int(input())
# i = 1
# sum = 0
#
# while i <= n:
#     sum += i**2
#     i += 1
# print(sum)
                    #Задача 5
# a = int(input('Введите вес Лимака:'))
# b = int(input('Введите вес Боба:'))
# year = 0
# while b > a:
#     year += 1
#     a = a * 3
#     b = b * 2
#
#
# print(year)

# list1 = [1,2,3]
# try:
#     print(list1[4]) #программа ловит ошибку, если мы попытаемся вытащить четвертый элемент
# except IndexError:
#     print(list1[-1]) #программа не допускает ошибку и выводит последний элемент!


def register(username, password, check_password):
    if password == check_password:
        if 8 < len(username) < 40 and 8 < len(password) < 14:
            print('Регистриация прошла успешно!')
            with open('database.txt', 'w') as db1:
                db1.write(username+'\n'+password)
            code = 1234
            return code
        else:
            print('Неправильная длина!')
    else:
        print('Пароли не совпадают!')

answer = register('falone641234', '12345678qwe', '12345678qwe')

print(answer)

def check_code(guess, answer):
    if answer == guess:
        print('Все успешно! Можете входить')
    else:
        print('Неверный код!')










