calc = 9
soma = 0
fact = 1
for calc in range(10,0,-1):
    fact = fact * calc
    # calc = calc - 1    Não é necessário pois no for é auto incrementado com o paço -1
print('O factorial de 9 é:', fact)