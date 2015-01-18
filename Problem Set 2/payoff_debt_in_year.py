# MITx 6.00
# Problem Set 2
# Jordan Hall

balance = 320000
annualInterestRate = 0.2

# Find the lowest monthly payment that will pay off the balance in a year (by multiples of 10)

payment = int(round(2*balance/12 + 10,-1))
test_balance = -1
while test_balance < 0:
    payment -= 10
    test_balance = balance
    for x in range(12):
        test_balance = test_balance - payment
        test_balance = test_balance*(1+annualInterestRate/12)

payment += 10

print('Lowest payment: ' + str(payment))
