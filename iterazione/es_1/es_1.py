#!/usr/bin/env python
# -*- coding: utf-8 -*-

#!/usr/bin/env python
# -*- coding: utf-8 -*-

while True:
    n = float(input("Inserisci un numero: "))
    if float.is_integer(n)==True and n>0:
        n=int(n)
        break
    print("Valori non accettabili. Requisiti: n>0 e intero")

print(f"Il numero successivo di {n} è {n+1}")