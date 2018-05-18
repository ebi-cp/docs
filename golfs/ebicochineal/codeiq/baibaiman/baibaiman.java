// java7 152
// class C{public static void main(String[] s){long a=1,b=0,c=0,d=0,e=0,f,i=0;for(;i<100;++i){System.out.println(a+b+c+d+e);f=c;c=b;b=d+a;a=d+e;d=e;e=f;}}}

// 138
// class C{public static void main(String[] s){long a=1,b=1,c=1,d=1,i=0,x;for(;i<100;++i){System.out.println(a);x=d-c+b+a;a=b;b=c;c=d;d=x;}}}

// 135
// class C{public static void main(String[] s){for(long a=1,b=1,c=1,d=1,i=0,x;i<100;++i,x=d-c+b+a,a=b,b=c,c=d,d=x)System.out.println(a);}}

// 134
// class C{public static void main(String[]s){for(long a=1,b=1,c=1,d=1,i=0,x;i<100;++i,x=d-c+b+a,a=b,b=c,c=d,d=x)System.out.println(a);}}

// 132
// class C{public static void main(String[]s){for(long a=1,b=1,c=1,d=1,i=0,x;i++<100;x=d-c+b+a,a=b,b=c,c=d,d=x)System.out.println(a);}}

// 129
// class C{public static void main(String[]s){for(long a=1,b=1,c=1,d=1,i=0,x;i++<100;a=b,b=c,c=d,d+=x+a-b)System.out.println(x=a);}}

// 125
// class C{public static void main(String[]s){for(long a=1,b=1,c=1,d=1,x;a>>34<4;a=b,b=c,c=d,d+=x+a-b)System.out.println(x=a);}}

// 124
// class C{public static void main(String[]s){for(long a=1,b=1,c=1,d=1,x;b%37>0;a=b,b=c,c=d,d+=x+a-b)System.out.println(x=a);}}

class C{public static void main(String[]s){for(long a=1,b=1,c=1,d=1;b%37>0;d=a+(a=b)-(b=c)+(c=d))System.out.println(a);}}