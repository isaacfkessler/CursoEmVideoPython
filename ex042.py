r1 = float(input('Primeira Reta: '))
r2 = float(input('Segunda Reta: '))
r3 = float(input('Terceira Reta: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('É triângulo!')
    if r1 == r2 and r2 == r3:
        print('EQUILATERO')
    elif r1 != r2 and r2 != r3:
        print('ESCALENO')
    else:
        print('ISÓSCELES')
else:
    print('NÃO É TRIANGULO!')