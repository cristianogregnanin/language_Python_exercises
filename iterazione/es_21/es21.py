while True:
    print("Inserisci un numero")
    N=int(input())
    controllo = True
    for i in range(2,N):
        if N%i==0:
            controllo = False
    if controllo == True:
        print("N è un numero primo")
    else:
        print("N non è un numeor primo")


