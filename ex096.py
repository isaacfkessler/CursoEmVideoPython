def area(l,c):
    a = l * c
    print(f'A área de um terreno {l}x{c} é de {a} M²')


print('Controle de Terrenos')
print('-'*30)
largura = float(input('Largura: '))
comprimento = float(input('Comprimento: '))
area(largura,comprimento)