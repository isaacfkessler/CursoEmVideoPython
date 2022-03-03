# MENSAGEM INTERATIVA
print('VERIFICANDO SE O NOME DA CIDADE POSSUI "SANTO" .')
#
cidade = input('Digite o nome da cidade: ')
cidade = cidade.upper()
cidade = cidade.split()

print('A CIDADE COMEÇA COM "SANTO"? {}'.format('SANTO' == cidade[0]))