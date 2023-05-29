#Suponha que desejava criar a classe racional Um número racional é qualquer número que possa ser expresso como o quociente
# de dois inteiros o num (um inteiro positivo, negativo ou nulo) e o den (um inteiro positivo ou negativo).
# Os racionais a/b e c/d iguais se e só se a d b c Assuma que a representação externa de um racional é apresentada de modo
# que o num e o den são primos entre si. A classe racional admite as operações nume e deno que devolvem,
# respetivamente o num e o den.
# (a) Defina a classe racional, incluindo o transformador de saída
class racional:
    def __init__(self, num, den): #metodo especial construtor para inicialização de uma nova classe
        self.num = num
        self.den = den
    def __str__(self): #metodo especial de representação para apresentação de resultado
        return f"{self.num}/{self.den}"
    def __add__(self, other): #metodo especial built-in de adicção
        novo_num = self.num * other.den + self.den * other.num
        novo_den = self.den * other.den
        return racional(novo_num, novo_den)
    def __sub__(self, other): #metodo especial built-in de subtração
        novo_num = self.num * other.den - self.den * other.num
        novo_den = self.den * other.den
        return racional(novo_num, novo_den)
    def __mul__(self, other): #metodo especial built-in de multiplicação
        novo_num = self.num * other.num
        novo_den = self.den * other.den
        return racional(novo_num, novo_den)
    def __truediv__(self, other): #metodo especial built-in de divisão normal
        novo_num = self.num * other.den
        novo_den = self.den * other.num
        return racional(novo_num, novo_den)
    def simplifica(self): #metodo de simplificação
        divisor_comum = self.mdc(self.num, self.den)
        self.num //= divisor_comum
        self.den //= divisor_comum
    def __repr__(self): # metodo de representação exerna do numerado e denominador
        return f"({self.num}, {self.den})"
    def primos_entre_si(self): #metodo de verificação se os numeros são primos entre si
        return self.mdc(self.num, self.den) == 1
    def nume(self):
        return self.num
    def deno(self):
        return self.den
 # (b)Usando operações polimórficas, escreva métodos para calcular a soma e o produto de racionais Se r 1 a/b e r 2 c/d
# então r 1 # r 2 (ad + bc bd e r 1 r 2 ==(a c)/(b d)
    def som(self, other):
        return self + other
    def produto(self, other):
        return self * other
    @staticmethod
    def mdc(a, b):
        if b == 0:
            return a
        return racional.mdc(b, a % b)

F1 = racional(2, 3)
print(F1.num,'e',F1.den, 'Primos?',F1.primos_entre_si())
print(f'Representação Externa {F1.__repr__()}')
F1.simplifica()
print('Simplificação de "F1"',F1)
print(f'Após simpliciação o Numerador é {F1.nume()} e o Denominador é {F1.deno()}\n------------------------------------------------------------------------')

F2 = racional(3, 2)
print(F2.num,'e',F2.den, 'Primos?',F2.primos_entre_si())
print(f'Representação Externa {F2.__repr__()}')
F2.simplifica()
print('Simplificação de  "F2"',F2)
print(f'Após simpliciação o Numerador é {F2.nume()} e o Denominador é {F2.deno()}\n------------------------------------------------------------------------')

c = F1 + F2
print('A Soma de "F1" + "F2" =', c)
Fsoma = F1.som(F2)
print('Resultado da soma de (a) com (b) usando o metodo da "soma" é: ',Fsoma)
Fsoma= F1.__add__(F2)
print('A soma das frações "F1" e "F2" é: ',Fsoma)

print('------------------------------------------------------------------------')
d = F1 * F2
print('A Multiplicação de "F1" * "F2" =', d)
Fmultiplicacao = F1.produto(F2)
print('Resultado da multiplicação de (a) com (b) usando o metodo da "soma" é: ',Fmultiplicacao)
Fmultiplicacao= F1.__mul__(F2)
print('A multiplicação das frações "F1" e "F2" é: ',Fmultiplicacao)
print('------------------------------------------------------------------------')
