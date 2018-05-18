#! /usr/bin/env python3

a,n,_,b,m,_=(input()+' '+input()).split()
print([[a,b][int(n)+int(m)],-1][m==n])