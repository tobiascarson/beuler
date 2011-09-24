#!/usr/bin/python
def isprime(n):
	n = abs(int(n))
	if n < 2: return False
	if n == 2: return True    
	if not n & 1: return False
	for x in range(3, int(n**0.5)+1, 2):
		if n % x == 0: return False
	return True


p=m=0
while m < 10001:
	p+=1
	if(isprime(p)): 
		m+=1

print p
