using System;
using System.Linq;
using System.Text;
using System.Numerics;
using System.Collections;
using System.Collections.Generic;
using System.Diagnostics;

public class Program {
    static string[] factor (string n) {
        var pinfo = new ProcessStartInfo() {
            FileName = "factor",
            Arguments = n,
            CreateNoWindow = true,
            UseShellExecute = false,
            RedirectStandardOutput = true
        };
        Process p = Process.Start(pinfo);
        string o = p.StandardOutput.ReadToEnd();
        p.WaitForExit();
        return o.Split(' ').Skip(1).ToArray();
    }
    
    static void Main (string[] args) {
        foreach (var i in factor("999999866000004473")) {
            Console.WriteLine(i);
        }
    }
}
