# MITx 6.00
# Problem Set 4
# Jordan Hall

balance = float(raw_input(r'Enter your beginning balance: '))
i_rate = float(raw_input(r'Enter your annual interest rate: '))
min_pmt_rate = float(raw_input(r'Enter your minimum monthly payment rate: '))

pmts_made = 0

for m in range(1,13):
    print 'Month: ' + str(m)

    min_pmt = balance*min_pmt_rate
    pmts_made += min_pmt
    print 'Minimum monthly payment: ' + str(round(min_pmt,2))

    balance = balance - min_pmt
    balance = balance*(1+i_rate/12)
    print 'Remaining balance: ' + str(round(balance,2)) + '\n'

print 'Total paid: ' + str(round(pmts_made,2))
print 'Remaining balance: ' + str(round(balance,2))
