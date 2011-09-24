#!/usr/bin/python
from math import sqrt,floor
def factor(n):  
	return set(reduce(list.__add__, ([i, n/i] for i in range(1, int(sqrt(n) + 1)) if n % i == 0)))	
def count_factors(n): return sum(1 for i in factor(n))
#print [i for i in factor(12)]
#print [i for i in factor(1000)]
#print count_factors(10)
for i in range(2,100000):
	s=sum(range(i))
	if(count_factors(s)>500):
		print s
		break
