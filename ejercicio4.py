from textblob import TextBlob

def traduccion(text):
    traduc=TextBlob(text)
    print (traduc.translate(to="en"))

frase=str(input("ingrese la frase a traducir\n"))
print("tu frase es:")
print(frase)
print("tu traduccion es: ")  
traduccion(frase)

def creartxt():
	archi=open('datos.txt', 'w')
	archi.close()

def grabartxt():
	archi=open('datos.txt', 'a')
	archi.write('linea1 \n')
	archi.close()

