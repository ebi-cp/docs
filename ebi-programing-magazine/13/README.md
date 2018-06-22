## .Net言語(C#, VB, Boo)でGUIプログラミング TitleUnk再び

#### C#
C:/Program Files (x86)/MSBuild/14.0/bin/csc.exe  
C:/Windows/Microsoft.NET/Framework/v4.0.30319/csc.exe  
C:/Windows/Microsoft.NET/Framework64/v4.0.30319/csc.exe  
csc ファイル.cs
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
        Program.f.Text = "unk";
    }
}
```

#### C#
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
        this.Text = "unk";
    }
}
```
---

#### Boo
[boo-lang](https://github.com/boo-lang/boo)  
bin/booc.exe  
booc ファイル.boo
```py
import System
import System.Windows.Forms

class Form1(Form):
    def constructor () :
        self.Click += EventHandler(TitleUnk)
    def TitleUnk (sender as object, e as EventArgs):
        self.Text = "unk"
Application.Run(Form1())
```

![Gif](https://raw.githubusercontent.com/ebi-cp/docs/master/ebi-programing-magazine/13/titleunk.gif)

---

#### Boo
```py
import System
import System.Windows.Forms

class Form1(Form):
    def constructor () :
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
    def Button1Click (sender as object, e as EventArgs):
        Console.WriteLine('あなたは入部しました')
    def Button2Click (sender as object, e as EventArgs):
        Console.WriteLine('残念ながらあなたは入部しました')
Application.Run(Form1())
```



