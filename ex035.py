############################ Verificar se 3 retas formam um triangulo ###############

# Solicito ao usuário 3 retas

r1 = float(input('Digite a primeira reta: '))
r2 = float(input('Digite a segunda reta: '))
r3 = float(input('Digite a terceira reta: '))

# Operação matemática para descobrir se as 3 retas podem formar um triângulo
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r3:
    print('É UM TRIANGULO!')
# Caso não formem
else:
    print('NÃO É UM TRIANGULO!')