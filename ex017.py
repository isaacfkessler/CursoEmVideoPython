# importei a biblioteca math, que ja vem instalada de padrão
from math import hypot

# solicitei o dado cateto oposto e depois solicitei o adjascente
cc = float(input('Qual o comprimento do cateto oposto? '))
ca = float(input('Qual o comprimento do cateto adjacente? '))

# Criei uma váriavel para calcular a hipotenusa, usando a função "hypot() da biblioteca MATH
hipo = hypot(cc,ca)

# Por fim, imprimi na tela o resultado da operação.
print('A hipotenusa vai medir {:.2f}'.format(hipo))