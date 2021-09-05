#!/usr/bin/env python3

import math

class FinanceFormulas():
    """ Common finance formulas.
        https://financeformulas.net/
    """

    def annual_percentage_yield(self, statedAnnualInterestRate, numberOfTimesCompounded):
        """ Calculates 'Annual Percentage Yield (APY)'

            statedAnnualInterestRate = Percentage (0-1)
            numberOfTimesCompounded = (number)

            Referenced as the effective annual rate in finance, is the rate of interest that is earned when taking
            into consideration the effect of compounding.
        """
        return ((1 + (statedAnnualInterestRate / numberOfTimesCompounded)) ** numberOfTimesCompounded) - 1


    def cost_of_goods_sold(self, openingInventoryValue, purchases, closingInventoryValue):
        """ Calculates 'Cost of Goods Sold (COGS)'

            openingInventoryValue = (number)
            purchases = (number)
            closingInventoryValue = (number)

            The formula calculates by adding purchases for the period to the beginning inventory and subtracting
            the ending inventory for the period.
        """
        return openingInventoryValue + purchases - closingInventoryValue


    def future_value_of_annuity(self, periodicPayment, ratePerPeriod, numberOfPeriods):
        """ Calculates 'Future Value of Annuity'

            periodicPayment = (number)
            ratePerPeriod = Percentage (0-1)
            numberOfPeriods = (number)

            The formula is used to calculate what the value at a future date would be for a series of periodic
            payments.
        """
        return periodicPayment * ((((1 + ratePerPeriod) ** numberOfPeriods) - 1) / ratePerPeriod)


    def future_value_of_annuity_with_continuous_compounding(self, cashFlow, rate, time):
        """ Calculates 'Future Value of Annuity - Continuous Compounding'

            cashFlow = (number)
            rate = Percentage (0-1)
            time = (number)

            The formula is used to calculate the ending balance on a series of periodic payments that are compounded
            continuously.
        """
        return cashFlow * ((math.exp(time * rate) - 1) / (math.exp(rate) - 1))


    def number_of_periods_for_future_value_of_annuity(self, futureValueOfAnnuity, ratePerPeriod, payment):
        """ Calculates 'Number of Periods for Future Value of Annuity'

            futureValueOfAnnuity = (number)
            ratePerPeriod = Percentage (0-1)
            payment = (number)

            The formula is used to calculate the number of periods based on the future value, rate and periodic cash
            flows.
        """
        return math.log(1 + ((futureValueOfAnnuity * ratePerPeriod) / payment)) / math.log(1 + ratePerPeriod)


    def annuity_payment_present_value(self, presentValue, ratePerPeriod, numberOfPeriods):
        """ Calculates 'Annuity Payment Present Value'

            presentValue = (number)
            ratePerPeriod = Percentage (0-1)
            numberOfPeriods = (number)

            The formula is used to calculate the periodic payment on an annuity. An annuity is a series of periodic
            payments that are received at a future date.
        """
        return (presentValue * ratePerPeriod) / (1 - (1 + ratePerPeriod) ** -numberOfPeriods)


    def annuity_payment_future_value(self, futureValue, ratePerPeriod, numberOfPeriods):
        """ Calculates 'Annuity Payment Future Value'

            futureValue = (number)
            ratePerPeriod = Percentage (0-1)
            numberOfPeriods = (number)

            The formula is used to calculate the cash flows of an annuity when future value is known. An annuity is
            denoted as a series of periodic payments.
        """
        return (futureValue * ratePerPeriod) / (((1 + ratePerPeriod) ** numberOfPeriods) - 1)


    def annuity_payment_factor(self, ratePerPeriod, numberOfPeriods):
        """ Calculates 'Annuity Payment Factor'

            ratePerPeriod = Percentage (0-1)
            numberOfPeriods = (number)

            The formula is used to simplify calculations for an annuity payment. Specifically for simplifying payment
            calculations when the present value of the annuity is known (in contrast to the future value being known).
        """
        return ratePerPeriod / (1 - ((1 + ratePerPeriod) ** -numberOfPeriods))


    def present_value_of_annuity(self, periodicPayment, ratePerPeriod, numberOfPeriods):
        """ Calculates 'Present Value of Annuity'

            periodicPayment = (number)
            ratePerPeriod = Percentage (0-1)
            numberOfPeriods = (number)

            The formula determines the value of a series of future periodic payments at a given time. The formula
            relies on the concept of time value of money, in that one dollar present day is worth more than that
            same dollar at a future date.
        """
        return periodicPayment * ((1 - ((1 + ratePerPeriod) ** -numberOfPeriods)) / ratePerPeriod)


    def present_value_of_annuity_with_continuous_compounding(self, cashFlow, ratePerPeriod, time):
        """ Calculates 'Present Value of Annuity - Continuous Compounding'

            cashFlow = (number)
            ratePerPeriod = Percentage (0-1)
            time = (number)

            The formula is used to calculate the initial value of a series of periodic payments when the rate is
            continuously compounded.
        """
        return cashFlow * ((1 - math.exp(time * -ratePerPeriod)) / (math.exp(ratePerPeriod) - 1))


    def number_of_periods_for_present_value_of_annuity(self, presentValueOfAnnuity, ratePerPeriod, payment):
        """ Calculates 'Number of Periods for Present Value of Annuity'

            presentValueOfAnnuity = (number)
            ratePerPeriod = Percentage (0-1)
            payment = (number)

            The formula is used to determine the number of periods on an annuity using the present value, periodic
            payment, and periodic rate.
        """
        return math.log((1 - ((presentValueOfAnnuity * ratePerPeriod) / payment)) ** -1) / math.log(1 + ratePerPeriod)


    def present_value_annuity_factor(self, ratePerPeriod, numberOfPeriods):
        """ Calculates 'Present Value Annuity Factor'

            ratePerPeriod = Percentage (0-1)
            numberOfPeriods = (number)

            The formula is used to calculate the present value of future one dollar cash flows.
        """
        return (1 - ((1 + ratePerPeriod) ** -numberOfPeriods)) / ratePerPeriod


    def present_value_of_annuity_due(self, periodicPayment, ratePerPeriod, numberOfPeriods):
        """ Calculates 'Present Value of Annuity Due'

            periodicPayment = (number)
            ratePerPeriod = Percentage (0-1)
            numberOfPeriods = (number)

            The formula is sometimes referred to as an immediate annuity, is used to calculate a series of periodic
            payments, or cash flows, that start immediately.
        """
        return periodicPayment + (periodicPayment * ((1 - ((1 + ratePerPeriod) ** -(numberOfPeriods - 1))) /
            (ratePerPeriod)))


    def future_value_of_annuity_due(self, periodicPayment, ratePerPeriod, numberOfPeriods):
        """ Calculates 'Future Value of Annuity Due'

            periodicPayment = (number)
            ratePerPeriod = Percentage (0-1)
            numberOfPeriods = (number)

            The formula is used to calculate the ending value of a series of payments or cash flows where the first
            payment is received immediately. The first cash flow received immediately is what distinguishes an annuity
            due from an ordinary annuity. An annuity due is sometimes referred to as an immediate annuity.
        """
        return (1 + ratePerPeriod) * (periodicPayment * ((((1 + ratePerPeriod) ** numberOfPeriods) - 1) /
            ratePerPeriod))


    def annuity_due_payment_using_present_value(self, presentValue, ratePerPeriod, numberOfPeriods):
        """ Calculates 'Annuity Due Payment Using Present Value'

            presentValue = (number)
            ratePerPeriod = Percentage (0-1)
            numberOfPeriods = (number)

            The formula is used to calculate each installment of a series of cash flows or payments when the first
            installment is received immediately.
        """
        return presentValue * (ratePerPeriod / (1 - ((1 + ratePerPeriod) ** -numberOfPeriods))) * \
            (1 / (1 + ratePerPeriod))


    def annuity_due_payment_using_future_value(self, futureValue, ratePerPeriod, numberOfPeriods):
        """ Calculates 'Annuity Due Payment Using Future Value'

            futureValue = (number)
            ratePerPeriod = Percentage (0-1)
            numberOfPeriods = (number)

            The formula is used to calculate each equal cash flow or payment of a series of cash flows when the
            future value is known. This formula is specific to annuities where the initial cash flow is received
            immediately.
        """
        return futureValue * (ratePerPeriod / (((1 + ratePerPeriod) ** numberOfPeriods) - 1)) * \
            (1 / (1 + ratePerPeriod))


    def asset_to_sales_ratio(self, totalAssets, salesRevenue):
        """ Calculates 'Asset to Sales Ratio'

            totalAssets = (number)
            salesRevenue = (number)

            Calculated by dividing total assets by sales revenues. The formula can be used to compare how much in
            assets a company has relative to the amount of revenues the company can generate using their assets.
        """
        return totalAssets / salesRevenue


    def asset_turnover_ratio(self, salesRevenue, totalAssets):
        """ Calculates 'Asset Turnover Ratio'

            salesRevenue = (number)
            totalAssets = (number)

            The formula evaluates how well a company is utilizing its assets to produce revenue.
        """
        return salesRevenue / totalAssets


    def average_collection_period(self, receivablesTurnover):
        """ Calculates 'Average Collection Period'

            receivablesTurnover = (number)

            The formula is the number of days in a period divided by the receivables turnover ratio.
        """
        return 365 / receivablesTurnover


    def balloon_loan_payment(self, presentValue, balloonAmount, ratePerPeriod, numberOfPeriods):
        """ Calculates 'Balloon Loan Payment'

            presentValue = (number)
            balloonAmount = (number)
            ratePerPeriod = Percentage (0-1)
            numberOfPeriods = (number)

            The formula is used to calculate the payments on a loan that has a balance remaining after all periodic
            payments are made.
        """
        return (presentValue - (balloonAmount / ((1 + ratePerPeriod) ** numberOfPeriods))) * \
            self.annuity_payment_factor(ratePerPeriod, numberOfPeriods)


    def bid_ask_spread(self, bid, ask):
        """ Calculates 'Bid-Ask Spread'

            bid = (number)
            ask = (number)

            The formula is the difference between the asking price and bit price of a particular investment.
        """
        return ask - bid


    def bond_equivalent_yield(self, faceValue, bondPrice, daysToMaturity):
        """ Calculates 'Bond Equivalent Yield'

            faceValue = (number)
            bondPrice = (number)
            daysToMaturity = (number)

            The formula is used to determine the annual yield on a discount, or zero coupon, bond. When making
            investment decisions, comparing the yield or returns on the investment choices in relative terms is
            important.
        """
        return ((faceValue - bondPrice) / bondPrice) * (365 / daysToMaturity)


    def book_value_per_share(self, totalCommonStockholdersEquity, numberOfCommonShares):
        """ Calculates 'Book Value per Share'

            totalCommonStockholdersEquity = (number)
            numberOfCommonShares = (number)

            The formula is used to calculate the per share value of a company based on its equity available to
            common shareholders. The term "book value" is a company's assets minus its liabilities and is sometimes
            referred to as stockholder's equity, owner's equity, shareholder's equity, or simply equity.
        """
        return totalCommonStockholdersEquity / numberOfCommonShares


    def capital_asset_pricing_model(self, riskFreeRate, beta, returnOnTheMarket):
        """ Calculates 'Capital Asset Pricing Model (CAPM)'

            riskFreeRate = Percentage (0-1)
            beta = (number)
            returnOnTheMarket = Percentage (0-1)

            The formula calculates the expected return on a security based on its level of risk. The formula
            is the risk free rate plus beta times the difference of the return on the market and the risk free rate.
        """
        return riskFreeRate + (beta * (returnOnTheMarket - riskFreeRate))


    def capital_gains_yield(self, initialStockPrice, endingStockPrice):
        """ Calculates 'Capital Gains Yield'

            initialStockPrice = (number)
            endingStockPrice = (number)

            The formula is used to calculate the return on a stock based solely on the appreciation of the stock. The
            formula does not include dividends paid on the stock, which can be found using the dividend yield. The
            capital gains yield and dividend yield is combined to calculate the total stock return.
        """
        return (endingStockPrice - initialStockPrice) / initialStockPrice


    def compound_interest(self, principal, ratePerPeriod, numberOfPeriods):
        """ Calculates 'Compound Interest'

            principal = (number)
            ratePerPeriod = Percentage (0-1)
            numberOfPeriods = (number)

            The formula calculates the amount of interest earned on an account or investment where the amount earned
            is reinvested.
        """
        return principal * (((1 + ratePerPeriod) ** numberOfPeriods) - 1)


    def continuous_compounding(self, principal, rate, time):
        """ Calculates 'Continuous Compounding'

            principal = (number)
            rate = Percentage (0-1)
            time = (number)

            The formula is used to determine the interest earned on an account that is constantly compounded,
            essentially leading to an infinite amount of compounding periods.
        """
        return principal * math.exp(rate * time)


    def contribution_margin(self, pricePerProduct, variableCostPerProduct):
        """ Calculates 'Contribution Margin'

            pricePerProduct = (number)
            variableCostPerProduct = (number)

            The formula is the sales price of a product minus its variable costs. In other words, calculating the
            contribution margin determines the sales amount left over after adjusting for the variable costs of
            selling additional products.
        """
        return pricePerProduct - variableCostPerProduct


    def current_ratio(self, currentAssets, currentLiabilities):
        """ Calculates 'Current Ratio'

            currentAssets = (number)
            currentLiabilities = (number)

            The formula provides a calculable means to determining a company's liquidity in the short term. The terms
            of the equation Current Assets and Current Liabilities references the assets that can be realized or the
            liabilities that are payable in less than a year.
        """
        return currentAssets / currentLiabilities


    def current_yield(self, annualCoupons, currentBondPrice):
        """ Calculates 'Current Yield'

            annualCoupons = (number)
            currentBondPrice = (number)

            The formula is a bond's annual return based on its annual coupon payments and current price (as opposed
            to its original price or face). The formula for current yield is a bond's annual coupons divided by its
            current price.
        """
        return annualCoupons / currentBondPrice


    def days_in_inventory(self, inventoryTurnover):
        """ Calculates 'Days in Inventory'

            inventoryTurnover = (number)

            The formula to calculate days in inventory is the number of days in the period divided by the inventory
            turnover ratio. This formula is used to determine how quickly a company is converting their inventory
            into sales.
        """
        return 365 / inventoryTurnover


    def debt_coverage_ratio(self, netOperatingIncome, debtService):
        """ Calculates 'Debt Coverage Ratio'

            netOperatingIncome = (number)
            debtService = (number)

            The formula is net operating income divided by debt service. The debt coverage ratio is used in banking
            to determine a companies ability to generate enough income in its operatings to cover the expense of a
            debt.
        """
        return netOperatingIncome / debtService


    def debt_ratio(self, totalLiabilities, totalAssets):
        """ Calculates 'Debt Ratio'

            totalLiabilities = (number)
            totalAssets = (number)

            The formula is total liabilities divided by total assets. The formula is used in corporate finance and
            should not be confused with the debt to income ratio, sometimes shortened to debt ratio, used in
            consumer lending.
        """
        return totalLiabilities / totalAssets


    def debt_to_equity_ratio(self, totalLiabilities, totalEquity):
        """ Calculates 'Debt to Equity Ratio (D/E)'

            totalLiabilities = (number)
            totalEquity = (number)

            The formula is total liabilities divided by total equity. The debt to equity ratio is a financial leverage
            ratio. Financial leverage ratios are used to measure a company's ability to handle its long term and short
            term obligations.
        """
        return totalLiabilities / totalEquity


    def debt_to_income_ratio(self, monthlyDebtPayments, grossMonthlyIncome):
        """ Calculates 'Debt to Income Ratio'

            monthlyDebtPayments = (number)
            grossMonthlyIncome = (number)

            The formula is the applicant's montly debt payments divided by his or her gross monthly income.
        """
        return monthlyDebtPayments / grossMonthlyIncome


    def diluted_earnings_per_share(self, netIncome, averageShares, otherConvertibleInstruments):
        """ Calculates 'Diluted Earnings per Share (Diluted EPS)'

            netIncome = (number)
            averageShares = (number)
            otherConvertibleInstruments = (number)

            The formula is a firm's net income divided by the sum of it's average shares and other convertible
            instruments.
        """
        return netIncome / (averageShares + otherConvertibleInstruments)


    def discounted_payback_period(self, initialInvestment, rate, periodicCashFlow):
        """ Calculates 'Discounted Payback Period (DPP)'

            initialInvestment = (number)
            rate = Percentage (0-1)
            periodicCashFlow = (number)

            The formula is used to calculate the length of time to recoup an investment based on the investment's
            discounted cash flows. By discounting each individual cash flow, the discounted payback period formula
            takes into consideration the time value of money.
        """
        return math.log(1 / (1 - ((initialInvestment * rate) / periodicCashFlow))) / math.log(1 + rate)


    def dividend_payout_ratio(self, dividends, netIncome):
        """ Calculates 'Dividend Payout Ratio'

            dividends = (number)
            netIncome = (number)

            The formula is the amount of dividends paid to stockholders relative to the amount of total net income of
            a company. The amount that is not paid out in dividends to stockholders is held by the company for growth.
            The amount that is kept by the company is called retained earnings.
        """
        return dividends / netIncome


    def dividend_yield(self, dividendsForThePeriod, initialPriceForThePeriod):
        """ Calculates 'Dividend Yield (Stock)'

            dividendsForThePeriod = (number)
            initialPriceForThePeriod = (number)

            The formula is used to calculate the percentage return on a stock based solely on dividends. The total
            return on a stock is the combination of dividends and appreciation of a stock.
        """
        return dividendsForThePeriod / initialPriceForThePeriod


    def dividends_per_share(self, dividends, numberOfShares):
        """ Calculates 'Dividends Per Share (DPS)'

            dividends = (number)
            numberOfShares = (number)

            The formula is the annual dividends paid divided by the number of shares outstanding.
        """
        return dividends / numberOfShares


    def doubling_time(self, rateOfReturn):
        """ Calculates 'Doubling Time'

            rateOfReturn = Percentage (0-1)

            The formula is used in finance to calculate the length of time required to double an investment or money
            in an interest bearing account.
        """
        return math.log(2) / math.log(1 + rateOfReturn)


    def doubling_time_with_continuous_compounding(self, rateOfReturn):
        """ Calculates 'Doubling Time - Continuous Compounding'

            rateOfReturn = Percentage (0-1)

            The formula with continuous compounding is the natural log of 2 divided by the rate of return.
        """
        return math.log(2) / rateOfReturn


    def doubling_time_for_simple_interest(self, rateOfReturn):
        """ Calculates 'Doubling Time - Simple Interest'

            rateOfReturn = Percentage (0-1)

            The formula is simply 1 divided bt the periodic rate. The formula is used to calculate how long it would
            take to double the balance on an interesting bearing account that has simple interest.
        """
        return 1 / rateOfReturn


    def earnings_per_share(self, netIncome, weightedAverageOutstandingShares):
        """ Calculates 'Earnings Per Share (EPS)'

            netIncome = (number)
            weightedAverageOutstandingShares = (number)

            The formula is a company's net income expressed on a per share basis. Net income for a particular company
            can be found on its income statement. It is important to note that the earnings per share formula only
            references common stock and any preferred stock dividends is subtracted from the net income, if applicable.
        """
        return netIncome / weightedAverageOutstandingShares


    def equity_multiplier(self, totalAssets, stockholdersEquity):
        """ Calculates 'Equity Multiplier'

            totalAssets = (number)
            stockholdersEquity = (number)

            The formula is total assets divided by stockholder's equity. Equity multiplier is a financial leverage
            ratio that evaluates a company's use of debt to purchage assets.
        """
        return totalAssets / stockholdersEquity


    def equivalent_annual_annuity(self, netPresentValue, ratePerPeriod, numberOfPeriods):
        """ Calculates 'Equivalent Annual Annuity'

            netPresentValue = (number)
            ratePerPeriod = Percentage (0-1)
            numberOfPeriods = (number)

            The formula is used in capital budgeting to show the net present value of an investment as a series of
            equal cash flows for the length of the investment.
        """
        return (netPresentValue * ratePerPeriod) / (1 - ((1 + ratePerPeriod) ** -numberOfPeriods))


    def estimated_earnings(self, forecastedSales, forecastedExpenses):
        """ Calculates 'Estimated Earnings'

            forecastedSales = (number)
            forecastedExpenses = (number)

            The formula is forecasted sales minus forecasted expenses. The formula is a simple way of restating how
            to calculate net income, i.e. earnings, based on its estimated components. However, the practice of
            calculating estimated earnings is far more complex.
        """
        return forecastedSales - forecastedExpenses


    def free_cash_flow_to_equity(self, netIncome, depreciationAndAmortization, capitalExpenditure,
            changeInWorkingCapital, netBorrowing):
        """ Calculates 'Free Cash Flow to Equity (FCFE)'

            netIncome = (number)
            depreciationAndAmortization = (number)
            capitalExpenditure = (number)
            changeInWorkingCapital = (number)
            netBorrowing = (number)

            The formula is net income minus capital expenditures minus change in working capital plus net borrowing.
        """
        return netIncome + depreciationAndAmortization - changeInWorkingCapital - capitalExpenditure + netBorrowing


    def free_cash_flow_to_firm(self, ebit, taxRate, depreciationAndAmortization, capitalExpenditure,
            changeInWorkingCapital):
        """ Calculates 'Free Cash Flow to Firm (FCFF)'

            ebit = (number)
            taxRate = Percentage (0-1)
            depreciationAndAmortization = (number)
            capitalExpenditure = (number)
            changeInWorkingCapital = (number)

            The fomula is capital expenditures and change in working capital subtracted from the product of
            earnings before interest and taxes (EBIT) and one minus the tax rate (1-t).
        """
        return ebit * (1 - taxRate) + depreciationAndAmortization - capitalExpenditure - changeInWorkingCapital


    def future_value(self, initialCashFlow, rateOfReturn, numberOfPeriods):
        """ Calculates 'Future Value'

            initialCashFlow = (number)
            rateOfReturn = Percentage (0-1)
            numberOfPeriods = (number)

            The formula is used in finance to calculate the value of a value of a cash flow at a later date than
            originally received. This idea that an amount today is worth a different amount than at a future time
            is based on the time value of money.
        """
        return initialCashFlow * ((1 + rateOfReturn) ** numberOfPeriods)


    def future_value_with_continuous_compounding(self, presentValue, rate, time):
        """ Calculates 'Future Value - Continuous Compounding'

            presentValue = (number)
            rate = Percentage (0-1)
            time = (number)

            The formula is used in calculating the later value of a current sum of money.
        """
        return presentValue * math.exp(rate * time)


    def future_value_factor(self, ratePerPeriod, numberOfPeriods):
        """ Calculates 'Future Value Factor'

            ratePerPeriod = Percentage (0-1)
            numberOfPeriods = (number)

            The formula is used to calculate the future value of an amount per dollar of its present value. The future
            value factor is generally found on a table which is used to simplify calculations for amounts greater than
            one dollar.
        """
        return (1 + ratePerPeriod) ** numberOfPeriods


    def geometric_mean_return(self, ratesOfReturn):
        """ Calculates 'Geometric Mean Return'

            ratesOfReturn = (list)

            The formula is used to calculate the average rate per period on an investment that is compounded over
            multiple periods. The geometric mean return may also be referred to as the geometric average return.
        """
        root = 1
        for rateOfReturn in ratesOfReturn:
            root *= (1 + rateOfReturn)

        if len(ratesOfReturn) > 0:
            return (root ** (1 / len(ratesOfReturn))) - 1
        return 0


    def gross_profit_margin(self, salesRevenue, costOfGoodsSold):
        """ Calculates 'Gross Profit Margin'

            salesRevenue = (number)
            costOfGoodsSold = (number)

            The formula is a profitability ratio that is found by dividing a company's gross profit by its revenues.
            Gross profit is a company's revenues minus the COGS, Cost of Goods Sold. The cost of goods sold, or cost
            of sales, and sales revenues are both found on a company's income statement.
        """
        return (salesRevenue - costOfGoodsSold) / salesRevenue


    def future_value_of_growing_annuity(self, firstPayment, ratePerPeriod, growthRate, numberOfPeriods):
        """ Calculates 'Future Value of Growing Annuity'

            firstPayment = (number)
            ratePerPeriod = Percentage (0-1)
            growthRate = Percentage (0-1)
            numberOfPeriods = (number)

            The formula is used to calculate the future amount of a series of cash flows, or payments, that grow
            at a proportionate rate. A growing annuity may sometimes be referred to as an increasing annuity.
        """
        return firstPayment * ((((1 + ratePerPeriod) ** numberOfPeriods) - ((1 + growthRate) ** numberOfPeriods)) /
                (ratePerPeriod - growthRate))


    def growing_annuity_payment_from_present_value(self, presentValue, ratePerPeriod, growthRate,
            numberOfPeriods):
        """ Calculates 'Growing Annuity Payment - Present Value'

            presentValue = (number)
            ratePerPeriod = Percentage (0-1)
            growthRate = Percentage (0-1)
            numberOfPeriods = (number)

            The formula is used to calculate the initial payment of a series of periodic payments that grow at a
            proportionate rate. This formula is used specifically when present value is known.
        """
        return presentValue * ((ratePerPeriod - growthRate) / (1 - (((1 + growthRate) /
            (1 + ratePerPeriod)) ** numberOfPeriods)))


    def growing_annuity_payment_from_future_value(self, futureValue, ratePerPeriod, growthRate,
            numberOfPeriods):
        """ Calculates 'Growing Annuity Payment - Future Value'

            futureValue = (number)
            ratePerPeriod = Percentage (0-1)
            growthRate = Percentage (0-1)
            numberOfPeriods = (number)

            The formula is used to calculate the first cash flow or payment of a series of cash flows that grow at
            a proportionate rate. A growing annuity may sometimes be referred to as an increasing annuity.
        """
        return futureValue * ((ratePerPeriod - growthRate) / (((1 + ratePerPeriod) ** numberOfPeriods) - \
                ((1 + growthRate) ** numberOfPeriods)))


    def present_value_of_a_growing_annuity(self, firstPayment, ratePerPeriod, growthRate, numberOfPeriods):
        """ Calculates 'Present Value of a Growing Annuity'

            firstPayment = (number)
            ratePerPeriod = Percentage (0-1)
            growthRate = Percentage (0-1)
            numberOfPeriods = (number)

            The formula calculates the present day value of a series of future periodic payments that grow at a
            proportionate rate. A growing annuity may sometimes be referred to as an increasing annuity.
        """
        return (firstPayment / (ratePerPeriod - growthRate)) * (1 - (((1 + growthRate) /
            (1 + ratePerPeriod)) ** numberOfPeriods))


    def present_value_of_growing_perpetuity(self, dividendOrCouponAtFirstPeriod, discountRate, growthRate):
        """ Calculates 'Present Value of Growing Perpetuity'

            dividendOrCouponAtFirstPeriod = (number)
            discountRate = Percentage (0-1)
            growthRate = Percentage (0-1)

            The formula is the cash flow after the first period divided by the difference between the discount rate
            and the growth rate.
        """
        return dividendOrCouponAtFirstPeriod / (discountRate - growthRate)


    def holding_period_return(self, percentagePeriodReturns):
        """ Calculates 'Holding Period Return'

            percentagePeriodReturns = (list)

            The formula is used for calculating the return on an investment over multiple periods.
        """
        base = 1
        for periodReturn in percentagePeriodReturns:
            base *= (1 + periodReturn)

        if len(percentagePeriodReturns) > 0:
            return base - 1
        return 0


    def interest_coverage_ratio(self, ebit, interestExpense):
        """ Calculates 'Interest Coverage Ratio'

            ebit = (number)
            interestExpense = (number)

            The formula is used to measure a company's earnings relative to the amount of interest that it pays.
            The interest coverage ratio is considered to be a financial leverage ratio in that it analyzes one
            aspect of a company's financial viability regarding its debt.
        """
        return ebit / interestExpense


    def inventory_turnover_ratio(self, sales, inventory):
        """ Calculates 'Inventory Turnover Ratio'

            sales = (number)
            inventory = (number)

            The formula measures how well a company is turning their inventory into sales. The costs associated with
            retaining excess inventory and not producing sales can be burdensome. If the inventory turnover ratio is
            too low, a company may look at their inventory to appropriate cost cutting.
        """
        return sales / inventory


    def interest_rate_parity(self, interestRateForCurrencyY, forwardExchangeRateXY, spotExchangeRateXY):
        """ Calculates 'Interest Rate Parity'

            interestRateForCurrencyY = Percentage (0-1)
            forwardExchangeRateXY = (number)
            spotExchangeRateXY = (number)

            The formula is used to illustrate equilibrium based on the interest rate parity theory. The theory of
            interest rate parity argues that the difference in interest rates between two countries should be aligned
            with that of their forward and spot exchange rates.
        """
        return (forwardExchangeRateXY / spotExchangeRateXY) * (1 + interestRateForCurrencyY) - 1


    def balloon_balance_of_a_loan(self, presentValue, payment, ratePerPayment, numberOfPayments):
        """ Calculates 'Balloon Balance of a Loan'

            presentValue = (number)
            payment = (number)
            ratePerPayment = Percentage (0-1)
            numberOfPayments = (number)

            The formula is used to calculate the amount due at the end of a balloon loan.
        """
        return (presentValue * ((1 + ratePerPayment) ** numberOfPayments)) - \
                (payment * ((((1 + ratePerPayment) ** numberOfPayments) - 1) / ratePerPayment))


    def loan_payment(self, presentValue, ratePerPeriod, numberOfPeriods):
        """ Calculates 'Loan Payment'

            presentValue = (number)
            ratePerPeriod = Percentage (0-1)
            numberOfPeriods = (number)

            The formula is used to calculate the payments on a loan. The formula used to calculate loan payments
            is exactly the same as the formula used to calculate payments on an ordinary annuity. A loan, by
            definition, is an annuity, in that it consists of a series of future periodic payments.
        """
        return (ratePerPeriod * presentValue) / (1 - ((1 + ratePerPeriod) ** -numberOfPeriods))


    def remaining_balance_on_loan(self, presentValue, payment, ratePerPayment, numberOfPayments):
        """ Calculates 'Remaining Balance on Loan'

            presentValue = (number)
            payment = (number)
            ratePerPayment = Percentage (0-1)
            numberOfPayments = (number)

            The formula can be used to calculate the remining balance at a given time (time n), whether at a future
            date or at present. The formula is only used for a loan that is amortized, meaning that the portion of
            interest and principal applied to each payment is predetermined.
        """
        return (presentValue * ((1 + ratePerPayment) ** numberOfPayments)) - (payment * ((((1 + ratePerPayment) ** \
                numberOfPayments) - 1) / ratePerPayment))


    def loan_to_deposit_ratio(self, loans, deposits):
        """ Calculates 'Loan to Deposit Ratio'

            loans = (number)
            deposits = (number)

            The formula is exactly as its name implies, loans divided by deposits.
        """
        return loans / deposits


    def loan_to_value_ratio(self, loanAmount, valueOfCollateral):
        """ Calculates 'Loan to Value Ratio (LTV Ratio)'

            loanAmount = (number)
            valueOfCollateral = (number)

            The formula is the loan amount divided by the value of the collateral used for the loan.
        """
        return loanAmount / valueOfCollateral


    def net_asset_value(self, fundAssets, fundLiabilities, outstandingShares):
        """ Calculates 'Net Asset Value (NAV)'

            fundAssets = (number)
            fundLiabilities = (number)
            outstandingShares = (number)

            The formula is used to calculate a mutual fund's value per share. A mutual fund is a pool of investments
            that are divided into shares to be purchased by investors.
        """
        return (fundAssets - fundLiabilities) / outstandingShares


    def net_interest_income(self, interestIncome, interestExpense):
        """ Calculates 'Net Interest Income (NII)'

            interestIncome = (number)
            interestExpense = (number)

            The formula is used to calculate the amount of interest income that is left after covering interest
            expenses. The total interest income, total interest expense, and net interest income can be found on
            a bank's income statement.
        """
        return interestIncome - interestExpense


    def net_interest_margin(self, netInterestIncome, averageEarningAssets):
        """ Calculates 'Net Interest Margin'

            netInterestIncome = (number)
            averageEarningAssets = (number)

            The formula is used to evaluate how well a bank is using it's earning assets to produce a (net)
            interest income.
        """
        return netInterestIncome / averageEarningAssets


    def net_interest_spread(self, interestIncomeRate, interestExpenseRate):
        """ Calculates 'Net Interest Spread'

            interestIncomeRate = (number)
            interestExpenseRate = (number)

            The formula is used to determine the difference between the rate a bank is earning versus the rate a bank
            is incurring.
        """
        return interestIncomeRate - interestExpenseRate


    def net_present_value(self, initialInvestment, cashFlows, discountRate):
        """ Calculates 'Net Present Value'

            initialInvestment = (number)
            cashFlows = (list)
            discountRate = Percentage (0-1)

            The formula is used to determine the present value of an investment by the discounted sum of all cash
            flows received from the project.
        """
        sum = 0
        for count, cashFlowAtPeriod in enumerate(cashFlows):
            sum += cashFlowAtPeriod / ((1 + discountRate) ** (count + 1))

        return -initialInvestment + sum


    def net_profit_margin(self, netIncome, salesRevenue):
        """ Calculates 'Net Profit Margin'

            netIncome = (number)
            salesRevenue = (number)

            The formula looks at how much of a company's revenues are kept as net income. The net profit margin is
            generally expressed as a percentage. Both net income and revenues can be found on a company's income
            statement.
        """
        return netIncome / salesRevenue


    def net_working_capital(self, currentAssets, currentLiabilities):
        """ Calculates 'Net Working Capital'

            currentAssets = (number)
            currentLiabilities = (number)

            The formula is sometimes referred to as simply working capital, is used to determine the availability
            of a company's liquid assets by subtracting its current liabilities.
        """
        return currentAssets - currentLiabilities


    def number_of_periods_for_present_value_to_reach_future_value(self, futureValue, presentValue, ratePerPeriod):
        """ Calculates 'Number of Periods for Present Value to reach Future Value'

            futureValue = (number)
            presentValue = (number)
            ratePerPeriod = Percentage (0-1)

            The formula is used to calculate the length of time required for a single cash flow (present value) to
            reach a certain amount (future value) based on the time value of money.
        """
        return math.log(futureValue / presentValue) / math.log(1 + ratePerPeriod)


    def operating_margin(self, operatingIncome, salesRevenue):
        """ Calculates 'Operating Margin'

            operatingIncome = (number)
            salesRevenue = (number)

            The formula is one of the multiple profitability ratioes used by investors and companies to determine how
            well the company is earning relative to its revenues.
        """
        return operatingIncome / salesRevenue


    def payback_period(self, initialInvestment, periodicCashFlow):
        """ Calculates 'Payback Period'

            initialInvestment = (number)
            periodicCashFlow = (number)

            The formula is used to determine the length of time it will take to recoup the initial amount invested
            on a project or investment. The payback period formula is used for quick calculations and is generally
            not considered an end-all for evaluating whether to invest in a particular situation.
        """
        return initialInvestment / periodicCashFlow


    def present_value_of_perpetuity(self, dividendOrCouponPerPeriod, discountRate):
        """ Calculates 'Present Value of Perpetuity'

            dividendOrCouponPerPeriod = (number)
            discountRate = Percentage (0-1)

            A perpetuity is a type of annuity that receives an infinite amount of periodic payments. An annuity is a
            financial instrument that pays consistent periodic payments. As with any annuity, the perpetuity value
            formula sums the present value of future cash flows.
        """
        return dividendOrCouponPerPeriod / discountRate


    def perpetuity_payment(self, presentValue, rate):
        """ Calculates 'Perpetuity Payment'

            presentValue = (number)
            rate = Percentage (0-1)

            The formula for the payment on a perpetuity is its present value times its rate. A perpetuity is a type
            of annuity where the payments continue on infinitely.
        """
        return presentValue * rate


    def perpetuity_yield(self, payment, presentValue):
        """ Calculates 'Perpetuity Yield'

            payment = (number)
            presentValue = (number)

            The formula that is used to calculate the yield on a perpetuity is the payment divided by the present
            value of the perpetuity. A perpetuity is a form of annuity that has an infinite amount of periodic
            payments.
        """
        return payment / presentValue


    def preferred_stock_value(self, dividend, discountRate):
        """ Calculates 'Preferred Stock'

            dividend = (number)
            discountRate = Percentage (0-1)

            The formula is for a simple straight preferred stock that does not have additional features, such as
            those found in convertible, retractable, and callable preferred stocks. A preferred stock is a type of
            stock that provides dividends prior to any dividend paid to common stocks.
        """
        return dividend / discountRate


    def present_value(self, cashFlowAtFirstPeriod, rateOfReturn, numberOfPeriods):
        """ Calculates 'Present Value'

            cashFlowAtFirstPeriod = (number)
            rateOfReturn = Percentage (0-1)
            numberOfPeriods = (number)

            The formula is used in Finance that calculates the present day value of an amount that is received at
            a future date. The premise of the equation is that there is "time value of money".
        """
        return cashFlowAtFirstPeriod / ((1 + rateOfReturn) ** numberOfPeriods)


    def present_value_factor(self, rateOfReturn, numberOfPeriods):
        """ Calculates 'Present Value Factor'

            rateOfReturn = Percentage (0-1)
            numberOfPeriods = (number)

            The formula is used to calculate the present value per dollar that is received in the future.
        """
        return 1 / ((1 + rateOfReturn) ** numberOfPeriods)


    def present_value_with_continuous_compounding(self, cashFlow, rate, time):
        """ Calculates 'Present Value - Continuous Compounding'

            cashFlow = (number)
            rate = Percentage (0-1)
            time = (number)

            The formula is used to calculate the current value of a future amount that has earned at a continuously
            compounded rate.
        """
        return cashFlow / math.exp(rate * time)


    def present_value_with_continuous_compounding_factor(self, rate, time):
        """ Calculates 'Present Value - Continuous Compounding Factor'

            rate = Percentage (0-1)
            time = (number)

            The formula is used to calculate the present value of $1 received at a future date, discounted on a
            constant compounding basis.
        """
        return 1 / math.exp(rate * time)


    def price_to_book_value_ratio(self, marketPricePerShare, bookValuePerShare):
        """ Calculates 'Price to Book Value Ratio'

            marketPricePerShare = (number)
            bookValuePerShare = (number)

            The formula, sometimes referred to as the market to book ratio, is used to compare a company's net
            assets available to common shareholders relative to the sale price of its stock. The formula for price
            to book value is the stock price per share divided by the book value per share.
        """
        return marketPricePerShare / bookValuePerShare


    def price_to_cash_flows_ratio(self, marketCapitalization, cashFlowsFromOperations):
        """ Calculates 'Price to Cash Flows Ratio (P/CF Ratio)'

            marketCapitalization = (number)
            cashFlowsFromOperations = (number)

            The formula is a company's market capitalization divided by its cash flows from operations.
        """
        return marketCapitalization / cashFlowsFromOperations


    def price_to_dividend_ratio(self, pricePerShare, dividendsPerShare):
        """ Calculates 'Price to Dividend Ratio'

            pricePerShare = (number)
            dividendsPerShare = (number)

            The price to dividend ratio is calculated by dividing the price per share by the dividends paid per share.
        """
        return pricePerShare / dividendsPerShare


    def price_to_earnings_ratio(self, pricePerShare, earningsPerShare):
        """ Calculates 'Price to Earnings Ratio (P/E Ratio)'

            pricePerShare = (number)
            earningsPerShare = (number)

            The formula is the price per share divided by earnings per share. The price to earnings ratio is used
            as a quick calculation for how a company's stock is perceived by the market to be worth relative to
            the company's earnings.
        """
        return pricePerShare / earningsPerShare


    def price_to_sales_ratio(self, sharePrice, salesPerShare):
        """ Calculates 'Price to Sales Ratio (P/S Ratio)'

            sharePrice = (number)
            salesPerShare = (number)

            The formula is the perceived value of a stock by the market compared to the revenues of the company.
            The price to sales ratio is calculated by dividing the stock price by sales per share.
        """
        return sharePrice / salesPerShare


    def profitability_index(self, presentValueOfFutureCashFlows, initialInvestment):
        """ Calculates 'Profitability Index'

            presentValueOfFutureCashFlows = (number)
            initialInvestment = (number)

            The formula is used calculate the profitability of a project based on its future discounted returns
            relative to the initial investment. The PV of future cash flows does not include the initial investment.
            It only includes the inflows or future returns.
        """
        return presentValueOfFutureCashFlows / initialInvestment


    def quick_ratio(self, quickAssets, currentLiabilities):
        """ Calculates 'Quick Ratio'

            quickAssets = (number)
            currentLiabilities = (number)

            The formula is used for determining a company's ability to cover its short term debt with assets that
            can readily be transferred into cash, or quick assets. The Current Liabilities portion references
            liabilities that are payable within one year.
        """
        return quickAssets / currentLiabilities


    def rate_of_inflation(self, initialConsumerPriceIndex, endingConsumerPriceIndex):
        """ Calculates 'Rate of Inflation'

            initialConsumerPriceIndex = (number)
            endingConsumerPriceIndex = (number)

            The formula measures the percentage change in purchasing power of a particular currency. As the cost
            of prices increase, the purchasing power of the currency decreases.
        """
        return (endingConsumerPriceIndex - initialConsumerPriceIndex) / initialConsumerPriceIndex


    def real_rate_of_return(self, nominalRate, inflationRate):
        """ Calculates 'Real Rate of Return'

            nominalRate = Percentage (0-1)
            inflationRate = Percentage (0-1)

            The formula is the sum of one plus the nominal rate divided by the sum of one plus the inflation rate
            which then is subtracted by one. The formula for the real rate of return can be used to determine the
            effective return on an investment after adjusting for inflation.
        """
        return ((1 + nominalRate) / (1 + inflationRate)) - 1


    def receivables_turnover_ratio(self, salesRevenue, averageAccountsReceivable):
        """ Calculates 'Receivables Turnover Ratio'

            salesRevenue = (number)
            averageAccountsReceivable = (number)

            The formula, sometimes referred to as accounts receivable turnover, is sales divided by the average of
            accounts receivables.
        """
        return salesRevenue / averageAccountsReceivable


    def retention_ratio(self, netIncome, dividends):
        """ Calculates 'Retention Ratio'

            netIncome = (number)
            dividends = (number)

            The formula, sometimes referred to as the plowback ratio, is the amount of retained earnings relative to
            earnings. Earnings can be referred to as net income and is found on the income statement.
        """
        return (netIncome - dividends) / netIncome


    def return_on_assets(self, netIncome, averageTotalAssets):
        """ Calculates 'Return on Assets (ROA)'

            netIncome = (number)
            averageTotalAssets = (number)

            The formula is a company's net income divided by its average of total assets. The return on assets
            formula looks at the ability of a company to utilize its assets to gain a net profit.
        """
        return netIncome / averageTotalAssets


    def return_on_equity(self, netIncome, averageStockholdersEquity):
        """ Calculates 'Return on Equity (ROE)'

            netIncome = (number)
            averageStockholdersEquity = (number)

            The formula is a company's net income divided by its average stockholder's equity. The numerator of
            the return on equity formula, net income, can be found on a company's income statement.
        """
        return netIncome / averageStockholdersEquity


    def return_on_investment(self, earnings, initialInvestment):
        """ Calculates 'Return on Investment (ROI)'

            earnings = (number)
            initialInvestment = (number)

            The formula measures the percentage return on a particular investment. ROI is used to measure
            profitability for a given amount of time.
        """
        return (earnings - initialInvestment) / initialInvestment


    def risk_premium(self, assetOrInvestmentReturn, riskFreeReturn):
        """ Calculates 'Risk Premium'

            assetOrInvestmentReturn = (number)
            riskFreeReturn = (number)

            The formula, sometimes referred to as default risk premium, is the return on an investment minus the
            return that would be earned on a risk free investment. The risk premium is the amount that an investor
            would like to earn for the risk involved with a particular investment.
        """
        return assetOrInvestmentReturn - riskFreeReturn


    def rule_of_72(self, rate):
        """ Calculates 'Rule of 72'

            rate = Percentage (0-1)

            The formula is used to estimate the length of time required to double an investment. The rule of 72
            is primarily used in off the cuff situations where an individual needs to make a quick calculation
            instead of working out the exact time it takes to double an investment.
        """
        return 72 / (rate * 100)


    def simple_interest(self, principal, rate, time):
        """ Calculates 'Simple Interest'

            principal = (number)
            rate = Percentage (0-1)
            time = (number)

            The formula is used to calculate the interest accrued on a loan or savings account that has simple
            interest.
        """
        return principal * rate * time


    def present_value_of_stock_with_constant_growth(self, estimatedDividendsForNextPeriod,
            requiredRateOfReturn, growthRate):
        """ Calculates 'Present Value of Stock - Constant Growth'

            estimatedDividendsForNextPeriod = (number)
            requiredRateOfReturn = Percentage (0-1)
            growthRate = Percentage (0-1)

            The formula is the estimated dividends to be paid divided by the difference between the required rate of
            return and the growth rate.
        """
        return estimatedDividendsForNextPeriod / (requiredRateOfReturn - growthRate)


    def present_value_of_stock_with_zero_growth(self, dividendsPerPeriod, requiredRateOfReturn):
        """ Calculates 'Present Value of Stock - Zero Growth'

            dividendsPerPeriod = (number)
            requiredRateOfReturn = Percentage (0-1)

            The formula is dividends per period divided by the required return per period.
        """
        return dividendsPerPeriod / requiredRateOfReturn


    def tax_equivalent_yield(self, taxFreeYield, taxRate):
        """ Calculates 'Tax Equivalent Yield'

            taxFreeYield = Percentage (0-1)
            taxRate = Percentage (0-1)

            The formula is used to compare the yield between a tax-free investment and an investment that is taxed.
        """
        return taxFreeYield / (1 - taxRate)


    def total_stock_return(self, initialStockPrice, endingStockPrice, dividends):
        """ Calculates 'Total Stock Return'

            initialStockPrice = (number)
            endingStockPrice = (number)
            dividends = (number)

            The formula is the appreciation in the price plus any dividends paid, divided by the original price
            of the stock.
        """
        return ((endingStockPrice - initialStockPrice) + dividends) / initialStockPrice


    def weighted_average(self, weights, values):
        """ Calculates 'Weighted Average'

            weights = (list)
            values = (list)

            The formula is used to calculate the average value of a particular set of numbers with different levels
            of relevance. The relevance of each number is called its weight. The weights should be represented as
            a percentage of the total relevancy. Therefore, all weights should be equal to 100%, or 1.
        """
        return sum([values[i]*weights[i] for i in range(len(values))]) / sum(weights)


    def yield_to_maturity(self, couponOrInterestPayment, faceValue, price, yearsToMaturity):
        """ Calculates 'Yield to Maturity (Approx YTM)'

            couponOrInterestPayment = (number)
            faceValue = (number)
            price = (number)
            yearsToMaturity = (number)

            The formula is used to calculate the yield on a bond based on its current price on the market. The
            formula looks at the effective yield of a bond based on compounding as opposed to the simple yield
            which is found using the dividend yield formula.
        """
        return (couponOrInterestPayment + ((faceValue - price) / yearsToMaturity)) / ((faceValue + price) / (2))


    def zero_coupon_bond_value(self, faceValue, rateOrYield, timeToMaturity):
        """ Calculates 'Zero Coupon Bond Value'

            faceValue = (number)
            rateOrYield = Percentage (0-1)
            timeToMaturity = (number)

            The formula, sometimes referred to as a pure discount bond or simply discount bond, is a bond that does
            not pay coupon payments and instead pays one lump sum at maturity. The amount paid at maturity is called
            the face value. The term discount bond is used to reference how it is sold originally at a discount from
            its face value instead of standard pricing with periodic dividend payments as seen otherwise.
        """
        return faceValue / ((1 + rateOrYield) ** timeToMaturity)


    def zero_coupon_bond_effective_yield(self, faceValue, presentValue, numberOfPeriods):
        """ Calculates 'Zero Coupon Bond Effective Yield'

            faceValue = (number)
            presentValue = (number)
            numberOfPeriods = (number)

            The formula is used to calculate the periodic return for a zero coupon bond, or sometimes referred
            to as a discount bond.
        """
        return ((faceValue / presentValue) ** (1 / numberOfPeriods)) - 1
