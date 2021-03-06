## .Net言語(C#, VB, Boo)でGUIプログラミング TitleUnk再び
[3 実技で学ぶPython3 TkinterでGUIアプリを作ろう｡](https://github.com/ebi-cp/docs/blob/master/ebi-programming-magazine/3/README.md)  
.Net言語(C#, VB, Boo)に移植  
.Net言語はGUIが楽なので  
C++よりは遅いけどPython, Pypyなんかよりは全然早い  


## C#
Unityでゲーム制作ができる  
GUIアプリを作るのも楽  
Xamarinでスマホアプリが作れる  
競技プログラミングでも使えるAtCoder, TopCoder  
コンパイラの場所 多分この辺にあると思う  
C:/Program Files (x86)/MSBuild/14.0/bin/csc.exe  
C:/Windows/Microsoft.NET/Framework/v4.0.30319/csc.exe  
C:/Windows/Microsoft.NET/Framework64/v4.0.30319/csc.exe  
コマンド  
パス通して  
csc ファイル.cs  
か  
C:/Windows/Microsoft.NET/Framework64/v4.0.30319/csc.exe ファイル.cs  
とすれば良い

#### ウィンドウクリックするとウィンドウタイトルunk
```cs
using System;
using System.Windows.Forms;

class Program {
    static void Main () {
        Form f = new Form();
        f.Click += new EventHandler(TitleUnk);
        Application.Run(f);
    }
    static void TitleUnk (object sender, EventArgs e) {
        (sender as Form).Text = "unk";    // object型なのでForm型にキャストします
    }
}
```

#### ウィンドウクリックするとウィンドウタイトルunk Form継承版
```cs
using System;
using System.Windows.Forms;

class Form1 : Form {
    public Form1 () {    // コンストラクタ
        this.Text = "Form1";
        this.Click += new EventHandler(this.TitleUnk);
    }
    void TitleUnk (object sender, EventArgs e) {
        (sender as Form1).Text = "unk";    // object型なのでForm1型にキャストします
    }
}

class Program {
    static void Main () {
        Application.Run(new Form1());
    }
}
```
---
## VB.net
VBは型をちゃんと書かないとobject型になってしまって速度が極端に落ちることがあるmonoとかバージョンが古いとか、最新のなら多分問題ない、頻繁にアクセスしないやつでも大して問題ないと思う。遅くなると５０～１００倍くらい遅くなる。

コンパイラの場所
C:/Program Files (x86)/MSBuild/14.0/bin/vbc.exe  
C:/Windows/Microsoft.NET/Framework/v4.0.30319/vbc.exe  
C:/Windows/Microsoft.NET/Framework64/v4.0.30319/vbc.exe  
コマンド  
vbc ファイル.vb  
か  
C:/Windows/Microsoft.NET/Framework64/v4.0.30319/vbc.exe ファイル.vb  


#### ウィンドウクリックするとウィンドウタイトルunk
```vb
Imports System
Imports System.Windows.Forms

class Program
    shared sub main ()
        dim f as Form = new Form()
        AddHandler f.Click, AddressOf TitleUnk
        Application.Run(f)
    end sub
    shared sub TitleUnk (ByVal sender as object, ByVal e as EventArgs)
        CType(sender, Form).Text = "unk"
    end sub
end class
```

#### ウィンドウクリックするとウィンドウタイトルunk Form継承版
```vb
Imports System
Imports System.Windows.Forms

public class Form1
    inherits Form ' Formの継承
    public sub new () ' コンストラクタ
        me.Text = "Form1"
        AddHandler me.Click, AddressOf me.TitleUnk
    end sub
    private sub TitleUnk (ByVal sender as object, ByVal e as EventArgs)
        CType(sender, Form).Text = "unk"
    end sub
end class

class Program
    shared sub main ()
        Application.Run(new Form1())
    end sub
end class
```
---

## Boo
昔Unityで使えた(0.44%の人しか使っていなかったらしい)Pythonに似ている言語。  
廃止になると聞いてPythonに似ている言語であることを初めて知った。  
今でも使おうとすれば使えるはず(Unity)  
行コメントは //でも#でもいいっぽい  
[Booコンパイラ](https://github.com/boo-lang/boo)  
bin/booc.exe  
booc ファイル.boo  

#### ウィンドウクリックするとウィンドウタイトルunk
```py
import System
import System.Windows.Forms

def TitleUnk(sender as object, e as EventArgs):
    (sender as Form).Text = "unk"    // object型なのでForm型にキャストします
f = Form()
f.Click += EventHandler(TitleUnk)
Application.Run(f)
```

#### ウィンドウクリックするとウィンドウタイトルunk Form継承版
```py
import System
import System.Windows.Forms

class Form1(Form):
    def constructor():    // コンストラクタ
        self.Click += EventHandler(self.TitleUnk)
    def TitleUnk(sender as object, e as EventArgs):
        (sender as Form1).Text = "unk"    // object型なのでForm1型にキャストします
Application.Run(Form1())
```

![Gif](https://raw.githubusercontent.com/ebi-cp/docs/master/ebi-programming-magazine/13/titleunk.gif)

---
## ボタンを２つ表示それぞれにイベント  

TableLayoutPanelに追加することで自動的に配置してくれる。  
Formに追加すると座標指定しないとボタンが重なる。  

#### C#
```cs
using System;
using System.Windows.Forms;

class Form1 : Form {
    public Form1 () {
        var b1 = new Button() { Text = "海老競プロ部に入部します", Width = 240 };    // オブジェクト初期化子
        b1.Click += new EventHandler(this.Button1Click);
        var b2 = new Button() { Text = "海老競プロ部に入部しません", Width = 240 };
        b2.Click += new EventHandler(this.Button2Click);
        var p = new TableLayoutPanel() { Width = 260 };
        p.Controls.Add(b1);
        p.Controls.Add(b2);
        this.Width = 260;
        this.Height = 100;
        this.Controls.Add(p);
    }
    void Button1Click (object sender, EventArgs e) {
        Console.WriteLine("あなたは入部しました");
    }
    void Button2Click (object sender, EventArgs e) {
        Console.WriteLine("残念ながらあなたは入部しました");
    }
}

class Program {
    static void Main () {
        Application.Run(new Form1());
    }
}
```


#### VB.net
```vb
Imports System
Imports System.Windows.Forms

public class Form1
    inherits Form
    public sub new ()
        dim b1 as Button = new Button() with { .Text = "海老競プロ部に入部します", .Width = 240 }    ' オブジェクト初期化子
        AddHandler b1.Click, AddressOf me.Button1Click
        dim b2 as Button = new Button() with { .Text = "海老競プロ部に入部しません", .Width = 240 }
        AddHandler b2.Click, AddressOf me.Button2Click
        dim p as TableLayoutPanel = new TableLayoutPanel() with { .Width = 260 }
        p.Controls.Add(b1)
        p.Controls.Add(b2)
        me.Width = 260
        me.Height = 100
        me.Controls.Add(p)
    end sub
    private sub Button1Click (ByVal sender as object, ByVal e as EventArgs)
        Console.WriteLine("あなたは入部しました")
    end sub
    private sub Button2Click (ByVal sender as object, ByVal e as EventArgs)
        Console.WriteLine("残念ながらあなたは入部しました")
    end sub
    
end class

class Program
    shared sub main ()
        Application.Run(new Form1())
    end sub
end class
```

#### Boo
```py
import System
import System.Windows.Forms

class Form1(Form):
    def constructor():
        b1 = Button(Text : '海老競プロ部に入部します', Width : 240)
        b1.Click += EventHandler(self.Button1Click)
        b2 = Button(Text : '海老競プロ部に入部しません', Width : 240)
        b2.Click += EventHandler(self.Button2Click)
        p = TableLayoutPanel(Width : 260)
        p.Controls.Add(b1)
        p.Controls.Add(b2)
        self.Width = 260
        self.Height = 100
        self.Controls.Add(p)
    def Button1Click(sender as object, e as EventArgs):
        Console.WriteLine('あなたは入部しました')
    def Button2Click(sender as object, e as EventArgs):
        Console.WriteLine('残念ながらあなたは入部しました')
Application.Run(Form1())
```

![Gif](https://raw.githubusercontent.com/ebi-cp/docs/master/ebi-programming-magazine/13/button2.gif)

