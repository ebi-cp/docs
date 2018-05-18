#! /usr/bin/env python3


l,r,w=[],[],len
a=b=n=m=t=u=0
for i in input():
 if'('==i:l+=[2+u];t+=1
 if')'==i:n+=a;m+=b
 if'^'==i:u+=1;b+=w(r);r=[x-1for x in r if x>1];b-=w(r)
 if'*'==i:a+=w(l);l=[x-u for x in l if x>u];a-=w(l);r+=[2]*t;t=u=0
print(n,m)

"""

def main():
    S = input()
    l = []
    cnt = 0
    lans = rans = 0
    for i in range(len(S)):
        if S[i] == '(':
            l += [2]
        elif S[i] == ')':
            lans += cnt
        elif S[i] == '^':
            l = [x-1 for x in l]
        elif S[i] == '*':
            d = len(l)
            l = [x for x in l if x > 0]
            cnt += d - len(l)
    l = []
    cnt = 0
    S = S[::-1]
    for i in range(len(S)):
        if S[i] == ')':
            l += [2]
        elif S[i] == '(':
            rans += cnt
        elif S[i] == '^':
            l = [x-1 for x in l]
        elif S[i] == '*':
            d = len(l)
            l = [x for x in l if x > 0]
            cnt += d - len(l)
    print(lans, rans)

if __name__ == '__main__':
    main()


"""
# a=b=c=d=e=f=g=h=l=r=0
# for i in input():
#  if'('==i:a+=1;e+=1
#  if')'==i:l+=d;r+=h
#  if'^'==i:c+=b;b=a;a=0;h+=g;g=f;f=0
#  if'*'==i:d+=c;c=0;f+=e;e=0 
# print(l,r)