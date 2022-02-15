'''
Dati due numeri interi positivi N1 e N2 con N2>N1, generare e
visualizzare in ordine crescente i numeri interi compresi
nell'intervallo chiuso [N1,N2]. 
Descrivere il problema mediante flow chart
'''
N1=1
N2=0

while(N2<N1):
    print("inserire valore di n1")
    N1=int(input())
    print("inserire valore di n2")
    N2=int(input())

print("\nI valori tra N1 e N2 sono:")
for x in range(N1,N2+1):
    print(x)