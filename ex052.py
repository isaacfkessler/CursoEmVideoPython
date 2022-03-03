####### TENTAR NOVAMENTE


n = int(input('Digite um número: '))
tot = 0
for c in range(1,n + 1):
    if n % c == 0:
        print('\033[34m',end='')
        tot += 1
    else:
        print('\033[m',end='')
    print('{} '.format(c),end='')
print('\nO número {} foi divisivel {} vezes'.format(n,tot))
if tot == 2:
    print('É NÚMERO PRIMO')
else:
    print('NÃO É NÚMERO PRIMO.')
