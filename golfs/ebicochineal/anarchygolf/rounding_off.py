#! /usr/bin/env python2

while 1:x,y=raw_input().split(".");print(y>="5")+int(x)
# while 1:x,y=input().split(".");print(int(x)+(y>="5"))

"""
while 1:x,y=raw_input().split(".");print(y>="5")+int(x)
while 1:x,y=input().split(".");print(int(x)+(y>="5"))


while 1:x,y=input().split(".");print(int(x)+(y[0]>"4"))


while 1:x,y=input().split(".");print(int(x)+(ord(y[0])>52))

import sys
for i in sys.stdin:x,y=i.split(".");print(int(x)+(y[0]>"4"))

import sys
for i in sys.stdin:x,y=i.split(".");print(int(x)+(ord(y[0])>52))

import sys
for i in[round(float(x[:x.find(".")+2]))for x in sys.stdin]:print(i)





1.4999999999999998
1.4999999999999999
1.5000000000000000
1.5000000000000001
9999999999999998.9
9999999999999999.4
9999999999999999.5




"""