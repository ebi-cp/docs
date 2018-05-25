using System;
using System.Linq;
using System.Text;
using System.Numerics;
using System.Collections;
using System.Collections.Generic;
using System.Diagnostics;

public class Program {
    static List<UInt64> factor (UInt64 n) {
        var pinfo = new ProcessStartInfo() {
            FileName = "factor",
            Arguments = n.ToString(),
            CreateNoWindow = true,
            UseShellExecute = false,
            RedirectStandardOutput = true
        };
        Process p = Process.Start(pinfo);
        string[] sp = p.StandardOutput.ReadToEnd().Split();
        p.WaitForExit();
        List<UInt64> r = new List<UInt64>();
        for (int i = 0; i < sp.Length - 2; ++i) { r.Add(UInt64.Parse(sp[i+1])); }
        return r;
    }
    
    static void Main (string[] args) {
        foreach (var i in factor(999999866000004473)) {
            Console.WriteLine(i);
        }
    }
}