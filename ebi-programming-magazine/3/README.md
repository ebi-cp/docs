## 実技で学ぶPython3 TkinterでGUIアプリを作ろう  
競プロと関係ないのばかりやっているけど、まずプログラミングに興味を持ってもらわないとなのでGUIアプリを作り方を説明します。
tkinterによるGUIプログラミングはマラソンマッチのヴィジュアライザ作成にも利用できるはず。  

#### Tkinterでウィンドウ表示するだけならすごく簡単
```py
import tkinter    # GUIのライブラリインポート
root = tkinter.Tk()    # ウィンドウを作る
root.mainloop()    # メインループ
```
mainloopで処理が止まる感じになるのでそのあとに何か書くとウィンドウが閉じた後に処理されます


---

#### ウィンドウを表示しクリックされたらタイトルをunkにする  
```py
import tkinter    # GUIのライブラリインポート
def titleunk(e):    # タイトルうんこ関数
    root.title('unk')
root = tkinter.Tk()    # ウィンドウを作る
root.bind('<Button-1>', titleunk)    # <Button-1>クリックされたら タイトルうんこ関数を呼ぶ
root.mainloop()
```
---

#### ウィンドウを表示し海老競プロ部に入部しますボタンを作る  
```py
import tkinter
def button1() : print('あなたは入部しました')
def button2() : print('残念ながらあなたは入部しました')
root = tkinter.Tk()
tkinter.Button(root, text = '海老競プロ部に入部します', command = button1).pack()
tkinter.Button(root, text = '海老競プロ部に入部しません', command = button2).pack()
root.mainloop()
```
---

#### ウィンドウの中にキャンバスを設置し画面内の左クリックした地点に小さな円を描く。右クリックで消去  
```py
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
[Cassiopeiaの日記 Tkinter イベントのバインディング - Tkinter Event and binding](http://d.hatena.ne.jp/Cassiopeia/20070821/1187701922)  
[Tkinter の bind とイベントシーケンス](http://www.rouge.gr.jp/~fuku/tips/python-tkinter/bind.shtml)  

![Gif](https://raw.githubusercontent.com/ebi-cp/docs/master/ebi-programming-magazine/3/unk.gif)


GUIの場合コンソールを表示したくない事がありますが、その場合は拡張子をpyではなくpywにするとコンソールは非表示になります。  
