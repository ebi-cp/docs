// class C{
// 	static void Main(){
// 		var l=new long[5];l[0]=1;
// 		for(var i=0;i<100;++i){
// 			long a=l[0],b=l[1],c=l[2],d=l[3],e=l[4];
// 			System.Console.WriteLine(a+b+c+d+e);
// 			l=new long[]{d+e,d+a,b,e,c};
// 		}
// 	}
// }

// class C{
// 	static void Main(){
// 		var l=new long[5];l[0]=1;
// 		for(var i=0;i<100;++i){
// 			System.Console.WriteLine(l[0]+l[1]+l[2]+l[3]+l[4]);
// 			l=new long[]{l[3]+l[4],l[3]+l[0],l[1],l[4],l[2]};
// 		}
// 	}
// }

// class C{static void Main(){var l=new long[5];l[0]=1;for(var i=0;i<100;++i){System.Console.WriteLine(l[0]+l[1]+l[2]+l[3]+l[4]);l=new long[]{l[3]+l[4],l[3]+l[0],l[1],l[4],l[2]};}}}

// class C{
// 	static void Main(){
// 		long a=1,b=0,c=0,d=0,e=0,f,i=0;
// 		for(;i<100;++i){
// 			System.Console.WriteLine(a+b+c+d+e);
// 			f=c;c=b;b=d+a;a=d+e;d=e;e=f;
// 		}
// 	}
// }

// 141
// class C{static void Main(){long a=1,b=0,c=0,d=0,e=0,f,i=0;for(;i<100;++i){System.Console.WriteLine(a+b+c+d+e);f=c;c=b;b=d+a;a=d+e;d=e;e=f;}}}

// 127
// class C{static void Main(){long a=1,b=1,c=1,d=1,i=0,x;for(;i<100;++i){System.Console.WriteLine(a);x=d-c+b+a;a=b;b=c;c=d;d=x;}}}

// 126
// class C{static void Main(){for(long a=1,b=1,c=1,d=1,i=0,x;i<100;++i){System.Console.WriteLine(a);x=d-c+b+a;a=b;b=c;c=d;d=x;}}}

// 124
// class C{static void Main(){for(long a=1,b=1,c=1,d=1,i=0,x;i<100;++i,x=d-c+b+a,a=b,b=c,c=d,d=x)System.Console.WriteLine(a);}}

// 122
// class C{static void Main(){for(long a=1,b=1,c=1,d=1,i=0,x;i++<100;x=d-c+b+a,a=b,b=c,c=d,d=x)System.Console.WriteLine(a);}}

// 121
// class C{static void Main(){for(long a=1,b=1,c=1,d=1,i=0,x;i++<100;x=b+a-c,a=b,b=c,c=d,d+=x)System.Console.WriteLine(a);}}

// 119
// class C{static void Main(){for(long a=1,b=1,c=1,d=1,i=0,x;i++<100;a=b,b=c,c=d,d+=x+a-b)System.Console.WriteLine(x=a);}}

// 115
// class C{static void Main(){for(long a=1,b=1,c=1,d=1,x;a>>34<4;a=b,b=c,c=d,d+=x+a-b)System.Console.WriteLine(x=a);}}

// 114
class C{static void Main(){for(long a=1,b=1,c=1,d=1,x;b%37>0;a=b,b=c,c=d,d+=x+a-b)System.Console.WriteLine(x=a);}}

// class C{static void Main(){for(long a=1,b=1,c=1,d=1,x;a>>34<4;a=b,b=c,c=d,d+=x+a-b)System.Console.WriteLine(x=a);}}

// class C{static void Main(){for(long a=1,b=1,c=1,d=1,x;b%37>0;a=b,b=c,c=d,d+=x+a-b)System.Console.WriteLine(x=a);}}
// 111
// class C{static void Main(){for(long a=1,b=1,c=1,d=1;b%37>0;d=a+(a=b)-(b=c)+(c=d))System.Console.WriteLine(a);}}

