x=int(input("ingrese un numero:"))
y=int(input("ingrese un numero:"))
def multiplos(x,y):
	if x>y:
		print("no hay numeros")
	else:
		cadena=[]
		n=0
		for i in range(x,y,x):
			n+=1
			cadena.append(i)

		cadena=str(cadena).replace('[',"")
		cadena=str(cadena).replace(']',"")
		print("hay n numeros"+str(x))
		print(cadena)
	
multiplos(x,y)





