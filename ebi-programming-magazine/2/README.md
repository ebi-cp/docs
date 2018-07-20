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

---

- #### コメント  
```#```から後ろの文字はコメントとして無視されます。

---

- #### 条件分岐 if文  
```py
if 条件式:
    条件式の結果がTrueの時の処理

if 条件式:
    条件式の結果がTrueの時の処理
else:
    条件式の結果がFalseの時の処理


if 条件式1:
    条件式1の結果がTrueの時の処理
else if 条件式2:
    条件式1でFalseで条件式2の結果がTrueの時の処理
else:
    すべての条件式の結果がFalseの時の処理


if 条件式1 and 条件式2:
    条件式1と2の結果がTrueの時の処理

if 条件式1 or 条件式2:
    条件式1か2の結果がTrueの時の処理
```
---

- #### 繰り返し while文  
```py
while 条件式:
    条件式の結果がTrueの時の処理

cnt = 0
while cnt < 3:
    print(cnt)
    cnt += 1
# 0
# 1
# 2


while True:
    常に式がTrueのため無限ループになる

cnt = 0
while True:
    if cnt = 3:# cntが3ならループを抜ける
        break
    print(cnt)
    cnt += 1
# 0
# 1
# 2
```

---

- #### 繰り返し for文  
```python
for 値を受け取る変数 in range(3):
    処理
# 0
# 1
# 2

for i in range(3):
    print(i)
# 0
# 1
# 2

for i in [0, 1, 2]:
    print(i)
# 0
# 1
# 2


for i in 'abc':
    print(i)
# a
# b
# c
```
---

- #### continue文, break文
```py
for i in range(3):
    if i == 1 : continue
    print(i)
# 0
# 2

for i in range(3):
    if i == 1 : break
    print(i)
# 0
```
---

- #### pythonの文の有効範囲  
```python
if 条件式:処理 この行だけ有効 処理を2つ書くなら;を使う

if 条件式:処理;処理;処理

if 条件式:  
    インデントすると複数行有効  
    ...
    ...
    ...

if 条件式:  
  インデントすると複数行有効  
  ...
  ...
  ...
```
#### インデント  
多くのテキストエディタではtabキーでできます。  
インデントを消すにはshift+tabキー  
複数行選択してもできます。  
tab文字かスペース4かスペース2かなどはテキストエディタの設定で変更できます。  



---