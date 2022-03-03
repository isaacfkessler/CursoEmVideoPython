from random import randint
print('-='*15)
print('VAMOS JOGAR PAR OU IMPAR')
print('-='*15)
cont = 0
while True:
    c = randint(1,10)
    n = int(input('Diga um valor: '))
    op = input('Par ou Impar? [P/I] : ').upper().strip()
    print('-'*30)
    soma = c + n
    if soma % 2 == 0:
        print(f'Você jogou {n} e o computador {c}. Total de {soma} DEU PAR')
        print('-'*30)
        if op == 'P':
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
            cont += 1
        else:
            print('Você PERDEU!')
            break
    else:
        print(f'Você jogou {n} e o computador {c}. Total de {soma} DEU IMPAR')
        print('-'*300)
        if op == 'I':
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
            cont += 1
        else:
            print('Você PERDEU!')
            break
    print('=-'*15)
print('=-'*15)
print(f'GAME OVER! Você venceu {cont} vezes.')