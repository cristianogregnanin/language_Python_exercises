'''Dato N un numero intero positivo, generare e visualizzare 
in ordine crescente i numeri dispari minori o uguali a N. 
'''
n=0
scelta=-1
while(n<=0):
    print("Inserire numero intero positivo")
    n=(int(input()))


#la funzione range (n) stampa tutto fino a n
#la funzione range(n1,n2) stampa da n1 a n2(escluso)
#la funzioen range(n1,n2,n3) stampa da n1 a n2 con passo n3
for x in range(1,n,2):
    print(x)
