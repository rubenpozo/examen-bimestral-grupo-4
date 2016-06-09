def creartxt(list):
    archi=open("txteje2.txt","a")
    archi.write(list)
    archi.write("\n")
    archi.close()
    pass

x=int(input("ingrese un numero:"))
y=1000
cadena=[]
if x>y:
	print("no hay numeros")
else:
	n=0
	for i in range(x,y+1,x):
		n+=1
		creartxt(str(i))
		cadena.append(str(i))

cadena=str(cadena).replace('[',"")
cadena=str(cadena).replace(']',"")
print("hay n numeros"+str(x))
print(cadena)
pass
		






