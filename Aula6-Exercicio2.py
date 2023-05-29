#Conversor de tempo - Crie um programa utilizando Tkinter que, dado um tempo em segundos, converta este tempo em horas,
# minutos e segundos.

from tkinter import *
def tempo():
    segundos_final = int(entrada1.get())
    horas = int(segundos_final // 3600)
    minutos = int((segundos_final - (horas * 3600)) // 60)
    segundos = int(segundos_final - (horas * 3600) - (minutos * 60))
    res.config(text=f'{horas}:{minutos}:{segundos}', font=('arial', 10, 'bold'))

# Cria a frame
master = Tk()
master.title('Conversor de tempo')
p1=Label(master, text='Introduza o tempo em segundos',width=25, height=5)
p1.grid(row=0)
entrada1 = Entry(master)
entrada1.grid(row=1, column=0)

button = Button(master, text='Converter', width=25, command=tempo)
button.grid(row=2, column=0)

res=Label(master, text='',width=15, height=5)
res.grid(row=5,column=1)

mainloop()
