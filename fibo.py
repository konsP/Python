#!/bin/env python
#Returns the Fibonacci series up to n
#F21SC: Programming and Scripting 

def fibs(n):
  result = []
  a, b = 0, 1
  while b < n:
    result.append(b)
    a, b = b, a+b
  return result

# 
f100 = fibs(100)  # call 
print(f100)       # print result
