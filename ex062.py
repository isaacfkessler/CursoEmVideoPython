########## REVISE SEMPRE!!!!!!!!! ############
from time import sleep
print('Gerador de PA')
print('-='*15)
termo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
cont = 0
op = False
c = 10
total = 0
while not op:
    total += c
    while cont < c:
        print('{} → '.format(termo),end='')
        termo += razao
        cont += 1
    print('PAUSA')
    c = int(input('Quantos termos você quer mostrar a mais? '))
    cont = 0
    if c == 0:
        op = True
        print('OK ! Encerrando o programa...')
        sleep(0.5)
print('\nPrograma encerrado.')
print('Progressão finalizada com {} termos mostrados.'.format(total))