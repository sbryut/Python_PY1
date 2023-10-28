money_capital = 20000  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен
count = 0
while (True):
    if count != 0:
        spend += spend * increase
    money_capital -= spend - salary
    if money_capital > 0:
        count += 1
    else:
        break
print("Количество месяцев, которое можно протянуть без долгов:", count)
