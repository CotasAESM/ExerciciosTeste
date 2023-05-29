from tkinter import *
from tkinter import messagebox, colorchooser
from tkinter import filedialog
from tkinter import simpledialog
import os
from tkinter.ttk import Combobox
from collections import Counter, defaultdict
import enum
from tkinter import colorchooser
from datetime import date, datetime

ws=Tk()
ws.title("Gestao de clientes")
ws.geometry("600x300")

# função para limpar widgets da frame
def limpar():
    for widget in ws.winfo_children():
        if not isinstance(widget, Menu):
             widget.destroy()

# função para criar cliente
def criar():
    ws.title("Gestao de clientes")
    ws.geometry("600x300")
    limpar()
    label_numero = Label(ws, text="Número de cliente:", width=20, height=1, font=('arial', 10, 'bold'))
    label_numero.grid(row=0, column=0,sticky="w")
    numero_entry = Entry(ws)
    numero_entry.grid(row=0, column=1,sticky="e")
    numero_entry.configure(width=10)

    label_nome = Label(ws, text="Nome de cliente:",width=20, height=1,font=('arial', 10, 'bold'))
    label_nome.grid(row=2, column=0,sticky="w")
    nome_entry = Entry(ws)
    nome_entry.grid(row=2, column=1,sticky="e")
    nome_entry.configure(width=50)

    label_telefone = Label(ws, text="Morada de cliente:",width=20, height=1,font=('arial', 10, 'bold'))
    label_telefone.grid(row=4, column=0,sticky="w")
    morada_entry = Entry(ws)
    morada_entry.grid(row=4, column=1,sticky="e")
    morada_entry.configure(width=50)

    def registar():
        f_cliente = 'Aula8_Trabalho\cliente.txt'
        numero = numero_entry.get()
        nome = nome_entry.get()
        morada = morada_entry.get()
        if numero and nome and morada:
            numero_entry.delete(0, END)
            nome_entry.delete(0, END)
            morada_entry.delete(0, END)
            with open(f_cliente, "a") as f:
                f.write(f"{numero},{nome},{morada}\n")
            messagebox.showinfo("Cliente", f"Contato {nome} cadastrado com sucesso!")

    registar_button = Button(ws, text="Criar Cliente", command=registar,width=10, height=2,font=('arial', 12))
    registar_button.grid(row=6, column=0)
# função para alterar cliente
def alterar():
    f_cliente = 'Aula8_Trabalho\cliente.txt'
    limpar()

    def modificar():
        numero_alterar = simpledialog.askstring("Modificar cliente", "Insira o número do cliente que deseja modificar:")
        if not numero_alterar:
            return
        novo_conteudo = []
        with open(f_cliente, "r") as f:
            for linha in f:
                numero, nome, morada = linha.strip().split(",")
                if numero == numero_alterar:
                    nome_alterar = simpledialog.askstring("Modificar cliente",
                                                            f"Insira o novo nome do cliente (atual: {nome}):")
                    morada_alterar = simpledialog.askstring("Modificar cliente",
                                                              f"Insira a nova morada do cliente (atual: {morada}):")
                    if not nome_alterar or not morada_alterar:
                        continue
                    linha = f"{numero_alterar},{nome_alterar},{morada_alterar}\n"
                    messagebox.showinfo("Cliente","Contato {nome} modificado com sucesso")
                novo_conteudo.append(linha)
        novo_arquivo = f_cliente + ".new"
        with open(novo_arquivo, "w") as f:
            f.writelines(novo_conteudo)
        os.replace(novo_arquivo, f_cliente)

    alterar_botao = Button(ws, text="Modificar Cliente", command=modificar, width=15, height=2,font=('arial', 12))
    alterar_botao.grid(row=6, column=4)

# função para eliminar cliente
def eliminar():
    limpar()
    def apagar():
        f_cliente = 'Aula8_Trabalho\cliente.txt'
        numero_apagar = simpledialog.askstring("Apagar cliente",
                                                "Insira o número do cliente que deseja apagar:")
        if not numero_apagar:
            return
        with open(f_cliente, "r") as arquivo, open("Aula8_Trabalho\cliente_temp.txt", "w") as arquivo_temp:
            encontrado = False
            for linha in arquivo:
                if linha.startswith(numero_apagar + ","):
                    encontrado = True
                else:
                    arquivo_temp.write(linha)

            if encontrado:
                os.remove("Aula8_Trabalho\cliente.txt")
                os.rename("Aula8_Trabalho\cliente_temp.txt", "Aula8_Trabalho\cliente.txt")
                messagebox.showinfo("Cliente","Cliente", f"Cliente {numero_apagar} removido com sucesso!")
            else:
                os.remove("Aula8_Trabalho\cliente_temp.txt")
                messagebox.showinfo("Cliente","Cliente {numero_apagar} não encontrado")

    apagar_botao = Button(ws, text="Apagar Cliente", command=apagar, width=15, height=2,font=('arial', 12))
    apagar_botao.grid(row=6, column=4)

