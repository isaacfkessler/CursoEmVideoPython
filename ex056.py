verificador = 0
velho = 'Ninguem'
qtdm = 0
media = 0
for c in range(0,4):
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    print('''Qual o SEXO?
    [ 1 ] MASCULINO
    [ 2 ] FEMININO''')
    sexo = int(input('Sexo: '))
    media += idade
    if idade > verificador and sexo == 1:
        verificador = idade
        velho = nome
    if sexo == 2 and idade < 20:
        qtdm += 1
print('A média da idade do grupo é de {} anos.'.format(media / 4))
print('O nome do homem mais velho é {}'.format(velho))
print('Há {} mulheres com menos de 20 anos.'.format(qtdm))