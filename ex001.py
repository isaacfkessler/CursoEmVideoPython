msg = 'Olá mundo!'
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'verde':'\033[32m',
         'vermelho':'\033[31m',
         'amarelo':'\033[33m',
         'ciano':'\033[36m',
         'roxo':'\033[35m'}
print('{}{}{}'.format(cores['azul'],msg,cores['limpa']))