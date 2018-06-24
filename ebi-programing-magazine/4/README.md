## 実技で学ぶPython3 九九の表示からマンデルブロ集合の表示まで｡  
  

forループ文とrangeの使いかた
Python3で九九を表示
```py
for i in range(9):    # 0~8の値が順番にiに入ります
    for j in range(9):
        a, b = i + 1, j + 1    # 0からなので+1します
        print(a, '*', b, '=', a*b)



for i in range(1, 10):    # 1~9の値が順番にiに入ります
    for j in range(1, 10):
        print(i, '*', j, '=', i*j)
        # print('%d + %d = %d'%(i, j, i*j))    # このように書くこともできます
```
  
前回までの知識と2重ループでできる  
マンデルブロ集合をTkinterで描画する
```py
import tkinter
def mandelbrot(x, y):
    # 座標を修正します 0が真ん中に来るように
    px = x / 240.0 * 4.0 - 3.0    # x -3.0 ~ 1.0(0.98) xは1.0ずらします
    py = y / 240.0 * 4.0 - 2.0    # y -2.0 ~ 2.0(1.98)
    c = px + py * 1j
    z = 0j
    for n in range(32):
        z = z**2 + c
        if abs(z**2) > 4.0 : return (n*6+64, n*6+64, n*6+64)    # 色が32段階 暗いので*6 + 64で明るくします
    return (0, 0, 0)

root = tkinter.Tk()
cv = tkinter.Canvas(root, width = 240, height = 240)    # 図形を表示できるキャンバス作成
cv.pack()
im = tkinter.PhotoImage(width = 240, height = 240)    # イメージ作成
for y in range(240):    # 240回繰り返します 0~239の値が yに順番に入ります
    for x in range(240):    # 240回繰り返します 0~239の値が xに順番に入ります
        color = mandelbrot(x, y)    # mandelbrot関数に座標を渡し色を取得します
        im.put('#%02x%02x%02x'%color, (x, y))    # 色2桁の16進数3つにします, 座標
cv.create_image(2, 2, image = im, anchor = 'nw')    # イメージをキャンバスに表示させます。２ピクセルずれるので2, 2とセットします。 nw(左上)が0, 0
root.mainloop()
```

最初に240*240ピクセル分の計算をしていたので最初に時間がかかってしまいます。
なので1ラインずつ表示してみます。

```py
import tkinter
def mandelbrot(x, y):
    px = x / 240.0 * 4.0 - 3.0
    py = y / 240.0 * 4.0 - 2.0
    c = px + py * 1j
    z = 0j
    for n in range(32):
        z = z**2 + c
        if abs(z**2) > 4.0 : return (n*6+64, n*6+64, n*6+64)
    return (0, 0, 0)

y = 0
def drawline():
    global y    # 関数の外にあるyに値を入れるために必要です。見るだけで代入しないのであれば必要ありません。
    cv.delete('unk')    # キャンバスの画像を削除します
    for x in range(240):
        color = mandelbrot(x, y)    # mandelbrot関数に座標を渡し色を取得します
        im.put('#%02x%02x%02x'%color, (x, y))    # 色2桁の16進数3つにします, 座標
    cv.create_image(2, 2, image = im, tag = 'unk', anchor = 'nw')
    root.update()
    y += 1    # 次のラインのために+1します
    if y < 240 : root.after(1, drawline)    # 240未満なら1ms後にこの関数を呼び出します

root = tkinter.Tk()
cv = tkinter.Canvas(root, width = 240, height = 240)
cv.pack()
im = tkinter.PhotoImage(width = 240, height = 240)
root.after(1, drawline)    # 1ms後にdrawlineを呼び出す
root.mainloop()
```
![Gif](https://raw.githubusercontent.com/ebi-cp/docs/master/ebi-programing-magazine/4/mandelbrot.gif)