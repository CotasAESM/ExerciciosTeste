#Ler uma lista de 10 números reais e mostre os na ordem inversa
L=[]
print('O números da lista escritos da forma inversa são:')
L=[x for x in range(10,0,-1)]
print(L) # o print foi feito fora para que tenha respresentação da lista tenha os []
#L=[print(f" {x} ", end=',') for x in range(10,0,-1)] # print dentro da lista se []