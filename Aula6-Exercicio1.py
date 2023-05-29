# Soma de inteiros - Crie uma interface com dois campos de entrada e um Label. Os dois campos servirão para a entrada
# de dois inteiros, um em cada campo, e o Label servirá para aplicar o evento de clique com o botão esquerdo do mouse,
# a fim de somar os dois inteiros das entradas e na label o resultado

from tkinter import *
def soma():
    a = int(entrada1.get())
    b = int(entrada2.get())
    res.config(text=str(a+b),font=('arial',10,'bold'))

# Cria a frame
master = Tk()
master.title('Soma de inteiros')
p1=Label(master, text='Primeiro Inteiro',width=15, height=5)
p1.grid(row=0)
p2=Label(master, text='Segundo Inteiro',width=15, height=5)
p2.grid(row=1)
entrada1 = Entry(master)
entrada1.grid(row=0, column=1)
entrada2 = Entry(master)
entrada2.grid(row=1, column=1)

button = Button(master, text='Somar', width=25, command=soma)
button.grid(row=3, column=1)

res=Label(master, text='',width=15, height=5)
res.grid(row=5,column=1)

mainloop()
