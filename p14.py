#!/usr/bin/python
def gen(n):
	while n != 1:
		if(n % 2 == 0): n = n/2
		else: n = 3*n + 1
		yield n
	yield n
#print [i for i in gen(100)]
b=0
x=0
for i in range(1,1000000):
	c=sum(1 for n in gen(i))	
	print "%i : %i" % (i, c)
	if(c > b):
		b=c
		x=i

print x
	
