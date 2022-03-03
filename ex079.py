ls = []
while True:
    n = int(input('Digite um valor: '))
    if n not in ls:
        ls.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    op = input('Quer continuar? [S/N]: ').upper().strip()
    while op != 'S' and op != 'N':
        op = input('Quer continuar: [S/N]: ').upper().strip()
    if op == 'N':
        break
print('-='*40)
ls.sort()
print(f'Você digitou os valores {ls}')