'''Dato un numero intero positivo N verificare se N è un numero primo.
'''
n=0
rstzero=0
while(n<=0):
    print("Inserire numero intero positivo")
    n=(int(input()))

for i in range(1,n+1):
    if(n%i==0):
        rstzero=rstzero+1
if(rstzero==2):
    print("\nIl valore inserito è un numero primo")
else:
    print("\nIl valore inserito non è primo")

