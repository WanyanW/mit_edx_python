
## this code calculates the credit card balance after one year if a person only pays the minimum monthly payment
## required by the credit card company each month

## math included here
# Monthly interest rate= (Annual interest rate) / 12.0
# Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
# Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
# Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

##  variables list
# balance - the outstanding balance on the credit card

# annualInterestRate - annual interest rate as a decimal

# monthlyPaymentRate - minimum monthly payment rate as a decimal

# month - 12

def final_balance(annualInterestRate, monthlyPaymentRate, month, balance):
    if month == 0:
        return balance
    else:
        Monthlyinterestrate = annualInterestRate / 12.0
        Minimummonthlypayment = monthlyPaymentRate * final_balance(annualInterestRate, monthlyPaymentRate, month-1, balance)
        Monthlyunpaidbalance = final_balance(annualInterestRate, monthlyPaymentRate, month-1, balance) - Minimummonthlypayment
        Updatedbalanceeachmonth = Monthlyunpaidbalance + Monthlyinterestrate * Monthlyunpaidbalance
        return round(Updatedbalanceeachmonth, 2)

final_balance(0.2, 0.04, 12, 42)