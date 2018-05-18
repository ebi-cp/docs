#! /usr/bin/env python3

A,B=map(int,input().split())
a,b=A+B,A*B
while a:b,a=a,b%a
print(b)


# import math
# A,B=map(int,input().split())
# print(math.gcd(A+B,A*B))




