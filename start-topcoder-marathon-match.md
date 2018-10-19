# TopCoder MarathonMatchの始め方 2018

# 必要な物
[TopCoder](https://www.topcoder.com/)のアカウント  
Java1.8(1.7の方が良いのかな自分は1.8使ってるけど)  
使用する言語環境  

#### TopCoder対応言語
C++ – g++ (GCC) 4.8.1.
Compilation options: /usr/local/gcc48/bin/g++ --std=c++0x -W -Wall -Wno-sign-compare -O2 -s -pipe -mmmx -msse -msse2 -msse3  
Java – java version "1.7.0_17"  
Python – Python 2.6.6  
C# – .NET Framework 4.0, Microsoft (R) Visual C# 2010 Compiler version 4.0.30319.1  
VB – .NET Framework 4.0, Microsoft (R) Visual Basic Compiler version 10.0.30319.233  

#### カレンダー
[Competitive Programming Contests Calendar](https://competitiveprogramming.info/calendar)  

#### マラソンマッチ参加登録
[開催されているマラソンマッチ](https://community.topcoder.com/longcontest/?module=ViewActiveContests)  

#### 参加登録しなくても問題は見ることができる
#### 参加登録しても提出しなければレーティング対象にならない

#### 問題を見たら次にすること
問題ページのどこかにあるリンクから次の３つを入手    
tester.jar  
問題名Vis.java  
問題名.cpp,java,py,cs  

たまに用意されていないことがある  

#### tester.jar
プログラムをテストし結果を確認できる。オプションで視覚化して表示もできるものがある。  

#### ***Vis.java
tester.jarのビルド前のソースファイル、カスタマイズして使っている人もいる。  

#### ***.cpp,java,py,cs
見本。この中のクラスを書き換えて提出する。  

#### ローカルでテストする
c++ならコンパイルして(command)に実行ファイルをを入れる。  
(seed)で指定したテストケースを生成してテストしてくれる。  
java -jar tester.jar -exec "(command)" -seed (seed)  

例  
java -jar tester.jar -exec ”***.exe” -seed 1  
java -jar tester.jar -exec ”python ***.py” -seed 1  
java -jar tester.jar -exec ”py ***.py” -seed 1  
  
注意 windows環境で実行できないときは  
Javaのパス通っているか  
pythonのテストをする場合はpythonのパスが通っているか  
カレントディレクトリがtester.jarやテストファイルのある場所か  
を確認  

#### 時間計測する手段を用意する
Topcoderサーバー上では時間取得関数が非常に遅い  
http://topcoder.g.hatena.ne.jp/CKomaki/20141202/1418158488

遅いけど簡単に使える時間計測  
https://github.com/ebi-cp/docs/blob/master/snippets/stopwatch.cpp

#### 簡単にマルチスレッドでテストしたい
https://github.com/ebicochineal/marathon_match/tree/master/topcoder_mm_template

#### マラソンマッチキュー
誰かが提出すると[ここ](https://community.topcoder.com/longcontest/?module=ViewQueue)に表示される。空いてるときに提出しないと結果がすぐ帰ってこない。  
システムテストの時もここに表示される。

#### システムテスト
最終テスト大体2000件  

#### レーティング確認
システムテスト終了後。半日～1週間で結果が出てレーティングが反映される  

- TopCoder Arena(Java)  
- `https://community.topcoder.com/tc?module=SimpleStats&c=long_comp_history&d1=statistics&d2=longHistory&cr=自分の数字プロフィールへのリンクなどから入手`  
- [TopCoder CoderRank](https://community.topcoder.com/longcontest/stats/?&sr=1&nr=50&module=CoderRank)
- プロフィール　一番反映が遅い

#### マラソンマッチの練習がしたい
[Practice Contests](https://community.topcoder.com/longcontest/?module=ViewPractice)


