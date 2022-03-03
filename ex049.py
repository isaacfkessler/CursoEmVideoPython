print('=-'*10,' GERADOR DE TABUADAS ','=-'*10)
numero = int(input('Digite um número para ver sua tabuada: '))

for c in range(1,11):
    print('{} x {} = {}'.format(numero,c,numero*c))
print('=-'*25)
print('TABUADA DO {} FINALIZADA!'.format(numero))
