from textblob import TextBlob

def creartxt(list):
    archi=open("textoeje4.txt","a")
    archi.write(list)
    archi.write("\n")
    archi.close()
    pass

frase=str(input("ingrese la palabra a traducir\n"))
print("tu palabra es:")
print(frase)
print("tu traduccion es: ")
traduc=TextBlob(frase)
traduc.translate(to="en")
print (traduc.translate(to="en"))
creartxt(frase)