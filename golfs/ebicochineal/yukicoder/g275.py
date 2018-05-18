#! /usr/bin/env python3
n,a=int(input()),sorted(map(int,input().split()))
print((a[n//2-~n%2]+a[n//2])/2)