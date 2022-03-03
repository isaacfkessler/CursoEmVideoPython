n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
print('O aluno teve a média {} e está de: '.format(m))
if m < 5:
    print('REPROVADO')
elif m <= 6.9:
    print('RECUPERAÇÃO')
else:
    print('APROVADO')
