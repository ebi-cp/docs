#! /usr/bin/env python3
s=input()+' ';b='';l=[' '];c=m=0
for i in s:
 if i=='ｗ':c+=1
 else:
  if c>m and b:m,l=c,[]
  if c:
   if c==m:l+=[b]
   b,c='',0
  b+=i
*l,=map(print,l)