# função para criar produtos (Código, designação e preço)
def criar_produto():
    ws.title("Criação de produtos")
    ws.geometry("600x300")
    limpar()
    label_codigo = Label(ws, text="Código de produto:", width=20, height=1, font=('arial', 10, 'bold'))
    label_codigo.grid(row=0, column=0,sticky="w")
    codigo_entry = Entry(ws)
    codigo_entry.grid(row=0, column=1,sticky="e")
    codigo_entry.configure(width=10)

    label_nome = Label(ws, text="Nome de produto:",width=20, height=1,font=('arial', 10, 'bold'))
    label_nome.grid(row=2, column=0,sticky="w")
    nome_entry = Entry(ws)
    nome_entry.grid(row=2, column=1,sticky="e")
    nome_entry.configure(width=50)

    label_preco = Label(ws, text="Preço de produto:",width=20, height=1,font=('arial', 10, 'bold'))
    label_preco.grid(row=4, column=0,sticky="w")
    preco_entry = Entry(ws)
    preco_entry.grid(row=4, column=1,sticky="e")
    preco_entry.configure(width=10)

    def registar():
        f_produto = 'Aula8_Trabalho\produto.txt'
        codigo = codigo_entry.get()
        nome = nome_entry.get()
        preco = preco_entry.get()
        if codigo and nome and preco:
            codigo_entry.delete(0, END)
            nome_entry.delete(0, END)
            preco_entry.delete(0, END)
            with open(f_produto, "a") as f:
                f.write(f"{codigo},{nome},{preco}\n")
            messagebox.showinfo("Produto","Produto {nome} inserido com sucesso")

    registar_button = Button(ws, text="Criar Produto", command=registar,width=10, height=2,font=('arial', 12))
    registar_button.grid(row=6, column=0)

# Funçaõ para registar compra do cliente (Número do cliente, Data, código do produto e preço
def registrar_compra():
    ws.title("Gestao de clientes")
    ws.geometry("600x300")
    limpar()
    label_nome_cliente = Label(ws, text="Número de cliente:", width=20, height=1, font=('arial', 10, 'bold'))
    label_nome_cliente.grid(row=0, column=0, sticky="w")
    label_data = Label(ws, text="Data da compra:", width=20, height=1, font=('arial', 10, 'bold'))
    label_data.grid(row=1, column=0, sticky="w")
    data_entry = Entry(ws)
    data_entry.grid(row=1, column=1, sticky="e")
    data_entry.configure(width=10)
    data_atual = date.today()
    data_entry.insert(0, data_atual.strftime("%d/%m/%Y"))
    label_codigo_produto = Label(ws, text="Código de produto:", width=20, height=1, font=('arial', 10, 'bold'))
    label_codigo_produto.grid(row=2, column=0, sticky="w")
    label_preco = Label(ws, text="Preço de produto:", width=20, height=1, font=('arial', 10, 'bold'))
    label_preco.grid(row=3, column=0, sticky="w")
    preco_entry = Entry(ws)
    preco_entry.grid(row=3, column=1, sticky="e")
    preco_entry.configure(width=10)

    with open('Aula8_Trabalho\cliente.txt', 'r') as f:
        list_of_clients = [line.strip().split(",")[1] for line in f.readlines()]  # Ler clientes do arquivo
    combo_cliente = Combobox(ws, values=list_of_clients, width=20)
    combo_cliente.grid(row=0, column=1)

    with open('Aula8_Trabalho\produto.txt', 'r') as f:
        list_of_produto = [line.strip().split(",")[1] for line in f.readlines()] # Ler produtos do arquivo
        combo_produto = Combobox(ws, values=list_of_produto, width=20)
    combo_produto.grid(row=2, column=1)
    # if list_of_produto[1] == combo_produto:
    #     produto = list_of_produto[1]
    # preco = float(list_of_produto[2])

    def registar():
            f_compra = 'Aula8_Trabalho\compra.txt'
            nome_cliente = combo_cliente.get()
            data = data_entry.get()
            codigo_produto = combo_produto.get()
            preco = preco_entry.get()
            if nome_cliente and codigo_produto:
                combo_cliente.delete(0, END)
                combo_produto.delete(0, END)
                with open(f_compra, "a") as f:
                    f.write(f"{nome_cliente},{data},{codigo_produto},{preco}\n")
                messagebox.showinfo("Compra", f"Compra do cliente {nome_cliente} registada com sucesso!")

    registar_button = Button(ws, text="Registar compra", command=registar, width=15, height=2, font=('arial', 12))
    registar_button.grid(row=6, column=0)

