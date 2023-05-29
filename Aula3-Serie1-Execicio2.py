# Crie um Python Script que realize o mesmo procedimento da questão anterior No entanto, ao invés do conteúdo da lista nomes ser
# atribuído no próprio script, faça uma estrutura de repetição na qual ela leia uma string do utilizador e adicione os nomes digitados por
# ele, um de cada vez, na lista nomes O término da adição de nomes deve ser indicado quando o utilizador inserir uma string vazia
L_nomes=[]
D_nomes={}
nome=1
while 1:
    nome=str(input('Introduza um nome'))
    L_nomes.append(nome)
    if nome=='':
        break
print(L_nomes)

for i in L_nomes:
    if i not in D_nomes:
        D_nomes_temp = {i: L_nomes.count(i)}
        D_nomes.update(D_nomes_temp)
        D_nomes_temp.clear()
print(D_nomes)