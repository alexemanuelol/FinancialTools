#!/usr/bin/env python3

# Swedish savings account

class InvestmentSavingsAccount():
    """ Is a Swedish savings option whereby you can save in stocks, shares and other types of securities.
        Also known as Investeringssparkonto (ISK).
    """

    def calculate_flat_rate_tax(self, quaterValues, deposits, governmentBorrowingRate):
        """ Calculates the taxes for the entire year of a investment savings account.
            Flat-tax rate is also known as Schablonskatt in Sweden.

            quaterValues = (list) The values of the account at the beginning of each quater (Q1, Q2, Q3, Q4).
            deposits = All deposits made to the account this year.
            governmentBorrowingRate = Also known as 'Statslåneräntan'.
        """
        capitalBase = (sum(quaterValues) + deposits) / 4

        # 1.25% is the lower limit
        imputedIncome = .0125 if (governmentBorrowingRate + .01) < .0125 else governmentBorrowingRate + .01

        # Capital Gain Tax (30%)
        return (capitalBase * imputedIncome) * .3
