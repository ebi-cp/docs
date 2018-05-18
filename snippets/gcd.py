#! /usr/bin/env python3

def gcd(a, b):
    if a < b: a, b = b, a
    while b > 0 : b, a = a % b, b
    return a

#最小公倍数
def lcm(a, b):
    return a // gcd(a, b) * b
