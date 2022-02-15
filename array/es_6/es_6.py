#!/usr/bin/env python
# -*- coding: utf-8 -*-

def Palindroma(stringa):
    i = 0
    j = len(stringa) - 1
    while i < j:
        if stringa[i] != stringa[j]:
            return -1
        else:
            i += 1
            j -= 1
    return 1

stringa = input("Inserire una stringa\n")
if Palindroma(stringa) == 1:
    print("%s e' una stringa palindroma" %stringa)
else:
    print("%s non e' una stringa palindroma" %stringa)