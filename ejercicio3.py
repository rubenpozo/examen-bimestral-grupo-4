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