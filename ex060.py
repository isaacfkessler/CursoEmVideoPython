##### REFAZER BASTANTE PARA ENTENDER MELHOR
from math import factorial
n = int(input('Digite um número inteiro: '))
soma = 1
print('Calculando {}! = '.format(n), end='')
while n > 0:
    soma = soma * n
    if n != 1:
        print('{} x '.format(n),end='')
    else:
        print('{} = '.format(n),end='')
        print(soma)
    n -= 1