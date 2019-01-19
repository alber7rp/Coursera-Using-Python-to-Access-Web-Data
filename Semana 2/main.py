#!/usr/bin/env python
import re

sum = 0
data = open('regex_sum_176570.txt')
for line in data:
    aux= re.findall('[0-9]+', line)
    for n in aux:
        sum += int(n)

print "The sum of all numbers is: ", sum
