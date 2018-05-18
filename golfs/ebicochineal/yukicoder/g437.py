#! /usr/bin/env python3

g={}
def f(s,n):
 g[n]=1
 for i in s:a,b=s.split(i,1);['0'<i!=j!=b.count(j)>1!=f(a+b.replace(j,'',2),n+int(i+j+j))for j in b]
f(input(),0)
print(max(g))

# g={}
# def f(s,n):
#  g[n]=1
#  for i in s:
#   a,b=s.split(i,1);['0'<i!=j!=b.count(j)>1!=f(a+b.replace(j,'',2),n+int(i+j+j))for j in b]
# f(input(),0)
# print(max(g))


# l={}
# def f(s,n):
#  l[n]=1
#  for i in s:
#   p,q=s.split(i,1)
#   for j in s:'0'<i!=j!=q.count(j)>1!=f(p+q.replace(j,'',2),n+int(i+j+j))
# f(input(),0)
# print(max(l))

# def f(s,n):
#  r=n
#  for i in s:
#   p,q=s.split(i,1)
#   for j in s:
#    if'0'<i!=j!=q.count(j)>1:r=max(r,f(p+q.replace(j,'',2),n+int(i+j+j)))
#  return r
# print(f(input(),0))

# 外のループを辞書にして高速化
# def f(s,n):
#  r=n
#  for i in{*s}:
#   p,q=s.split(i,1)
#   for j in s:
#    if'0'<i!=j!=q.count(j)>1:r=max(r,f(p+q.replace(j,'',2),n+int(i+j+j)))
#  return r
# print(f(input(),0))


# def f(s,n):
#  r=n
#  for i in s:
#   for j in s:
#    p,q=s.split(i,1);a=p+q.replace(j,'',2)
#    if q.count(j)>1!='0'<i!=j:r=max(r,f(a,n+int(i+j+j)))
#  return r
# print(f(input(),0))

# def f(s,n):
#  r=n
#  for i in s:
#   for j in s:
#    p,q=s.split(i,1);a=p+q.replace(j,'',2)
#    if q.count(j)>1and'0'<i!=j:r=max(r,f(a,n+int(i+j+j)))
#  return r
# print(f(input(),0))

# def f(s,n):
#  r=n
#  for i in s:
#   for j in s:
#    p,q=s.split(i,1);a=p+q.replace(j,'',2)
#    if len(s)-len(a)>2and'0'<i!=j:r=max(r,f(a,n+int(i+j+j)))
#  return r
# print(f(input(),0))

# def f(s,n):
#  r=n
#  for i in s:
#   for j in s:
#    p,q=s.split(i,1);a=p+q.replace(j,'',2)
#    if len(s)-len(a)>2and i>'0'and i!=j:r=max(r,f(a,n+int(i+j+j)))
#  return r
# print(f(input(),0))

# def f(s,n):
#  r=n
#  for i in s:
#   for j in s:
#    p=s.split(i,1);a=p[0]+p[1].replace(j,'',2)
#    if len(s)-len(a)>2and i>'0'and i!=j:r=max(r,f(a,n+int(i+j+j)))
#  return r
# print(f(input(),0))

# def f(s,n):
#  r=n
#  for i in s:
#   for j in s:
#    p=s.split(i,1);a=p[0]+p[1].replace(j,'',2)
#    if len(s)-len(a)>2and i!='0'and i!=j:r=max(r,f(a,n+int(i+j+j)))
#  return r
# print(f(input(),0))

# def f(s,n):
#  r=n;d=set(s)
#  for i in d:
#   for j in d:
#    p=s.split(i,1);a=p[0]+p[1].replace(j,'',2)
#    if len(s)-len(a)>2and i!='0'and i!=j:r=max(r,f(a,n+int(i+j+j)))
#  return r
# print(f(input(),0))

# def f(s,n):
#  r=n;d=set(s)
#  for i in d:
#   for j in d:
#    t=i+j+j;a=''
#    for k in s:
#     if t and k==t[0]:t=t[1:]
#     else:a+=k
#    if all((i!=j,i!='0',not t)):r=max(r,f(a,n+int(i+j+j)))
#  return r
# print(f(input(),0))

# def g(s,t):
#  r=''
#  for i in s:
#   if t and i==t[0]:t=t[1:]
#   else:r+=i
#  return'e'if t else r
# def f(s,n):
#  r=n
#  for i in range(1,10):
#   for j in range(10):
#    x=i*100+j*10+j;a=g(s,str(x))
#    if i-j and a!='e':r=max(r,f(a,n+x))
#  return r
# print(f(input(),0))