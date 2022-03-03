# DESAFIO 026 - Faça um programa que leia uma frase pelo teclado e mostre:
#   QUANTAS VEZES APARECE A LETRA "A"
#   EM QUE POSIÇÃO ELA APARECE A PRIMEIRA VEZ
#   EM QUE POSIÇÃO ELA APARECE A ÚLTIMA VEZ

# Função STRIP para remover os espaços iniciais e finais
# Função UPPER para colocar tudo em Maíuscula
frase = input('Digite uma frase: ').strip().upper()
# Usei função COUNT para contar quantas vezes a letra A aparece.
print('A letra "A" aparece {} vezes.'.format(frase.count('A')))
# Usei função FIND para buscar onde a letra A aparece primeiro
print('A letra "A" aparece pela primeira vez na {} posição.'.format(frase.find('A')))
# Usei função RFIND para buscar onde está a ultima letra A.
## NO CASO, O "R" FAZ COM QUE COMEÇE A PROCURAR PELO LADO ---> DIREITO <--- .
print('A letra "A" aparece pela ultima vez na {} posição.'.format(frase.rfind('A')))