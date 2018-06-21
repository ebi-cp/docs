## 実技で学ぶPython3 ライフゲームを作る 矩形選択(追加､削除)


１つずつ置くのはしんどいので一気に追加できるように改良しましょう。  

左クリックで 時間止める セル追加削除  
左ドラッグで セル矩形追加削除(開始地点に無いなら追加、あるなら削除)  
右クリックで 再生  

```python
#! /usr/bin/env python3
import tkinter
cellcolor = '#c82c55'    # cochinealred
d = [(x, y) for x in [-1, 0, 1] for y in [-1, 0, 1]]    # 周辺と中心の座標
alive = set()
rid = None
start_pos = (0, 0)    # 左ドラッグ開始地点
def draw():
    cv.delete('cells')
    for x, y in alive:
        rx, ry= x*8+2, y*8+2
        cv.create_rectangle(rx, ry, rx+7, ry+7, fill = cellcolor, tag = 'cells')
def leftdown(e):
    global start_pos
    if rid : root.after_cancel(rid)
    k = ((e.x-2) // 8, (e.y-2) // 8)
    start_pos = k    # 左ドラッグ開始地点
def leftup(e):
    k = ((e.x-2) // 8, (e.y-2) // 8)
    s = start_pos
    sx, ex = min(s[0], k[0]), max(s[0], k[0])    # rangeでexまで+1して行くので小さい方をsx大きい方をex
    sy, ey = min(s[1], k[1]), max(s[1], k[1])
    mode = (s[0], s[1]) in alive    # マウス左が押された地点に生きたセルがあったか無かったか
    for x in range(sx, ex + 1):
        for y in range(sy, ey + 1):
            if mode:    # 削除
                if (x, y) in alive : alive.remove((x, y))    # 集合の中にないものを消そうとするとエラーになるのであるか確かめる
            else:    # 追加
                alive.add((x, y))
                
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
root.bind('<ButtonRelease-1>', leftup)    # マウス左がリリースされたときに呼ぶ関数を登録
root.bind('<Button-3>', rightdown)
root.mainloop()
```

![Gif](https://raw.githubusercontent.com/ebi-cp/docs/master/ebi-programing-magazine/9/lifegame2.gif)


---
