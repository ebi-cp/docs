## 競技プログラミングとゴルフ

[AtCoderの始め方](https://github.com/ebi-cp/docs/blob/master/start-atcoder.md)  

ABCのA問題は非常に簡単です。  
[ABC100a](https://abc100.contest.atcoder.jp/tasks/abc100_a)

１６等分されたケーキがあって二人でそのケーキを取る、隣り合ったものを取ってはいけない、それぞれA切れとB切れ取ることができるか？できるなら```Yay!```と出力、できないなら```:(```を出力しろという問題。  

```py
#! /usr/bin/env python3

A, B = map(int, input().split())
if A <= 8 and B <= 8:
    print('Yay!')
else:
    print(':(')
```
1つ飛ばしに取るとして最大で８切れまでしか取れないので、AとBが８以下かどうか判定するだけで解けてしまいます。  

コードゴルフすることでプログラミング言語の理解深めつつA問題でも楽しむことができるかもしれません。


ABC100aゴルフすると  
```
A,B=map(int,input().split());print(['Yay!',':('][A>8or B>8])
```
60byte  
解説  
- 削ることができるスペースを削り;で改行を削ります。

- さらにif文を削るためにリストを使います。  
式```A>8or B>8```の結果が```True```となれば```1```と同じなので```:(```が選ばれ出力されます。  
ゴルフ前はどちらも８以下なら```Yay!```としていましたがandよりorのが短いためどちらかが８より大きいなら```:(```とします。  

この問題はさらに削ることができます。  

```
s=input();print(['Yay!',':('][len(s)>3or'9'in s])
```
49byte  
解説
- ```len(s)>3```  
どちらも８以下でなければならないなら文字列の長さは３になるはずです。なので３より大きいなら```:(```です。  
- ```'9'in s```  
長さ３の文字列のうち条件を満たさないのは９を含む文字列です。なのでこれも```:(```です。  

[ABC100a order_by=source_length Python](https://abc100.contest.atcoder.jp/submissions/all/1?order_by=source_length&task_screen_name=abc100_a&language_screen_name=python3_3.4.3&status=AC)


























