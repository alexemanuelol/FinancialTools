#!/usr/bin/env python3

import math

def convert_to_percentage(number):
    """ Convert (0-100) percentage number to (0-1)"""
    number = float(number)
    if number < 0: raise Exception('Percentage is outside interval.')
    return 0 if number == 0 else number / 100

def format_number(number):
    return str(format(math.ceil(number), ',').replace(',', ' ').replace('.', ','))


if __name__ == "__main__":
    # Ask for initial values
    try:
        propertyCost = input('Enter the Property Cost (Default 2000000): ')
        propertyCost = 2000000.0 if propertyCost == '' else float(propertyCost)
        if propertyCost <= 0: raise Exception('Invalid property cost.')

        downPayment = input('Enter the Down Payment Percentage (Default 15%): ')
        downPayment = .15 if downPayment == '' else convert_to_percentage(downPayment)

        mortgageType = input('Enter the Mortgage type in years (Default 15 years): ')
        mortgageType = 15.0 if mortgageType == '' else float(mortgageType)
        if mortgageType <= 0: raise Exception('Invalid Mortgage type.')

        interestRate = input('Enter the interest rate percentage (Default 4%): ')
        interestRate = .04 if interestRate == '' else convert_to_percentage(interestRate)
    except ValueError:
        print('Could not convert string to float.')
        exit(1)
    except Exception as e:
        print(e)
        exit(1)

    loanAmount = propertyCost * (1 - downPayment)
    amortizationNumberOfPayments = mortgageType * 12
    amortizationPayment = loanAmount / amortizationNumberOfPayments

    print()
    print('Down Payment: '.ljust(20) + f'{format_number(propertyCost - loanAmount)}')
    print('Loan Amount:'.ljust(20) + f'{format_number(loanAmount)}\n')

    string = 'Month:'.ljust(10)
    string += 'Amortization:'.ljust(17)
    string += 'Interest:'.ljust(13)
    string += 'Total Payment:'.ljust(18)
    string += 'Loan Left:'
    string += '\n' + ('-' * 68)
    print(string)

    loanLeft = loanAmount
    interestTotal = 0
    for i in range(1, int(amortizationNumberOfPayments) + 1):
        interest = loanLeft * (interestRate / 12)
        interestTotal += interest
        loanLeft -= amortizationPayment
        if loanLeft <= 0: loanLeft = 0

        line = str(i).ljust(10)
        line += format_number(amortizationPayment).ljust(17)
        line += format_number(interest).ljust(13)
        line += format_number(amortizationPayment + interest).ljust(18)
        line += format_number(loanLeft)
        print(line)

    line = 'Total:'.ljust(10)
    line += format_number(loanAmount).ljust(17)
    line += format_number(interestTotal).ljust(13)
    line += format_number(loanAmount + interestTotal).ljust(18)
    line += format_number(loanLeft)
    print(line)
