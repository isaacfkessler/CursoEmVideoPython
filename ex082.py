ls = []
li = []
lp = []
while True:
    ls.append(int(input('Digite um número: ')))
    op = input('Quer continuar? [S/N] ').upper().strip()
    while op != 'S' and op != 'N':
        op = input('Quer continuar? [S/N] ').upper().strip()
    if op == 'N':
        break
for c in ls:
    if c % 2 == 0:
        lp.append(c)
    else:
        li.append(c)
print('-='*40)
print(f'A lista completa é {ls}')
print(f'A lista de pares é {lp}')
print(f'A lista de impares é {li}')

