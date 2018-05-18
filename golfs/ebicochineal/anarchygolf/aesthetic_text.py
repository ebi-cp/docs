#! /usr/bin/env python3

# s=raw_input().upper()
# print" ".join(s)
# print"\n".join(s[1:])

# s=raw_input().upper();print" ".join(s);print"\n".join(s[1:])
# s=raw_input().upper();print" ".join(s);print"\n".join(s)
# s=input().upper();print(" ".join(s));print("\n".join(s))

# s=raw_input().upper()
# for i in" \n":
#     for j in s:print j,end=i;s=s[1:]
# s=raw_input().upper();print" ".join(s)+"\n"+"\n".join(s[1:])

# s=input().upper();print(*s),print("\n".join(s[1:]))

# s=list(raw_input().upper());s[0]=" ".join(s)
# for i in s:print i

# s=raw_input().upper();print" ".join(s);print"\n".join(s[1:])


# s=list(raw_input().upper());s[0]=" ".join(s)
# for i in s:pr nt i


# w=a,*s=raw_input().upper()
# for i in[w]+s:print(*i)
# w=a,*s=input().upper()
# for i in[w]+s:print(*i)

# s=list(raw_input().upper());print" ".join(s);print"\n".join(s[1:])


s=input().upper()
for i in[s,*s[1:]]:print(*i)

s=a,*l=input().upper()
for i in[s]+l:print(*i)



"""
s=input().upper()
for i in[s,*s[1:]]:print(*i)

s=a,*l=input().upper()
for i in[s]+l:print(*i)



s=input().upper()
for i in[s,*s[1:]]:print(*i)

w=a,*s=input().upper()
for i in[w]+s:print(*i)

w=*s,=input().upper();s[0]=w
for i in s:print(*i)


w=*s,=input().upper();s[0]=w
for i in s:print(*i)

s=input().upper();print(*s,end="\n".join(s[1:]))
s=input().upper();print(*s),print("\n".join(s[1:]))
s=input().upper();print(*s,"\n"+"\n".join(s[1:]))

s=input().upper();print(" ".join(s)+"\n".join(s[1:]))

"""