'''Dato N un numero intero positivo, calcolare e visualizzare la somma dei
primi N numeri interi. 
'''
n=0
while(n<=0):
    print("Inserire numero intero positivo")
    n=(int(input()))

x=0
for i in range(0,n+1):  #inclusi estremi
    x=x+i
print("\nLa somma dei valori tra 0 e n è:")
print(x)