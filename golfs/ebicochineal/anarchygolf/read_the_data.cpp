#import<iostream>
using namespace std;main(){string s="[",t;int i,j;for(cin>>i;cin>>j;s+=(--i>0?"], ":"]")){s+="[";for(;j-->0;){cin>>t;s+=t+(j>0?", ":"");}}cout<<s+"]";}

/*
#include <iostream>
using namespace std;
main(){
    string s="[",t;int i,j;
    for(cin>>i;i-->0;s+=(i>0?"], ":"]")){s+="[";
        for(cin>>j;j-->0;){cin>>t;
        s+=t+(j>0?", ":"");
        }
    }
    cout<<s+"]";
}

#import<iostream>
using namespace std;main(){string s="[",t;int i,j;for(cin>>i;cin>>j;s+=(--i>0?"], ":"]")){s+="[";for(;j-->0;){cin>>t;s+=t+(j>0?", ":"");}}cout<<s+"]";}

#import<iostream>
using namespace std;main(){string s="[",t;int i,j;for(cin>>i;i-->0;s+=(i>0?"], ":"]")){s+="[";for(cin>>j;j-->0;){cin>>t;s+=t+(j>0?", ":"");}}cout<<s+"]";}


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