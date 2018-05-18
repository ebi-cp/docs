
//using S=System.Console;using System.Linq;class C{static void Main(){int M=int.Parse(S.ReadLine().Split()[0]),m=0,i,j;int[]a={};var s=a.ToList();try{for(i=0;;){j=int.Parse(S.ReadLine());m=i++<M&&j>m?j:m;if(j<=m)s.Add(j);}}catch{}var l=a.ToList();for(i=s.Count;--i>=M;){for(j=i;j>=M;l.Add(s[i]*s[j--]));}l.Sort();for(i=0;i<M;++i,S.WriteLine(j))for(m=0;(j=l[m++]-s[i])<0;);}}

/// ac
//using S=System.Console;using System.Text;using System.Linq;class C{static void Main(){int M=int.Parse(S.ReadLine().Split()[0]),m=0,i,j;int[]a={};var s=a.ToList();try{for(i=0;;){j=int.Parse(S.ReadLine());m=i++<M&&j>m?j:m;if(j<=m)s.Add(j);}}catch{}var l=a.ToList();for(i=s.Count;--i>=M;){for(j=i;j>=M;l.Add(s[i]*s[j--]));}l.Sort();var b=new StringBuilder();for(i=0;i<M;++i){for(m=0;(j=l[m++]-s[i])<0;);b.Append(j.ToString()+"\n");}S.Write(b.ToString());}}

/// ac
//using S=System.Console;using System.Linq;class C{static void Main(){int M=int.Parse(S.ReadLine().Split()[0]),m=0,i,j;int[]a={};var b=a.ToList();try{for(i=0;;){j=int.Parse(S.ReadLine());m=i++<M&&j>m?j:m;if(j<=m)b.Add(j);}}catch{}var c=a.ToList();for(i=b.Count;--i>=M;){for(j=i;j>=M;c.Add(b[i]*b[j--]));}c.Sort();var s=new System.Text.StringBuilder();for(i=0;i<M;++i){for(m=0;(j=c[m++]-b[i])<0;);s.Append(j+"\n");}S.Write(s);}}

namespace System{using S=Console;using Linq;class C{static void Main(){int M=int.Parse(S.ReadLine().Split()[0]),m=0,i,j;int[]a={};var b=a.ToList();try{for(i=0;;){j=int.Parse(S.ReadLine());m=i++<M&&j>m?j:m;if(j<=m)b.Add(j);}}catch{}var c=a.ToList();for(i=b.Count;--i>=M;){for(j=i;j>=M;c.Add(b[i]*b[j--]));}c.Sort();var s=new Text.StringBuilder();for(i=0;i<M;++i){for(m=0;(j=c[m++]-b[i])<0;);s.Append(j+"\n");}S.Write(s);}}}


// using S=System.Console;using System.Linq;class C{static void Main(){int M=int.Parse(S.ReadLine().Split()[0]),m=0,i,j;int[]a={};var s=a.ToList();try{for(i=0;;){j=int.Parse(S.ReadLine());m=i++<M&&j>m?j:m;if(j<=m)s.Add(j);}}catch{}var l=a.ToList();for(i=s.Count;--i>=M;){for(j=i;j>=M;l.Add(s[i]*s[j--]));}l.Sort();for(i=0;i<M;++i,S.Write(j+"\n"))for(m=0;(j=l[m++]-s[i])<0;);}}

//using S=System.Console;using System.Linq;class C{static void Main(){int M=int.Parse(S.ReadLine().Split()[0]),m=0,i,j;int[]a={};var s=a.ToList();try{for(i=0;;){j=int.Parse(S.ReadLine());m=i++<M&&j>m?j:m;if(j<=m)s.Add(j);}}catch{}var l=a.ToList();for(i=s.Count;--i>=M;){for(j=i;j>=M;l.Add(s[i]*s[j--]));}l.Sort();for(i=0;i<M;++i,S.WriteLine(j))for(m=0;(j=l[m++]-s[i])<0;);}}



