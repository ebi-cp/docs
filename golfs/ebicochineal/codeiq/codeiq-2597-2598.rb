#! /usr/bin/env python3



y,m,d=input().split('.')
print(chr(116+(int(y)*2+(m=ord(m)-65)*3+(m*7|15)%5+int(d))%7))

# y,m,d=input().split('.');m=ord(m)
# print(chr(116+(int(y)*2+(m-65)*3+sum(1for x in'2469'if m-17>ord(x))+int(d))%7))

# y,m,d=input().split('.')
# print(chr(116+(int(y)*2+(ord(m)-65)*3+len(list(filter(lambda x:ord(m)-65>x,[2,4,6,9])))+int(d


# for o in '+*-^|&':
#     for k in range(100):
#         for j in range(10):
#             c=0
#             for i in range(11):
#                 if eval("(i*j"+o+"k)")%5 == sum(1for x in[2,4,6,9]if i>x):
#                     c+=1
#             if c>10:
#                 print(j,k,o)
# 76146.G.8 x
# 40000.F.6 w
# 4000.C.1 y
# 1600.A.1    t
# 1601.B.7    x
# 1602.C.14   v
# 1603.D.19   z
# 
# 1605.F.31   u1604.E.25   w
# ■平年の場合 
#    A, B, D, F, H, I, K月は31日
#    C, E, G, J月は32日
# ■うるう年の場合 
#    A, B, D, E, F, H, I, K月は31日
#    C, G, J月は32日

# ラゲ暦年が20で割り切れる年はうるう年 
# ただし、ラゲ暦年が80で割り切れる年は平年 
# ただし、ラゲ暦年が4000で割り切れる年はうるう年


putc 116+eval("(y=%s)*2+(m=?%s.ord-65)*3-5+(m*7|15)%%5-(m>3?y:y-=1)/20+y/80-y/4000+%s"%gets.split(?.))%7

#ややリアル編 104
putc 116+eval("(y=%s)*2+(m=?%c.ord-65)*3-5+(m*7|15)%%5-(m>3?y:y-=1)/20+y/80-y/4000+%s"%gets.split(?.))%7

f=->x{x/20-x/80+x/4000};putc 116+eval("(y=%s)*2+(m=?%c.ord-65)*3-5+(m*7|15)%%5-f[m>3?y:y-1]+%s"%gets.split(?.))%7

f=->x{x/20-x/80+x/4000};putc 116+eval("(y=%s)*2-f[y-1]+(m=?%c.ord-65)*3-5+(m*7|15)%%5-(m>3?f[y]-f[y-1]:0)+%s"%gets.split(?.))%7

# f=->x{x*0.0375}
# f=->x{x*151/4000}
# f=->x{x*3/80+x/4000}
# f=->x{(x*3+x/50)/80}
# f=->x{(x*4-x+x/50)/80}

f=->x{x/20-x/80+x/4000};putc 116+eval("(y=%s)*2-f[y-1]+(m=?%c.ord-65)*3-5+(m*7|15)%%5-(m>3?f[y]-f[y-1]:0)+%s"%gets.split(?.))%7

y,m,d=gets.split(?.);m=m.ord-65;y=y.to_i;f=->x{x/20-x/80+x/4000}
putc 116+(y*2-f[y]-5+m*3+(m*7|15)%5+(m>3?f[y+1]-f[y]:0)+d.to_i)%7
puts f[y+1]
puts f[y]
puts 4000/4000

y,m,d=gets.split(?.);m=m.ord-65;y=y.to_i;f=->x{x/20+x/80-x/4000}
putc 116+(y*2-f[y]-5+m*3+(m*7|15)%5+m>3?f[y+1]-f[y]:0+d.to_i)%7

y,m,d=gets.split(?.);m=m.ord-65;y=y.to_i;f={|x|x/20+x/80-x/4000}
putc 116+(y*2-f(y)-5+m*3+(m*7|15)%5+d.to_i)%7

y,m,d=gets.split(?.);m=m.ord-65;y=y.to_i
putc 116+(y*2-y/20+y/80-y/4000+m*3+(m*7|15)%5+d.to_i)%7




putc 116+eval("%s*2+(m=?%s.ord-65)*3+(m*7|15)%%5+%s"%gets.split(?.))%7
# 初級 70
putc 116+eval("%s*2+(m=?%c.ord-65)*3+(m*7|15)%%5+%s"%gets.split(?.))%7
# $><<(116+eval("%s*2+(m=?%c.ord-65)*3+(m*7|15)%%5+%s"%gets.split(?.))%7).chr


# y,m,d=gets.split(?.);m=m.ord-65
# $><<(116+(y.to_i*2+m*3+(m*7|15)%5+d.to_i)%7).chr

# y,m,d=gets.split(?.);m=m.ord-65
# $><<(116+(eval(y+"*2+"+d)+m*3+(m*7|15)%5)%7).chr


# y,m,d=gets.split(?.);m=m.ord-65
# $><<(116+(y.to_i*2+m*3+(m-1)/2+(m<1?1:m==9?-1:0)+d.to_i)%7).chr

# y,m,d=gets.split(?.);m=m.ord-65
# $><<(116+(y.to_i*2+m*3+(m>4?m>9?4:m>6?3:2:m>2?1:0)+d.to_i)%7).chr

# y,m,d=gets.split(?.);m=m.ord-65;$><<(116+(y.to_i*2+m*3+[2,4,6,9].select{|x|m>x}.size+d.to_i)%7).chr

# y,m,d=gets.split(?.);m=m.ord-65
# $><<(116+(y.to_i*2+m*3+[2,4,6,9].select{|x|m>x}.size+d.to_i)%7).chr

# y,m,d=gets.split(".");m=m.ord-65;d=y.to_i*2+m*3+[2,4,6,9].select{|x|m>x}.size+d.to_i
# puts (116+d%7).chr


# y,m,d=gets.split(".");m=m.ord-65;d=d.to_i;[2,4,6,9].map{|x|m>x&&d+=1}
# puts (116+(y.to_i*2+m*3+d)%7).chr





