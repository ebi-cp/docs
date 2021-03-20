# TopCoder MarathonMatchの始め方

# 必要な物
[TopCoder](https://www.topcoder.com/)のアカウント  
Java1.8  
使用する言語環境  

#### TopCoder対応言語
C++, Java, Python2, C#, VB  
[Processing Server Specifications](https://apps.topcoder.com/wiki/display/tc/Processing+Server+Specifications)

#### カレンダー
[Community - Events](https://www.topcoder.com/community/events/)  
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
tester.jarのビルド前のソースファイル。  

#### ***.cpp,java,py,cs
見本。この中のクラスを実装して提出する。  

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

#### フォーラムを確認する
開始時はテスターのバグが結構あるので確認する  

#### 時間計測する手段を用意する
Topcoderサーバー上では時間取得関数が非常に遅い  
http://topcoder.g.hatena.ne.jp/CKomaki/20141202/1418158488

遅いけど簡単に使える時間計測  
https://github.com/ebi-cp/docs/blob/master/snippets/stopwatch.cpp

#### 簡単にマルチスレッドでテストしたい
https://github.com/ebicochineal/marathon_match/tree/master/marathon_contest_template_v2

#### マラソンマッチキュー
誰かが提出すると[ここ](https://community.topcoder.com/longcontest/?module=ViewQueue)に表示される。空いてるときに提出しないと結果がすぐ帰ってこない。  
システムテストの時もここに表示される。

#### システムテスト
最終テスト大体1000~2000件  

#### レーティング確認
システムテスト終了後。半日～1週間で結果が出てレーティングが反映される  

- TopCoder Arena(Java)  
- `https://community.topcoder.com/tc?module=SimpleStats&c=long_comp_history&d1=statistics&d2=longHistory&cr=自分の数字プロフィールへのリンクなどから入手`  
- [TopCoder CoderRank](https://community.topcoder.com/longcontest/stats/?&sr=1&nr=50&module=CoderRank)
- プロフィール　一番反映が遅い

#### マラソンマッチの練習がしたい
[Practice Contests](https://community.topcoder.com/longcontest/?module=ViewPractice)

#### ビジュアライザをGIFで撮りたい
ScreenToGif  

#### リンク
[焼きなまし法のコツ Ver. 1.2](http://shindannin.hatenadiary.com/entry/20121224/1356364040)  
[マラソンマッチにおける精神論](http://chokudai.hatenablog.com/entry/2014/12/04/000132)  
[マラソンマッチで最初の12時間にすべきこと](http://hama-du.hatenablog.com/entry/2015/12/14/000000)  
[Topcoderマラソンマッチの探索問題で重要なこと](https://qiita.com/takapt0226/items/b2f6d1d77a034b529e21)  
[競プロ解法紹介～レベル別マラソンの戦い方～](https://qiita.com/tsukammo/items/7041a00e429f9f5ac4ae)  
[競プロ解法紹介～大局観で高得点を取る！～](https://qiita.com/tsukammo/items/85ffbe907e89b051d715)  
[競技プログラミングにおいて焼きなまし法に堕ちずに落とすコツ](https://qiita.com/tsukammo/items/b410f3202372fe87c919)  

----
#### MM110から新プラットフォームに移行しました
- ソースコードの提出ではなくソースファイルとshファイルをzipでまとめた物を提出するようになった。ファイルはフォルダに入れてから圧縮したものを提出すると失敗するのでファイルを複数選択したものを圧縮してまとめる。(TCO19 MM Round2からソースファイルのみになった。ソースファイルをzipファイルに圧縮して提出)
- 提出後順位表に反映されるまで数十分かかる。
- 提出すると[ここ](https://submission-review.topcoder.com/)から提出ファイルやエラーメッセージなどがダウンロードできる。
- マラソンマッチのQueue Statusを確認することできなくなった。
- Python3になった。
- 時間計測が遅い問題が無くなった。

[Topcoder Marathon Matchの始め方（最新版）](https://qiita.com/phocom/items/da0f8123f7a8d5201cbf)  
[Marathon Match Discussion](https://apps.topcoder.com/forums/?module=ThreadList&forumID=506048&mc=3073)  
[新プラットフォームに移行したMM110のフォーラム１](https://apps.topcoder.com/forums/?module=ThreadList&forumID=7120)  
[新プラットフォームに移行したMM110のフォーラム２](https://apps.topcoder.com/forums/?module=ThreadList&forumID=673710)  
[MM わくわく新プラットフォームまとめ](http://hakomof.hatenablog.com/entry/2019/06/05/214722)  

[練習マッチ VanishingMaze  ](https://www.topcoder.com/challenges/30092483)  
[順位表](http://leaderboards.topcoder.com/challenges/30091712?reviewTypeId=0d5b13d6-7562-4045-af35-d6a5cf62de31)  

[練習マッチ TCO19 Marathon Match Round 1](https://www.topcoder.com/challenges/30092166)  
[順位表](http://cmap-leaders.topcoder.com/challenges/30092166?reviewTypeId=0d5b13d6-7562-4045-af35-d6a5cf62de31)  

---
## 海老競プロ部リンク
- [トップ](https://github.com/ebi-cp/docs/blob/master/README.md)
- [TopCoder MarathonMatchの始め方](https://github.com/ebi-cp/docs/blob/master/start-topcoder-marathon-match.md)
- [TCO18 MM R1 - RoadsAndJunctions](https://github.com/ebi-cp/docs/blob/master/TopCoderMM/RoadsAndJunctions.md)
- [AtCoderの始め方](https://github.com/ebi-cp/docs/blob/master/start-atcoder.md)
- [闇Python入門](https://github.com/ebi-cp/docs/blob/master/dark-pythonista.md)
- [海老ライブラリ](https://github.com/ebi-cp/docs/tree/master/library)
- [海老バーチャルコンテスト](https://github.com/ebi-cp/docs/blob/master/ebi-virtual-contest.md)
- [ゴルフコード置き場](https://github.com/ebi-cp/golf)
- [VB.netでACしてみた](https://github.com/ebi-cp/vb/tree/master/ebicochineal)
---
