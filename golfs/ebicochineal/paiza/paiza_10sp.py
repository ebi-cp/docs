#! /usr/bin/env python3

# 実行速度最速＋ゴルフのランキング

### コンテスト終了後
M,N,*s=map(int,open(0).read().split());m=max(s[:M]);p=[x for x in s[M:]if x<=m];l=sorted({y*x for x in p for y in p})
for i in s[:M]:
 for j in l:
  if i<=j:print(j-i);break


#3
M,N=map(int,input().split());s=[int(input())for x in'0'*(M+N)];m=max(s[:M]);p=[x for x in s[M:]if x<=m];l=sorted({y*x for x in p for y in p})
for i in s[:M]:
 for j in l:
  if i<=j:print(j-i);break

#2
r=raw_input;M,N=map(int,r().split());s=[int(r())for x in'0'*(M+N)];m=max(s[:M]);p=[x for x in s[M:]if m/x];l=sorted(y*x for x in p for y in p)
for i in s[:M]:
 for j in l:
  if j/i:print j-i;break

#######################################

#3
M,N=map(int,input().split());s=[int(input())for x in'0'*(M+N)];m=max(s[:M]);p=[x for x in s[M:]if x<=m];l=sorted(y*p[x]for x in range(len(p))for y in p[x:])
for i in s[:M]:
 for j in l:
  if i<=j:print(j-i);break




r,z=raw_input,int;M,N=r().split();s=[z(r())for x in[0]*z(M)];m=max(s);p=[y for y in[z(r())for x in[0]*z(N)]if y<=m];l=sorted(y*p[x]for x in range(len(p))for y in p[x:])
for i in s:
 for j in l:
  if i<=j:print j-i;break


r,z=input,int;M,N=r().split();s=[z(r())for x in'0'*z(M)];m=max(s);p=[y for y in[z(r())for x in'0'*z(N)]if y<=m];l=sorted(y*p[x]for x in range(len(p))for y in p[x:])
for i in s:
 for j in l:
  if i<=j:print(j-i);break



# ac 238
import sys,bisect;r,z=sys.stdin.readline,int;M,N=r().split();s=[z(r())for x in'0'*z(M)];m=max(s);p=[y for y in[z(r())for x in'0'*z(N)]if y<m];l=sorted(y*p[x]for x in range(len(p))for y in p[x:])
for i in s:print(l[bisect.bisect(l,i-1)]-i)


# 
from bisect import*
def f():
 r,z=input,int;M,N=r().split();s=[z(r())for x in'0'*z(M)];m=max(s);p=[y for y in[z(r())for x in'0'*z(N)]if y<m];l=sorted(y*p[x]for x in range(len(p))for y in p[x:])
 for i in s:print(l[bisect(l,i-1)]-i)
f()

#33444
from bisect import*
def f():
 r,z=input,int;M,N=r().split();s=[z(r())for x in[0]*z(M)];m=max(s);p=[y for y in[z(r())for x in[0]*z(N)]if y<m];l=sorted(y*p[x]for x in range(len(p))for y in p[x:])
 for i in s:print(l[bisect(l,i-1)]-i)
f()

import bisect
def f():
 r,z=input,int;M,N=r().split();s=[z(r())for x in'0'*z(M)];m=max(s);p=[y for y in[z(r())for x in'0'*z(N)]if y<m];l=sorted(y*p[x]for x in range(len(p))for y in p[x:])
 for i in s:print(l[bisect.bisect(l,i-1)]-i)
f()


# 　33444
import bisect
def f():
 r,z=input,int;M,N=r().split();s=[z(r())for x in[0]*z(M)];m=max(s);p=[y for y in[z(r())for x in[0]*z(N)]if y<m];l=sorted(y*p[x]for x in range(len(p))for y in p[x:])
 for i in s:print(l[bisect.bisect(l,i-1)]-i)
f()

