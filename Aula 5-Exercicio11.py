# Defina a classe estacionamento, que simula o funcionamento de um parque de estacionamento A criação de instâncias desta classe
# recebe um inteiro que determina a lotação do parque e devolve um objeto com os seguintes métodos entra(), corresponde à entrada de
# um carro sai(), corresponde à saída de um carro lugares() indica o número de lugares livres no estacionamento Por exemplo,
# ist estacionamento(20)
# ist lugares
# 20
# ist entra
# ist entra
# ist entra
# ist entra
# ist sai
# ist lugares
# 17
import os
class estacionamento:
    def __init__(self, lotacao):
        self.lotacao = lotacao
        self.vagas_disponiveis = lotacao
    def entra(self):
        if self.vagas_disponiveis == 0:
            print('O parque encntra-se cheio, de momento não existem vagas disponíveis.')
            os.system('pause')
        else:
            self.vagas_disponiveis -= 1
            print(f'De momento exitem {self.vagas_disponiveis} vagas disponíveis.')
            os.system('pause')
    def sai(self):
        if self.vagas_disponiveis == self.lotacao:
            print(f'O parque encontra-se vazio, encontram-se diponiveis {self.vagas_disponiveis} ')
            os.system('pause')
        else:
            self.vagas_disponiveis += 1
            print("Veículo saiu do parque de estacionamento. Vagas disponíveis:", self.vagas_disponiveis)
            os.system('pause')

e=estacionamento(20)
print(f'Este estacionamento tem capacidade para {e.lotacao} lugares de estacionamento')
print(f'Existem {e.lotacao} lugares vagos.')
os.system('pause')
escolha = True
while escolha !=0:
    os.system('cls')
    print("""
        \t1. Entrada de veiculo
        \t2. Saida de veiculo
        \t0.Exit/Quit
        """)
    escolha = int(input('Escolha uma opção?'))
    if escolha==1:
        os.system('cls')
        e.entra()
    elif escolha==2:
        os.system('cls')
        e.sai()
    elif escolha != '':
        os.system('cls')
        print('Obrigado pelo visita')
        os.system('pause')

