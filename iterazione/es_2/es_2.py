'''Dato N un numero intero positivo, generare e visualizzare in ordine 
crescente i primi N numeri interi positivi'''

numero=0
n_cresenti=0

while(numero<=0):
    print("Inserire numero intero positivo\n")
    numero=(int(input()))

n_crescenti=(int(input("Inserire quanti valori stampare da quello inserito in precedenza\n")))
for i in range(numero,numero+n_crescenti):
    print("\n")
    print(i)
