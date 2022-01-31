while True:
    i=0
    x=1
    print("inserisci un numero")
    N=int(input())
    if N<0:
        continue
    while i!=N:
        print(x)
        x+=2
        i+=1

