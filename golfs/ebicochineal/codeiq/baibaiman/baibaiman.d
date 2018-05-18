// D 101 98 //95
// import std.stdio;void main(){for(long a=1,b=1,c=1,d=1,i=100,x;i--;a=b,b=c,c=d,d+=x+a-b)writeln(x=a);}
// import std.stdio;void main(){for(long a=1,b=1,c=1,d=1,x;a>>34<4;a=b,b=c,c=d,d+=x+a-b)writeln(x=a);}
 import std.stdio;void main(){for(long a=1,b=1,c=1,d=1,x;b%37>0;a=b,b=c,c=d,d+=x+a-b)writeln(x=a);}
//import std.stdio;void main(){for(long a=1,b=1,c=1,d=1;b%37>0;d=a+(a=b)-(b=c)+(c=d))writeln(a);}

