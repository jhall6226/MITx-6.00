# MITx 6.00
# Problem Set 1
# Jordan Hall

# Find the longest substring of characters in alphabetical order in a random string (s)

s = 'abdfgiuhafdgafgfgsbjuinlwrssdacdhkrs'

alphabet = 'abcdefghijklmnopqrstuvwxyz'
a_substrs = []
count = 1
for x in range(1,len(s)):
    alpha_sub = alphabet[alphabet.find(s[x-1]):]
    if s[x] in alpha_sub:
        if x == len(s) - 1:
            a_substrs.append(s[x-count:])
        else:
            count += 1
    else:
        a_substrs.append(s[x-count:x])
        count = 1
longest = a_substrs[0]
for a_sub in a_substrs:
    if len(a_sub) > len(longest):
        longest = a_sub
        
print('Longest substring in alphabetical order is: ' + longest)
