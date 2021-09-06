#!/usr/bin/env python3

import formulas.financeFormulas as FM
import investmentsavingsaccount.investmentsavingsaccount as ISK
import math


def format_number(number):
    return str(format(math.ceil(int(number)), ",").replace(",", " ").replace(".", ","))

if __name__ == "__main__":
    fm = FM.FinanceFormulas()
    isk = ISK.InvestmentSavingsAccount()

    ans = input("Enter Start Capital (Default 100000): ")
    startCapital = 100000 if ans == "" else float(ans)
    ans = input("Enter Monthly Save (Default 2000): ")
    monthlySave = 2000 if ans == "" else float(ans)
    ans = input("Enter Yearly Return (Default 8): ")
    yearlyReturn = .08 if ans == "" else (float(ans) / 100)
    ans = input("Enter Years (Default 40): ")
    years = 40 if ans == "" else int(ans)

    flatratetax = False
    ans = input("Should Flat-Rate tax be included? (y/n) (Default y): ")
    flatratetax = True if ans.lower() == "y" or ans == "" else False

    totalSum = totalSaved = startCapital
    totalGained = 0

    print("\nStart Capital: ".ljust(25) + format_number(startCapital))
    print("Monthly Save:  ".ljust(25) + format_number(monthlySave))
    print("Yearly Return: ".ljust(25) + str(format_number(round((yearlyReturn) * 100)) + " %"))
    print("Years:         ".ljust(25) + format_number(years))
    print("Flat-Rate Tax included: ".ljust(25) + str(flatratetax) + "\n")

    string = "Year:".ljust(8)
    string += "Gained:".ljust(15)
    string += "Salary/Month:".ljust(15)
    string += "Flat-tax Rate:".ljust(15)
    string += "Tax %:".ljust(10)
    string += "Tot Saved:".ljust(15)
    string += "Tot Gained:".ljust(15)
    string += "Tot Capital:".ljust(15)
    string += "\n" + ("-" * 105)
    print(string)

    yearCounter = 1
    for month in range(1, (years * 12) + 1):
        totalSum += monthlySave
        totalSaved += monthlySave

        # If the end of a year.
        if (month % 12) == 0 and month != 0:
            compound = fm.compound_interest(totalSum, yearlyReturn, 1)
            totalGained += compound

            quaterValues = list()
            for i in range(4):
                quaterValues.append(totalSum + ((compound / 3) * i))

            tax = isk.calculate_flat_rate_tax(quaterValues, 0, .0002)
            if flatratetax:
                totalSum += compound - tax
            else:
                totalSum += compound

            line = str(yearCounter).ljust(8)
            line += format_number(compound).ljust(15)
            line += format_number(compound / 12).ljust(15)
            line += format_number(tax).ljust(15)
            line += "{:.2f}".format((tax/compound) * 100).ljust(10)
            line += format_number(totalSaved).ljust(15)
            line += format_number(totalGained).ljust(15)
            line += format_number(totalSum)
            print(line)

            yearCounter += 1
