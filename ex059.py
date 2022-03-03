n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
print('''[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos numeros
[ 5 ] sair do programa''')
op = int(input('Escolha uma opção: '))
while op != 5:
    if op == 1:
        soma = n1 + n2
        print('Você escolheu soma e o resultado de {} + {} é igual a {}.'.format(n1,n2,soma))
    elif op == 2:
        soma = n1 * n2
        print('Você escolheu multiplicar e o resultado de {} x {} é igual a {}'.format(n1,n2,soma))
    elif op == 3:
        if n1 > n2:
            print('Você escolheu descobrir o maior valor e o maior valor digitado foi {}'.format(n1))
        elif n2 > n1:
            print('Você escolheu descobrir o maior valor e o maior valor digitado foi {}'.format(n2))
        else:
            print('Os dois valores são iguais.')
    elif op == 4:
        print('Você escolheu digitar novos números!')
        n1 = int(input('Digite um valor: '))
        n2 = int(input('Digite outro valor: '))
    else:
        print('Você digitou uma opção invalida!')
    print('[ 1 ] somar')
    print('[ 2 ] multiplicar')
    print('[ 3 ] maior')
    print('[ 4 ] novos numeros')
    print('[ 5 ] sair do programa')
    op = int(input('Digite uma opção: '))
