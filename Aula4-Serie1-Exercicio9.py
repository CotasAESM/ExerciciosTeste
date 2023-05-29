#Inicialize uma lista de 20 números inteiros Usando compreensão de listas, armazene os números pares em uma lista PAR e os
#números ímpares em uma lista IMPAR Imprima as listas PAR e IMPAR
import random
L=[random.randint(0,100) for i in range(20)]
L1=[x for x in L if x%2==0] #lista para calculo dos lumeros pares
L2=[x for x in L if x%2 != 0] #lista para calculo dos numeros impares
print(f"Os números PARES são {L1} \nOs números IMPARES são {L2}") #impressão dos dois
