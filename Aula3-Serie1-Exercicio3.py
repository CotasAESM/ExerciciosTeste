# Crie um programa que lê uma mensagem do utilizador Com esta mensagem, faça uma nova omitindo/trocando
# todos os caracteres de nomes próprios por Exemplo se a mensagem for
# ’Lucas foi ao shopping com Fernanda assistir ver um filme da Marvel’, a nova mensagem deverá ser foi ao
# shopping com ver um filme da Assuma que um nome próprio começa sempre com letra maiúscula e contém
# apenas letras

frase=str(input('Escreva uma frase: \n'))
for i in frase.split():
    print('1-',frase)
    if i[0].isupper() and i.isalpha():
        frase = frase.replace(i,'*'*len(i))
        print('2-',frase)
print('Mensagem editada:\n',frase)
