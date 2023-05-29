# Crie um Python Script que conte quantas vezes cada nome está presente em uma lista [’nome 1 ’,’,’nome 2 e armazena essa contagem
# num dicionário {’nome 1 xvezes ,,’nome 2 yvezes

L_nomes=['João','Nelson','Gonçalo','Rui','Nelson','Nelson']
D_nomes={}
for i in L_nomes:
    if i not in D_nomes:
        D_nomes_temp = {i: L_nomes.count(i)}
        #print(D_nomes_temp)
        D_nomes.update(D_nomes_temp)
        D_nomes_temp.clear()
print(D_nomes)






