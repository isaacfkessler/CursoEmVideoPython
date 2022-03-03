cores = {'limpa':'\033[m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         'amarelo':'\033[33m',
         'azul':'\033[34m',
         'roxo':'\033[35m',
         'ciano':'\033[36m'}

valor = float(input('Digite o valor em metros : '))
cen = valor * 100
mil = cen * 10
km = valor / 10
print('O valor em metros é {}{:.0f}{} metros'.format(cores['roxo'],valor,cores['limpa']))
print('O valor em centimetros é {}{:.0f}{} centimetros'.format(cores['azul'],cen,cores['limpa']))
print('O valor em milimetros é {}{:.0f}{} milimetros'.format(cores['ciano'],mil,cores['limpa']))
print('O valor em KM é {}{:.1f}{} KM'.format(cores['amarelo'],km,cores['limpa']))
