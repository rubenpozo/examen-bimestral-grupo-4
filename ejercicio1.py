n=int(input("ingrese un nuemero hasta el cual desea desplegar numeros primos\n"))
for i in range(2,n+1):
	for x in range(2,i):
		if (i%x==0 ):
			break
	else:
		print(i)
pass