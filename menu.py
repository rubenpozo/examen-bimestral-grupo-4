def creartxt(list):
    archi=open("txtprimos.txt","a")
    archi.write(list)
    archi.write("\n")
    archi.close()
    pass
def ejercicio1():
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

def menu():
	print('------menu-----')
	print('1.-Secuencia de numeros primos')
	print('2.-Multiplos de un numero')
	print('3.-Contar palabras y saltos de linea')
	print('4.-Traductor')
	print('5.-Area y volumen de una esfera')
	print('6.-Graficar figura')
	print('________________')	
os.system('cls')
continuar=1
while(continuar==1):
	menu()	
	
	if(opcion==1):
		ejercicio(1)
	if(opcion==2):

	if(opcion==3):

	if(opcion==4):

	if(opcion==5):

	if(opcion==6):

	continuar=1
		
