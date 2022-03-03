from datetime import date
ano = date.today().year
n = int(input('Qual o ano de nascimento do atleta? : '))
idade = ano - n

print('O atleta possui {} anos'.format(idade))
if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade <= 20:
    print('SENIOR')
else:
    print('MASTER')
