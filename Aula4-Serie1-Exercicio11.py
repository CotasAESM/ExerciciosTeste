#Faça um programa que leia uma lista L com valores informados pelo utilizador e gere uma nova lista cujos valores
# consistem do dobro dos valores lidos
L=[]
num = int(input("Digite o número de valores que deseja inserir na lista: ")) # pede a quantidade de valores ao utlizador
L=[input(f"{x+1}ºnum: ") for x in range (num) ] #pede os valores ao utlizador
Ldobro=[int(x)*2 for x in L] # calculo do dobro de cada valor da lista
print('O dobro dos valores inseridos é: ',Ldobro) #print esfuado noutra linha para ter a representação de uma lista com []
