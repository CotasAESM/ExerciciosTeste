class fracao():

# 7 - Refine ainda mais a classe faça com que a classe possa ser instanciada num objeto com nenhum parâmetro, atribuindo 0 1,
# instanciada com apenas um parâmetro inteiro qualquer n, atribuindo n/ 1 à ela e melhorando a simplificação para que atribua, caso
# necessário, sinal negativo apenas para o numerador
    def __init__(self,num=0,den=1): # instanciar os atributos para o exercicio 7
        try:
            if den !=0:
                self.num = num
                self.den = den
            else:
                raise ValueError ('O denominador não pode ser zero.')
        except ValueError as erro:
            print(erro)

    def __str__(self):
        return f'{self.num}/{self.den}'
    @staticmethod
    def simplificar(self):
        def mdc(a, b):
            while b:
                a, b = b, a % b
            return a
    
        dc = mdc(self.num, self.den)
        self.num = self.num // dc
        self.den = self.den // dc
# 8 - Altere os métodos de sobrecarga de operadores para que suportem também operações com inteiros, isto é, para que A/B seja válido,
# sendo A um objeto fracao e B um objeto int Sugestões utilize a função type para verificar a classe, utilize exceções
    def __add__(self, other):
        if isinstance(other, int):
            num = self.num + other * self.den
            den = self.den
        elif isinstance(other, fracao):
            num = self.num * other.den + other.num * self.den
            den = self.den * other.den
        else:
            raise TypeError("O numero inserido não foi inteiro.")
        return fracao(num, den)
    def __sub__(self, other):
        if isinstance(other, int):
            num = self.num - other * self.den
            den = self.den
        elif isinstance(other, fracao):
            num = self.num * other.den - other.num * self.den
            den = self.den * other.den
        else:
            raise TypeError("O numero inserido não foi inteiro.")
        return fracao(num, den)
    def __mul__(self, other):
        if isinstance(other, int):
            num = self.num * other.num
            den = self.den * other.den
        elif isinstance(other, fracao):
            num = self.num * other.num
            den = self.den * other.den
        else:
            raise TypeError("O numero inserido não foi inteiro.")
        return fracao(num, den)
    def __truediv__(self, other):
        if isinstance(other, int):
            num = self.num * other.den
            den = self.den * other.num
        elif isinstance(other, fracao):
            num = self.num * other.den
            den = self.den * other.num
        else:
            raise TypeError("O numero inserido não foi inteiro.")
        return fracao(num, den)

    def __int__(self):
        return self.num//self.den
    def __float__(self):
        return self.num/self.den
    def __bool__(self):
        return (self.num//self.den) !=0

# 9 - Adicione os operadores unários, e a função abs à classe fracao
    def __invert__(self):
        return fracao(~self.num,self.den)
    def __neg__(self):
        return fracao(-self.num,self.den)
    def __abs__(self):
        num=abs(self.num)
        den=abs(self.den)
        return fracao(num,den)
# 10 - Adicione os operadores relacionais à classe fracao.
    def __eq__(self, other): #operador de igualdade
        return self.num * other.den == self.den * other.num
    def __ne__(self, other):#operador de diferença
        return self.num * other.den != self.den * other.num
    def __ge__(self, other): #operador de maior ou igual que
        return self.num * other.den >= self.den * other.num
    def __le__(self, other): #operador de menor ou igual que
        return self.num * other.den <= self.den * other.num

    
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
        # Saida de dados do exercicios 7
        print('Resultado Exercicio 7:',F1, F2)
        print('------------------------------------------------------------------------')
        # Saida de dados do exercicios 8
        Fsoma = F1.__add__(F2)
        print('A soma das frações F1 e F2 é: ',Fsoma)
        Fsubtracao= F1.__sub__(F2)
        print('A subtração das frações F1 e F2 é: ',Fsubtracao)
        Fmultiplicacao= F1.__mul__(F2)
        print('A multiplicação das frações F1 e F2 é: ',Fmultiplicacao)
        Fdivisao= F1.__truediv__(F2)
        print('A divisão das frações F1 e F2 é: ',Fdivisao)
        print('------------------------------------------------------------------------')
        # Saida de dados do exercicios 9
        print(f'Primeira Fração \n\tUnário da inversão: {F1.__invert__()} \n\tUnário da negação: {F1.__neg__()} \n\tUnário do valor absoluto: {F1.__abs__()}')
        print(f'Segunda Fração\n\tUnário da inversão: {F2.__invert__()} \n\tUnário da negação: {F2.__neg__()} \n\tUnário do valor absoluto: {F2.__abs__()}')
        print('------------------------------------------------------------------------')
        #Saida de dados do exercicio 10
        print(f'Fração1 é igual á Fração2? {F1.__eq__(F2)}\nFração1 é diferente á Fração2? { F1.__ne__(F2)}\nFração1 é menor ou igual á Fração2? {F1.__le__(F2)}\nFração1 é maior ou igual á Fração2? {F1.__ge__(F2)}')
except ValueError as erro:
    print(erro)
