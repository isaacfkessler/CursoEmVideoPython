from datetime import date
ano = int(input('Qual o ano de nascimento? '))
print('''Escolha uma opção:
[ 1 ] Homem
[ 2 ] Mulher''')
sexo = int(input('Você é? : '))

idade = date.today().year - ano

if sexo == 1:
    if idade < 18:
        print('Você ainda irá se alistar no exercito!')
        print('Faltam {} anos.'.format(18 - idade))
    elif idade == 18:
        print('Você deve se alistar!')
    else:
        print('Ja passou do tempo de se alistar! CORRA!')
        print('Você está {} anos atrasado'.format(idade - 18))
elif sexo == 2:
    print('Você não precisa se ALISTAR pois é MULHER!')
else:
    print('OPÇÃO DIGITADA INVALIDA!')
