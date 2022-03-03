# Treinar mais
# Importei somente a função que irei usar, no caso "shuffle"
from random import shuffle
# Solicitei ao usuário 4 nomes
a1 = input('Digite o nome do primeiro aluno: ')
a2 = input('Digite o nome do segundo aluno: ')
a3 = input('Digite o nome do terceiro aluno: ')
a4 = input('Digite o nome do quarto aluno: ')
# Criei uma lista com os 4 nomes
# PARA CRIAR LISTA, USAR []
lista = [a1,a2,a3,a4]
# USEI A FUNÇÃO "shuffle" para embaralhar a lista
shuffle(lista)
print('A ordem de apresentação será:')

# Imprimi a lista, que após ter passado pelo shuffle, foi embaralhada.
print(lista)