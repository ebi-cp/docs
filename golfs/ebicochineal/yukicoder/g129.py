#! /usr/bin/env python3

N,M=int(input())//1000,int(input());r=i=1
exec('r=r*(M-i+1)//i;i+=1;'*(N%M))
print(r%10**9)

# N,M=input()/1000,input();r=i=1
# exec 'r=r*(M-i+1)/i;i+=1;'*(N%M)
# print r%10**9
