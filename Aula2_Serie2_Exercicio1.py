num = int(input('Qual o numero que pretende visualizar na sequencia de Firbonacci: '))
t1 = 1
t2 = 1
print(t1, '- ',t2, '- ', end= '')
cont = 3
while cont <= num:
    t3 = t1 + t2
    print(t3, '- ', end= '')
    t1 = t2
    t2 = t3
    cont = cont + 1


