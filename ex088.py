from random import randint
from time import sleep
ls = []
p = []
print('-='*40)
print('{:^40}'.format('SEJA BEM VINDO AO GERADOR DE PALPITES DA MEGA!!!'))
print('-='*40)
qtd = int(input('Quantos jogos você quer gerar? '))
cont = 1
print('-='*3,end='')
print(f' SORTEANDO {qtd} JOGOS ',end='')
print('-='*3)
while cont <= qtd:
    for c in range(0,6):
        v = randint(0,60)
        if v not in p:
            p.append(v)
        else:
            while v in p:
                v = randint(0,60)
            p.append(v)
    ls.append(p[:])
    p.sort()
    print(f'Jogo {cont}: {p}')
    p.clear()
    cont += 1
    sleep(0.5)
print('-='*6,' < BOA SORTE! > ','-='*6)
