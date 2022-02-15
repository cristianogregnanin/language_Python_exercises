'''
Dati due numeri interi positivi N1 ed N2 calcolare, mediante la somma
ripetuta, il prodotto dei due numeri e visualizzarli.
'''

n1=0
n2=0
while(n1<=0 or n2<=0):
    print("Inserire N1 intero positivo")
    n1=(int(input()))
    print("Inserire N2 intero positivo")
    n2=(int(input()))

sum=0
print("\n La somma ripetuta dei due numeri è:")
for i in range(n2):
    sum=sum+n1

print(sum)