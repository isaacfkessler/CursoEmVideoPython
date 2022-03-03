nome = input('Digite o seu nome : ')
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'roxo':'\033[35m',
         'ciano':'\033[36m',
         'verde':'\033[32m',
         'vermelho':'\033[31m',
         'amarelo':'\033[33m'}
print('Seja bem vindo(a) {}{}{} !'.format(cores['roxo'],nome,cores['limpa']))