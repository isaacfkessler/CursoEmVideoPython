cores = {'limpa':'\033[m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         'amarelo':'\033[33m',
         'azul':'\033[34m',
         'roxo':'\033[35m',
         'ciano':'\033[36m'}

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
soma = n1 + n2
print('A soma entre {} e {} é {}{}{} .'.format(n1,n2,cores['ciano'],soma,cores['limpa']))