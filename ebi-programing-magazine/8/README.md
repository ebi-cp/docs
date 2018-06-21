## 実技で学ぶPython3 ライフゲームを作る

#### [wikipedia](https://ja.wikipedia.org/wiki/%E3%83%A9%E3%82%A4%E3%83%95%E3%82%B2%E3%83%BC%E3%83%A0)より
- 誕生 死んでいるセルに隣接する生きたセルがちょうど3つあれば、次の世代が誕生する。
- 生存 生きているセルに隣接する生きたセルが2つか3つならば、次の世代でも生存する。
- 過疎 生きているセルに隣接する生きたセルが1つ以下ならば、過疎により死滅する。
- 過密 生きているセルに隣接する生きたセルが4つ以上ならば、過密により死滅する。


左クリックで 時間止める セル追加削除  
右クリックで 再生  


```python
#! /usr/bin/env python3
import tkinter
cellcolor = '#c82c55'    # cochinealred
d = [(x, y) for x in [-1, 0, 1] for y in [-1, 0, 1]]    # 周辺と中心の座標
alive = set()
rid = None
def draw():    # 集合aliveのすべてのセルを描画します
    cv.delete('cells')    # 前のセルが残っているので消します
    for x, y in alive:
        rx, ry= x*8+2, y*8+2    # セルの大きさが8なので8倍し2ピクセルずれるのでずらします
        cv.create_rectangle(rx, ry, rx+7, ry+7, fill = cellcolor, tag = 'cells')
def leftdown(e):
    if rid : root.after_cancel(rid)    # 再生中かもしれないのでその場合はキャンセルします
    k = ((e.x-2) // 8, (e.y-2) // 8)
    if k in alive:    # aliveに含まれている場合は削除し無いなら追加します
        alive.remove(k)
    else:
        alive.add(k)
    draw()    # 最後にdrawを呼び結果を画面に反映させます
def rightdown(e):
    if rid : root.after_cancel(rid)
    update()
def update():
    global rid
    m = dict()
    for sx, sy in alive:    # 辞書に周辺にいくつ生きたセルがあるか記録する
        for dx, dy in d:
            t = (sx+dx, sy+dy)
            if t in m:
                m[t] += 1
            else:
                m[t] = 1
    for k, v in m.items():    # 生きたセルがちょうど3つあれば、次の世代が誕生する
        if v == 3 : alive.add(k)
    for i in list(alive):    # 死のループ
        a = m[i] < 3 or m[i] > 4    # 過疎、過密による死です
        x = abs(i[0]-32) > 64    # 知りすぎてしまった探検家は殺さなければなりません
        y = abs(i[1]-32) > 64    #
        if a or x or y : alive.remove(i)
    draw()
    rid = root.after(100, update)    # 次のフレーム100ms後にupdateを呼び出します
root = tkinter.Tk()
cv = tkinter.Canvas(root, width = 512, height = 512)
cv.pack()
root.bind('<Button-1>', leftdown)
root.bind('<Button-3>', rightdown)
root.mainloop()
```

![Gif](https://raw.githubusercontent.com/ebi-cp/docs/master/ebi-programing-magazine/8/lifegame.gif)


---
#### 集合 set型
- 要素が重複しない
- 要素が存在するかO(1)調べることができる

#### 辞書 dict型
- 要素が重複しない
- 要素が存在するかO(1)調べることができる
- キーと値がありキーで値にアクセスできるO(1)

リストで要素が存在するか調べるには先頭から順に調べるためO(n)かかります

ここでは要素が重複しないのと(0, 0)のようなタプル型をキーにできて便利なので使っています。  

---

#### シバン文
```
Unix環境でスクリプトを読み込むインタプリタを指定するものですpython2か3かとか、Windows環境でもPythonランチャーのpy.exeで有効なので書くようにすると良いです
#! /usr/bin/env python3

フルパスで指定されているpython3
#! /usr/bin/python3

環境変数のどこかにあるpython3を探す
#! /usr/bin/env python3

Windowsなら
#! python3 だけ書けばいいはずだけど
どの環境でも一番見つけてくれそうな #! /usr/bin/env python3を書いとくと良いかも
何も書かなくても良いけど
```
---