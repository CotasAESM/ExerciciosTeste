import tkinter as tk
#1 - Criação de um botão
# r=tk.Tk()
# r.title('Countig Seconds')
# button=tk.Button(r,text='Stop', width=20,command=r.destroy)
# button.pack()
# r.mainloop()

#2 - Canvas desenhar imagens, graficos texto, widgets, etc
# from tkinter import *
# master=Tk()
# w=Canvas(master,width=40,height=60)
# w.pack()
# canvas_heigth=20
# canvas_whidth=200
# y=int(canvas_heigth/2)
# w.create_line(0,y,canvas_whidth,y)
# mainloop()

#3 - CheckButton selecionar qualquer numero de opções, exibido-as
# from tkinter import *
# master=Tk()
# master.title('Teste')
# var1=IntVar()
# Checkbutton(master,text='masculino',variable=var1).grid(row=0,sticky=W)
# var2=IntVar()
# Checkbutton(master,text='feminino',variable=var2).grid(row=1,sticky=W)
# var3=IntVar()
# Checkbutton(master,text='outro',variable=var3).grid(row=2,sticky=W)
# mainloop()

# 4 - Entrada é usado para inserir a entrada de linha de um utilizador
# from tkinter import *
# master=Tk()
# Label(master,text='Fist Name').grid(row=0)
# Label(master,text='Last Name').grid(row=1)
# e1=Entry(master)
# e2=Entry(master)
# e1.grid(row=0,column=1)
# e2.grid(row=1,column=1)
# mainloop()

# 5 - Frame recipiente para armazenar os widgets, arrumar e agurpa-los
# from tkinter import *
# root=Tk()
# frame=Frame(root)
# frame.pack()
# bottomframe=Frame(root)
# bottomframe.pack(side=BOTTOM)
# redbutton=Button(frame,text='Red',fg='red')
# redbutton.pack(side=LEFT)
# greenbutton=Button(frame,text='Brown',fg='brown')
# greenbutton.pack(side=RIGHT)
# bluebutton=Button(frame,text='Blue',fg='blue')
# bluebutton.pack(side=RIGHT)
# blackbutton=Button(frame,text='Black',fg='black')
# blackbutton.pack(side=LEFT)
# mainloop()

# 6 - Etiqueta
# from tkinter import *
# root=Tk()
# w=Label(root,text='Turma Informática')
# w.pack()
# root.mainloop()

# 7 - Caixa de Listagem (drop down)
# from tkinter import *
# top=Tk()
# Lb=Listbox(top)
# Lb.insert(1,'Pyton')
# Lb.insert(2,'Java')
# Lb.insert(3,'C')
# Lb.insert(4,'Any Other')
# Lb.pack()
# top.mainloop()

# 8 - Menu (botão menu)
# from tkinter import *
# from tkinter import messagebox
# ws=Tk()
# ws.title("Pyton Guides")
# ws.geometry("300x250")
#
# def about():
# messagebox.showinfo('PytonGuides','Pyton Guides aims at providing best practical toturials')
# menubar=Menu(ws,background='#ff8000',foreground='black', activebackground='white', activeforeground='black')
# file=Menu(menubar,tearoff=1,background='#ffcc99',foreground='black')
# file.add_command(label='Novo')
# file.add_command(label='Abrir')
# file.add_command(label='Guardar')
# file.add_command(label='Guardar como')
# file.add_separator()
# file.add_command(label='Sair', command=ws.quit)
# menubar.add_cascade(label='Ficheiro',menu=file)
#
# edit=Menu(menubar,tearoff=0)
# edit.add_command(label='Desfazer')
# edit.add_separator()
# edit.add_command(label='Cortar')
# edit.add_command(label='Copiar')
# edit.add_command(label='Colar')
# menubar.add_cascade(label='Editar',menu=edit)
#
# help=Menu(menubar,tearoff=0)
# help.add_command(label='Sobre', command=about)
# menubar.add_cascade(label='Ajuda',menu=help)
#
# ws.config(menu=menubar)
# ws.mainloop()

# 9 - Menu
# from tkinter import *
# root=Tk()
# menu=Menu(root)
# root.config(menu=menu)
# filemenu=Menu(menu)
# menu.add_cascade(label='Ficheiro',menu=filemenu)
# filemenu.add_command(label='Novo')
# filemenu.add_command(label='Abrir')
# filemenu.add_separator()
# filemenu.add_command(label='Sair',command=root.quit)
# helpmenu=Menu(menu)
# menu.add_cascade(label='Ajuda',menu=helpmenu)
# helpmenu.add_command(label='Sobre')
# mainloop()

# 10 - Mensagem (multilinha não editável)
# from tkinter import *
# main=Tk()
# ourMessage='A nossa mensagem'
# messageVar=Message(main,text=ourMessage)
# messageVar.config(bg='lightgreen')
# messageVar.pack()
# main.mainloop()

# 11 - Radio Button opção de escolha multipla
# from tkinter import *
# root=Tk()
# v=IntVar()
# Radiobutton(root,text='Opção1', variable=v,value=1).pack(anchor=W)
# Radiobutton(root,text='Opção2', variable=v,value=2).pack(anchor=W)
# Radiobutton(root,text='Opção3', variable=v,value=3).pack(anchor=W)
# Radiobutton(root,text='Opção4', variable=v,value=4).pack(anchor=W)
# mainloop()

# 12 - Escala exemplo zoom in /out
# from tkinter import *
# master=Tk()
# w=Scale(master,from_=0,to=42)
# w.pack()
# w=Scale(master,from_=0,to=200,orient=HORIZONTAL)
# w.pack()
# mainloop()


# 13 - Barra de Rolagem
# from tkinter import *
# root=Tk()
# scroolbar=Scrollbar(root)
# scroolbar.pack(side=RIGHT,fill=Y)
# mylist=Listbox(root,yscrollcommand=scroolbar.set)
# for line in range(100):
#     mylist.insert(END,'Linha '+ str(line))
# mylist.pack(side=LEFT,fill=BOTH)
# scroolbar.config(command=mylist.yview)
# mainloop()

# 14 - Texto editar várias linhas e formatar
# from tkinter import *
# root=Tk()
# T=Text(root,height=4,width=30)
# T.pack()
# T.insert(END,'IPT\nCurso Informática\n')
# T.insert(END,'IPT1\nCurso Informática1\n')
# mainloop()

# 15 - Top Level -n precisa de janela pai
# from tkinter import *
# root=Tk()
# root.title('IPT-Informática')
# top=Toplevel()
# top.title('Mafra')
# top.mainloop()

# 15 - SpinBox É uma entrada com setas para mudar a opção
# from tkinter import *
# master=Tk()
# w=Spinbox(master,from_=0,to=10)
# w.pack()
# mainloop()

# 16 - PannerWindow é um container
# from tkinter import *
# m1=PanedWindow()
# m1.pack(fill=BOTH,expand=1)
# left=Entry(m1,bd=5)
# m1.add(left)
# m2=PanedWindow(m1,orient=VERTICAL)
# m1.add(m2)
# top=Scale(m2,orient=HORIZONTAL)
# m2.add(top)
# mainloop()