# Faça um programa que leia seis valores numéricos atribuindo os à duas variáveis do tipo lista com três elementos
# cada. Cada variável representará um vetor, informe o produto escalarp e o produto vetorial destes vetores
import random
num=6
L_seis=[]
L_um=[]
L_dois=[]
for i in range(num):
    rand=random.randint(0,100)
    L_seis.append(rand)
    #print(L_seis)
    L_um=L_seis[0:3:1]
    L_dois=L_seis[3:6:1]
print('Lista original com 6 numeros-', L_seis)
print('Lista com os primiros 3 numeros-',L_um)
print('Lista com os segundos 3 numeros-',L_dois)
import numpy as np
v1 = np.array(L_um)
v2 = np.array(L_dois)
produto_escalar = np.dot(v1, v2)
print(produto_escalar)

