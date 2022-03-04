from time import sleep
from random import randint
def sorteia():
    print('Sorteando 5 valores da lista: ',end='')
    for c in range(0,5):
        v = randint(0,10)
        print(f'{v} ',end='')
        sleep(0.5)
        numeros.append(v)
    print('PRONTO!')
def somaPar():
    soma = 0
    for i in numeros:
        if i % 2 == 0:
            soma += i
    print(f'Somando os valores pares de {numeros}, temos {soma}')


numeros = []
sorteia()
somaPar()