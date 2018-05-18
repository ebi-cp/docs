#! /usr/bin/env python3
# n=int(input())
# A=sorted(map(int,input().split()));d=A[1]-A[0]
# print(['NO','YES'][[x*d+A[0]for x in range(n)]*(d>0)==A])

input()
A=sorted(map(int,input().split()))
print(['NO','YES'][len({y-x for x,y in zip(A,A[1:])if y-x})==1])