/*
// 5 0.01
using S=System.Console;using System.Text;using System.Linq;
class C{static void Main(){
int M=int.Parse(S.ReadLine().Split()[0]),m=0,i,j;
int[]a={};
var s=a.ToList();
try{for(i=0;;){j=int.Parse(S.ReadLine());m=i++<M&&j>m?j:m;if(j<=m)s.Add(j);}}catch{}
var l=a.ToList();
for(i=s.Count;--i>=M;){for(j=i;j>=M;l.Add(s[i]*s[j--]));}
l.Sort();
var b=new StringBuilder();
for(i=0;i<M;++i){for(m=0;(j=l[m++]-s[i])<0;);b.Append(j.ToString());b.Append("\n");}
S.Write(b.ToString());
}}



using S=System.Console;
using System.Linq;
class C{static void Main(){
int M=int.Parse(S.ReadLine().Split()[0]),m=0,i,j;
int[]a={};
var s=a.ToList();
try{for(i=0;;){j=int.Parse(S.ReadLine());m=i++<M&&j>m?j:m;if(j<=m)s.Add(j);}}catch{}
var l=a.ToList();
for(i=s.Count;--i>=M;){for(j=i;j>=M;l.Add(s[i]*s[j--]));}
l.Sort();
for(i=0;i<M;++i,S.Write(j+"\n"))for(m=0;(j=l[m++]-s[i])<0;);
}}


using S=System.Console;
using System.IO;
using System.Linq;
class C{static void Main(){
int M=int.Parse(S.ReadLine().Split()[0]),m=0,i,j;
int[]a={};
var s=a.ToList();
try{for(i=0;;){j=int.Parse(S.ReadLine());m=i++<M&&j>m?j:m;if(j<=m)s.Add(j);}}catch{}
var l=a.ToList();
for(i=s.Count;--i>=M;){for(j=i;j>=M;l.Add(s[i]*s[j--]));}
l.Sort();
var sw = new StreamWriter(S.OpenStandardOutput()){AutoFlush = false};
S.SetOut(sw);
for(i=0;i<M;++i){for(m=0;(j=l[m++]-s[i])<0;);S.WriteLine(j);}
S.Out.Flush();
}}



using S=System.Console;
using System.Linq;
class C{static void Main(){
int M=int.Parse(S.ReadLine().Split()[0]),m=0,i,j;
int[]a={};
var s=a.ToList();
try{for(i=0;;){j=int.Parse(S.ReadLine());m=i++<M&&j>m?j:m;if(j<=m)s.Add(j);}}catch{}
var l=a.ToList();
for(i=s.Count;--i>=M;){for(j=i;j>=M;l.Add(s[i]*s[j--]));}
l.Sort();
for(i=0;i<M;++i){for(m=0;(j=l[m++]-s[i])<0;);S.Write(j+"\n");}
}}




*/

/*
using S=System.Console;
using System.Linq;
class C{static void Main(){
int M,m=0,i,j;
var y=S.ReadLine().Split().Select(x => int.Parse(x)).ToList();
M=y[0];
int[]a={};
var s=a.ToList();
for(i=M+y[1];i-->0;s.Add(int.Parse(S.ReadLine())));
var l=a.ToList();
for(i=s.Count;i-->M;){for(j=i;j>M;l.Add(s[i]*s[j--]));}
l.Sort();
for(i=0;i<M;){for(m=0,j=s[i++];l[m]<j;++m);S.WriteLine(l[m]-j);}
}}
*/




// [9, 15, 18, 21, 25, 30, 35, 36, 42, 49]
/*



using S=System.Console;class C{static void Main(){
int M,N,m=0,i=0,j,t,c=0;
var y=S.ReadLine().Split();
var s=new int[2000];
for(M=t=int.Parse(y[0]);i<M;s[i++]=j=int.Parse(S.ReadLine()),m=j>m?j:m){}
for(N=int.Parse(y[1]);N-->0;){j=int.Parse(S.ReadLine());if(j<m)s[t++]=j;}
var l=new System.Collections.Generic.List<int>();
for(;i<t;++i){for(j=i;j<t;l.Add(s[i]*s[j++])){}}
l.Sort();
var a=new int[m*m];
foreach(var k in l){for(j=0;j<k-c;a[c+j++]=k){}c+=k-c;}
for(i=0;i<M;S.WriteLine(a[s[i]-1]-s[i++])){}
}}










using S=System.Console;
using System.Collections.Generic;
class C{static void Main(){
int M,N,m=0,i=0,j,t;
var y=S.ReadLine().Split();
var s=new int[2000];
var l=new List<int>();
for(M=t=int.Parse(y[0]);i<M;l.Add(s[i++]=j=int.Parse(S.ReadLine())),m=j>m?j:m){}
for(N=int.Parse(y[1]);N-->0;){j=int.Parse(S.ReadLine());if(j<m)s[t++]=j;}
for(;i<t;++i){for(j=i;j<t;l.Add(s[i]*s[j++])){}}
l.Sort();
for(i=0;i<M;){S.WriteLine(l[l.BinarySearch(s[i])+1]-s[i++]);}
}}



*/