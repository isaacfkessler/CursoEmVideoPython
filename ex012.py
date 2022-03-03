preco = float(input('Digite o preço do produto: '))
desc = preco * 0.05
print('O preço do produto é R$ {}'.format(preco))
print('O desconto é de R$ {}'.format(desc))
print('O preço final é de R$ {}'.format(preco - desc))