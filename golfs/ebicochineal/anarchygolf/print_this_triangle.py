#! /usr/bin/env python3

# 114 ...
i=1
while i<63:z=[];j=2;exec("s='';t=i+1\nwhile t:s=chr(48+t%j+39*(t%j>9))+s;t//=j\nz+=s,;j+=1;"*i);print(*z);i+=1

# 115
i=1
while i<63:z=[];j=2;exec("s='';t=i+1\nwhile t:s=chr(48+t%j+39*(t%j>9))+s;t//=j\nz+=[s];j+=1;"*i);print(*z);i+=1

# 117
i=2
while i<64:z=[];j=2;exec("s='';t=i\nwhile t:s=chr(48+t%j+39*(t%j>9))+s;t//=j\nz+=[s];j+=1;"*(i-1));print(*z);i+=1

# 118
for i in range(2,64):z=[];j=2;exec("s='';t=i\nwhile t:s=chr(48+t%j+39*(t%j>9))+s;t//=j\nz+=[s];j+=1;"*(i-1));print(*z)

# 121
i=2
exec("z=[];j=2\nwhile j<=i:\n s='';t=i\n while t:s=chr(48+t%j+39*(t%j>9))+s;t//=j\n z+=[s];j+=1\nprint(*z);i+=1;"*62)

# 127
def f(n,d):c=chr(48+n%d+39*(n%d>9));return f(n//d,d)+c if n//d else c
y=2
while y<64:print(*[f(y,j+2)for j in range(y-1)]);y+=1

# 134
def f(s,n,d):s=chr(48+n%d+39*(n%d>9))+s;return f(s,n//d,d)if n//d else s
for i in range(62):print(*[f('',i+2,j+2)for j in range(i+1)])

# 146
def f(s,n,d):p,q=n//d,n%d;s=chr(48+q+39*(q>9))+s;return f(s,p,d)if p else s
for i in range(62):print(' '.join([f('',i+2,j+2)for j in range(i+1)]))

# 146 ループを１つにしてみるとか
i=z=t=0;j=5;s=''
while i<63:
 if t:s=chr(48+t%j+39*(t%j>9))+s;t//=j
 elif s:z+=[s];j+=1;s=''
 elif j<i+2:t=i+1
 else:z and print(*z);z=[];j=2;i+=1

# while 1:a=input();print a[-1]-a[0]
# while 1:a,*b,c=eval(input());print(c-a)

"""
def f(s,n,d):p,q=n//d,n%d;s=chr(48+q+39*(q>9))+s;return f(s,p,d)if p else s

for i in range(62):
    print(' '.join([f('',i+2,j+2)for j in range(i+1)]))


def f(s,n,d):s=chr(48+n%d+39*(n%d>9))+s;return f(s,n//d,d)if n//d else s
for i in range(62):print(*[f('',i+2,j+2)for j in range(i+1)])

def f(n,d):c=chr(48+n%d+39*(n%d>9));return f(n//d,d)+c if n//d else c
for i in range(62):print(*[f(i+2,j+2)for j in range(i+1)])

def f(n,d):c=chr(48+n%d+39*(n%d>9));return f(n//d,d)+c if n//d else c
y=2
while y<64:print(*[f(y,j+2)for j in range(y-1)]);y+=1

48+n%d+39*(n%d>9)
[48,87][n%d>9]+n%d


i=2
while i<64:
 z=[]
 for j in range(2,i+1):
  s='';t=i
  while t:s=chr(48+t%j+39*(t%j>9))+s;t=t//j
  z+=[s]
 print(*z);i+=1
 
 
i=2
while i<64:
 z=[];j=2
 while j<=i:
  s='';t=i
  while t:s=chr(48+t%j+39*(t%j>9))+s;t//=j
  z+=[s];j+=1
 print(*z);i+=1



i=2
exec("z=[];j=2\nwhile j<=i:\n s='';t=i\n while t:s=chr(48+t%j+39*(t%j>9))+s;t//=j\n z+=[s];j+=1\nprint(*z);i+=1;"*62)


for i in range(2,64):z=[];j=2;exec("s='';t=i\nwhile t:s=chr(48+t%j+39*(t%j>9))+s;t//=j\nz+=[s];j+=1;"*(i-1));print(*z)

i=2
while i<64:z=[];j=2;exec("s='';t=i\nwhile t:s=chr(48+t%j+39*(t%j>9))+s;t//=j\nz+=[s];j+=1;"*(i-1));print(*z);i+=1


i=1
while i<63:z=[];j=2;exec("s='';t=i+1\nwhile t:s=chr(48+t%j+39*(t%j>9))+s;t//=j\nz+=[s];j+=1;"*i);print(*z);i+=1



i=z=t=0;j=5;s=''
while i<63:
 if t:s=chr(48+t%j+39*(t%j>9))+s;t//=j
 elif s:z+=[s];j+=1;s=''
 elif j<i+2:t=i+1
 else:z and print(*z);z=[];j=2;i+=1
"""
