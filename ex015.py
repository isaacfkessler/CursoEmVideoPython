dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
precod = 60 * dias
precok = 0.15 * km
print('O preço da Km é de R${}'.format(precok))
print('O preço dos dias é de R${:.2f}'.format(precod))
print('O preço total é de R${}'.format(precod + precok))