# Investment report.
# Developers: A. Mazenkov -,
#             A. Mikhailov -,
#             K. Kravtsov -

# Разработать программу, позволяющую получать информацию за каждый месяц об инвестициях капитала в течение нескольких
# лет при ежемесячной капитализации.


# НЕ ЗАБУДЬТЕ ПРО КОММЕНТАРИИ!!!!!!!

term = int(input("Срок размещения капитала (лет):"))                            # Input period.
initial_capital = float(input("Начальный капитал ($):"))                        # Initial capital input.
percent = float(input("Процентная ставка (%/мес.):"))                           # Input interest rate.
infusion = float(input("Инвестиционные вливания ($/мес.):"))                    # Input additional investments.
year_output = float(input("Раз в сколько лет выводить депозит:"))               # Input output step.

all_sum = initial_capital
# We will consider interest and infusion for each period
for i in range(1, term+1):

    if i % year_output == 0 or i == term or i == 1:
        #TODO(Mikhailov): String for print table header

        first_sum = all_sum                                                     # Variable for original amount

    for j in range(12):
        all_sum *= (1+(percent/100))                                            # Interest accrual

        accruals = all_sum - first_sum                                          # Monthly accrual

        if j < 11:                                                              # Interest infusion
            all_sum += infusion

        if i % year_output == 0 or i == term or i == 1:                         # If in order to display a table
            print(all_sum)                                                      # TODO(Mikhailov): Print for table for month

    all_sum += infusion


# TODO(Mikhailov): Когда Костя сделает формулу, сделай красиво, чтобы она выводилась в таблице, которая снизу

# for year in range(1, years + 1):                                                # Loop with an example
#     print(year, "год")                                                          # of the final output.
#     print("-------------------------------------------")
#     print("|       |   основа   | сумма %  |         |")
#     print("| месяц | инвестиций | за месяц | капитал |")
#     print("-------------------------------------------")

