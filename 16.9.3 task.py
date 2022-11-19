# В проекте «Дом питомца» добавим новую услугу — электронный кошелек.
# Необходимо создать класс «Клиент»,
# который будет содержать данные о клиентах
# и их финансовых операциях.
# О клиенте известна следующая информация: имя, фамилия, город, баланс.
#
# Далее сделайте вывод о клиентах в консоль в формате:
# «Иван Петров. Москва. Баланс: 50 руб.»

class Customers:
    def __init__(self, first_name, second_name, city, balance):
        self.first_name = first_name
        self.second_name = second_name
        self.city = city
        self.balance = balance

    def __str__(self):
        return f'''{self.first_name}, {self.second_name}. {self.city}. Баланс: {self.balance} руб'''

costomer_1 = Customers('Василий', 'Сидоров', 'Саратов',100)
costomer_2 = Customers('\n''Матвей', 'Кошечкин', 'Москва', 500)
costomer_3 = Customers('\n''Геннадий', 'Иванов', 'Красноярск', 50)
print(costomer_1, costomer_2, costomer_3)
