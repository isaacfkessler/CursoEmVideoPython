# Importei função RANDINT da biblioteca RANDOM
#   Função gera números inteiros aleatórios
from random import randint
#   Função gera um tempo de espera
from time import sleep
# Guardei na memória, criando uma váriavel para receber o número aleatório
numero = randint(0,5)

# Solicitei ao usuário para que mande um número inteiro
n = int(input('Advinhe: Qual o número que o computador pensou? '))
# Se o número for igual ao número que o computador gerou
#   Ele escreve uma mensagem de acerto
print('Processando...')
sleep(3)
if n == numero:
    print('Parabens!! Você acertou!!!')
# Senão ele escreve que você perdeu.
else:
    print('Você perdeu :c')

# Por fim, revelo o número ao usuario.
print('O número foi {}'.format(numero))