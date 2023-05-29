import os
print('Para SOMA prima 1')
print('Para SUBTRAÇÃO prima 2')
print('Para MULTIPLICAÇÃO prima 3')
print('Para DIVISÃO prima 4')
print('------------------------')
escolha=int (input('Qual a sua escolha?'))
num1 = int(input('Introduza o 1º numero: '))
num2 = int(input('Introduza o 2º numero: '))
if escolha == 1:
    print('A Soma de %d mais %d é:'%(num1,num2), num1 + num2)
elif escolha == 2:
     print('A Subtração de %d menos %d é:'%(num1,num2), num1 - num2)
elif escolha == 3:
    print('A Multiplicação de %d vezes %d é:'%(num1,num2), num1 * num2)
elif escolha == 4:
    print('A Divisão de %d a dvidir por %d é:'%(num1,num2), num1 / num2)
os.system('cls')