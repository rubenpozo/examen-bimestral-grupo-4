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
	opcion = int(input('ingrese una opcion: '))
	if(opcion==1):
		
