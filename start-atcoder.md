## AtCoderの始め方
[海老レンジャイ](https://github.com/ebi-cp/docs/blob/master/README.md)向けに適当に書いたので間違っているとこもあるかも

#### AtCoderに登録しよう
[AtCoder](https://atcoder.jp/?lang=ja)

#### AtCoder対応言語やバージョン
[https://language-test-201603.contest.atcoder.jp/](https://language-test-201603.contest.atcoder.jp/)

#### プログラミング未経験
アプリのインストールとかネットゲームとか検索とか問題なくできるなら、３日あればプログラミングがなんとかできるレベルにはなると思う  
[闇Python入門](https://github.com/ebi-cp/docs/blob/master/dark-pythonista.md)

#### 多くのコンテストで禁止される行為
2人以上で結託し、解答する行為  
コンテスト中にTwitterなどでネタバレ  

#### 多くのコンテストで許可されている行為
自作ライブラリの使用  
インターネットでの検索  

#### コンテスト
ほぼ毎週 1, 2つのアルゴリズム系コンテスト(１時間～数時間)が開催されている  
マラソンマッチ系(数時間～数週間)の企業コンテストも不定期で開催されている  
#### アルゴリズム系コンテスト
- [AtCoder Beginner Contest](https://atcoder.jp/contests/archive?ratedType=1&category=0&keyword=)(ABC), [ABCクラスのコンテスト](https://atcoder.jp/contests/archive?ratedType=1&category=0&keyword=)  
レーティング変化 ~ 1999  
- [AtCoder Regular Contest](https://atcoder.jp/contests/archive?ratedType=2&category=0&keyword=)(ARC), [ARCクラスのコンテスト](https://atcoder.jp/contests/archive?ratedType=2&category=0&keyword=)  
レーティング変化 ~ 2799  
- [AtCoder Grand Contest](https://atcoder.jp/contests/archive?ratedType=3&category=0&keyword=)([AGC](https://www.youtube.com/watch?v=Xh7Uc486SrM&feature=emb_logo)), [AGCクラスのコンテスト](https://atcoder.jp/contests/archive?ratedType=3&category=0&keyword=)  
レーティング変化 すべて  
天才以外お断りパズルコンテスト  
ABCクラスのCDくらいの難易度から超高難易度の問題が出題される  
#### マラソン系コンテスト
マラソンはまだ公式なレーティングがありません  
[AtCoder Marathon Ranking (Unofficial)](https://tomerun.github.io/atcoder_marathon_ranking/index.html)
- Chokudai Contest(大根)
- RCO日本橋ハーフマラソン  
- HACK TO THE FUTUREコンテスト  
- Hokkaido Univ.& Hitachi New-concept Computing Contest  
- Asprova プログラミングコンテスト  

#### コンテストの流れ
- 準備  
無くても良いけど、ノートとかメモ用紙とか  
スマホでもできるけどプログラムが実行可能なPC  
標準入出力が分からなかったら[ここを見て試しましょう](https://atcoder.jp/contests/practice/tasks/practice_1)

- 登録  
トップページか[AtCoder コンテストページ](https://atcoder.jp/contests/)から登録  
登録していても１回提出するまではレーティングに反映されません
- 開始～提出  
時間になったら問題のページを開きコードが書き終わったら提出(１ファイルまたはコピペで)  
問題ごとに複数テストされすべて正解でAC  
１ケースでも間違うとWA(多くのコンテストでペナルティ５分 ５分遅く提出したのと同じ感じ)  
プログラムの実行時間が遅すぎるとTLE(数秒かかるとか)  
コンパイルエラーCE  
- 終了後  
レーティング更新(数十分～数時間後)

#### サンプルケーステストスクリプト
[atcoder_samplecase_localtest](https://github.com/ebicochineal/atcoder_samplecase_localtest)  
- ここが便利  
入力と出力とプログラムの出力を並べてみることができる  
ブラウザパスを設定していると問題ページを開くことができる  
- とても小さな問題  
login.txtにIDパスを平文で保存(安心と信頼の海老レンジャイ製ソフトウェア)  
Javaとかkotlinは使えません  
正解が複数ある系の問題も使えません  
#### マラソンマッチ用のテストスクリプト
[atcoder_rcomm_template/a](https://github.com/ebicochineal/marathon_match/tree/master/atcoder_rcomm_template/a)  
[atcoder_rcomm_template/interactive](https://github.com/ebicochineal/marathon_match/tree/master/atcoder_rcomm_template/interactive)  
```rco_mm_mtest.py 開始位置 件数```  
```setting.ini```  
テストするソールファイル名  
実行時に追加するパス  
スコア比較大小の設定  
スレッド数  
コンパイルオプション  

#### レーティングについて
１０回は参加しないと低く出ます  
プロフィール->コンテスト成績表からコンテストごとのパフォーマンスを見ると、どれくらいのレーティングに収束するか知ることができます  
#### 色ランク  
赤/虹(金冠) > 赤/虹(銀冠) > 赤 > 橙 > 黄 > 青 > 水 > 緑 > 茶 > 灰 > 無  
虹 好きな色つけられるよってこと  

#### 今の仕事辛い転職したい
[AtCoderJobs](https://jobs.atcoder.jp/)

  
---
## 海老競プロ部リンク
- [トップ](https://github.com/ebi-cp/docs/blob/master/README.md)
- [TopCoder MarathonMatchの始め方](https://github.com/ebi-cp/docs/blob/master/start-topcoder-marathon-match.md)
- [TCO18 MM R1 - RoadsAndJunctions](https://github.com/ebi-cp/docs/blob/master/TopCoderMM/RoadsAndJunctions.md)
- [AtCoderの始め方](https://github.com/ebi-cp/docs/blob/master/start-atcoder.md)
- [闇Python入門](https://github.com/ebi-cp/docs/blob/master/dark-pythonista.md)
- [海老ライブラリ](https://github.com/ebi-cp/docs/tree/master/library)
- [海老バーチャルコンテスト](https://github.com/ebi-cp/docs/blob/master/ebi-virtual-contest.md)
- [海老プログラミングマガジン](https://github.com/ebi-cp/docs/blob/master/ebi-programming-magazine/README.md)
- [ゴルフコード置き場](https://github.com/ebi-cp/golf)
- [VB.netでACしてみた](https://github.com/ebi-cp/vb/tree/master/ebicochineal)
---

