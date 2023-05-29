#Faça um programa que receba a temperatura média de cada mês do ano e armazene as em uma lista Em seguida, calcule a
#média anual das temperaturas e mostre a média calculada juntamente com todas as temperaturas acima da média anual, e
#em que mês elas ocorreram (mostrar o mês por extenso 1 Janeiro, 2 Fevereiro,....)
import random
Lmes=['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
Ltemp=[random.randint(5,40) for i in range(12)]
media = sum(Ltemp)/len(Ltemp)
print("A temperatura de média de cada mês foi: ",Ltemp)
print("A temperatura de média do ano foi: ",media)
Lindex=[Ltemp.index(x) for x in Ltemp if x>media] #encontra a(s) posição em que a temperatura é superior à média
Lmedia=[x for x in Ltemp if x>media] #encontra o(s) meses em que a temperatura é superior à média
Lf = [print(f"{m} , {t}") for m, t in zip(Lmes, Ltemp) if t > media]
