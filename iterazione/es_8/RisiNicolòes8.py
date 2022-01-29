while True:
    print("inserisci un numero")
    N=int(input())
    if N<0:
        continue
    while N!=0:
        print(N)
        N-=1
