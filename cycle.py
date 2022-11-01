userTickets = [input("Введите Ваше имя: "), input("Введите число билетов, которые хотите приобрести: ")]
bill = 0
while not userTickets[1].isdigit():
    userTickets[1] = input("Значение должно быть числом: ")
for i in list(range(int(userTickets[1]))):
    ageGuest = int(input(f"Введите возраст гостя {i+1}: "))
    if ageGuest < 18:
        bill += 0
        i += 1
    elif 18 <= ageGuest < 25:
        bill += 990
        i += 1
    elif ageGuest > 25:
        bill += 1390
        i += 1
if userTickets[1] > "3":
    bill = round(bill - (bill * 10/100), 2)
    print(f"{userTickets[0]}, так как Вы приобрели более 3 билетов, то ваша скидка составила 10%. \n"
          f"Стоимость Ваших билетов составляет {bill} руб.")
else:
    print(f"{userTickets[0]}, стоимость Ваших билетов составляет {bill} руб.")
