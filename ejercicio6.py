from tkinter import *
tk = Tk()
tk.title('TABLERO')
cont=0
for i in range (5):
	for j in range(5):
		if(cont%2==0 and i%2==0):
			if((j%2)==0):
				boton1 = Button(tk,text=" ",width=10, height=5,bg='white')
				boton1.grid(row=i,column=j)	
			else:
				boton1 = Button(tk,text=" ",width=10, height=5,bg='black')
				boton1.grid(row=i,column=j)
		else:
			if((j%2)==0):
				boton1 = Button(tk,text=" ",width=10, height=5,bg='black')
				boton1.grid(row=i,column=j)	
			else:
				boton1 = Button(tk,text=" ",width=10, height=5,bg='white')
				boton1.grid(row=i,column=j)
	
	cont=cont+1
print(cont)
tk.mainloop()