#Faça um programa que crie uma matriz aleatoriamente. O tamanho da matriz deve ser informado pelo utilizador
import random
L=[]
numl = int(input("Introduza o numero de linhas da matriz "))
numc = int(input("Introduza o numero de colunas da matriz "))
Lf=[[(random.randint(0,100),random.randint(0,100)) for x in range(numl)] for y in range(numc)]
print(Lf)
#Lf=[print(f"[({random.randint(0,100)})],({random.randint(0,100)})", end='') for x in range(numl) for y in range(numc)]
# print encadeado mas a represenção da matriz não é a melhor pois os valores estão dentro do ciclo