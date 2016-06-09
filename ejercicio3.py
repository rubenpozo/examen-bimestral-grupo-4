from tkinter import *
contador2=0
contador= 0
archi= open('archivooriginal.txt','r')
Linea = archi.read()
#Linea= "hola qur ,mas\n"+"que tal"
for renglon in range(len(Linea)):
	if(Linea[renglon]==" "):
		contador=contador+1
	if(Linea[renglon]=="\n"):
		contador2=contador2+1

def call():
	archi2=open('datos.txt','r')
	linea=archi2.read()
	li = linea.split(',')
	listb = Listbox(root,width=40, height=10)
	for item in li:
		listb.insert(len(li),item)
	listb.pack()
	

print(contador) 
print(contador2)
informacion= ("Palabras:"+ str(contador)+(",saltos de linea:")+str(contador2))
archi=open('datos.txt','w')
archi.write(informacion)
archi.close()

root = Tk()

root.geometry('100x110+350+70')
boton = Button(root,text='presionar',command=call)
boton.pack()
root.mainloop()