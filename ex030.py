# Solicita ao usuário um número inteiro
n = int(input('Digite um número: '))

# Para descobrir se o número é PAR, o número precisa que o RESTO DA DIVISÃO POR 2 seja 0
if (n % 2 == 0):
    print('O número é PAR!')
# Se o RESTO DA DIVISÃO não for 0
# Exibe mensagem avisando que o número é IMPAR.
else:
    print('O número é IMPAR!')