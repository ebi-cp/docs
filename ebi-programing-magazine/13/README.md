## .Net言語(C#, VB, Boo)でGUIプログラミング TitleUnk再び
[3 実技で学ぶPython3 TkinterでGUIアプリを作ろう｡](https://github.com/ebi-cp/docs/blob/master/ebi-programing-magazine/3/README.md)  
他の言語に移植  
.Net言語はGUIが楽なので  


## C#
コンパイラの場所多分この辺にあると思う  
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
    static Form f = new Form();
    static void Main () {
        Program.f.Click += new EventHandler(TitleUnk);
        Application.Run(f);
    }
    
    static void TitleUnk (object sender, EventArgs e) {
        (sender as Form).Text = "unk";
    }
}
```

#### ウィンドウクリックするとウィンドウタイトルunk Form継承版
```cs
using System;
using System.Windows.Forms;

class Program {
    static void Main () {
        Application.Run(new Form1());
    }
}

class Form1 : Form {
    public Form1 () {    // コンストラクタ
        this.Text = "Form1";
        this.Click += new EventHandler(TitleUnk);
    }
    
    void TitleUnk (object sender, EventArgs e) {
        (sender as Form).Text = "unk";
    }
}
```
---
## Boo
昔Unityで使えた(0.44%の人しか使っていなかったらしい)Pythonに似ている言語。  
廃止になると聞いてPythonに似ている言語であることを初めて知った。  
今でも使おうとすれば使えるはず(Unity)  
[Booコンパイラ](https://github.com/boo-lang/boo)  
bin/booc.exe  
booc ファイル.boo  

#### ウィンドウクリックするとウィンドウタイトルunk
```py
import System
import System.Windows.Forms

def TitleUnk(sender as object, e as EventArgs):
    (sender as Form).Text = "unk"
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
        (sender as Form1).Text = "unk"
Application.Run(Form1())
```

![Gif](https://raw.githubusercontent.com/ebi-cp/docs/master/ebi-programing-magazine/13/titleunk.gif)

---

#### Boo
#### ボタンを２つ表示それぞれにイベント  
TableLayoutPanelに追加することで自動的に配置してくれる。  
Formに追加すると座標指定しないとボタンが重なる。  
```py
import System
import System.Windows.Forms

class Form1(Form):
    def constructor():
        b1 = Button(Text : '海老競プロ部に入部します', Width : 240)
        b1.Click += EventHandler(Button1Click)
        b2 = Button(Text : '海老競プロ部に入部しません', Width : 240)
        b2.Click += EventHandler(Button2Click)
        tlp = TableLayoutPanel(Width : 260)
        tlp.Controls.Add(b1)
        tlp.Controls.Add(b2)
        self.Width = 260
        self.Height = 100
        self.Controls.Add(tlp)
    def Button1Click(sender as object, e as EventArgs):
        Console.WriteLine('あなたは入部しました')
    def Button2Click(sender as object, e as EventArgs):
        Console.WriteLine('残念ながらあなたは入部しました')
Application.Run(Form1())
```



