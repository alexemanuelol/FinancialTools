#!/usr/bin/env python3

import formulas.financeFormulas as FM
import investmentsavingsaccount.investmentsavingsaccount as ISK
import math

if __name__ == "__main__":
    fm = FM.FinanceFormulas()
    isk = ISK.InvestmentSavingsAccount()

    # Ask for initial values
    values = input("Enter the rate of return (percentage) for every year (seperate with space):\n").split(" ")

    # Convert values to integers
    for index, value in enumerate(values):
        value = float(value.replace(",", "."))
        values[index] = value / 100

    print(str(round(fm.geometric_mean_return(values) * 100, 2)) + " %")
