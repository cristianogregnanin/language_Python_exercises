'''Dato N un numero intero positivo, generare e visualizzare in ordine
decrescente i primi N numeri interi positivi.
'''
n=0
while(n<=0):
    print("Inserire numero intero positivo")
    n=(int(input()))

print("\nI valori tra zero e il valore inserito (in ordine decrescente) sono:")
# python INCREMENTA in modo automatico le variabili nei for
for i in range(n,0,-1):
    print(i)