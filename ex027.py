# STRIP - Para remover espaços iniciais e finais
nome = str(input('Digite o seu nome completo: ')).strip()
# Convertendo nome para uma lista com a função SPLIT
n = nome.split()
# Imprimindo o primeiro item da lista
print('Seu primeiro nome é {}'.format(n[0]))
# Criei váriavel para contar a posição do ultimo item da lista
qt = len(n) - 1
# Com essa váriavel, foi possivel imprimir o ultimo item da lista
print('Seu ultimo nome é {}'.format(n[qt]))

