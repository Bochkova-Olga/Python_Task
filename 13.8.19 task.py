# # # ЗАДАНИЕ 13.8.19 (HW-03)
ticket = int(input('Введите количество необходимых билетов: \n'))
list_visitors = []
cost_tickets_age = {'age < 18': 0, '18 < age <= 25': 990, 'age > 25': 1390}
total = []
count = 0
while count != ticket:
    age = int(input("Введите возраст посетителя: "))
    list_visitors.append(age)
    count += 1
    if age < 18:
        total.append(cost_tickets_age.get('age < 18')),
    elif 8 < age <= 25:
        total.append(cost_tickets_age.get('18 < age <= 25')),
    elif age > 25:
        total.append(cost_tickets_age.get('age > 25')),
        print("Сумма к оплате, руб.:", sum(total))
        S = 0
for cost_tickets_age in list_visitors:
    if age < 18:
        print("Бесплатно")
        continue
    if 18 < age <= 25:
       sum([total] * 990)
    if age > 25:
       sum([total] * 1390)
    if ticket > 3:
        S *= 0.1
        print(f"Сумма оплаты в руб. с учетом скидки 10%", "{S:. ticket}")
        break

