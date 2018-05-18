// using S=System.Console;
// class P{
//     static void Main(){
//         var s="[";int i=2,j=0,n,b=0;
//         for(;i-->0;--j){
//             var t=S.ReadLine();n=int.Parse(t);
//             if(b>0){j+=n;b=0;s+="[";}
//             if(j<1){i+=n;b=1;s+="[";}
//             s+=(j>0?t+(j>1?", ":""):"");
//         }
//         S.Write(s+"]");
//     }
// }

/*
using static System.Console;class P{static void Main(){var s="[";int i=int.Parse(ReadLine()),j;for(;i-->0;s+=i>0?"], ":"]")for(s+="[",j=int.Parse(ReadLine());j-->0;)s+=ReadLine()+(j>0?", ":"");Write(s+"]");}}
*/

/*213
using S=System.Console;class P{static void Main(){var s="[";int i=int.Parse(S.ReadLine()),j;for(;i-->0;s+=i>0?"], ":"]"){s+="[";for(j=int.Parse(S.ReadLine());j-->0;)s+=S.ReadLine()+(j>0?", ":"");}S.Write(s+"]");}}

using S=System.Console;class P{static int f()=>int.Parse(S.ReadLine());static void Main(){var s="[";int i=f(),j;for(;i-->0;s+=i>0?"], ":"]"){s+="[";for(j=f();j-->0;)s+=$"{f()}"+(j>0?", ":"");}S.Write(s+"]");}}


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


using S=System.Console;
class P{
    static void Main(){
        var s="[";int i,j;
        for(i=int.Parse(S.ReadLine());i-->0;s+=(i>0?"], ":"]")){s+="[";
            for(j=int.Parse(S.ReadLine());j-->0;){
            s+=S.ReadLine()+(j>0?", ":"");
            }
        }
        S.Write(s+"]");
    }
}
*/