ls = []
dado = []
maior = 0
nomaior = []
menor = 0
nomenor = []
c = 0
while True:
    dado.append(input('Nome: ').capitalize().strip())
    dado.append(float(input('Peso: ')))
    ls.append(dado[:])
    if c == 0:
        maior = dado[1]
        menor = dado[1]
        nomaior.append(dado[0])
        nomenor.append(dado[0])
    elif dado[1] == maior:
        nomaior.append(dado[0])
    elif dado[1] > maior:
        maior = dado[1]
        nomaior.clear()
        nomaior.append(dado[0])
    elif dado[1] == menor:
        nomenor.append(dado[0])
    elif dado[1] < menor:
        menor = dado[1]
        nomenor.clear()
        nomenor.append(dado[0])
    dado.clear()
    c += 1
    while True:
        op = input('Você deseja continuar? [S/N] ').upper().strip()
        if op == 'S' or op == 'N':
            break
    if op == 'N':
        break
print('-='*50)
print(f'Ao todo, você cadastrou {len(ls)} pessoas')
print(f'O maior peso foi de {maior}Kg. Peso de {nomaior}')
print(f'O menor peso foi de {menor}Kg. Peso de {nomenor}')