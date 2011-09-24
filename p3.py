#!/usr/bin/python
"""
What is the largest prime factor of the number 600851475143 ?
"""

def isprime(n):
	n = abs(int(n))
	if n < 2: return False
	if n == 2: return True    
	if not n & 1: return False
	for x in range(3, int(n**0.5)+1, 2):
		if n % x == 0: return False
	return True

number = last = 600851475143
x = 1
while x < last:
	if(number%x==0 and isprime(number/x)): 
		print number/x
		break
	x+=1

