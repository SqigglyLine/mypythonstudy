good_credit = True
price = 1000000
if good_credit:
    down_pay = 10/100*price
else:
    down_pay = 20/100*price
print('Your down payment is £' + str(down_pay))