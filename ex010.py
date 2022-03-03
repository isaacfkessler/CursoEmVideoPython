cores = {'limpa':'\033[m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         'amarelo':'\033[33m',
         'azul':'\033[34m',
         'roxo':'\033[35m',
         'ciano':'\033[36m'}

dinheiro = float(input('Quantos R$ você tem? R$'))
dolar = dinheiro / 3.27
print('Você tem R${}{}{} , equivalente a US${}{:.2f}{}.'.format(cores['roxo'],dinheiro,cores['limpa'],cores['ciano'],dolar,cores['limpa']))
