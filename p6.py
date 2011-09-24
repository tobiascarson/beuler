#!/usr/bin/python

n=m=0
for i in range(1,101): n+=i*i
for i in range(1,101): m+=i
m=m*m
print (m-n)
