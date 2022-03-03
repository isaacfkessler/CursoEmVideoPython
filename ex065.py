n = int(input('Digite um numero inteiro: '))
cont = 1
soma = n
menor = n
maior = n
op = input('Você deseja continuar a digitar valores? [S/N]: ').upper()
while op == 'S':
    n = int(input('Digite um numero inteiro: '))
    if n > maior:
        maior = n
    elif n < menor:
        menor = n
    cont += 1
    soma += n
    op = input('Você deseja continuar a digitar valores? [S/N]: ').upper()
print('A média entre todos os valores é de {}'.format(soma / cont))
print('O maior número lido foi {}'.format(maior))
print('O menor número lido foi {}'.format(menor))
