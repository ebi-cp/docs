## .Net言語(C#, VB, Boo)でGUIプログラミング ライフゲームの移植
[8 実技で学ぶPython3 ライフゲームを作る](https://github.com/ebi-cp/docs/blob/master/ebi-programing-magazine/8/README.md)  
.Net言語(C#, VB, Boo)に移植  

## C#
```cs
using System;
using System.Linq;
using System.Drawing;
using System.Windows.Forms;
using System.Collections.Generic;

class Game : Form {
    private static int CVSize = 512;
    private static int CellSize = 8;
    private SolidBrush cellcolor = new SolidBrush(Color.FromArgb(255, 200, 44, 85));
    private Graphics g;
    private Bitmap bm;
    private PictureBox pb;
    private HashSet<Point> alive = new HashSet<Point>();
    private Timer timer = new Timer() { Interval = 100 };
    public Game () {
        this.pb = new PictureBox() { Width = Game.CVSize, Height = Game.CVSize };
        this.bm = new Bitmap(this.pb.Width, this.pb.Height);
        this.g = Graphics.FromImage(bm);
        this.pb.MouseDown += new MouseEventHandler(this.MouseDownEvent);
        this.Width = Game.CVSize+16;
        this.Height = Game.CVSize+16;
        this.Text = "LifeGame";
        this.Controls.Add(this.pb);
        this.timer.Tick += new EventHandler(this.GameUpdate);
    }
    private void MouseDownEvent (object sender, MouseEventArgs e) {
        if (e.Button == MouseButtons.Left) {
            this.timer.Stop();
            var pos = this.PointToClient(System.Windows.Forms.Cursor.Position);
            var p = new Point(pos.X / Game.CellSize, pos.Y / Game.CellSize);
            if (this.alive.Contains(p)) {
                this.alive.Remove(p);
            } else {
                this.alive.Add(p);
            }
            this.Draw();
        }
        if (e.Button == MouseButtons.Right) { this.timer.Start(); }
    }
    private void Draw () {
        this.g.FillRectangle(Brushes.White, 0, 0, Game.CVSize, Game.CVSize);
        foreach (var i in this.alive) {
            int px = Game.CellSize * i.X;
            int py = Game.CellSize * i.Y;
            this.g.FillRectangle(Brushes.Black, px, py, Game.CellSize, Game.CellSize);
            this.g.FillRectangle(cellcolor, px+1, py+1, Game.CellSize-2, Game.CellSize-2);
        }
        this.pb.Image = this.bm;
    }
    private void GameUpdate (object sender, EventArgs e) {
        var s = Game.CVSize / Game.CellSize;
        var m = new Dictionary<Point, int>();
        foreach (var i in this.alive) {
            for (int dy = -1; dy < 2; ++dy) {
                for (int dx = -1; dx < 2; ++dx) {
                    var t = new Point(i.X+dx, i.Y+dy);
                    if (m.ContainsKey(t)) {
                        m[t] += 1;
                    } else {
                        m[t] = 1;
                    }
                }
            }
        }
        foreach (var i in m) { if (i.Value == 3) { alive.Add(i.Key); } }
        foreach (var i in alive.ToList()) {
            var a = m[i] < 3 || m[i] > 4;
            var x = Math.Abs(i.X-s) > s*2;
            var y = Math.Abs(i.Y-s) > s*2;
            if (a || x || y) { this.alive.Remove(i); }
        }
        this.Draw();
    }
}
class Program {
    static void Main () {
        Application.Run(new Game());
    }
}
```
---

## VB.net
```vb
Imports System
Imports System.Linq
Imports System.Drawing
Imports System.Windows.Forms
Imports System.Collections.Generic

public class Game
    inherits Form
    private shared CVSize as Int32 = 512
    private shared CellSize as Int32 = 8
    private cellcolor as SolidBrush = new SolidBrush(Color.FromArgb(255, 200, 44, 85))
    private g as Graphics
    private bm as Bitmap
    private pb as PictureBox
    private alive as HashSet(of Point) = new HashSet(of Point)
    private timer as Timer = new Timer() with { .Interval = 100 }
    public sub new ()
        me.pb = new PictureBox() with { .Width = Game.CVSize, .Height = Game.CVSize }
        me.bm = new Bitmap(me.pb.Width, me.pb.Height)
        me.g = Graphics.FromImage(bm)
        AddHandler me.pb.MouseDown , AddressOf me.MouseDownEvent
        me.Width = Game.CVSize+16
        me.Height = Game.CVSize+16
        me.Text = "LifeGame"
        me.Controls.Add(me.pb)
        AddHandler me.timer.Tick , AddressOf me.GameUpdate
    end sub
    private sub MouseDownEvent (ByVal sender as object, ByVal e as MouseEventArgs)
        if e.Button = MouseButtons.Left then
            me.timer.Stop()
            dim pos as Point = me.PointToClient(System.Windows.Forms.Cursor.Position)
            dim p = new Point((pos.X - Game.CellSize / 2) / Game.CellSize, (pos.Y - Game.CellSize / 2) / Game.CellSize)
            if me.alive.Contains(p) then
                me.alive.Remove(p)
            else
                me.alive.Add(p)
            end if
            me.Draw()
        end if
        if e.Button = MouseButtons.Right then
            me.timer.Start()
        end if
    end sub
    private sub Draw()
        me.g.FillRectangle(Brushes.White, 0, 0, Game.CVSize, Game.CVSize)
        for each i as Point in me.alive
            dim px as Int32 = Game.CellSize * i.X
            dim py as Int32 = Game.CellSize * i.Y
            me.g.FillRectangle(Brushes.Black, px, py, Game.CellSize, Game.CellSize)
            me.g.FillRectangle(cellcolor, px+1, py+1, Game.CellSize-2, Game.CellSize-2)
        next
        me.pb.Image = me.bm
    end sub
    private sub GameUpdate (ByVal sender as object, ByVal e as EventArgs)
        dim s as Int32 = Game.CVSize / Game.CellSize
        dim m as Dictionary(of Point, Int32) = new Dictionary(of Point, Int32)
        for each i as Point in me.alive
            for dy as Int32 = -1 to 1
                for dx as Int32 = -1 to 1
                    dim t as Point= new Point(i.X+dx, i.Y+dy)
                    if m.ContainsKey(t) then
                        m(t) += 1
                    else
                        m(t) = 1
                    end if
                next dx
            next dy
        next
        for each i as KeyValuePair(Of Point, Int32) in m
            if i.Value = 3 : alive.Add(i.Key) : end if
        next
        for each i as Point in alive.ToList()
            dim a as Boolean = m(i) < 3 or m(i) > 4
            dim x as Boolean = Math.Abs(i.X-s) > s*2
            dim y as Boolean = Math.Abs(i.Y-s) > s*2
            if a or x or y : me.alive.Remove(i) : end if
        next
        me.Draw()
    end sub
end class
class Program
    shared sub main ()
        Application.Run(new Game())
    end sub
end class
```

---

## Boo
```py
import System
import System.Linq
import System.Drawing
import System.Windows.Forms
import System.Collections.Generic

class Game(Form):
    private static CVSize = 512
    private static CellSize = 8
    private cellcolor = SolidBrush(Color.FromArgb(255, 200, 44, 85))
    private g as Graphics
    private bm as Bitmap
    private pb as PictureBox
    private alive = HashSet[of Point]()
    private timer as Timer = Timer(Interval : 100)
    def constructor():
        self.pb = PictureBox(Width : Game.CVSize, Height : Game.CVSize)
        self.bm = Bitmap(self.pb.Width, self.pb.Height)
        self.g = Graphics.FromImage(bm)
        self.pb.MouseDown += MouseEventHandler(self.MouseDownEvent)
        self.Width = Game.CVSize+16
        self.Height = Game.CVSize+16
        self.Text = "LifeGame"
        self.Controls.Add(self.pb)
        self.timer.Tick += EventHandler(self.GameUpdate)
    private def MouseDownEvent (sender as object, e as MouseEventArgs):
        if e.Button == MouseButtons.Left:
            self.timer.Stop()
            pos = self.PointToClient(System.Windows.Forms.Cursor.Position)
            p = Point(pos.X / Game.CellSize, pos.Y / Game.CellSize)
            if self.alive.Contains(p):
                self.alive.Remove(p)
            else:
                self.alive.Add(p)
            self.Draw()
        if e.Button == MouseButtons.Right : self.timer.Start()
    private def Draw():
        self.g.FillRectangle(Brushes.White, 0, 0, Game.CVSize, Game.CVSize)
        for i in self.alive:
            px = Game.CellSize * i.X
            py = Game.CellSize * i.Y
            self.g.FillRectangle(Brushes.Black, px, py, Game.CellSize, Game.CellSize)
            self.g.FillRectangle(cellcolor, px+1, py+1, Game.CellSize-2, Game.CellSize-2)
        self.pb.Image = self.bm
    private def GameUpdate (sender as object, e as EventArgs):
        s = Game.CVSize / Game.CellSize
        m = Dictionary[of Point, int]()
        for i in self.alive:
            for dy in range(-1, 2):
                for dx in range(-1, 2):
                    t = Point(i.X+dx, i.Y+dy);
                    if m.ContainsKey(t):
                        m[t] += 1
                    else:
                        m[t] = 1
        for i in m:
            if i.Value == 3 : alive.Add(i.Key)
        for i in alive.ToList():
            a = m[i] < 3 or m[i] > 4
            x = Math.Abs(i.X-s) > s*2
            y = Math.Abs(i.Y-s) > s*2
            if a or x or y : self.alive.Remove(i)
        self.Draw()
Application.Run(Game())
```