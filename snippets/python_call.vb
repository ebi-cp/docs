Imports System
Imports System.IO
Imports System.Text
Imports System.Numerics
Imports System.Collections
Imports System.Collections.Generic
Imports System.Diagnostics

class Program
    shared function python_call (ByVal python as String) as String
        dim pinfo as new ProcessStartInfo()
        pinfo.FileName = "python"
        pinfo.Arguments = "-c '" + python + "'"
        pinfo.CreateNoWindow = true
        pinfo.UseShellExecute = false
        pinfo.RedirectStandardOutput = true
        dim p as Process = Process.Start(pinfo)
        p.WaitForExit()
        return p.StandardOutput.ReadToEnd()
    end function
    
    shared sub main ()
        Console.WriteLine(python_call("print(\'unk\')"))
    end sub
end class
