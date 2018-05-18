#! /usr/bin/env python3

# t=True;x=t+t+t;y=x+x-t
# for i in range(t,int(input())+t):f,b=i%x<t,i%y<t;print(['Fizz'*f+'Buzz'*b,i][f+b<t])

# t=True;x=t+t+t
# for i in range(t,int(input())+t):f,b=i%x<t,i%(x+x-t)<t;print([i,'Fizz'*f+'Buzz'*b][f|b])

# t=True;x=t+t+t;i=t*t
# exec("f,b=i%x<t,i%(x+x-t)<t;print([i,'Fizz'*f+'Buzz'*b][f|b]);i+=t;"*int(input()))

t=True;q=t+t
for i in range(int(input())):print(i%(q+t)//q*'Fizz'+i%(q*q+t)//(q*q)*'Buzz'or i+t)
