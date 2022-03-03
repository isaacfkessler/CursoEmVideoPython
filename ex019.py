# Importei a biblioteca de gerar números aleatórios
import random

# Solicitei o nome de 4 alunos
aluno1 = input('Escreva o nome do primeiro aluno: ')
aluno2 = input('Escreva o nome do segundo aluno: ')
aluno3 = input('Escreva o nome do terceiro aluno: ')
aluno4 = input('Escreva o nome do quarto aluno: ')
# Criei variavel que sorteia entre os 4 alunos
# Para isso, usei a função "choice", que escolhe uma das 4 opções
# Importante colocar [], pois sem elas, não estava lendo e estava dando erros.
sort = random.choice([aluno1,aluno2,aluno3,aluno4])
# Por fim, pedi para imprimir o valor.
print(sort)