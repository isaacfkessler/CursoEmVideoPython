cores = {'limpa':'\033[m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         'amarelo':'\033[33m',
         'azul':'\033[34m',
         'roxo':'\033[35m',
         'ciano':'\033[36m'}


n = int(input('Digite um número: '))
dobro = n * 2
triplo = n * 3
raiz = n ** (1/2)
print('O número é {}{}{}'.format(cores['roxo'],n,cores['limpa']))
print('O dobro é {}{}{}'.format(cores['azul'],dobro,cores['limpa']))
print('O triplo é {}{}{}'.format(cores['verde'],triplo,cores['limpa']))
print('A raiz é {}{:.0f}{}'.format(cores['vermelho'],raiz,cores['limpa']))
