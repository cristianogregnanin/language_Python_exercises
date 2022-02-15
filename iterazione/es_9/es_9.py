'''Dati due numeri interi e positivi N1 e N2 con N2>N1, generare e
visualizzare in ordine decrescente i numeri compresi tra N1 e N2. 
'''
N1=1
N2=0

while(N2<N1):
    print("inserire valore di n1")
    N1=int(input())
    print("inserire valore di n2")
    N2=int(input())

print("\nI valori tra N1 e N2 decrescenti sono:") #ho incluso gli estremi
for i in range(N2,N1-1,-1):
    print(i)