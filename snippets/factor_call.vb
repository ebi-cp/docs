Imports System
Imports System.IO
Imports System.Text
Imports System.Numerics
Imports System.Collections
Imports System.Collections.Generic
Imports System.Diagnostics

class Program
    shared function factor (ByVal n as UInt64) as List(of UInt64)
        dim pinfo as new ProcessStartInfo()
        pinfo.FileName = "factor"
        pinfo.Arguments = n.ToString()
        pinfo.CreateNoWindow = true
        pinfo.UseShellExecute = false
        pinfo.RedirectStandardOutput = true
        dim p as Process = Process.Start(pinfo)
        dim sp() as String = p.StandardOutput.ReadToEnd().Split()
        p.WaitForExit()
        dim r as new List(of UInt64)
        for i as Int32 = 0 to sp.Length - 3 : r.Add(UInt64.Parse(sp(i+1))) : next i
        return r
    end function
    
    shared sub main ()
        for each i as UInt64 in factor(999999866000004473)
            Console.WriteLine(i)
        next
    end sub
end class

