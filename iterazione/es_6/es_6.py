'''Dato N un numero intero positivo, generare e visualizzare in ordine
crescente i numeri compresi maggiori uguali di -N e minori uguali di N.
'''
n=0
while(n<=0):
    print("Inserire numero intero positivo")
    n=(int(input()))
x=-n
print("\nI valori tra N e -N sono:")
for i in range(x,n+1):
    print(i)
