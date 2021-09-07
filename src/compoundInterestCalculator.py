#!/usr/bin/env python3

import formulas.financeFormulas as FM
import investmentsavingsaccount.investmentsavingsaccount as ISK
import math

def format_number(number):
    return str(format(math.ceil(int(number)), ",").replace(",", " ").replace(".", ","))

if __name__ == "__main__":
    fm = FM.FinanceFormulas()
    isk = ISK.InvestmentSavingsAccount()

    # Ask for initial values
    startCapital = input("Enter Start Capital (Default 250000): ")
    monthlyDeposit = input("Enter Monthly Save (Default 5000): ")
    rateOfReturn = input("Enter Yearly Return (Default 8): ")
    yearsToSave = input("Enter Years to Save (Default 20): ")
    flatRateTax = input("Should Flat-Rate Tax be included? (y/n) (Default y): ")

    # Convert to actual values (string -> number/bool)
    startCapital = 250000 if startCapital == "" else float(startCapital)
    monthlyDeposit = 5000 if monthlyDeposit == "" else float(monthlyDeposit)
    rateOfReturn = .08 if rateOfReturn == "" else (float(rateOfReturn) / 100)
    yearsToSave = 20 if yearsToSave == "" else int(yearsToSave)
    flatRateTax = True if flatRateTax.lower() == "y" or flatRateTax == "" else False

    avgRateOfReturnPerMonth = fm.average_rate_of_return_per_year(rateOfReturn + 1, 12)

    print("\nStart Capital: ".ljust(25) + format_number(startCapital))
    print("Monthly Deposit:  ".ljust(25) + format_number(monthlyDeposit))
    print("Rate of Return: ".ljust(25) + str(format_number(round((rateOfReturn) * 100)) + " %"))
    print("Years to Save:         ".ljust(25) + format_number(yearsToSave))
    print("Flat-Rate Tax included: ".ljust(25) + str(flatRateTax) + "\n")
    string = "Year:".ljust(8)
    string += "Gained:".ljust(15)
    string += "Salary/Month:".ljust(15)
    string += "Flat-tax Rate:".ljust(15)
    string += "Tot Saved:".ljust(15)
    string += "Tot Gained:".ljust(15)
    string += "Tot Capital:".ljust(15)
    string += "\n" + ("-" * 95)
    print(string)

    totalCapital = totalSaved = startCapital
    totalGained = yearlyGained = 0
    quaterValues = list()
    yearCounter = 1
    for month in range(yearsToSave * 12):
        totalCapital += monthlyDeposit
        totalSaved += monthlyDeposit

        monthCompound = fm.compound_interest(totalCapital, avgRateOfReturnPerMonth, 1)
        yearlyGained += monthCompound
        totalGained += monthCompound
        totalCapital += monthCompound

        if (month % 12) in [0, 3, 6, 9]:
            quaterValues.append(totalCapital)

        # If the end of a year.
        if month % 12 == 11:
            tax = isk.calculate_flat_rate_tax(quaterValues, monthlyDeposit * 12, .0002)
            quaterValues = list()
            totalCapital -= tax if flatRateTax else 0

            line = str(yearCounter).ljust(8)
            line += format_number(yearlyGained).ljust(15)
            line += format_number(yearlyGained / 12).ljust(15)
            line += format_number(tax).ljust(15)
            line += format_number(totalSaved).ljust(15)
            line += format_number(totalGained).ljust(15)
            line += format_number(totalCapital)
            print(line)

            yearlyGained = 0
            yearCounter += 1

