#!/usr/bin/python

def ispalindrome(n):
	string=str(n)
	return string==string[::-1]


answer = 0
for m in range(100,999):
	for n in range(100,999):
		t = m*n
		if(t > answer and ispalindrome(t)): answer = t

print answer
