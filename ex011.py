cores = {'limpa':'\033[m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         'amarelo':'\033[33m]',
         'azul':'\033[34m',
         'roxo':'\033[35m',
         'ciano':'\033[36m'}

larg = float(input('Digite a largura: '))
alt = float(input('Digite a altura: '))
area = larg * alt
tinta = area * 0.5
print('A largura é de {}{}{} metros'.format(cores['ciano'],larg,cores['limpa']))
print('A altura é de {}{}{} metros'.format(cores['roxo'],alt,cores['limpa']))
print('A área é de {}{}{} m²'.format(cores['vermelho'],area,cores['limpa']))
print('A quantidade necessária de tinta é de {}{}{} litros.'.format(cores['verde'],tinta,cores['limpa']))