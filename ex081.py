ls = []
while True:
    ls.append(int(input('Digite um número: ')))
    op = input('Quer continuar? [S/N] ').upper().strip()
    while op != 'N' and op != 'S':
        op = input('Quer continuar? [S/N] ').upper().strip()
    if op == 'N':
        break
print('-='*40)
print(f'Você digitou {len(ls)} elementos.')
ls.sort(reverse=True)
print(f'Os valores em ordem decrescente são {ls}')
if 5 in ls:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não faz parte da lista!')