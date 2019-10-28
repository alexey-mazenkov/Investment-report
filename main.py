# Investment report.
# Developers: A. Mazenkov - 40 %,
# A. Mikhailov - ,
# K. Kravtsov - 45%

import localization as lc

term = int(input(lc.term))                    # Input period.
initial_capital = float(input(lc.initial))                # Initial capital input.
percent = float(input(lc.percent))                   # Input interest rate.
infusion = float(input(lc.infusion))            # Input additional investments.
year_output = float(input(lc.year_output))       # Input output step.

all_sum = initial_capital

# We will consider interest and infusion for each period
for i in range(1, term + 1):

    if i % year_output == 0 or i == term or i == 1:
        print()
        print(i, lc.year)
        print(lc.table)

    first_sum = all_sum                                                 # Variable for original amount

    for j in range(12):
        all_sum *= (1 + (percent / 100))                                # Interest accrual

        accruals = all_sum - first_sum                                  # Monthly accrual

        if i % year_output == 0 or i == term or i == 1:                 # If in order to display a table
            str_1 = str("%.2f" % (first_sum))                           # Strings for table output
            len_1 = 12 - len(str_1)
            str_2 = str(j+1)
            len_2 = 5 - len(str_2)
            str_3 = str("%.2f" % (accruals))
            len_3 = 12 - len(str_3)
            str_4 = str("%.2f" % (all_sum))
            len_4 = 11 - len(str_4)
            print("|", " " * len_2, j+1, " " * 4, "|", str_1, " " * len_1, sep="", end="")
            print("|", str_3, " " * len_3, "|", str_4, " " * len_4, "|", sep="", end="")
            print()

        if j < 11:                                                      # Interest infusion
            all_sum += infusion

        first_sum = all_sum

    if i % year_output == 0 or i == term or i == 1:
        print("-------------------------------------------------")

    all_sum += infusion