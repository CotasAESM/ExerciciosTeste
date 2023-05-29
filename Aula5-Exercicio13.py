#Os automóveis mais recentes mostram a distância que é possível percorrer até ser necessário um reabastecimento.
# Pretende se criar esta funcionalidade em Python através da classe automóvel Esta classe é construída indicando a capacidade do depósito,
# a quantidade de combustível no depósito e o consumo do automóvel em litros aos 100 km. A classe automóvel apresenta os seguintes métodos:
# • combustivel devolve a quantidade de combustível no depósito
# • autonomia devolve o numero de Km que é possível percorrer com o combustível no depósito
# • abastece( n_litros aumenta em n_litros o combustível no depósito Se este abastecimento exceder a capacidade do depósito,
#um erro e não aumenta a quantidade de combustível no depósito
# • percorre( n_km percorre n_km Km, desde que a quantidade de combustível no depósito o permita, em caso contrário gera um
# e o trajeto não é efetuado
import os
class auto_med:
    def __init__(self, capacidade, consumo):
        self.capacidade = capacidade
        self.quantidade_combustivel = 0
        self.consumo = consumo

    def combustivel(self): #metodo de indicação da quantidade combustivel
        return self.quantidade_combustivel
    def autonomia(self): #metodo de calculo de comsumo de combustivel por cada 100KM
        return self.quantidade_combustivel * 100 / self.consumo
    def abastece(self, n_litros): #metodo de adicionar combustivel com validação da capacidade do depósito
        if self.quantidade_combustivel + n_litros > self.capacidade:
            raise ValueError("O depósito não tem dimensão suficiente para a quantidade de combustivel pretnido.")
        else:
            self.quantidade_combustivel += n_litros
    def percorre(self, n_km): #metodo de calculo no numero de KM possiveis com o combustivel que existe em depósito com validação da autonomia
        autonomia = (self.quantidade_combustivel * 100) / self.consumo
        if autonomia < n_km:
            raise ValueError("Não compbustivel suficiente.")
        else:
            self.quantidade_combustivel -= (n_km * self.consumo)/100
            return n_km

c = auto_med(60, 8)
while True:
        os.system('pause')
        os.system('cls')
        print(f"\nDepósito p/{c.capacidade}Lts. \nConsumo médio de {c.consumo} Lts/100km")
        print("\nEscolha uma opção:")
        print("""
                \t1. Abastecer
                \t2. Nivel de combustível
                \t3. Autonomia
                \t4. Percorrer uma distância
                \t0. Exit/Quit
                """)
        escolha = input("\nQual a sua pretenção: ")
        if escolha == "1":
            n_litros = float(input("Quantos litros deseja abastecer? "))
            try:
                c.abastece(n_litros)
                print("Abastecido com sucesso.")
            except ValueError as e:
                print(e)
        elif escolha == "2":
            print(f"O depósito tem: {c.combustivel()} litros")
        elif escolha == "3":
            print(f"Autonomia para {c.autonomia()} km")
        elif escolha == "4":
            n_km = float(input("Qual a distância a percorrer? "))
            try:
                km_percorridos = c.percorre(n_km)
                print(f"Distância percorrida: {km_percorridos} km")
            except ValueError as e:
                print(e)
        elif escolha == "0":
            break
        else:
            print("Escolha uma das opções do menu.")
        

