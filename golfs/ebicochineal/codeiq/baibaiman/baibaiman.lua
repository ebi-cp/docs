-- lua 87
-- a=1;b=0;c=0;d=0;e=0;f=0;for i=1,100 do print(a+b+c+d+e);f=c;c=b;b=d+a;a=d+e;d=e;e=f end
-- lua 79
-- a,b,c,d,e=1,0,0,0,0;for i=1,100 do print(a+b+c+d+e);a,b,c,d,e=d+e,d+a,b,e,c end
-- lua 64
-- a,b,c,d=1,1,1,1;for i=0,99 do print(a);a,b,c,d=b,c,d,d-c+b+a end

a,b,c,d=1,1,1,1;for i=0,99 do print(a);a,b,c,d=b,c,d,d-c+b+a end
