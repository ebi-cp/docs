#! /usr/bin/env python3
import time
import os

r=range;n,h,w=[int(input())for x in'nhw'];s=[input()for x in'*'*h]
for m in'*'*n:
 s=[''.join((lambda a:m if m==s[i][j]and a==4or a==3 else'.')(sum(1for o in[s[(y+i-1)%h][(x+j-1)%w]for y in r(3)for x in r(3)]if m==o))for j in r(w))for i in r(h)]
 time.sleep(0.1)
 os.system('cls')
 for i in s:print(i)


# exec("r=range;n,h,w=[int(input())%s'nhw'];s=[input()%s'*'*h]\n%s'*'*n:s=[''.join((lambda a:m if m==s[i][j]and a==4or a==3 else'.')(sum(1%s[s[(y+i-1)%%h][(x+j-1)%%w]%sr(3)%sr(3)]if m==o))%sr(w))%sr(h)]\n%ss:print(i)"%tuple('for %s in '%s for s in'xxmoyxjii'))


# r=range;n,h,w=[int(input())for x in'nhw'];s=[input()for x in'*'*h]
# for m in'*'*n:s=[''.join((lambda a:m if m==s[i][j]and a==4or a==3 else'.')(sum(1for o in[s[(y+i-1)%h][(x+j-1)%w]for y in r(3)for x in r(3)]if m==o))for j in r(w))for i in r(h)]
# for i in s:print(i)


# r=range;n,h,w=[int(input())for x in'nhw'];s=[input()for x in'*'*h]
# for m in'*'*n:
#  s=[''.join((lambda a:'*'if'*'==s[i][j]and a==4or a==3 else'.')(sum(1for o in[s[(y+i-1)%h][(x+j-1)%w]for y in r(3)for x in r(3)]if'*'==o))for j in r(w))for i in r(h)]
# for i in s:print(i)


# r=range;n,h,w=[int(input())for x in'nhw'];s=[input()for x in'*'*h];t=s[:]
# for m in'*'*n:
#  for i in r(h):
#   v=''
#   for j in r(w):
#    a=sum(1for o in[s[(y+i-1)%w][(x+j-1)%w]for y in r(3)for x in r(3)]if'*'==o)
#    v+='*'if'*'==s[i][j]and a==4or a==3 else'.'
#   t[i]=v
#  s=t[:]
# for i in s:print(i)



# r=range;n,y,x=[int(input())for x in'nyx'];s=[input()for x in'.'*y];t=s[:]
# for g in'*'*n:
#  for i in r(y):
#   v=''
#   for j in r(x):a=sum(1for o in[s[(i-1+k)%y][(j-1+l)%x]for k in r(3)for l in r(3)]if o==g);v+=g if g==s[i][j]and a==4or a==3 else'.'
#   t[i]=v
#  s=t[:]
# for h in s:print(h)

# r=range;n,y,x=[int(input())for x in'nyx'];s=[input()for x in'.'*y];t=s[:]
# for g in'*'*n:
#  for i in r(y):
#   v=''
#   for j in r(x):
#    a=sum(1for o in[s[(i-1+k)%y][(j-1+l)%x]for k in r(3)for l in r(3)]if o==g)
#    v+=g if g==s[i][j]and a==4or a==3 else'.'
#   t[i]=v
#  s=t[:]
# for h in s:print(h)

# def f(m,q):
#  if m<1:
#   for h in q:print(h)
#   return
#  t=q[:]
#  for i in r(y):
#   v=''
#   for j in r(x):
#    a=sum(1for o in[q[(i-1+k)%y][(j-1+l)%x]for k in r(3)for l in r(3)]if o=='*')
#    v+='*'if'*'==q[i][j]and a==4 or a==3 else'.'
#   t[i]=v
#  f(m-1,t)
# r=range;n,y,x=[int(input())for x in'nyx'];s=[input()for x in'.'*y]
# f(n,s)





# r,g=range,'*';n,y,x=[int(input())for x in g*3];s=[input()for x in g*y]
# t=s[:]
# for u in g*n:
#  for i in r(y):
#   v=''
#   for j in r(x):
#    a=sum(1for o in[s[(i-1+k)%y][(j-1+l)%x]for k in r(3)for l in r(3)]if o==g)
#    v+=g if g==s[i][j]and a==4 or a==3 else'.'
#   t[i]=v
#  s=t[:]
# for h in s:print(h)


# r=range;n,y,x=[int(input())for x in'nyx'];s=[input()for x in'.'*y]
# t=s[:]
# for g in'.'*n:
#  for i in r(y):
#   v=''
#   for j in r(x):
#    a=sum(1for o in[s[(i-1+k)%y][(j-1+l)%x]for k in r(3)for l in r(3)]if o=='*')
#    v+='*'if'*'==s[i][j]and a==4 or a==3 else'.'
#   t[i]=v
#  s=t[:]
# for h in s:print(h)




# r=range;n,y,x=[int(input())for x in'nyx'];s=[input()for x in'.'*y]
# t=s[:]
# for g in'.'*n:
#  for i in r(y):
#   v=''
#   for j in r(x):
#    a=sum(1for o in[s[(i-1+k)%y][(j-1+l)%x]for k in r(3)for l in r(3)]if o=='*')
#    b=s[i][j]
#    v+=(lambda a,b:('*'if b=='*'and a==4 or a==3 else'.'))(a,b)
#   t[i]=v
#  s=t[:]
# for h in s:print(h)

# time.sleep(60)



# r=range;n,y,x=[int(input())for x in'nyx'];s=[input()for x in'.'*y]
# t=s[:]
# for g in'.'*n:
#  for i in r(y):
#   v=''
#   for j in r(x):
#    a=sum(1for o in[s[(i-1+k)%y][(j-1+l)%x]for k in r(3)for l in r(3)]if o=='*')
#    if s[i][j]=='*':a-=1
#    b=s[i][j]
#    v+=('*'if a in(2,3)else'.')if b=='*'else('*'if a==3 else b)
#   t[i]=v
#  s=t[:]
# for h in s:
#  print(h)

# time.sleep(60)
# print([s[i][j]for i in r(y)for j in r(x)])


time.sleep(60)