#! /usr/bin/env python3

def factor(n):
    from subprocess import Popen, PIPE
    o = Popen(['factor', str(n)], stdout=PIPE).communicate()[0]
    return list(map(int, o.decode('utf-8').strip().split(' ')[1:]))
    
print(factor(999999866000004473))