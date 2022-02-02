while True:
    print("Inserisci un numero intero positivo ")
    N1=int(input())
    print("Inserisci un numero intero psositivo ")
    N2=int(input())
    if N1<0:
        continue
    if N2<0:
        continue
    x=0
    for i in range (0,N1):
        x+=N2
    print("somma ripetuta = ", x)
    print("prodotto = " ,N1*N2)

