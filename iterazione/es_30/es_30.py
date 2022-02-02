'''Dati due numeri interi positivi N1 e N2, verificare se N1 è il quadrato 
di N2.'''

n1=0
n2=0
while(n1<=0 or n2<=0):
    print("Inserire N1 intero positivo")
    n1=(int(input()))
    print("Inserire N2 intero positivo")
    n2=(int(input()))

if(n1==(n2**2)):
    print("N1 è il quadrato di n2")
else:
    print("N1 NON è il quadrato di N2")