# 3 34343 ac
from bisect import*;r,z=input,int;M,N=r().split();s=[z(r())for x in'0'*z(M)];m=max(s);p=[y for y in[z(r())for x in'0'*z(N)]if y<m];l=sorted(y*p[x]for x in range(len(p))for y in p[x:])
for i in s:print(l[bisect(l,i-1)]-i)



# rangeのが早い気がする　[0]*nが一番遅いような
import bisect
def f():
 r,z,w=input,int,range;M,N=r().split();s=[z(r())for x in w(z(M))];m=max(s);p=[y for y in[z(r())for x in w(z(N))]if y<m];l=sorted(y*p[x]for x in w(len(p))for y in p[x:])
 for i in s:print(l[bisect.bisect(l,i-1)]-i)
f()

# ac
import sys,bisect
def f():
 r,z=sys.stdin.readline,int;M,N=r().split();s=[z(r())for x in'0'*z(M)];m=max(s);p=[y for y in[z(r())for x in'0'*z(N)]if y<m];l=sorted(y*p[x]for x in range(len(p))for y in p[x:])
 for i in s:print(l[bisect.bisect(l,i-1)]-i)
f()

#! /usr/bin/env python2
import bisect
def f():
 r=raw_input;M,N=map(int,r().split());s=[int(r())for x in[0]*M];m=max(s);p=[y for y in[int(r())for x in[0]*N]if y<m];l=sorted(y*p[x]for x in range(len(p))for y in p[x:])
 for i in s:print l[bisect.bisect(l,i-1)]-i
f()

#! /usr/bin/env python2 #239
import bisect
def f():
 r,z=raw_input,int;M,N=r().split();s=[z(r())for x in[0]*z(M)];m=max(s);p=[y for y in[z(r())for x in[0]*z(N)]if y<m];l=sorted(y*p[x]for x in range(len(p))for y in p[x:])
 for i in s:print l[bisect.bisect(l,i-1)]-i
f()

# 22222
import bisect
r,z=raw_input,int;M,N=r().split();s=[z(r())for x in[0]*z(M)];m=max(s);p=[y for y in[z(r())for x in[0]*z(N)]if y<m];l=sorted(y*p[x]for x in range(len(p))for y in p[x:])
for i in s:print l[bisect.bisect(l,i-1)]-i
# 22223 -2
from bisect import*;r,z=raw_input,int;M,N=r().split();s=[z(r())for x in[0]*z(M)];m=max(s);p=[y for y in[z(r())for x in[0]*z(N)]if y<m];l=sorted(y*p[x]for x in range(len(p))for y in p[x:])
for i in s:print l[bisect(l,i-1)]-i


