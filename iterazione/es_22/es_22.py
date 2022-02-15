'''Dato un numero N(positivo)calcolare e visualizzare tutte le coppie di numeri che
danno per somma il numero stesso.
'''

n=0
num1=0
num2=0
while(n<=0):
    print("Inserire numero intero positivo")
    n=(int(input()))
for i in range(0,(n+1)//2): #le coppie non si ripetono mai
    num1=i
    num2=n-num1
    print("Coppia che per somma dà il numero inserito:{0},{1}",num1,num2)



