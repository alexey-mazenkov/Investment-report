# Investment report.
# Developers: A. Mazenkov -,
#             A. Mikhailov -,
#             K. Kravtsov -

years = int(input("Срок размещения капитала (лет):"))
initial_capital = float(input("Начальный капитал ($):"))
percent = float(input("Процентная ставка (%/мес.):"))
investment_infusion = float(input("Инвестиционные вливания ($/мес.):"))

for year in range (1, years + 1):
    print(year,"год")
    print ("-------------------------------------------")
    print ("|       |   основа   | сумма %  |         |")
    print ("| месяц | инвестиций | за месяц | капитал |")
    print ("-------------------------------------------")