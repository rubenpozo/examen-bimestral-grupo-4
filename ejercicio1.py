def creartxt(list):
    archi=open("txtprimos.txt","a")
    archi.write(list)
    archi.write("\n")
    archi.close()
    pass

n=int(input("ingrese un nuemero hasta el cual desea desplegar numeros primos\n"))
listap=[]
for i in range(2,n+1):
	for x in range(2,i):
		if (i%x==0 ):
			break
	else:
		creartxt(str(i))
		listap.append(str(i))
print(listap)
pass