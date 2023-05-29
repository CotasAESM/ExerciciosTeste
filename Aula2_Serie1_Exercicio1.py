tempo = int(input('Digite o numero de segundos que pretende calcular: '))
if (tempo // 3600 > 0):
    horas = int(tempo // 3600)
    minutos = int((tempo - (horas * 3600)) // 60)
    segundos = int(tempo - (horas * 3600) - (minutos * 60))
    dias = int((tempo // 3600)//24)
print('\tDias: ', dias,'\n','\tHoras: ', horas, '\n', '\tMinutos: ', minutos, '\n', '\tSegundos: ', segundos, '\n')