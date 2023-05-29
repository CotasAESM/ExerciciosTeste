# 1 -Defina uma classe chamada fracao que contém dois atributos, num e den inicializados com os valores que quiser
class fracao():
    num=12
    den=2
# 2- Adicione a classe fracao o método de inicialização, em que os dois parâmetros passados na definição sejam referentes
# a num e den respetivamente
    def __init__(self,num=0,den=1):
        self.num = num
        self.den = den

# 3- Adicione também o método especial de impressão, para que a classe seja mostrada do tipo " den
    def __str__(self):
        return f'{self.num}/{self.den}'
# 4- Adicione a sobrecarga de operadores para realizar as quatro operações matemáticas básicas, de modo que, por exemplo,
# dois objetos A # B, resultem em uma terceira fracao Não se preocupe em simplificar as frações
    def __add__(self, other):
        num=self.num*other.den+self.den*other.num
        den=self.den*other.den
        return fracao(num, den)
    def __sub__(self, other):
        num = self.num * other.den - self.den * other.num
        den = self.den * other.den
        return fracao(num, den)
    def __mul__(self, other):
        num = self.num * other.num
        den = self.den * other.den
        return fracao(num, den)
    def __truediv__(self, other):
        num = self.num * other.den
        den = self.den * other.num
        return fracao(num, den)
# 5 - Adicione os métodos de conversão, isto é, se A for um objeto do tipo fracao faça com que int (A) retorne um inteiro,
# float (A) retorne um float e bool (A) retorne um booleano. Utilize os critérios que julgar mais conveniente
# Obs str (A) já irá retornar uma string pois este método foi definido na questão 3
    def __int__(self):
        return self.num//self.den
    def __float__(self):
        return self.num/self.den
    def __bool__(self):
        return (self.num//self.den) !=0
# 6 - Adicione um método estático responsável por simplificar a uma fração qualquer, isto é, dado dois valores a e b, encontre
# a fração irredutível que represente a/b. Depois, adicione o método de simplificação no método construtor da classe
    @staticmethod
    def simplificar(self):
        def mdc(a,b):
            while b:
                a,b=b,a%b
            return a

        dc = mdc(self.num,self.den)
        self.num = self.num // dc
        self.den = self.den // dc


# Saida de dados do exercicios 1, 2 e 3

num1= int(input(' Introduza o valor do numerador da primeira fração'))
den1= int(input(' Introduza o valor do denominador da primeira fração'))
num2= int(input(' Introduza o valor do numerador da segunda fração'))
den2= int(input(' Introduza o valor do denominador da segunda fração'))
F1=fracao(num1,den1)
F2=fracao(num2,den2)
try:
    if den1 ==0 or den2==0:
        raise ValueError ('ERRO - O denominador não pode ser zero')
    else:
        print('A primeira fração  é: ',F1)
        print('A segunda fração é: ',F2)

        # Saida de dados do exercicios 4
        Fsoma= F1.__add__(F2)
        print('A soma das frações F1 e F2 é: ',Fsoma)
        Fsubtracao= F1.__sub__(F2)
        print('A subtração das frações F1 e F2 é: ',Fsubtracao)
        Fmultiplicacao= F1.__mul__(F2)
        print('A multiplicação das frações F1 e F2 é: ',Fmultiplicacao)
        Fdivisao= F1.__truediv__(F2)
        print('A divisão das frações F1 e F2 é: ',Fdivisao)

        # Saida de dados do exercicios 5
        print('O resultado inteiro da fração "Fsoma" é: ',Fsoma.__int__())
        print('O resultado decimal da fração "Fsoma" é: ',Fsoma.__float__())
        print('O resultado inteiro da fração "Fsoma" é: ',Fsoma.__bool__())

        # Saida de dados do exercicios 6
        F1.simplificar(F1)
        F2.simplificar(F2)
        print(f'Resultado apresentado com o metodo estático da fração 1 é {F1} e da fração 2 é {F2}')
except ValueError as erro:
    print(erro)