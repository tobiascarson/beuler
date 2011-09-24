#!/usr/bin/python


def isprime(n):
	n = abs(int(n))
	if n < 2: return False
	if n == 2: return True    
	if not n & 1: return False
	for x in range(3, int(n**0.5)+1, 2):
		if n % x == 0: return False
	return True

max=2000000
print sum(i for i in range(max) if isprime(i))


