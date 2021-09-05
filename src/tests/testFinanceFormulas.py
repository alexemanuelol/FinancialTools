import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + "/formulas/")

import financeFormulas

if __name__ == "__main__":
    print("Testing Finance Formulas...")

    obj = financeFormulas.FinanceFormulas()
    assert round(obj.annual_percentage_yield(.06, 12), 5) == .06168
    assert round(obj.break_even_point(100, 20, 10), 2) == 10.0
    assert round(obj.cost_of_goods_sold(100, 200, 150), 2) == 150.0
    assert round(obj.future_value_of_annuity(1000, .02, 5), 2) == 5204.04
    assert round(obj.future_value_of_annuity_with_continuous_compounding(1000, .005, 12), 2) == 12336.42
    assert round(obj.number_of_periods_for_future_value_of_annuity(19600, .05, 1000), 0) == 14.0
    assert round(obj.annuity_payment_present_value(150, .05, 8), 2) == 23.21
    assert round(obj.annuity_payment_future_value(5000, .03, 5), 2) == 941.77
    assert round(obj.annuity_payment_factor(.07, 5), 5) == .24389
    assert round(obj.present_value_of_annuity(1500, .05, 10), 2) == 11582.60
    assert round(obj.present_value_of_annuity_with_continuous_compounding(100, .005, 36), 2) == 3286.37
    assert round(obj.number_of_periods_for_present_value_of_annuity(19660, .01, 1000), 0) == 22.0
    assert round(obj.present_value_annuity_factor(.05, 5), 4) == 4.3295
    assert round(obj.present_value_of_annuity_due(100, .08, 10), 2) == 724.69
    assert round(obj.future_value_of_annuity_due(1000, .03, 5), 2) == 5468.41
    assert round(obj.annuity_due_payment_using_present_value(5000, .03, 5), 2) == 1059.97
    assert round(obj.annuity_due_payment_using_future_value(5000, .03, 5), 2) == 914.34
    assert round(obj.asset_to_sales_ratio(20, 10), 2) == 2.0
    assert round(obj.asset_turnover_ratio(10, 20), 2) == .5
    assert round(obj.average_collection_period(8), 2) == 45.62
    assert round(obj.balloon_loan_payment(11000, 5000, .01, 36), 2) == 249.29
    assert round(obj.bid_ask_spread(40, 50), 2) == 10
    assert round(obj.bond_equivalent_yield(100, 90, 5), 2) == 8.11
    assert round(obj.book_value_per_share(100, 50), 2) == 2.0
    assert round(obj.capital_asset_pricing_model(.08, 4, .1), 4) == .16
    assert round(obj.capital_gains_yield(10, 15), 2) == .5
    assert round(obj.compound_interest(1000, .01, 12), 2) == 126.83
    assert round(obj.continuous_compounding(1000, .1, 2), 2) == 1221.4
    assert round(obj.contribution_margin(1000000, 400000), 2) == 600000
    assert round(obj.current_ratio(100, 50), 2) == 2.0
    assert round(obj.current_yield(100, 900), 4) == .1111
    assert round(obj.days_in_inventory(4.32), 2) == 84.49
    assert round(obj.debt_coverage_ratio(200000, 35000), 2) == 5.71
    assert round(obj.debt_ratio(2500000, 3000000), 4) == .8333
    assert round(obj.debt_to_equity_ratio(100, 130), 4) == .7692
    assert round(obj.debt_to_income_ratio(10, 15), 4) == .6667
    assert round(obj.diluted_earnings_per_share(100, 15, 50), 2) == 1.54
    assert round(obj.discounted_payback_period(5000, .1, 1000), 3) == 7.273
    assert round(obj.dividend_payout_ratio(100, 140), 5) == .71429
    assert round(obj.dividend_yield(10, 140), 5) == .07143
    assert round(obj.dividends_per_share(100, 4), 2) == 25.0
    assert round(obj.doubling_time(.005), 2) == 138.98
    assert round(obj.doubling_time_with_continuous_compounding(.06), 2) == 11.55
    assert round(obj.doubling_time_for_simple_interest(.25), 2) == 4.0
    assert round(obj.earnings_growth_rate(.04, .07), 5) == .0028
    assert round(obj.earnings_per_share(125, 3), 2) == 41.67
    assert round(obj.earnings_per_share_growth_rate(100, 172), 2) == .72
    assert round(obj.equity_multiplier(125, 8), 3) == 15.625
    assert round(obj.equivalent_annual_annuity(100000, .08, 4), 2) == 30192.08
    assert round(obj.estimated_earnings(500, 400), 2) == 100.0
    assert round(obj.free_cash_flow_to_equity(50, 20, 24, 12, 8), 2) == 42.0
    assert round(obj.free_cash_flow_to_firm(100, .2, 20, 55, 13), 2) == 32.0
    assert round(obj.future_value(1000, .005, 12), 2) == 1061.68
    assert round(obj.future_value_with_continuous_compounding(3000, .04, 4), 2) == 3520.53
    assert round(obj.future_value_factor(.01, 12), 4) == 1.1268
    assert round(obj.geometric_mean_return([.04, .05, .06, .07]), 5) == .05494
    assert round(obj.gross_profit(200, 100), 2) == 100.0
    assert round(obj.gross_profit_margin(20000000, 10000000), 2) == .5
    assert round(obj.future_value_of_growing_annuity(2000, .03, .05, 5), 2) == 11700.75
    assert round(obj.growing_annuity_payment_from_present_value(100, 0.1, 0.15, 6), 2) == 16.36
    assert round(obj.growing_annuity_payment_from_future_value(100, .04, .06, 4), 2) == 21.59
    assert round(obj.present_value_of_a_growing_annuity(50, .05, .06, 3), 2) == 144.22
    assert round(obj.present_value_of_growing_perpetuity(1000, .1, .05), 2) == 20000.0
    assert round(obj.holding_period_return([.1, .05, -.02]), 4) == .1319
    assert round(obj.interest_coverage_ratio(150, 65), 2) == 2.31
    assert round(obj.inventory_turnover_ratio(500, 40), 2) == 12.5
    assert round(obj.interest_rate_parity(.07, 80, 60), 5) == .42667
    assert round(obj.balloon_balance_of_a_loan(100000, 843.86, .005, 60), 2) == 76008.88
    assert round(obj.loan_payment(50, .08, 8), 2) == 8.7
    assert round(obj.remaining_balance_on_loan(60, 20, .13, 2), 2) == 34.01
    assert round(obj.loan_to_deposit_ratio(60, 67), 4) == .8955
    assert round(obj.loan_to_value_ratio(50, 66), 4) == .7576
    assert round(obj.net_asset_value(1000000, 100000, 100000), 2) == 9.0
    assert round(obj.net_interest_income(60, 40), 2) == 20.0
    assert round(obj.net_interest_margin(500, 40), 4) == 12.5
    assert round(obj.net_interest_spread(.5, .2), 2) == .3
    assert round(obj.net_present_value(400, [50, 60, 70, 100, 500], .12), 2) == 89.56
    assert round(obj.net_profit_margin(50, 60), 4) == .8333
    assert round(obj.net_working_capital(68, 24), 2) == 44.0
    assert round(obj.number_of_periods_for_present_value_to_reach_future_value(2000, 1500, .005), 2) == 57.68
    assert round(obj.operating_margin(600, 234), 3) == 2.564
    assert round(obj.payback_period(66, 55), 2) == 1.2
    assert round(obj.present_value_of_perpetuity(10, .05), 2) == 200.0
    assert round(obj.perpetuity_payment(1000, .1), 2) == 100.0
    assert round(obj.perpetuity_yield(100, 1000), 2) == .1
    assert round(obj.preferred_stock_value(88, .05), 2) == 1760.0
    assert round(obj.present_value(56, .24, 6), 2) == 15.4
    assert round(obj.present_value_factor(.66, 7), 5) == 0.02879
    assert round(obj.present_value_with_continuous_compounding(1100, .08, 2), 2) == 937.36
    assert round(obj.present_value_with_continuous_compounding_factor(.24, 2), 4) == 0.6188
    assert round(obj.price_to_book_value_ratio(56, 24), 3) == 2.333
    assert round(obj.price_to_cash_flows_ratio(500, 50), 2) == 10.0
    assert round(obj.price_to_dividend_ratio(75, 5), 2) == 15.0
    assert round(obj.price_to_earnings_ratio(43, 23), 3) == 1.87
    assert round(obj.price_to_earnings_to_growth_ratio(10, .28), 3) == 35.714
    assert round(obj.price_to_sales_ratio(76, 55), 3) == 1.382
    assert round(obj.profitability_index(950.96, 1000), 3) == .951
    assert round(obj.quick_ratio(543, 56), 3) == 9.696
    assert round(obj.rate_of_inflation(34, 45), 5) == .32353
    assert round(obj.real_rate_of_return(.05, .03), 5) == .01942
    assert round(obj.receivables_turnover_ratio(78, 24), 3) == 3.25
    assert round(obj.retention_ratio(56, 22), 5) == .60714
    assert round(obj.return_on_assets(45, 22), 3) == 2.045
    assert round(obj.return_on_equity(800, 56), 3) == 14.286
    assert round(obj.return_on_investment(67, 63), 5) == .06349
    assert round(obj.risk_premium(100, 24), 2) == 76.0
    assert round(obj.rule_of_72(.07), 3) == 10.286
    assert round(obj.simple_interest(500, .07, 5), 2) == 175.0
    assert round(obj.present_value_of_stock_with_constant_growth(100, .04, .02), 2) == 5000.0
    assert round(obj.present_value_of_stock_with_zero_growth(500, .88), 3) == 568.182
    assert round(obj.tax_equivalent_yield(.04, .34), 4) == .0606
    assert round(obj.total_stock_return(400, 300, 129), 5) == .0725
    assert round(obj.weighted_average([.2, .4, .1, .3], [.04, .05, .06, .07]), 5) == .055
    assert round(obj.yield_to_maturity(100, 1000, 920, 10), 4) == .1125
    assert round(obj.zero_coupon_bond_value(100, .06, 5), 2) == 74.73
    assert round(obj.zero_coupon_bond_effective_yield(400, 78, 5), 5) == .38673

    print("Testing successful")
