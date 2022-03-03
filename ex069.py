from time import sleep
sexo = ''
mais = 0
mulheres = 0
homens = 0
while True:
    print('-' * 30)
    print('CADASTRE UMA PESSOA')
    print('-' * 30)
    idade = int(input('Idade: '))
    sexo = input('Sexo: [M/F] ').upper().strip()
    while sexo != 'M' and sexo != 'F':
        sexo = input('Sexo: [M/F] ').upper().strip()
    print('-'*30)
    if idade > 18:
        mais += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1
    elif sexo == 'M':
        homens += 1
    op = input('Quer continuar? [S/N] ').upper().strip()
    while op != 'S' and op != 'N':
            print('Você digitou uma opção inválida! Tente novamente.')
            op = input('Quer continuar? [S/N] ').upper().strip()
    if op == 'N':
        print('Ok! O programa será encerrado...')
        sleep(1)
        break

print('='*10,' FIM DO PROGRAMA ','='*10)
print(f'Total de pessoas com mais de 18 anos: {mais}')
print(f'Ao todo temos {homens} homens cadastrados')
print(f'E temos {mulheres} mulheres com menos de 20 anos')