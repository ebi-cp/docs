#! /usr/bin/env python3
# s='1';exec("print(len(s));s=''.join(str(int(x)*2)for x in s);"*100)

# l=[1,0,0,0,0];exec('print(sum(l));l=[l[3]+l[4],l[0]+l[3],l[1],l[4],l[2]];'*100)

# l=[1]+[0]*5;exec('print(sum(l));l=[l[3]+l[4],l[0]+l[3],l[1],l[4],l[2]];'*100)

# l=[1]+[0]*4;exec('print(sum(l));l=l[3]+l[4],l[3]+l[0],l[1],l[4],l[2];'*100)
# l=[1]+[0]*4;exec('print(sum(l));l=l[4]+l[3],l[0]+l[3],l[1],l[4],l[2];'*100)
# l=[1]+[0]*4;exec'print sum(l);l=l[3]+l[4],l[0]+l[3],l[1],l[4],l[2];'*100


# l=[1]+[0]*5;exec '],l['.join('print sum(l);l=l[3]+l[4','0]+l[3','1','4','2];')

# 3 66byte
# l=[1]+[0]*4;exec('print(sum(l));a,b,c,d,e=l;l=d+e,d+a,b,e,c;'*100)

# 2 63byte
# l=[1]+[0]*4;exec'print sum(l);a,b,c,d,e=l;l=d+e,d+a,b,e,c;'*100


# a=1;b=c=d=e=f=0;exec'print a+b+c+d+e;f=c;c=b;b=d+a;a=d+e;d=e;e=f;'*100


# n=n(-1)+d+e
# n=n(-1)+e(-2)+e(-1)

# f = open("f.txt","w")
# l=[1]+[0]*4;x=1;exec'print>>f,sum(l),l,x;a,b,c,d,e=l;l=d+e,d+a,b,e,c;x*=2;'*100

# l=[1]+[0]*4;exec'print sum(l);a,b,c,d,e=l;l=d+e,d+a,b,e,c;'*100



# l=[1]+[0]*4;exec'print sum(l);a,b,c,d,e=l;l=d+e,d+a,b,e,c;'*100

# f(n) = f(n-1)-f(n-2)+f(n-3)+f(n-4)
# d={1:1,2:1,3:1,4:1}
# def f(n):
#     if n in d:return d[n]
#     d[n]=f(n-1)-f(n-2)+f(n-3)+f(n-4)
#     return d[n]
# for i in range(1,101):
#     print f(i)

# l=[1]*4;exec'a,b,c,d=l[-4:];l+=[a+b-c+d];'*96
# for n in l:print n

# l=[1]*4;exec'l+=[sum(l[-4:])-l[-2]*2];'*96
# for n in l:print n

# 57
# l=[1]*4;exec'print l[0];n=sum(l)-l[2]*2;l=l[1:]+[n];'*100

# 56
# l=[1]*4;exec'a,b,c,d=l;print a;n=d-c+b+a;l=b,c,d,n;'*100

# 54
# a,b,c,d=[1]*4;exec'print a;a,b,c,d=b,c,d,d-c+b+a;'*100

# 52
# l=[1]*4;exec'a,b,c,d=l;print a;l=b,c,d,d-c+b+a;'*100

# 50
# a=b=c=d=1;exec'print a;a,b,c,d=b,c,d,d-c+b+a;'*100

#50byte###########################################
a=b=c=d=1;exec'print a;a,b,c,d=b,c,d,d-c+b+a;'*100


# python3
a=b=c=d=1;exec('print(a);a,b,c,d=b,c,d,d-c+b+a;'*100)

# l=[1]*4;exec'print l[3];l=[sum(l[:4])-l[1]*2]+l;'*100
# l=[1]*4;exec'a,b,c,d=l;print d;l=a-b+c+d,a,b,c;'*100

# l=[]
# a=b=c=d=1;exec'l+=[a];a,b,c,d=b,c,d,d-c+b+a;'*102
# for i in range(1,100):
#     c=0
#     n=l[101]%i
#     for j in l[:-1]:
#         if n==j%i:
#             c+=1
#     if c == 0:
#         print(i,n)

