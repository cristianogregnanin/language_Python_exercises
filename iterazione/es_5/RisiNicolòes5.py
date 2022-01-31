while True:
	print("inserisci un numero positivo intero")
	N1=int(input())
	print("inserisci un numero positivo intero maggiore rispetto a quello di prima")
	N2=int(input())
	if N1<N2:
	    while N1!= N2+1:
	        print(N1)
	        N1+=1
	else: continue
