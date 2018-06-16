海老競プロマガジン 実技で学ぶPython3  
TkinterでGUIアプリを作ろう  
競プロと関係ないのばかりやっているけど、まずプログラミングに興味を持ってもらわないとなのでGUIアプリを作り方を説明します。
tkinterによるGUIプログラミングはマラソンマッチのヴィジュアライザ作成にも利用できるはず。  

Python3のインストールがまだな方はインストールをしてください。  

URL https://www.python.org/downloads/release/python-365/  
Windows x86-64 web-based installer


#### ウィンドウを表示しクリックされたらタイトルをunkにする  
```python
import tkinter    # GUIのライブラリインポート
def titleunk(e):    # タイトルうんこ関数
    root.title('unk')
root = tkinter.Tk()    # ウィンドウを作る
root.bind('<Button-1>', titleunk)    # <Button-1>クリックされたら タイトルうんこ関数を呼ぶ
root.mainloop()
```

#### ウィンドウを表示し海老競プロ部に入部しますボタンを作る  
```python
import tkinter
def button1() : print('あなたは入部しました')
def button2() : print('残念ながらあなたは入部しました')
root = tkinter.Tk()
tkinter.Button(root, text = '海老競プロ部に入部します', command = button1).pack()
tkinter.Button(root, text = '海老競プロ部に入部しません', command = button2).pack()
root.mainloop()
```

#### ウィンドウの中にキャンバスを設置し画面内の左クリックした地点に小さな円を描く。右クリックで消去  
```python
import tkinter
def leftclick(e):    # 引数eにクリックされた位置などが入ってるprint(dir(e))とかで色々出てくる
    cv.create_oval(e.x-4, e.y-4, e.x+4, e.y+4, tag = 'unk')    # tag無しでも行けるけど、付けると消去したりできる
def rightclick(e):    # tagを指定して消去
    cv.delete('unk')
root = tkinter.Tk()
cv = tkinter.Canvas(root, width = 640, height = 480)    # 図形を表示できるキャンバス作成
cv.pack()
root.bind('<Button-1>', leftclick)
root.bind('<Button-3>', rightclick)
root.mainloop()
```
![Gif](https://raw.githubusercontent.com/ebi-cp/docs/ebi-programing-magazine/3/master/unk.gif)



GUIの場合コンソールを表示したくない事がありますが、その場合は拡張子をpyではなくpywにするとコンソールは非表示になります。  
