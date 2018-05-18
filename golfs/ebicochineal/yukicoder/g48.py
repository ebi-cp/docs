#! /usr/bin/env python3

X,Y,L=[int(input())for x in'...']
f=lambda x:abs(x)//L+(x%L>0)
print(f(X)+f(Y)+[X!=0,2][Y<0])









