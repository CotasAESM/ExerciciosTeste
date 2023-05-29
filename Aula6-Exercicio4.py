# Agenda telefónica - Crie um programa para uma simples lista telefônica. O objetivo é possibilitar ao utilizador a
# inserção de duas informações: o nome e o telefone do novo contato.
# Em seguida, ao clicar no botão “cadastrar” será ativado um FileDialog que possibilite a criação de um novo arquivo
# para o guardar os dados. Além disso, verifique a cada nova inserção se o utilizador já possui um arquivo para guardar
# os dados criados, evitando que a cada novo contato seja aberto num novo fileDialog, através de uma variável de controle.

from tkinter import *
from tkinter import filedialog

class ListaTelefonica:
    def __init__(self, master):
        self.master = master
        self.master.title("Lista Telefónica")
        self.master.geometry("500x400")

        self.label_nome = Label(master, text="Nome:",width=10, height=5,font=('arial', 20, 'bold'))
        self.label_nome.grid(row=1, column=0)
        self.nome_entry = Entry(master)
        self.nome_entry.grid(row=1, column=1)
        self.nome_entry.configure(width=50)

        self.label_telefone = Label(master, text="Telefone:",width=10, height=5,font=('arial', 20, 'bold'))
        self.label_telefone.grid(row=3, column=0)
        self.telefone_entry = Entry(master)
        self.telefone_entry.grid(row=3, column=1,sticky="e")
        self.telefone_entry.configure(width=20)

        self.registar_button = Button(master, text="Registar", command=self.cadastrar,width=15, height=2,font=('arial', 14))
        self.registar_button.grid(row=5, column=0)

        self.arquivo = None

    def cadastrar(self):
        nome = self.nome_entry.get()
        telefone = self.telefone_entry.get()
        if nome and telefone:
            self.nome_entry.delete(0, END)
            self.telefone_entry.delete(0, END)
            if not self.arquivo:
                self.arquivo = filedialog.asksaveasfilename(defaultextension=".txt")
            with open(self.arquivo, "a") as f:
                f.write(f"{nome},{telefone}\n")
            print(f"Contato {nome} cadastrado com sucesso!")


if __name__ == "__main__":
    master = Tk()
    app = ListaTelefonica(master)
    master.mainloop()
