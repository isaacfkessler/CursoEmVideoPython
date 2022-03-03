cores = {'limpa':'\033[m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         'amarelo':'\033[33m',
         'azul':'\033[34m',
         'roxo':'\033[35m',
         'ciano':'\033[36m'}


n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print('A primeira nota foi {}{}{}'.format(cores['verde'],n1,cores['limpa']))
print('A segunda nota foi {}{}{}'.format(cores['roxo'],n2,cores['limpa']))
print('A média é de {}{}{}'.format(cores['azul'],media,cores['limpa']))