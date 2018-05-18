
#Nimrod 76+8
var a,b,c,d,x:int64=1
for i in 0..99:
 echo a
 x=a
 a=b
 b=c
 c=d
 d=d+x+a-b

var a=[1,1,1,1:int64]
for i in 0..99:
 echo a[0]
 a=[a[1],a[2],a[3],a[0]+a[1]-a[2]+a[3]]
