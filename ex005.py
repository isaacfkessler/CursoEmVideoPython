n = int(input('Digite um número: '))
cores = {'vermelho':'\033[31m',
         'verde':'\033[32m',
         'amarelo':'\033[33m',
         'azul':'\033[34m',
         'roxo':'\033[35m',
         'ciano':'\033[36m',
         'limpa':'\033[m'}
ant = n - 1
suc = n + 1
print('O número é {}{}{}'.format(cores['roxo'],n,cores['limpa']))
print('O seu antecessor é {}{}{}'.format(cores['verde'],ant,cores['limpa']))
print('O seu sucessor é {}{}{}'.format(cores['vermelho'],suc,cores['limpa']))