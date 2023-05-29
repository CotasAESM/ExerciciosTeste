valor=int(input('Digite o valor do angulo: '))
import math
radiano=float(math.radians(valor))
print('O valor em radianos é: ',radiano)
print('O valor do seno é: ',math.sin(radiano))
print('O valor do coseno é: ',math.cos(radiano))
print('O valor da tangente é: ',math.tan(radiano))
from numpy import deg2rad
print('O valor em radianos é: ',deg2rad(int(valor)))