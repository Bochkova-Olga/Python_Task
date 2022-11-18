# # Задание 12.7.3 (второй вариант решения)
# percent = {"ТКБ": 5.6, "СКБ": 5.9, "ВТБ": 4.28, "СБЕР": 4.0}
# print('Предложения от банков:')
# for key, value in percent.items(): print('\tБанк: {0}, ставка: {1}'.format(key, value))
# money = float(input("\nВведите сумму: "))
# print("\nНакопленные средства за год: ")
# deposit = []
# max_deposit_over_plus = 0;
# max_deposit_over_minus = 0;
#
# # Произвести умножение значений из словаря на введенное значение суммы
# # Понять, как умножать переменную на словарь и занести только значения ключей из словаря в массив
# for key, value in percent.items(): deposit.append(round((value / 100) * money))
# print(deposit)
#
# i = 0
# while i < len(deposit):
#     if deposit[i] > max_deposit_over_plus:
#         max_deposit_over_plus = deposit[i]
#     i += 1
#
# j = len(deposit)-1
# while j >= 0:
#     if deposit[j] > max_deposit_over_minus:
#         max_deposit_over_minus = deposit[j]
#     j -= 1
#
# print("\nCircle sort: \n\t" + max_deposit_over_plus.__str__() + " | " + max_deposit_over_minus.__str__())
#
# deposit.sort(reverse=True)
# print('\nВыгодный вклад:')
# print("\t" + deposit[0].__str__())

Задание 12.7.3 (первый вариант решения)
percent = {"ТКБ": 5.6, "СКБ": 5.9, "ВТБ": 4.28, "СБЕР": 4.0}
print('Предложения от банков:')
for key, value in percent.items(): print('\tБанк: {0}, ставка: {1}'.format(key, value))
money = float(input("\nВведите сумму: "))
print("\nНакопленные средства за год: ")
deposit = []
for key, value in percent.items(): deposit.append(round((value / 100) * money))
print(deposit)
deposit.sort(reverse=True)

print("\nВыгодный вклад:\n\t" + deposit[0].__str__())