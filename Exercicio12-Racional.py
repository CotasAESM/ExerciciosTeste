class Racional:
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def __str__(self):
        return f"{self.numerador}/{self.denominador}"

    def __repr__(self):
        return f"Racional({self.numerador}, {self.denominador})"

    def __add__(self, other):
        novo_numerador = self.numerador * other.denominador + self.denominador * other.numerador
        novo_denominador = self.denominador * other.denominador
        return Racional(novo_numerador, novo_denominador)

    def __sub__(self, other):
        novo_numerador = self.numerador * other.denominador - self.denominador * other.numerador
        novo_denominador = self.denominador * other.denominador
        return Racional(novo_numerador, novo_denominador)

    def __mul__(self, other):
        novo_numerador = self.numerador * other.numerador
        novo_denominador = self.denominador * other.denominador
        return Racional(novo_numerador, novo_denominador)

    def __truediv__(self, other):
        novo_numerador = self.numerador * other.denominador
        novo_denominador = self.denominador * other.numerador
        return Racional(novo_numerador, novo_denominador)

    def simplifica(self):
        divisor_comum = self.mdc(self.numerador, self.denominador)
        self.numerador //= divisor_comum
        self.denominador //= divisor_comum
#primos_entre_si que retorna True se o numerador e o denominador são primos entre si e False caso contrário.
#método usando o algoritmo de Euclides para calcular o máximo divisor comum (mdc) entre o numerador e o denominador.
# Se o mdc for 1, então o numerador e o denominador são primos entre si.
# Caso contrário, eles têm um fator comum e a fração não está na forma simplificada.
    def primos_entre_si(self):
        return self.mdc(self.numerador, self.denominador) == 1

    def nume(self):
        return self.numerador

    def deno(self):
        return self.denominador

    def soma(self, other):
        return self + other

    def produto(self, other):
        return self * other

    @staticmethod
    def mdc(a, b):
        if b == 0:
            return a
        return Racional.mdc(b, a % b)

a = Racional(6, 35)
print(a.numerador,'e',a.denominador, 'Primos?',a.primos_entre_si())
a.simplifica()
print('simplifica a',a)
print('numerador:',a.nume())
print('denominador:',a.deno())

b = Racional(8, 12)
print(b.numerador,'e',b.denominador, 'Primos?',b.primos_entre_si())
b.simplifica()
print('simplifica b',b)
print('numerador:',b.nume())
print('denominador:',b.deno())

c = a + b
print('a + b =', c)

d = a.soma(b)
print(d, '= soma(a) com (b)')

