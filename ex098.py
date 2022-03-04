from time import sleep
def contador(i,f,p):
    if p == 0:
        p += 1
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if i < f:
        for c in range(i,f,p):
            print(f'{c}',end=' ')
            sleep(0.3)
        print('FIM!')
    elif p < 0:
        for c in range(i,f-1,p):
            print(f'{c}',end=' ')
            sleep(0.3)
        print('FIM!')
    else:
        for c in range(i,f-1,-p):
            print(f'{c}',end=' ')
            sleep(0.3)
        print('FIM!')

print('-='*40)
print('Contagem de 1 até 10 de 1 em 1')
for c in range(1,11):
    print(f'{c}',end= ' ')
    sleep(0.3)
print('FIM!')
print('-='*40)
print('Contagem de 10 até 0 de 2 em 2')
for c in range(10,-1,-2):
    print(f'{c}',end= ' ')
    sleep(0.3)
print('FIM!')
print('-='*40)
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i,f,p)