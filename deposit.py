per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = float(input("Введите сумму, которую планируете положить под проценты:", ))
per_cent_values = list(per_cent.values())
deposit = list()
for i in range(len(per_cent_values)):
    deposit.append(round(per_cent_values[i] * money / 100, 2))
print("Максимальная сумма, которую вы можете заработать — ", max(deposit))
