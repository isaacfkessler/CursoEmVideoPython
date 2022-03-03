cores = {'limpa':'\033[m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         'amarelo':'\033[33m',
         'azul':'\033[34m',
         'roxo':'\033[35m',
         'ciano':'\033[36m'}


n = int(input('Digite um número: '))
print('{} * {:2} = {}{}{}'.format(n,1,cores['roxo'],n * 1,cores['limpa']))
print('{} * {:2} = {}{}{}'.format(n,2,cores['ciano'],n * 2,cores['limpa']))
print('{} * {:2} = {}{}{}'.format(n,3,cores['azul'],n * 3,cores['limpa']))
print('{} * {:2} = {}{}{}'.format(n,4,cores['vermelho'],n * 4,cores['limpa']))
print('{} * {:2} = {}{}{}'.format(n,5,cores['verde'],n * 5,cores['limpa']))
print('{} * {:2} = {}{}{}'.format(n,6,cores['amarelo'],n * 6,cores['limpa']))
print('{} * {:2} = {}{}{}'.format(n,7,cores['roxo'],n * 7,cores['limpa']))
print('{} * {:2} = {}{}{}'.format(n,8,cores['ciano'],n * 8,cores['limpa']))
print('{} * {:2} = {}{}{}'.format(n,9,cores['azul'],n * 9,cores['limpa']))
print('{} * {:2} = {}{}{}'.format(n,10,cores['vermelho'],n * 10,cores['limpa']))