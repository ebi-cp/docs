#! /usr/bin/env python

N=input()+1;a,l,c,r=N,[1],0,{}
while c<a:
 q=l;l=[];c+=1
 for i in q:b=bin(i).count('1');a=[a,c][i==N-1];l=[l+[i+b]*(i+b<N)+[i-b]*(i>b),l][i in r];r[i]=1
print[-1,a][a<N]
"""3 177
N=int(input())+1;a,l,c,r=N,[1],0,{}
while c<a:
 q=l;l=[];c+=1
 for i in q:b=bin(i).count('1');a=[a,c][i==N-1];l=[l+[i+b]*(i+b<N)+[i-b]*(i>b),l][i in r];r[i]=1
print([-1,a][a<N])
"""