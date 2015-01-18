# MITx 6.00
# Problem Set 1
# Jordan Hall

# Count the number of occurences of the string 'bob' in a random string (s)

s = 'bobaskdhfboaobbobobaobbob'

count = 0
for x in range(0,len(s)-2):
    if s[x:x+3] == 'bob':
        count += 1
print('Number of times bob occurs is: ' + str(count))
