from datetime import date
ano = date.today().year
s = 0
m = 0
for c in range(0,7):
    n = int(input('Digite o ano de nascimento: '))
    idade = ano - n
    if idade < 18:
        s += 1
    else:
        m += 1
print('{} pessoas não atingiram a maioridade ainda.'.format(s))
print('{} pessoas atingiram a maioridade.'.format(m))
