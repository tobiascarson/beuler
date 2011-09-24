#!/usr/bin/python
"""
By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
"""

a = b = 1
sum = 0
while a < 4000000:
	if(b%2 == 0): sum += b;
	a, b = b, a+b

print sum
