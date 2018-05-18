#! /usr/bin/env python3

a=c=0
for i in input():
 c=[0,c+1][i=='…']
 a=max(a,c)
print(a)

# c=m=0
# for i in input()+' ':
#  c+=1
#  if i!='…':m,c=max(c-1,m),0
# print(m)
