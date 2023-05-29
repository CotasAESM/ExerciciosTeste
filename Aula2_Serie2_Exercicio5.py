num=int(input('Introduza um numero para cálculo do fatorial: '))
res=num
fact=1
while num > 0:
    fact =fact*num
    num=num-1
print('O fatorial de %i é %i' %(res,fact))