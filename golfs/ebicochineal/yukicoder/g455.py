#! /usr/bin/env python3

a,b='*-'
_,_,*S=open(0).read().split()
for i in S:
 c=a in i
 if[c,c<1][sum(a in x for x in S)<2]:i=i.replace(b,a,1);b=a
 print(i)





"""
a,b='*-'
S=[input()for x in a*int(input().split()[0])]
for i in S:
 c=a in i
 if[c,c<1][sum(a in x for x in S)<2]:i=i.replace(b,a,1);b=a
 print(i)


a,b='*-'
S=[input()for x in a*int(input().split()[0])]
for i in S:
 c=i.count(a)
 if[c,c<1][sum(a in x for x in S)<2]:i=i.replace(b,a,1);b=a
 print(i)

a,b='*-'
S=[input()for x in a*int(input().split()[0])]
for i in S:
 c=i.count(a)
 if[c,c<1][sum(a in x for x in S)<2]:i=i.replace(b,a,1);b=a
 print(i)


a,b='*-'
S=[input()for x in a*int(input().split()[0])]
for i in S:
 c=i.count(a)
 if[c,c<1][sum(x.count(a)>1for x in S)]:i=i.replace(b,a,1);b=a
 print(i)



4 10
----------
-----*-*--
----------
----------
4 10
*---------
*---------
----------
----------

4 10
-*--------
*---------
----------
----------
4 10
*---------
-*--------
----------
----------

3 3
---
-*-
--*

3 3
-*-
--*
---

2 2
--
**

2 2
*-
*-

2 2
*-
*-
"""