def foo(n):
    n *= 3
    print(n)
def foo2(n):
    n *= 4
    print(n)
x=int(input(':'))
if x==1:
    foo(10)
elif x==2:
    foo2(x)
elif x==3:
    foo(5)
else:
    print('Erro')