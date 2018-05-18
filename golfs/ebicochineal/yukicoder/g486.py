#! /usr/bin/env python3

s=input()
e,w=s.find('OOO'),s.find('XXX')
print(['EWaesstt'[e<0 or-1<w<e::2],'NA'][e==w])