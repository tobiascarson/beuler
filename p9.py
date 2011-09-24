#!/usr/bin/python
"""
A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""


from math import sqrt, floor

def calc():
	for h in range(1000):
		for n in range(h):
			for m in range(n):
				if((n*n) + (m*m) == (h*h) and n+m+h == 1000):
					print n * m * h
					return

calc()
