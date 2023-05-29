#Ler uma lista com 4 notas, em seguida o programa deve mostrar as notas e a média
L=[10,12,14,16] #lista com valores de notas
L1=[print(f"A nota {L.index(x)+1} é: {x} ") for x in L] # mostra nova lista para fazer o ciclo de mostra de cada uma das notas
media = sum(L)/len(L) # calculo da média
print(f"A média das notas é: {media}") # impressão da média
