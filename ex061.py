# TIVE DIFICULDADE
print('='*30)
print('       10 TERMOS DA PA')
print('='*30)

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
cont = 0

while cont < 10:
    print('{} → '.format(termo),end='')
    termo += razao
    cont += 1
print('FIM')