while True:
    n = int(input('Qual tabuada você quer? '))
    if n < 0:
        break
    print('-'*30)
    for c in range(1,11):
        soma = n * c
        print(f'{n} x {c} = {soma}')
    print('-'*30)
print('Você digitou um número negativo e o programa foi encerrado.')