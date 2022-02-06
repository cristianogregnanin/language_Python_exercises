#!/usr/bin/env python
# -*- coding: utf-8 -*-

stringheConcat = ""

while True:
    stringa = input("Inserire una stringa. Digitare z o Z per terminare l-inserimento\n")
    if stringa == "z" or stringa == "Z": break
    else:
        stringheConcat += stringa

print(stringheConcat)
