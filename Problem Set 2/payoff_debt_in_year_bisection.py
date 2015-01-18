# MITx 6.00
# Problem Set 2
# Jordan Hall

balance = 320000
annualInterestRate = 0.2

def balance_in_a_year(balance,annualInterestRate,payment):
    for x in range(12):
        balance = balance - payment
        balance = balance*(1+annualInterestRate/12)
    return balance


lower_bound = balance/12.0
upper_bound = (balance*((1+annualInterestRate)**12))/12.0

maxGuesses = 100
epsilon = 0.0001
n = 0
while n <= maxGuesses:
    n += 1
    payment = (upper_bound + lower_bound)/2.0
    test_balance = balance_in_a_year(balance,annualInterestRate,payment)
    if abs(test_balance) < epsilon:
        break
    elif test_balance > epsilon:
        lower_bound = payment
    else:
        upper_bound = payment

print('Lowest payment: ' + str(round(payment,2)))
print('Guesses: ' + str(n))
        
        
