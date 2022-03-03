print('-'*30)
print('LOJA SUPER BARATÃO')
print('-'*30)
total = 0
qtd = 0
menor = 0
nomenor = ''
cont = 0
while True:
    nome = input('Nome do produto: ').strip().capitalize()
    preco = float(input('Preço: R$'))
    total += preco
    cont += 1
    if preco > 1000:
        qtd += 1
    if cont == 1:
        menor = preco
        nomenor = nome
    elif preco < menor:
        menor = preco
        nomenor = nome
    op = input('Quer continuar? [S/N] ').strip().upper()
    while op != 'S' and op != 'N':
        op = input('Quer continuar? [S/N] ').strip().upper()
    if op == 'N':
        break
print('-'*10,' FIM DO PROGRAMA ','-'*10)
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {qtd} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nomenor} que custa R${menor:.2f}')