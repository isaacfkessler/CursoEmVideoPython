print('='*30)
print('BANCO CEV')
print('='*30)
cel50 = 0
while True:
    valor = int(input('Que valor você quer sacar? R$'))
    if valor >= 50:
        while valor // 50 == 0:
            valor -= 50
            cel50 += 1
            print(cel50)
    break
print(f'Total de {cel50} cédulas de R$50')