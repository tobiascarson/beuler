#!/usr/bin/python
"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""


factors = range(1,21)
for n in reversed(range(1,21)):
	for m in range(1,21):
		if(n != m and n%m == 0):
			if m in factors: factors.remove(m)


answer=1
for n in factors:  answer*=n
for n in factors:
	if((answer/n)%n==0):
		answer/=n

print answer
