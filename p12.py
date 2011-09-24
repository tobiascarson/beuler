#!/usr/bin/python


def factors(x):
	
	return factors



#def factors(n): return (i for i in range(1,n) if n%i==0)
def count_factors(n): return len(factors(n))#return sum(1 for e in factors(n))
print factors(10)
print count_factors(10)
for i in range(1,100000):
	s=sum(range(i))
	if(count_factors(s)>50):
		print s
		break
