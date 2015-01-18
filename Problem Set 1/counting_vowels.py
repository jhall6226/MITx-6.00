# MITx 6.00
# Problem Set 1
# Jordan Hall

# Counting Vowels in a supplied string (s)

s = 'kljabfdglkahbfgaafg'

vowels = ['a','e','i','o','u']
count = 0
for c in s:
    if c in vowels:
        count += 1
print('Number of vowels: ' + str(count))
