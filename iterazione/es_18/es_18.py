'''Data una misura di tempo espressa in secondi S1, convertirla in ore H,
minuti M e secondi S.
Descrivere il problema mediante flow chart. 
Esempio: se il numero dei secondi è 1630, si dovrà ottenere, in uscita
dal programma, 0h 27m 10s.
'''


S1=0
minuti=0
ore=0

while(S1<=0):
    print("Inserire numero intero positivo")
    S1=(int(input()))
ore=S1//3600
S1=S1-(ore*3600)
minuti=S1//60
S1=S1-(minuti*60)

print("I secondi convertiti sono: {0},{1},{2}",ore,minuti,S1)