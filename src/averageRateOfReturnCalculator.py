#!/usr/bin/env python3

import formulas.financeFormulas as FM
import investmentsavingsaccount.investmentsavingsaccount as ISK
import math

if __name__ == "__main__":
    fm = FM.FinanceFormulas()
    isk = ISK.InvestmentSavingsAccount()

    # Ask for initial values
    totalRateOfReturn = input("Enter the total rate of return of the period: ")
    years = input("Enter the length of the period in years?: ")

    # Convert to actual values
    totalRateOfReturn = float(totalRateOfReturn)
    years = int(years)

    print(str(round(fm.average_rate_of_return_per_year(totalRateOfReturn, years) * 100, 2)) + " %")
