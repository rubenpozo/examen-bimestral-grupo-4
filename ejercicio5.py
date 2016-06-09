from tkinter import *
import tkinter.messagebox
import math

def area():
	n1=float(caja1.get())
	suma=4*math.pi*n1*n1
	tkinter.messagebox.showinfo("Mensaje","El resultado es: %.2f"%suma)
	caja1.delete(0, 20)
	caja2.delete(0, 20)

def volumen():
	n1=float(caja1.get())
	suma=(4/3)*math.pi*n1*n1*n1
	tkinter.messagebox.showinfo("Mensaje","El resultado es: %.2f"%suma)
	caja1.delete(0, 20)
	caja2.delete(0, 20)

gui=Tk()
gui.title("Area y Volumen de una esfera")
gui.geometry("400x250+400+200")

var1=StringVar()
var1.set("Ingresa el radio:")
label1= Label(gui, bd=4, textvariable=var1, height=2)
label1.pack()

numero1=StringVar()
caja1=Entry(gui, bd=4, textvariable=numero1)
caja1.pack()


boton1=Button(gui, text="Area", command=area, width=15)
boton1.pack()

boton1=Button(gui, text="Volumen", command=volumen, width=15)
boton1.pack()