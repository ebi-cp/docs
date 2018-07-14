## 普通に学ぶPython3 クラス

- クラス  
関数と変数のセットみたいな、インスタンスの設計図。例えば三角形の３つの頂点の位置とそれを移動させたり回転させたりする処理をひとまとめにするとかに使う。
- インスタンス  
実態。変数 = クラス名()でインスタンスを生成できる。
- メソッド  
関数
- コンストラクタ  
```__init__```がメソッド名なインスタンス生成時に呼ばれるメソッド。  
- インスタンス変数、メンバ変数  
self.変数名。インスタンスを生成するごとに違う値を持つことができる。多くの他の言語と違い宣言はメソッド内で行う。インスタンス変数にアクセスするにはクラス内からはself.変数名、インスタンスでアクセスするにはインスタンス.変数名
- クラス変数、スタティック変数  
インスタンスを生成しなくてもアクセスできる。異なるインスタンスで共有できる。
- インスタンスメソッド  
第一引数にselfがある関数。インスタンス変数にアクセスするにはself.変数名、インスタンスメソッドを呼ぶにはクラス内からはself.メソッド名()、インスタンスで呼ぶ場合はインスタンス.メソッド名()
- スタティックメソッド  
```@staticmethod```デコレータを付ける。インスタンスを作らなくてもクラス名.メソッド名で呼べる。インスタンス変数にはアクセスできない。クラス変数にアクセスするにはクラス名.変数名  
- クラスメソッド  
```@classmethod```デコレータを付けて第一引数をclsにする。インスタンスを作らなくてもクラス名.メソッド名で呼べる。インスタンス変数にはアクセスできない。クラス変数にアクセスするにはクラス名.変数名、第一変数cls.変数名。大体スタティックメソッドと同じ、第一引数で自クラスを受け取るか受け取らないかの違いだと思う。  
- 継承  
class クラス名(継承元クラス名):で継承できる。
- オーバーライド  
継承し継承元のメソッドの動作を書き換える。Pythonの場合は継承先で同じメソッドを作ればオーバーライドされそう。
- self, cls  
インスタンスメソッドself、クラスメソッドのclsのselfとclsの名前は実は何でも良くて、でも推奨されてるのでselfとclsを使った方が良いかも。他の言語ではselfはthisキーワードなことが多い。
---
#### クラスの作り方。使いかた。
```py
class ebi:
    cn = 2    # クラス変数 異なるインスタンスで共有される
    def __init__(self, n):    # コンストラクタ
        self.n = n    # メンバ変数
    def printn(self):    # メソッド
        print(self.n)
    def printcn(self):    # メソッド
        print(ebi.cn)
a = ebi(5)    # インスタンス生成
a.printn()    # 5
a.printcn()    # 2
b = ebi(1)    # インスタンス生成
b.printn()    # 1
b.printcn()    # 2
```
---
#### クラスメソッド、スタティックメソッド
```py
class ebi1:
    a = '1'
    def __init__(self):
        pass    # 何もしない
    @classmethod
    def cprint(cls):
        print(cls.a)
    @staticmethod
    def sprint():
        print(ebi1.a)
class ebi2(ebi1):    # 継承
    a = '2'
ebi1.cprint()    # 1
ebi1.sprint()    # 1
ebi2.cprint()    # 2
ebi2.sprint()    # 1
```
---
#### 継承とオーバーライド
```py
class ebi:
    def __init__(self):
        pass
    def sewata_remove(self):
        self.sewata = 0
    def eat(self):
        print('美味しい')
class ebirenjai(ebi):
    def __init__(self, sewata):
        self.sewata = sewata
    def eat(self):    # メソッドのオーバーライド
        if self.sewata > 20:
            print('背ワタ未処理の海老プラチナだ。不味い。')
        else:
            print('美味しい。')
        
e1 = ebi()
e1.eat()    # 美味しい。

e2 = ebirenjai(0)
e2.eat()    # 美味しい。
e3 = ebirenjai(100)
e3.eat()    # 背ワタ未処理の海老プラチナだ。不味い。
e3.sewata_remove()    # ebiを継承しているので使える
e3.eat()    # 美味しい。

```
---
#### 外からは呼べないプライベートメソッド
```py
class ebi:
    def __init__(self):
        self.__n = 0    # 内部からしか見れないプライベート変数__を付けるとプライベート
    def __f(self):    # 内部からしか呼べないプライベートメソッド__を付けるとプライベート
        print('private')
    def f(self):    # publicなメソッド外からでも呼べるPythonでは普通はこれ
        self.__f()    # 内部からならプライベートメソッドを呼べる
a = ebi()
a.f()    # 普通に呼べる
a.__f()    # 呼べないここでエラーになる
a._ebi__f()    # こうすれば無理やり呼べる
```
---
### Tkinterで海老の画像をキャンバスにいっぱい描いてみる
#### ebiクラス
座標x, yとTkinter画像を持つクラス  
tkimage メソッド 海老の画像を生成する  

画像ファイルを読み込めばもっとシンプルにできるけどコピペで動いた方が楽そうだからpythonで画像生成するようにしました。  

```py
#! /usr/bin/env python3
import tkinter
class ebi:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.tkimage('#D03010')
    def tkimage(self, color):    # 海老の画像を生成
        self.im = tkinter.PhotoImage(width = 32, height = 32)    # 画像生成　ebi画像は16x16なのですが小さくて見にくいので２倍します
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
                    self.im.put(color, (x*2, y*2, x*2+2, y*2+2))    # 座標も２倍して４ピクセルずつ塗る
                if s[y][x] == '2':
                    self.im.put('#000000', (x*2, y*2, x*2+2, y*2+2))
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
#! /usr/bin/env python3
import tkinter
class ebi:
    def __init__(self, x, y):
        self.x = x    # 座標
        self.y = y
        self.tkimage('#D03010')    # 普通の海老なので普通な色
    def tkimage(self, color):    # 海老の画像を生成
        self.im = tkinter.PhotoImage(width = 32, height = 32)    # 画像生成　ebi画像は16x16なのですが小さくて見にくいので２倍します
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
                    self.im.put(color, (x*2, y*2, x*2+2, y*2+2))    # 座標も２倍して４ピクセルずつ塗る
                if s[y][x] == '2':
                    self.im.put('#000000', (x*2, y*2, x*2+2, y*2+2))
class ebirenjai(ebi):    # ebiを継承
    def __init__(self, x, y, color):    # 画像に色を設定できるようになった
        self.x = x
        self.y = y
        self.tkimage(color)    # 引数の色を渡してその色の画像を生成
root = tkinter.Tk()
cv = tkinter.Canvas(root, width = 512, height = 512)
cv.pack()
e = []
for x in range(16):
    for y in range(16):
        e += [ebirenjai(x*32, y*32, '#%02x%02x%02x'%(x*16, y*16, 255 - x*8 - y*8))]
for i in e:
    cv.create_image(2 + i.x, 2 + i.y, image = i.im, tags = 'ebi', anchor = 'nw')
root.mainloop()
```
![Image](https://raw.githubusercontent.com/ebi-cp/docs/master/ebi-programming-magazine/12/ebiebirenjaitk.png)


