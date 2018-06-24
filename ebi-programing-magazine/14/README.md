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
    private System.Timers.Timer timer = new System.Timers.Timer(100);
    public Game () {
        this.pb = new PictureBox() { Width = Game.CVSize, Height = Game.CVSize };
        this.bm = new Bitmap(this.pb.Width, this.pb.Height);
        this.g = Graphics.FromImage(bm);
        this.pb.MouseDown += new MouseEventHandler(this.MouseDownEvent);
        this.Width = Game.CVSize+16;
        this.Height = Game.CVSize+16;
        this.Text = "LifeGame";
        this.Controls.Add(this.pb);
        this.timer.Elapsed += new System.Timers.ElapsedEventHandler(this.GameUpdate);
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