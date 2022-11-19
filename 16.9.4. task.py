# Команда проекта «Дом питомца» планирует
# большой корпоратив для своих клиентов.
# Вам необходимо написать программу,
# которая позволит составить список гостей.
# В класс «Клиент» добавьте метод,
# который будет возвращать информацию только об имени,
# фамилии и городе клиента.
#
# Затем создайте список, в который будут добавлены все клиенты,
# и выведете его в консоль.

class Customers:
    def __init__(self, first_name, second_name, city, balance):
        self.first_name = first_name
        self.second_name = second_name
        self.city = city
        self.balance = balance

    def __str__(self):
        return f'''{self.first_name} {self.second_name}. {self.city}. Баланс: {self.balance} руб'''

    def get_guest(self):
        return f'{self.first_name} {self.second_name}. г.{self.city}.'

costomer_1 = Customers('\n''Василий', 'Сидоров', 'Саратов',100)
costomer_2 = Customers('\n''Матвей', 'Кошечкин', 'Москва', 500)
costomer_3 = Customers('\n''Геннадий', 'Иванов', 'Красноярск', 50)

_list = [costomer_1, costomer_2, costomer_3]

for guest in _list:
    print(guest.get_guest())
