# Com o programa acima, imprima A soma dos itens, a média dos valores, o maior e o menor valor
import random
num=int(input('Introduza o numero: '))
lista=[]
for i in range(num):
    rand=random.randint(0,100)
    lista.append(rand)

print('A lista ficará da seguinte forma: \n',lista)
print('O menor valor é:', min(lista))
print('O maior valor é:', max(lista))
print('A soma de todos os valores é:', sum(lista))
print('A média de todos os valores é:', (sum(lista))/num)
