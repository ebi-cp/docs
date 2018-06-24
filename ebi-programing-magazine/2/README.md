## 実技で学ぶPython3 海老もえぎの配信状況を知ろう  
moegi_live.pyなどで保存すれば動きます  

- 0 prev 前の状態を記録する変数を宣言
- 1 URLにアクセスしHTMLを取得
- 2 HTMLの中に文字列status: 'LIVE'が含まれるか調べるその状態を記録
- 3 前のループで配信していない　かつ　配信中 -> 配信開始 と表示
- 4 前のループで配信中　かつ　配信中 -> 配信中 と表示
- 5 前のループで配信していない　かつ　配信していない -> 配信していません と表示
- 6 前のループで配信中　かつ　配信していない -> 配信終了 と表示
- 7 今の状態を覚えておくprevに入れる
- 8 １０分待って1に戻る
```py
#!/usr/bin/python3
import time    # time.sleepを使うために必要
import urllib.request    # URLを開くために必要
prev = False
while True:    # 繰り返し
    u = urllib.request.urlopen('https://www.cavelis.net/live/yuh_')    # urlを開く
    r = u.read().decode('utf-8')    # 読んでutf-8でデコード 文字列になる
    islive = "status: 'LIVE'" in r    # rの文字列の中にstatus: 'LIVE'の文字列が含まれるか(真)True (偽)False
    if prev == False and islive == True:    # 前のループで配信していない　かつ　配信中
        print('配信開始')
    if prev == True and islive == True:    # 前のループで配信中　かつ　配信中
        print('配信中')
    if prev == False and islive == False:    # 前のループで配信していない　かつ　配信していない
        print('配信していません')
    if prev == True and islive == False:    # 前のループで配信中　かつ　配信していない
        print('配信終了')
    prev = islive    # 今の状態を覚えておく
    time.sleep(60 * 10)    # 秒 10分待つ 待たないとF5連打とかわらない
```
真 True, 偽 False   条件分岐などで計算結果が真となれば実行される  
n >= 0   if文に使えばnが0以上なら真(True)次の文が実行される。ループ文なら0以上ならずっと繰り返される。  
while True:   無限ループ  
  
条件分岐if文や繰り返しwhile文  
pythonの文の有効範囲  
```python
if 条件式:文 この行だけ有効 文を2つ書くなら;を使う

if 条件式:文;文;文

if 条件式:  
    字下げをすると  
    複数行有効  
```