def function(balance, annualInterestRate):
    Monthlyinterestrate = annualInterestRate / 12.0
    minpay = 0
    bal = 1
    while bal > 0:
        bal = balance
        minpay += 10
        for i in range(12):
            Monthlyunpaidbalance = bal - minpay
            bal = Monthlyunpaidbalance * (1 + Monthlyinterestrate)

    print('Lowest Payment:', minpay)

