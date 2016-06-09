
def leertxt():
    archi=open('textoej3.txt','r')
    linea=archi.readline()
    palabra=''
    contador=0
    while linea!="":
        print (linea)
        contador=contador+1
        for i in range (len(linea)):
        	if(linea[i]==' '):
        		contador = contador + 1	
        print(contador)		
        linea=archi.readline()
    archi.close()
    return contador	
palabra=leertxt()

print('encontro: '+str(palabra)+' palabras')

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

