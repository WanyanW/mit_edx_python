def minpay(Annualinterestrate, Balance):
    Monthlyinterestrate = Annualinterestrate / 12.0
    Monthlypaymentlowerbound = Balance / 12
    Monthlypaymentupperbound = Balance * (1 + Monthlyinterestrate)**12 / 12.0
    bal = 0.1
    while abs(bal) >= 0.1:
        bal = Balance
        monthlypay = (Monthlypaymentlowerbound + Monthlypaymentupperbound)/2
        for i in range(12):
            Monthlyunpaidbalance = bal - monthlypay
            bal = Monthlyunpaidbalance * (1 + Monthlyinterestrate)
        if bal > 0:
            Monthlypaymentlowerbound = monthlypay
        else:
            Monthlypaymentupperbound = monthlypay
    print('lowest payment:', round(monthlypay, 2))

minpay(0.18, 999999)