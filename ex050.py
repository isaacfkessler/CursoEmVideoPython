print('=-'*10,' SOMADOR NÚMEROS INTEIROS ','=-'*10)

s = 0
for c in range(0,6):
    n = int(input('Digite um número inteiro: '))
    if n % 2 == 0:
        s += n
print('=-'*20)
print('A soma entre os números é {}'.format(s))
