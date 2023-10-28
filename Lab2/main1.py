salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
money_capital = 0

for i in range(months, 0, -1):
    if i != 10:
        spend += spend * increase
    money_capital += spend - salary

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", f'{money_capital:.2f}')
