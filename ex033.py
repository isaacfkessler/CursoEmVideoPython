# Solicito ao usuário 3 números
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

# Fiz vários ELIF para descobrir qual o número digitado é o maior e qual é o menor
if n1 > n2 and n2 > n3:
    print('O maior número é {}'.format(n1))
    print('O menor número é {}'.format(n3))
elif n2 > n1 and n1 > n3:
    print('O maior número é {}'.format(n2))
    print('O menor número é {}'.format(n3))
elif n3 > n1 and n1 > n2:
    print('O maior número é {}'.format(n3))
    print('O menor número é {}'.format(n2))
elif n1 > n2 and n3 > n2:
    print('O maior número é {}'.format(n1))
    print('O menor número é {}'.format(n2))
elif n2 > n3 and n3 > n1:
    print('O maior número é {}'.format(n2))
    print('O menor número é {}'.format(n1))
# Else para em caso de erro de lógica, ser avisado.
else:
    print('FALTAM CONDIÇOES!')