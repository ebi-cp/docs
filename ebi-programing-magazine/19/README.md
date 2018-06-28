## ライフゲーム解説

[8 実技で学ぶPython3 ライフゲームを作る](https://github.com/ebi-cp/docs/blob/master/ebi-programing-magazine/8/README.md)の解説  


#### [wikipedia](https://ja.wikipedia.org/wiki/%E3%83%A9%E3%82%A4%E3%83%95%E3%82%B2%E3%83%BC%E3%83%A0)より
- 誕生 死んでいるセルに隣接する生きたセルがちょうど3つあれば、次の世代が誕生する。
- 生存 生きているセルに隣接する生きたセルが2つか3つならば、次の世代でも生存する。
- 過疎 生きているセルに隣接する生きたセルが1つ以下ならば、過疎により死滅する。
- 過密 生きているセルに隣接する生きたセルが4つ以上ならば、過密により死滅する。



```python
#! /usr/bin/env python3
import tkinter
グローバル変数
def draw():
    画面に描画
def leftdown(e):
    左クリックイベント　セルの追加削除
def rightdown(e):
    右クリックイベント　再生
def update():
    更新再生
tkinterウィンドウの作成
```
---

#### draw
生きたセルを画面に描画します
- 生きたセルはalive変数に入っていますsetがたで(x, y)の座標が生きたセルの数だけ入っています。
- ２回目呼ばれたら前のセルが残っているので削除します。cv.delete('cells')  
１回目呼ばれたときでもcv.delete('cells')で削除していますが、cellsタグの付いたrectangleは存在しないので何もしません。
- for x, y in alive:  
ループを回します生きたセルが{(0, 1), (2, 3)}の２つだった場合1回目のループではxに0,yに1。2回目のループではxに2,yに3が入ります。
- 大きさが８のセルなのでrx, ry= x*8+2, y*8+2で８倍し、少しずれて描画されてしまうので＋２にしています。
- cv.create_rectangleでcellcolor色で描画します。
‐ cvはキャンバスの情報が入っています  
このスクリプトの下の方でキャンバスを作成しています。  
cv = tkinter.Canvas(root, width = 512, height = 512)  
cv.pack()でウィンドウに配置しています。  
```py
def draw():
    cv.delete('cells')
    for x, y in alive:
        rx, ry= x*8+2, y*8+2
        cv.create_rectangle(rx, ry, rx+7, ry+7, fill = cellcolor, tag = 'cells')
```
---

#### leftdown
マウス左が押されたときに呼ばれる関数です。  
停止  
カーソル位置の座標のセルを置くまたは削除。  

- eからマウスの情報が取得できます。  
- if rid : root.after_cancel(rid)  
右クリックで再生する時は100msおきに再生するのですが、左クリックでセルを置いたり消したりするときは再生を止めなくてはならないのでridに登録されている予約を取り消します。
- k = ((e.x-2) // 8, (e.y-2) // 8)  
-2は先ほどのずれている座標のためこちらでもずらします。// 8で割り算をします/なら小数に、//なら整数になります。512ピクセルの座標が8ピクセルごとの0~31までの数値になります。
- if k in alive:
kに入れた座標がalive生きたセルの中に含まれるなら取り除き、無いなら追加します。左クリックを押したときの動作がその場所に無いならセルを置き、あるなら取り除くとしているためです。
- aliveの情報を更新しただけなので、このままでは画面に反映されないので最後に１度だけdrawを呼びます。

```py
def leftdown(e):
    if rid : root.after_cancel(rid)
    k = ((e.x-2) // 8, (e.y-2) // 8)
    if k in alive:
        alive.remove(k)
    else:
        alive.add(k)
    draw()
```
---

#### rightdown
マウス右が押されたときに呼ばれる関数です。  
再生
- if rid : root.after_cancel(rid)  
左クリックの時と同じくキャンセルします。キャンセルしないと２重に呼ばれてしまい、右クリックするたびに再生が早くなってしまいます。
- updateを呼び再生します
```py
def rightdown(e):
    if rid : root.after_cancel(rid)
    update()
```
---

#### update
状態を更新し100ms後に自信を呼ぶように予約する。  
状態の更新  
drawの呼び出し  
自身を呼び出すための予約  
- global rid  
ridは外側の変数でアクセスするには特に何もいりませんが、書き込むにはglobalと書かなければなりません。
- m = dict()  
辞書です。ここでは｛座標（キー）：セルの数（値）｝を記録して行きます。
- for sx, sy in alive:  
aliveの生きたセルの周辺の座標に順番にアクセスして値を＋１していきます。（周辺と中心を含む９つの座標に＋１します）  
for dx, dy in d:でxの-1~1,yの-1~1を＋して座標を少しずらし周辺の座標に順番にアクセスします。
- if t in m:  
座標がまだ辞書に無いなら最初の値１を、あるなら＋１します。
- for k, v in m.items():  
隣接する生きたセルがちょうど3つあれば、次の世代が誕生する。  
ので、3つカウントされている座標のセルをaliveに追加します。
- for i in list(alive):  
今生きているセルの座標に順にアクセスしていき、多すぎるセル、少なすぎるセル、画面外の離れすぎたセルをaliveから削除します。
- drawを呼び画面を更新します。
- rid = root.after(100, update)  
自身を呼ぶ予約をしidをridに入れます。

```py
def update():
    global rid
    m = dict()
    for sx, sy in alive:
        for dx, dy in d:
            t = (sx+dx, sy+dy)
            if t in m:
                m[t] += 1
            else:
                m[t] = 1
    for k, v in m.items():
        if v == 3 : alive.add(k)
    for i in list(alive):
        a = m[i] < 3 or m[i] > 4
        x = abs(i[0]-32) > 64
        y = abs(i[1]-32) > 64
        if a or x or y : alive.remove(i)
    draw()
    rid = root.after(100, update)
```
---

#### tkinter
ウィンドウの作成  
キャンバスの作成  
キャンバスの配置  
クリックイベントの登録  
メインループ  
```py
root = tkinter.Tk()
cv = tkinter.Canvas(root, width = 512, height = 512)
cv.pack()
root.bind('<Button-1>', leftdown)
root.bind('<Button-3>', rightdown)
root.mainloop()
```

---

全体のコードです。  
コピペするだけで動くのでPython3をインストールしぜひ試してみてください。  

```lifegame.py```
```python
#! /usr/bin/env python3
import tkinter
cellcolor = '#c82c55'
d = [(x, y) for x in [-1, 0, 1] for y in [-1, 0, 1]]
alive = set()
rid = None
def draw():
    cv.delete('cells')
    for x, y in alive:
        rx, ry= x*8+2, y*8+2
        cv.create_rectangle(rx, ry, rx+7, ry+7, fill = cellcolor, tag = 'cells')
def leftdown(e):
    if rid : root.after_cancel(rid)
    k = ((e.x-2) // 8, (e.y-2) // 8)
    if k in alive:
        alive.remove(k)
    else:
        alive.add(k)
    draw()
def rightdown(e):
    if rid : root.after_cancel(rid)
    update()
def update():
    global rid
    m = dict()
    for sx, sy in alive:
        for dx, dy in d:
            t = (sx+dx, sy+dy)
            if t in m:
                m[t] += 1
            else:
                m[t] = 1
    for k, v in m.items():
        if v == 3 : alive.add(k)
    for i in list(alive):
        a = m[i] < 3 or m[i] > 4
        x = abs(i[0]-32) > 64
        y = abs(i[1]-32) > 64
        if a or x or y : alive.remove(i)
    draw()
    rid = root.after(100, update)
root = tkinter.Tk()
cv = tkinter.Canvas(root, width = 512, height = 512)
cv.pack()
root.bind('<Button-1>', leftdown)
root.bind('<Button-3>', rightdown)
root.mainloop()
```
---


![Gif](https://raw.githubusercontent.com/ebi-cp/docs/master/ebi-programing-magazine/19/lifegame.gif)