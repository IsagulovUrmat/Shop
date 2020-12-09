# Нужно написать функцию которая будет считать текущий счет клиента, т е на вход подаются два аргумента
# деньги клиента и стоимость какого то товара, функция отнимает от суммы клиента счет товара и возвращает
# измененную сумму клиента. Клиент добавляет из общего каталога товаров, те которые хочет купить,
# т.е в список, затем пишется новая функция которая будет перебирать общий каталог и товары которые выбрал клиент,
# вызывать функцию счета,
# в случае если у клиента не хватает денег функия должна сказать ему об этом и
# передаются только те товары которые он успел выбрать.

catalogue = {'hot-dot':50,'hamburger':120,'shaurma':150,'naggets':130,'piza':930,
             'boso-lagman':250,'plov':190,'giro-lagman':240,'mantes':160,'rolls':600,
             'garnir':100,'grechka':70,'pelmeni':130,'french meat':400,'fish':500,
             't-bone':870,'Beijing duck':5000,'shashlyk assorti':50000 }

username1 = 'tralala'
password2 = 'youtouchmy2'

username = input('Введите логин:')
password = input('Введите пароль:')

def auth(username,password):
    if username == username1 and not password.isdigit() and not password.isalpha() and len(password) < 15 and password == password2:
                print('Регистрация прошла успешно!')
    else:
        print('Неправильные данные!')

auth(username,password)

def counter(money,price):
    if money < price:
        return 'no money'
    else:
        result = money - price
        return result

def choice(num_of_food):
    list1 = []
    for i in range(num_of_food):
        new_elem = input('Choose food:')
        if new_elem in catalogue:
        list1.append(new_elem)

    return list1


def order():
    money = 1000
    list1 = choice(3)
    for food in list1:
        price = catalogue[food]
        if money >= price:
            money = counter(money,price)
    print(money)















