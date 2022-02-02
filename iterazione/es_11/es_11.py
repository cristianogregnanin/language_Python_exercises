'''
Dato N un numero intero positivo, calcolare e visualizzare la somma dei
primi N numeri dispari.'''

n=0
while(n<=0):
    print("Inserire numero intero positivo")
    n=(int(input()))

sum=0
print("\nLa somma dei valori dispari tra 0 e n è:") #n compreso
for i in range(1,n+1,2):
    sum=sum+i
print(sum)