# Função Mostrar histórico de compras realizadas pelo cliente, ordenado por data
def mostrar_historico_compras():
    limpar()
    nome_cliente = simpledialog.askstring("Mostrar Histórico", "Digite o nome do cliente:")
    if nome_cliente:
        with open('Aula8_Trabalho\compra.txt', 'r') as f:
            linhas = f.readlines()

    compras = [] # Armazenar as compras em uma lista

    for linha in linhas:
        numero, data, codigo_produto, preco = linha.strip().split(",")
        compras.append((numero, data, codigo_produto, preco))

    compras_cliente = [compra for compra in compras if compra[0] == nome_cliente] # Filtrar as compras pelo número do cliente desejado

    if compras_cliente:
        compras_cliente.sort(key=lambda compra: compra[1]) # Ordenar as compras por data
        historico_compras = "" # Exibir as informações das compras
        for compra in compras_cliente:
            numero, data, codigo_produto, preco = compra
            historico_compras += f"A  {data} comprou {codigo_produto} pelo preço de: {preco}\n"
        messagebox.showinfo("Histórico de Compras", historico_compras)
    else:
        messagebox.showinfo("Histórico de Compras", "Nenhuma compra encontrada para o cliente.")

# Função para escolher um cliente e mostrar os dias da semana em que mais compra (usar o enum)
class DiaSemana(enum.Enum):
    SEGUNDA = 'Segunda-feira'
    TERCA = 'Terça-feira'
    QUARTA = 'Quarta-feira'
    QUINTA = 'Quinta-feira'
    SEXTA = 'Sexta-feira'
    SABADO = 'Sábado'
    DOMINGO = 'Domingo'


def mostrar_dias_compras():
    nome_cliente = simpledialog.askstring("","Digite o nome do cliente:")

    if nome_cliente:
        with open('Aula8_Trabalho\compra.txt', 'r') as f:
            dias_semana = defaultdict(int)
            for line in f:
                data = line.strip().split(";")
                if data[0] == nome_cliente:
                    data_compra = datetime.strptime(data[1], "%d/%m/%Y")
                    dia_semana = data_compra.strftime("%A")
                    dias_semana[dia_semana] += 1
            if dias_semana:
                dias_semana_str = "\n".join([f"{i + 1}. {DiaSemana[dia]}: {quantidade}" for i, (dia, quantidade) in
                                             enumerate(dias_semana.items())])
                messagebox.showinfo("Dias da Semana", dias_semana_str)
            else:
                messagebox.showinfo("Dias da Semana", f"Nenhuma compra encontrada para o cliente {nome_cliente}")

#Funão para criem um ficheiro com os gostos do cliente (cor, produto)
def criar_gostos_cliente():
    nome_cliente = simpledialog.askstring("","Digite o nome do cliente?") # Solicitar o nome do cliente

    gostos_cliente = {} # Criar um dicionário para armazenar os gostos do cliente

    cor_favorita = simpledialog.askstring("","Qual a sua cor favorita?")
    gostos_cliente['cor'] = cor_favorita

    produto_favorito = simpledialog.askstring("","Qual o seu produto favorito?") # Solicitar o produto favorito do cliente
    gostos_cliente['produto'] = produto_favorito

    diretorio = os.path.join(os.getcwd(), "Aula8_Trabalho") # Salvar os gostos do cliente num arquivo indicando o caminho
    nome_ficheiro = os.path.join(diretorio, f"gostos_{nome_cliente}.txt")
    with open(nome_ficheiro, 'w') as f:
        f.write(f"O cliente {nome_cliente} gosta da cor {cor_favorita} e o seu produto preferido é {produto_favorito}\n")

    messagebox.showinfo("Preferências", f"O arquivo '{nome_ficheiro}' foi criado com os gostos do cliente.")

# função para alterem o programa para que a cor de fundo do ecrã seja a de gosto do cliente
def personalizar():
    cor = colorchooser.askcolor(title="Escolha uma cor")
    if cor[1] is not None:
        ws.configure(bg=cor[1])

menubar=Menu(ws,background='#ff8000',foreground='black', activebackground='white', activeforeground='black')
cliente=Menu(menubar,tearoff=0,font=("arial", 16))
cliente.add_command(label='Novo', command=criar,font=("arial", 12))
cliente.add_command(label='Aterar',command=alterar,font=("arial", 12))
cliente.add_command(label='Eliminar',command=eliminar,font=("arial", 12))
cliente.add_separator()
cliente.add_command(label='Preferências', command=criar_gostos_cliente,font=("arial", 12))
cliente.add_separator()
cliente.add_separator()
cliente.add_command(label='Personalizar', command=personalizar,font=("arial", 12))
cliente.add_separator()
cliente.add_command(label='Sair', command=ws.quit,font=("arial", 12))
menubar.add_cascade(label='Cliente',menu=cliente)

produto=Menu(menubar,tearoff=0,font=("arial", 16))
produto.add_command(label='Criar', command=criar_produto,font=("arial", 12))
produto.add_separator()
produto.add_command(label='Registar compra',command=registrar_compra,font=("arial", 12))
produto.add_command(label='Histório de compra',command=mostrar_historico_compras,font=("arial", 12))
produto.add_command(label='Estatistica de cliente',command=mostrar_dias_compras ,font=("arial", 12))
menubar.add_cascade(label='Produto',menu=produto)

ws.config(menu=menubar)
mainloop()

