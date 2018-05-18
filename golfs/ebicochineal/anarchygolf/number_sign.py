#! /usr/bin/env python2


# n=input()
# for a,b in((["-+"]+[" |"]*n)*3)[1:]:print(a*n+b)*2+a*n

# n=input()
# for a,b in((["-+"]+[" |"]*n)*3)[1:]:print(a*n+b)*2+a*n

# n=input()
# for i in(([1]+[0]*n)*3)[1:]:a,b=[" |","-+"][i];print(a*n+b)*2+a*n

# n=input()
# for a,b in(["-+"]+[" |"]*n)*3:print(a*n+b)*2+a*n
# n=input()
# for i in(([1]+[0]*n)*3)[1:]:a,b=i*"-+"or" |";print(a*n+b)*2+a*n


# n=input()
# for a,b in((["-+"]+[" |"]*n)*3)[1:]:print(a*n+b)*2+a*n



# b=2
# a=3
# print(b*~-a*5)
# print(b*(a-1)*5)

"""
n=input()
for a,b in((["-+"]+[" |"]*n)*3)[1:]:print(a*n+b)*2+a*n

n=int(input())
for a,b in((["-+"]+[" |"]*n)*3)[1:]:print((a*n+b)*2+a*n)

n=input();x=["-+"]+[" |"]*n
for a,b in(x*3)[1:]:print(a*n+b)*2+a*n

n=int(input());x=["-+"]+[" |"]*n
for a,b in(x*3)[1:]:print((a*n+b)*2+a*n)


n=input();x=[" |"]*n+["-+"]
for a,b in(x*3)[:-1]:print(a*n+b)*2+a*n

n=int(input());x=[" |"]*n+["-+"]
for a,b in(x*3)[:-1]:print((a*n+b)*2+a*n)

n=input();x,y=[" |"]*n,["-+"]
for a,b in(x+y)*2+x:print(a*n+b)*2+a*n

n=int(input());x,y=[" |"]*n,["-+"]
for a,b in(x+y)*2+x:print((a*n+b)*2+a*n)

n=input();x,y=[" |"]*n,["-+"]
for a,b in(x+y)*2+x:a*=n;print(a+b)*2+a

n=int(input());x,y=[" |"]*n,["-+"]
for a,b in(x+y)*2+x:a*=n;print((a+b)*2+a)



n=input();x,y=[" |"]*n,["-+"]
for a,b in x+y+x+y+x:a*=n;print(a+b)*2+a

n=int(input());x,y=[" |"]*n,["-+"]
for a,b in x+y+x+y+x:a*=n;print((a+b)*2+a)

n,x,y=int(input()),[" |"],["-+"];z=x*n
for a,b in z+y+z+y+z:a*=n;print((a+b)*2+a)

n,x,y=int(input()),[" |"],["-+"]
for a,b in x*n+y+x*n+y+x*n:a*=n;print((a+b)*2+a)


n=input()
for i in range(n*3+2):a,b=" |"if(i+1)%(n+1)else"-+";a*=n;print(a+b)*2+a

n=input()
for i in range(1,n*3+3):a,b=" |"if i%(n+1)else"-+";a*=n;print(a+b)*2+a


n=int(input())
for i in range(1,n*3+3):a,b=" |"if i%(n+1)else"-+";a*=n;print((a+b)*2+a)


n=int(input())
for i in range(n*3+2):a,b=" |"if(i+1)%(n+1)else"-+";print(a*n+b+a*n+b+a*n)
"""