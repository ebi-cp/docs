using System;
using System.IO;
using System.Linq;
using System.Numerics;
using System.Collections;
using System.Collections.Generic;

public class EIO {
    private string[] reads;
    private int index;
    public EIO() {
        Console.SetOut(new StreamWriter(Console.OpenStandardOutput()));
        this.reads = new string[0];
        this.index = 0;
    }
    ~EIO() { Console.Out.Flush(); }
    private string NextValue () {
        this.index += 1;
        if (this.index > this.reads.Length) {
            this.reads = Console.ReadLine().Split();
            this.index = 0;
        }
        return this.reads[this.index];
    }
    private string[] NextLine () {
        this.reads = Console.ReadLine().Split();
        this.index = this.reads.Length;
        return this.reads;
    }
    public int[] NextIntArray () { return this.NextLine().Select(x => int.Parse(x)).ToArray(); }
    public long[] NextLongArray () { return this.NextLine().Select(x => long.Parse(x)).ToArray(); }
    public double[] NextDoubleArray () { return this.NextLine().Select(x => double.Parse(x)).ToArray(); }
    public string[] NextStringArray () { return this.NextLine(); }
    public List<int> NextIntList () { return this.NextLine().Select(x => int.Parse(x)).ToList(); }
    public List<long> NextLongList () { return this.NextLine().Select(x => long.Parse(x)).ToList(); }
    public List<double> NextDoubleList () { return this.NextLine().Select(x => double.Parse(x)).ToList(); }
    public List<string> NextStringList () { return this.NextLine().ToList(); }
    public int NextInt () { return int.Parse(this.NextValue()); }
    public long NextLong () { return long.Parse(this.NextValue()); }
    public double NextDouble () { return double.Parse(this.NextValue()); }
    public string NextString () { return this.NextValue(); }
}

public class Program {
    static void Main (string[] args) {
        EIO io = new EIO();
        var n = io.NextInt();
        Console.WriteLine(t[m+1]);
    }
}

