## 普通に学ぶPython3 クラス

---
#### クラス  
- インスタンス
- ```__init__```  
コンストラクタ。インスタンス生成時に呼ばれる。  
- インスタンス変数  
self.変数名。インスタンスを生成するごとに違う値を持つことができる。多くの他の言語と違い宣言はメソッド内で行う。インスタンス変数にアクセスするにはクラス内からはself.変数名、インスタンスでアクセスするにはインスタンス.変数名
- インスタンスメソッド  
第一引数にselfがある関数。インスタンス変数にアクセスするにはself.変数名、インスタンスメソッドを呼ぶにはクラス内からはself.メソッド名()、インスタンスで呼ぶ場合はインスタンス.メソッド名()

- ```@staticmethod```  
を付けるスタティックメソッド。インスタンスを作らなくてもクラス名.メソッド名で呼べる。インスタンス変数にはアクセスできない。クラス変数にアクセスするにはクラス名.変数名  
- ```@classmethod```  
を付けるクラスメソッド。インスタンスを作らなくてもクラス名.メソッド名で呼べる。インスタンス変数にはアクセスできない。クラス変数にアクセスするには第一変数cls.変数名  

---
### Tkinterで海老の画像をキャンバスにいっぱい描いてみる
#### ebiクラス
座標x, yとTkinter画像を持つクラス  
ebi_image staticメソッド 海老の画像を生成する  

画像ファイルを読み込めばもっとシンプルにできるけどコピペで動いた方が楽そうだからpythonで画像生成するようにしました。  

```py
import tkinter
class ebi:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.im = ebi.tkimage('#D03010')
    @staticmethod
    def tkimage(color):    # 海老の画像を返す
        im = tkinter.PhotoImage(width = 32, height = 32)    # 画像生成　ebi画像は16x16なのですが小さくて見にくいので２倍します
        s  = ['0000000000000000'] * 7
        s += ['0000000111100000']
        s += ['0000011000011000']
        s += ['0000100000000000']
        s += ['0111111111110000']
        s += ['0001121111111100']
        s += ['0000011110111110']
        s += ['0000100101010110']
        s += ['0001001010101100']
        s += ['0001001000011000']
        for y in range(16):    # 読み取り 1 color  2 black
            for x in range(16):
                if s[y][x] == '1':
                    im.put(color, (x*2, y*2, x*2+2, y*2+2))
                if s[y][x] == '2':
                    im.put('#000000', (x*2, y*2, x*2+2, y*2+2))
        return im
root = tkinter.Tk()
cv = tkinter.Canvas(root, width = 512, height = 512)
cv.pack()
e = []
for x in range(16):
    for y in range(16):
        e += [ebi(x*32, y*32)]
for i in e:
    cv.create_image(2 + i.x, 2 + i.y, image = i.im, tags = 'ebi', anchor = 'nw')
root.mainloop()

```
---
#### ebiクラスの継承 colorの追加
```py
import tkinter
class ebi:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.im = ebi.tkimage('#D03010')
    @staticmethod
    def tkimage(color):    # 海老の画像を返す
        im = tkinter.PhotoImage(width = 32, height = 32)    # 画像生成　ebi画像は16x16なのですが小さくて見にくいので２倍します
        s  = ['0000000000000000'] * 7
        s += ['0000000111100000']
        s += ['0000011000011000']
        s += ['0000100000000000']
        s += ['0111111111110000']
        s += ['0001121111111100']
        s += ['0000011110111110']
        s += ['0000100101010110']
        s += ['0001001010101100']
        s += ['0001001000011000']
        for y in range(16):    # 読み取り 1 color  2 black
            for x in range(16):
                if s[y][x] == '1':
                    im.put(color, (x*2, y*2, x*2+2, y*2+2))
                if s[y][x] == '2':
                    im.put('#000000', (x*2, y*2, x*2+2, y*2+2))
        return im
class ebirenjai(ebi):
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.im = ebi.tkimage(color)
root = tkinter.Tk()
cv = tkinter.Canvas(root, width = 512, height = 512)
cv.pack()
e = []
for x in range(16):
    for y in range(16):
        e += [ebirenjai(x*32, y*32, '#%02x%02x%02x'%(x*16, y*16, 127 - x*8 + 127 - y*8))]
for i in e:
    cv.create_image(2 + i.x, 2 + i.y, image = i.im, tags = 'ebi', anchor = 'nw')
root.mainloop()
```
![Image](https://raw.githubusercontent.com/ebi-cp/docs/master/ebi-programing-magazine/12/ebiebirenjaitk.png)

