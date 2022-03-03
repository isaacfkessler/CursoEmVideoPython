n = int(input('Digite um número: '))
cont = 1
soma = n
while n != 999:
    n = int(input('Digite um número: '))
    if n != 999:
        cont += 1
        soma += n
print('Foram digitados {} números'.format(cont))
print('A soma entre eles foi de {}'.format(soma))
