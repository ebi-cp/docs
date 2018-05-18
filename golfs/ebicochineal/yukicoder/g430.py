#! /usr/bin/env python3

# def main():
#     ans = 0; k = ''
#     s = input()
#     us = set([])
#     for i in range(int(input())) : us.add(input())
#     for i in range(len(s)):
#         k = ''
#         for j in range(min(10, len(s) - i)):
#             k += s[i + j];
#             if k in us : ans += 1
#     print(ans)
    
# if __name__ == '__main__':
#     main()
# s=input();u=set([input()for x in range(int(input()))]);print(sum(sum(1for j in range(min(10,len(s)-i))if s[i:i+j+1]in u)for i in range(len(s))))

# f=input;s=f();u=set([f()for _ in'_'*int(f())]);print(sum(sum(1for j in range(min(10,len(s)-i))if s[i:i+j+1]in u)for i in range(len(s))))

# f,r=input,range;s=f();l=len(s);d={f()for _ in r(int(f()))};print(sum(sum(s[i:i+j+1]in d for j in r(min(10,l-i)))for i in r(l)))


# f=input;s=f();l=len(s);d={*eval("f(),"*int(f()))};print(sum(sum(s[i:i+j+1]in d for j in range(min(10,l-i)))for i in range(l)))

# f=input;s=f();l=len(s);d={*eval("f(),"*int(f()))};print(sum(sum(s[j:j+i+1]in d for j in range(l-i))for i in range(10)))

# f=input;s=f();l=len(s);d={*eval("f(),"*int(f()))};a=0
# for i in range(10):
#  for j in range(l-i):a+=s[j:j+i+1]in d
# print(a)

f=input;s=f();a=0
for i in[0]*int(f()):
 k=f();b=0
 while-1<i:i,a,b=s.find(k,i+b),a+b,1
print(a)

# f=input;s=f();a=0
# for i in[0]*int(f()):
#  k=f();p=b=0
#  while-1<p:
#   p=s.find(k,p+b);a+=b;b=1
# print(a)

# f=input;s=f();a=0
# for i in[0]*int(f()):
#  k=f();p=s.find(k)
#  while-1<p:
#   p=s.find(k,p+1);a+=1
# print(a)