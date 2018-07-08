## ピクチャークロスワードパズルを作ろう

海老のピクロスファイル。  
元の形を知らないとかなり難しいかも。  
テキストファイルの拡張子をpixに変えた物、縦横長さ同じにしないとだめ  

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




```piX.py```
```py
#! /usr/bin/env python3
import os
import tkinter
import tkinter.filedialog

class pix:
    def __init__(self, filename, maxsize = 32):
        with open(filename, 'r') as f : reads = f.readlines()
        self.data = [i.strip()[:maxsize] for i in reads[:maxsize]]
        self.size = len(self.data)
        self.nsize = len(self.data) // 2 + len(self.data) % 2
        self.cvsize = (self.nsize + self.size) * 16
        self.rows = [self.__to_nums(self.__row_str(x))[::-1] for x in range(self.size)]
        self.cols = [self.__to_nums(self.__col_str(x))[::-1] for x in range(self.size)]
        self.__init_ans()
    def __row_str(self, n) : return ''.join(self.data[n])
    def __col_str(self, n): return ''.join([x[n] for x in self.data])
    def __to_nums(self, s) : return [len(x) for x in s.split('0') if x]
    def __init_ans(self):
        self.ans = set()
        for y in range(self.size):
            for x in range(self.size):
                if self.data[y][x] == '1' : self.ans.add((x+self.nsize, y+self.nsize))

def background():
    for x in range(p.nsize, p.nsize + p.size):
        cv.create_line(m + size * x, m, m + size * x, m + p.cvsize, tag = 'bg')
    for y in range(p.nsize, p.nsize + p.size):
        cv.create_line(m, m + size * y, m + p.cvsize, m + size * y, tag = 'bg')
    cv.create_rectangle(m, m, m + p.cvsize, m + p.cvsize, tag = 'bg')
    for i in range(p.size):
        for j in range(len(p.rows[i])):
            py = m + size * p.nsize + size * i + size // 2
            px = m + size * p.nsize - size * j - size // 2
            cv.create_text(px, py, text = p.rows[i][j], tag = 'bg')
    for i in range(p.size):
        for j in range(len(p.cols[i])):
            py = m + size * p.nsize - size * j - size // 2
            px = m + size * p.nsize + size * i + size // 2
            cv.create_text(px, py, text = p.cols[i][j], tag = 'bg')
def draw():
    cv.delete('cells')
    for x, y in l:
        rx, ry= x*size+m, y*size+m
        cv.create_rectangle(rx, ry, rx+15, ry+15, fill = 'black', tags = 'cells')
    if is_complete():
        cv.delete('bg')
        return
    for x, y in r:
        rx, ry= x*size+m, y*size+m
        cv.create_line(rx, ry, rx+size, ry+size, tags = 'cells')
        cv.create_line(rx, ry+size, rx+size, ry, tags = 'cells')
def leftdown(e):
    k = ((e.x-m) // size, (e.y-m) // size)
    if k[0] < p.nsize or k[1] < p.nsize or is_complete() : return
    if k in r : r.remove(k)
    if k in l:
        l.remove(k)
    else:
        l.add(k)
    draw()
def rightdown(e):
    k = ((e.x-m) // size, (e.y-m) // size)
    if k[0] < p.nsize or k[1] < p.nsize or is_complete() : return
    if k in l : l.remove(k)
    if k in r:
        r.remove(k)
    else:
        r.add(k)
    draw()
def is_complete() : return p.ans == l

l = set()
r = set()
size = 16
m = 2 # margin
root = tkinter.Tk()
dirpath = os.path.dirname(__file__).replace('\\', '/')
filetype = (('pix files', '*.pix'),)
root.filename = tkinter.filedialog.askopenfilename(initialdir = dirpath, filetypes = filetype)
p = pix(root.filename)
cv = tkinter.Canvas(root, width = p.cvsize+1, height = p.cvsize+1)
cv.pack()
background()
root.bind('<Button-1>', leftdown)
root.bind('<Button-3>', rightdown)
root.mainloop()
```


![Gif](https://raw.githubusercontent.com/ebi-cp/docs/master/ebi-programing-magazine/20/pix.gif)