"""
#! /usr/bin/env python2
import sys,bisect
def f():
 r=sys.stdin.readline;M,N=map(int,r().split());s=[int(r())for x in[0]*M];m=max(s);p=[y for y in[int(r())for x in[0]*N]if y<m];l=sorted(y*p[x]for x in range(len(p))for y in p[x:])
 for i in s:print l[bisect.bisect(l,i-1)]-i
f()

#! /usr/bin/env python3
import sys,bisect
def f():
 r=sys.stdin.readline;M,N=map(int,r().split());s=[int(r())for x in'0'*M];m=max(s);p=[y for y in[int(r())for x in'0'*N]if y<m];l=sorted(y*p[x]for x in range(len(p))for y in p[x:])
 for i in s:print(l[bisect.bisect(l,i-1)]-i)
f()

#python2
import sys,bisect
def f():
 r,w,z=sys.stdin.readline,range,int;M,N=map(z,r().split());s=[z(r())for x in w(M)];m=max(s);p=[y for y in[z(r())for x in w(N)]if y<m];l=sorted(y*p[x]for x in w(len(p))for y in p[x:])
 for i in s:print l[bisect.bisect(l,i-1)]-i
f()


#python3
import sys,bisect
def f():
 r,w,z=sys.stdin.readline,range,int;M,N=map(z,r().split());s=[z(r())for x in w(M)];m=max(s);p=[y for y in[z(r())for x in w(N)]if y<m];l=sorted(y*p[x]for x in w(len(p))for y in p[x:])
 for i in s:print(l[bisect.bisect(l,i-1)]-i)
f()

#python2
import sys,bisect
def f():
 r,w,z=sys.stdin.readline,range,int;M,N=map(z,r().split());s=[z(r())for x in w(M)];m=max(s);p=[y for y in set(z(r())for x in w(N))if y<m];l=sorted(y*p[x]for x in w(len(p))for y in p[x:])
 for i in s:print(l[bisect.bisect(l,i-1)]-i)
f()

#python3
import sys,bisect
def f():
 r,w,z=sys.stdin.readline,range,int;M,N=map(z,r().split());s=[z(r())for x in w(M)];m=max(s);p=[y for y in{z(r())for x in w(N)}if y<m];l=sorted(y*p[x]for x in w(len(p))for y in p[x:])
 for i in s:print(l[bisect.bisect(l,i-1)]-i)
f()

#python2
import sys,bisect
def f():
 r,w,z=sys.stdin.readline,range,int;M,N=map(z,raw_input().split());s=[z(r())for x in w(M)];m=max(s);p=[z(y)for y in set(r()for x in w(N))if len(y)<4]if M<334else[y for y in set(z(r())for x in w(N))if y<m];l=sorted(y*p[x]for x in w(len(p))for y in p[x:])
 for i in s:print(l[bisect.bisect(l,i-1)]-i)
f()


import sys,bisect
def f():
 r,w,z=sys.stdin.readline,range,int;M,N=map(z,r().split());s=[z(r())for x in w(M)];m=max(s);p=[z(y)for y in{r()for x in w(N)}if len(y)<4]if m<334else[y for y in{z(r())for x in w(N)}if y<m];l=sorted(y*p[x]for x in w(len(p))for y in p[x:])
 for i in s:print(l[bisect.bisect(l,i-1)]-i)
f()

import sys,bisect
def f():
 r,w,z=sys.stdin.readline,range,int;M,N=map(z,r().split());s=[z(r())for x in w(M)];m=max(s);p=[z(y)for y in set(r()for x in w(N))if len(y)<4]if M<500else[y for y in set(z(r())for x in w(N))if y<m];l=[y*p[x]for x in w(len(p))for y in p[x:]];l.sort()
 for i in s:print(l[bisect.bisect(l,i-1)]-i)
f()


import sys,bisect
def f():
 r,w,z=sys.stdin.readline,range,int;M,N=map(z,r().split());s=[z(r())for x in w(M)];m=max(s);p=[z(y)for y in{r()for x in w(N)}if len(y)<4]if M<500else[y for y in{z(r())for x in w(N)}if y<m];l=[y*p[x]for x in w(len(p))for y in p[x:]];l.sort()
 for i in s:print(l[bisect.bisect(l,i-1)]-i)
f()

#! /usr/bin/env python3
import sys
import bisect

def main():
    M, N = map(int, input().split())
    s = [int(sys.stdin.readline()) - 1 for x in range(M)]
    if M < 500:
        m = 4
        p = [int(y) for y in set(sys.stdin.readline() for x in range(N)) if len(y) < m]
        l = [p[x] * y for x in range(len(p)) for y in p[x:]]
        l.sort()
        for i in s : print(l[bisect.bisect(l, i)] - i - 1)
    else:
        m = max(s)
        p = [y for y in set(int(sys.stdin.readline()) for x in range(N)) if y < m]
        l = [p[x] * y for x in range(len(p)) for y in p[x:]]
        l.sort()
        for i in s : print(l[bisect.bisect(l, i)] - i - 1)
if __name__ == '__main__':
    main()




#! /usr/bin/env python3
import sys
import bisect

def main():
    M, N = map(int, input().split())
    s = [int(sys.stdin.readline()) - 1 for x in range(M)]
    m = max(s)
    p = [y for y in set(int(sys.stdin.readline()) for x in range(N)) if y < m]
    l = [p[x] * y for x in range(len(p)) for y in p[x:]]
    l.sort()
    for i in s : print(l[bisect.bisect(l, i)] - i - 1)
if __name__ == '__main__':
    main()



#! /usr/bin/env python

def main():
    M, N = map(int, raw_input().split())
    s = [input() for x in xrange(M)]
    p = list(set(input() for x in xrange(N)))
    l = [p[x] * y for x in xrange(len(p)) for y in p[x:]]
    l.sort()
    a = []
    m = max(s) - 1
    for i in l:
        a += [i] * (i - len(a))
        if len(a) > m : break
    for i in s : print(a[i-1] - i)

if __name__ == '__main__':
    main()



#! /usr/bin/env python3
import sys

def main():
    M, N = map(int, input().split())
    s = [int(sys.stdin.readline()) for x in range(M)]
    p = list(set(int(sys.stdin.readline()) for x in range(N)))
    l = [p[x] * y for x in range(len(p)) for y in p[x:]]
    l.sort()
    a = []
    for i in l:
        a += [i] * (i - len(a))
        if len(a) > 1000000 : break
    for i in s : print(a[i-1] - i)

if __name__ == '__main__':
    main()


import sys
import bisect

def main():
    M, N = map(int, input().split())
    s = [int(sys.stdin.readline()) - 1 for x in range(M)]
    p = list(set(int(sys.stdin.readline()) for x in range(N)))
    l = [p[x] * y for x in range(len(p)) for y in p[x:]]
    l.sort()
    for i in s : print(l[bisect.bisect(l, i)] - i - 1)

if __name__ == '__main__':
    main()


import bisect

def main():
    M, N = map(int, input().split())
    s = [int(input()) for x in range(M)]
    p = list(set([int(input()) for x in range(N)]))
    z = sorted(zip(s, range(M)))
    n = list(range(len(p)))
    il = sorted(p[x] * p[y] + 1 for x in n for y in n[x:])
    l = 0
    r = len(il)
    a = [0] * len(z)
    f = 1
    y = 0
    c = 0
    while c < len(z):
        x = bisect.bisect(il, z[y][0], l, r)
        a[z[y][1]] = il[x] - z[y][0] - 1
        if f < 0:
            f = 1
            r = x
            y += (-len(z)) + 1 + c
        else:
            f = -1
            l = x
            y += len(z)  - 1 - c
        c += 1
    for i in a : print(i)

if __name__ == '__main__':
    main()

#! /usr/bin/env python3
import bisect

def main():
    M, N = map(int, input().split())
    s = [int(input()) for x in range(M)]
    p = list(set([int(input()) for x in range(N)]))
    n = list(range(len(p)))
    l = sorted(p[x] * p[y] + 1 for x in n for y in n[x:])
    for i in s : print(l[bisect.bisect(l, i)] - i - 1)

if __name__ == '__main__':
    main()








1 1
1000000
1000000


from bisect import*;r,z=input,int;M,N=r().split();s=[z(r())for x in'0'*z(M)];m=max(s);p=[y for y in[z(r())for x in'0'*z(N)]if y<=m];l=sorted(y*p[x]for x in range(len(p))for y in p[x:])
for i in s:print(l[bisect(l,i-1)]-i)


from bisect import*;r,z=raw_input,int;M,N=r().split();s=[z(r())for x in[0]*z(M)];m=max(s);p=[y for y in[z(r())for x in[0]*z(N)]if y<=m];l=sorted(y*p[x]for x in range(len(p))for y in p[x:])
for i in s:print l[bisect(l,i-1)]-i












"""