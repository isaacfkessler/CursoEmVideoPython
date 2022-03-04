# REDO THIS EXERCISE
from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
rank = {}
print(jogo)
print('Valores sorteados: ')
for k,v in jogo.items():
    sleep(0.5)
    print(f'{k} jogou o dado e caiu o número {v}')
rank = sorted(jogo.items(), key=itemgetter(1),reverse=True) #### ISSO É IMPORTANTE ESTUDAR!!! ####
print('-='*50)
print('RANKING')
for i, v in enumerate(rank):
    print(f'{i + 1}° lugar: {v[0]} com {v[1]}')
