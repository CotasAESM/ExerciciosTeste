# Escreva um programa que leia um número N Em sequência, ele deve ser N números e armazená los numa lista
import random
num=int(input('Introduza o numero: '))
lista=[]
for i in range(num):
    rand=random.randint(0,100)
    lista.append(rand)
print('A lista ficará da seguinte forma: \n',lista)