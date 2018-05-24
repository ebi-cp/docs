Imports System
Imports System.IO
Imports System.Text
Imports System.Numerics
Imports System.Collections
Imports System.Collections.Generic
Imports System.Diagnostics

class Program
    shared function factor (ByVal n as String) as String()
        dim pinfo as new ProcessStartInfo()
        pinfo.FileName = "factor"
        pinfo.Arguments = n
        pinfo.CreateNoWindow = true
        pinfo.UseShellExecute = false
        pinfo.RedirectStandardOutput = true
        dim p as Process = Process.Start(pinfo)
        p.WaitForExit()
        dim s as String = p.StandardOutput.ReadToEnd()
        dim sp() as String = s.Split()
        dim r(sp.Length - 3) as String
        for i as Int32 = 0 to sp.Length - 3 : r(i) = sp(i+1) : next i
        return r
    end function
    
    shared sub main ()
        for each i as String in factor("999999866000004473")
            Console.WriteLine(i)
        next
    end sub
end class

