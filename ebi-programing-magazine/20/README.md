## ピクチャークロスワードパズルを作ろう


```pixファイル```テキストファイルの拡張子をpixに変えた物、縦横長さ同じにしないとだめ  

海老のピクロスファイル。元の形を知らないとかなり難しいかも。  
```ebi.pix```
```txt
0000000000000000
0000000000000000
0000000000000000
0000000000000000
0000000000000000
0000000000000000
0000000000000000
0000000111100000
0000011000011000
0000100000000000
0111111111110000
0001101111111100
0000011110111110
0000100101010110
0001001010101100
0001001000011000
```

#### pixクラス  
- size ピクロスの縦横のサイズ
- nsize 数字エリアのサイズ
- cvsize 縦横のサイズと数字エリアのサイズから計算したキャンバスのサイズ
- __row_str n行目を返す  
- __row_str 各行のn列目にアクセスして文字列を作りをn列目返す  
- __to_nums  
```'00011001'```の文字列をsplitで```['', '', '', '11', '', '1']```に  
リスト内法表記とifを使ったfilterと要素に対しlenを使うことで[2, 1]に変換  
- __init_ans 集合self.ansの初期化 1の座標にnsizeと加えたものを追加していく



```piX.py```
```py
#! /usr/bin/env python3
import os
import tkinter
import tkinter.filedialog

class pix:
    def __init__(self, filename, cellsize, maxsize = 32):
        with open(filename, 'r') as f : reads = f.readlines()
        self.data = [i.strip()[:maxsize] for i in reads[:maxsize]]
        self.size = len(self.data)
        self.nsize = len(self.data) // 2 + len(self.data) % 2
        self.cvsize = (self.nsize + self.size) * cellsize
        self.rows = [self.__to_nums(self.__row_str(x)) for x in range(self.size)]
        self.cols = [self.__to_nums(self.__col_str(x)) for x in range(self.size)]
        self.__init_ans()
    def __row_str(self, n) : return ''.join(self.data[n])
    def __col_str(self, n): return ''.join([x[n] for x in self.data])
    def __to_nums(self, s) : return [len(x) for x in s.split('0') if x]
    def __init_ans(self):
        self.ans = set()
        for y in range(self.size):
            for x in range(self.size):
                if self.data[y][x] == '1' : self.ans.add((x+self.nsize, y+self.nsize))

def background():    # 線や数字を描く
    s, e = 2, m + p.cvsize
    for x in range(p.nsize, p.nsize + p.size):    # 横線
        cv.create_line(m + size * x, s, m + size * x, e, tag = 'bg')
    for y in range(p.nsize, p.nsize + p.size):    # 縦線
        cv.create_line(s, m + size * y, e, m + size * y, tag = 'bg')
    cv.create_rectangle(s, s, e, e, tag = 'bg')    # 外枠
    s = m + size // 2    # 端のセルの中心座標
    for i in range(p.size):
        py = s + size * p.nsize + size * i
        sx = s + size * (p.nsize - len(p.rows[i]))
        for j in range(len(p.rows[i])):
            cv.create_text(sx + size * j, py, text = p.rows[i][j], tag = 'bg')
    for i in range(p.size):
        px = s + size * p.nsize + size * i
        sy = s + size * (p.nsize - len(p.cols[i]))
        for j in range(len(p.cols[i])):
            cv.create_text(px, sy + size * j, text = p.cols[i][j], tag = 'bg')
def draw():
    cv.delete('cells')
    for x, y in l:    # lのposを塗りつぶす
        rx, ry = x*size+m, y*size+m
        cv.create_rectangle(rx, ry, rx+size-1, ry+size-1, fill = 'black', tags = 'cells')
    if p.ans == l:    # 完成していたらbgを消してrを描かずにここでreturn
        cv.delete('bg')
        return
    for x, y in r:    # rのposに×を描く
        rx, ry = x*size+m, y*size+m
        cv.create_line(rx, ry, rx+size, ry+size, tags = 'cells')
        cv.create_line(rx, ry+size, rx+size, ry, tags = 'cells')
def leftdown(e) : mousedown(e, l, r)    # 塗りつぶすpos追加削除
def rightdown(e) : mousedown(e, r, l)    # ×を描くpos追加削除
def mousedown(e, a, b):
    k = ((e.x-m) // size, (e.y-m) // size)
    if k[0] < p.nsize or k[1] < p.nsize or p.ans == l : return
    if k in b : b.remove(k)    # k座標がb集合に含まれるなら取り除く
    if k in a:
        a.remove(k)
    else:
        a.add(k)
    draw()

l = set()    # 塗りつぶすpos 答えと比較する
r = set()    # ×を描くpos
size = 16    # セルサイズ
m = 2    # margin
root = tkinter.Tk()
dirpath = os.path.dirname(__file__).replace('\\', '/')
filetype = (('pix files', '*.pix'),)
root.filename = tkinter.filedialog.askopenfilename(initialdir = dirpath, filetypes = filetype)
p = pix(root.filename, size)
cv = tkinter.Canvas(root, width = p.cvsize+1, height = p.cvsize+1)
cv.pack()
background()
root.bind('<Button-1>', leftdown)
root.bind('<Button-3>', rightdown)
root.mainloop()
```


![Gif](https://raw.githubusercontent.com/ebi-cp/docs/master/ebi-programing-magazine/20/pix.gif)