while True:
    print("Inserisci un numero intero positivo")
    N1=int(input())
    print("Inserisci un numero intero positivo")
    N2=int(input())
    if N1<0:
        continue
    if N2<0:
        continue
    if N1/N2==N2:
        print("N1 è il quadrato di N2")
    else:
        print("N1 non è il quadrato di N2")

