import os
os.system('cls')
escolha = True
while escolha:

    print("""
        \t1. Calculo de valor de angulos
        \t2. Cálculo das horas
        \t3. Calculos matemáticos básicos
        \t4. Firbonacci
        \t5. Fatorial 9 Ciclo For
        \t6. Fatorial 9 Cilo While
        \t7. Calculos matemáticos básicos com menu
        \t8. Fatorial de um numero à escolha
        \t9. Alternativa ao swtich em liguagem C
        \t0.Exit/Quit
        """)
    escolha = int(input('Escolha uma opção?'))
    if escolha==1:
        os.system('cls')
        import Aula1_Exercicio1
    elif escolha==2:
        os.system('cls')
        import Aula2_Serie1_Exercicio1
    elif escolha==3:
        os.system('cls')
        import Aula2_Serie1_Exercicio2
    elif escolha==4:
        os.system('cls')
        import Aula2_Serie2_Exercicio1
    elif escolha==5:
        os.system('cls')
        import Aula2_Serie2_Exercicio2
    elif escolha==6:
        os.system('cls')
        import Aula2_Serie2_Exercicio3
    elif escolha==7:
        os.system('cls')
        import Aula2_Serie2_Exercicio4
    elif escolha==8:
        os.system('cls')
        import Aula2_Serie2_Exercicio5
    elif escolha==9:
        os.system('cls')
        import Aula2_Serie2_Exercicio6
    elif escolha != '':
        os.system('cls')
        print('A opção escolhida não existe')