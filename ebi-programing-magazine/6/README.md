## 実技で学ぶPython3 ファイル読み込み３Dファイルの平行投影表示

回転させて見ることはできませんが、１方向から見た３Dモデルの表示だけならTkinterで線を描くだけで簡単に行うことができます。  
とにかくPython3をインストールすれば色々なことがすぐにできる様になるのでインストールしてください。

ここではobj形式のファイルを使います。  
obj形式のファイルはテキストファイルなので簡単に読むことができます。  

頂点情報  
v (X座標) (Y座標) (Z座標)  

インデックス情報 何番目の頂点が三角になっているか  
f 1 2 3  

この２つの情報からワイヤーフレームを描くことができます。  

ではTkinterでobjファイルを表示してみましょう。  

同じフォルダに[suzanne.obj](https://github.com/ebi-cp/docs/blob/master/ebi-programing-magazine/6/suzanne.obj)を置くと読み込むことができます  
```python
#! /usr/bin/env python3

import os    # os.path.dirnameを使うために必要
import tkinter

i = 0
vertexs = []    # 空のリストを用意する
indexs = []

path = os.path.dirname(__file__).replace('\\', '/')    # このpythonファイルのフォルダパス
print(path)
with open(path + '/' + 'suzanne.obj', 'r') as f:    # ファイルを開く
    for i in f.readlines():    # 1行づつ読む
        if i.startswith('v '):    # v から始まるなら
            v1, v2, v3 = map(float, i[2:].split())    # 3文字目～をsplit mapで小数型に
            vertexs += [(v1*25+120, -v2*25+160, v3*25)]    # 数値が小さいので25倍する。あと線の表示位置をずらします。このキャンバスの中心座標が120
        if i.startswith('f '):    # f から始まるなら
            v1, v2, v3 = map(int, i[2:].split())    # 3文字目～をsplit mapで整数型に
            indexs += [(v1-1, v2-1, v3-1)]    # 1から始まるのでリストで利用できる用に-1で0からに修正する

def drawline():    # 呼ぶごとに１つの3角形を描く
    global i
    x1, y1, unk1 = vertexs[indexs[i][0]]    # 3つめのz座標は今回は使わない
    x2, y2, unk2 = vertexs[indexs[i][1]]
    x3, y3, unk3 = vertexs[indexs[i][2]]
    cv.create_line(x1, y1, x2, y2, x3, y3, x1, y1)    # 1から2、2から3最後3から1へ線を描いて閉じている
    i += 1    # 次の三角形のために+1する
    if i < len(indexs) : root.after(2, drawline)    # indexs全て書き終わるまでdrawlineを呼び続ける

root = tkinter.Tk()
cv = tkinter.Canvas(root, width = 240, height = 240)
cv.pack()
root.after(2, drawline)    # 2ms後にdrawlineを呼ぶ
root.mainloop()
```
![Gif](https://raw.githubusercontent.com/ebi-cp/docs/master/ebi-programing-magazine/6/linedraw.gif)