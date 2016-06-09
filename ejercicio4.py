from textblob import TextBlob

def traduccion(text):
    traduc=TextBlob(text)
    return traduc.translate(to="en")


frase=str(input("ingrese la frase a traducir\n"))
print("tu frase es:")
print(frase)
print("tu traduccion es: ")  
print(traduccion(frase))

def creartxt():
	archi=open('traducido.txt', 'w')
	archi.close()

texto= traduccion(frase)

def grabartxt():
	archi=open('traducido.txt', 'a')
	archi.write(str(texto))
	archi.close()

creartxt()
grabartxt()


