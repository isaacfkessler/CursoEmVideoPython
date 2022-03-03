from random import randint
from time import sleep
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
sleep(1)
print('Será que você consegue adivinhar qual foi?')
sleep(1)
acertou = False
pc = randint(0,10)
cont = 0
while not acertou:
    n = int(input('Qual seu palpite? '))
    cont += 1
    if n == pc:
        acertou = True
    elif n > pc:
        print('Menos! Quase la...')
    else:
        print('Mais! Quase la...')
print('Parabéns! Você acertou em {} tentativas!'.format(cont))