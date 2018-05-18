#! /usr/bin/env python2


exec"print[[input()"+"for x in'.'*input()]"*2

# f=input;f(eval("[[int(f())"+"for x in'.'*int(f())]"*2))


#f=lambda:int(input());print(eval("[[f()"+"for x in'.'*f()]"*2))
#i,r=int,input;print([[i(r())for y in'.'*i(r())]for x in'.'*i(r())])
"""

exec"f=input;print[[f()"+"for x in'.'*f()]"*2

3
print(eval("[[int(input())"+"for x in'.'*int(input())]"*2))
f=input;f(eval("[[int(f())"+"for x in'.'*int(f())]"*2))


5
2
11
22
3
111
222
333
4
10000
10000
10000
10000
1
3
2
0
5
"""