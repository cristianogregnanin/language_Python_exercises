'''Dati due numeri interi positivi N1 ed N2 calcolare, mediante la somma
ripetuta, il prodotto dei due numeri e visualizzarli.'''

#!/usr/bin/env python
# -*- coding: utf-8 -*-

S1=0
H=0
M=0
S=0
i=0

while S1<=0: 
    S1=int(input("Inserisci una misura di tempo in secondi "))
H=S1//3600
S1=S1-(H*3600)
M=S1//60
S1=S1-(M*60)
S=S1

print(H,"h ",M,"m ",S,"s")