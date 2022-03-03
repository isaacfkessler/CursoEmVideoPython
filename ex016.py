# importei a biblioteca "math"
import math
# solicitei ao usuário que informasse um número
numero = float(input('Digite um número : '))
# Após isso, criei uma váriavel para pegar somente número inteiro, usando a função "trunc" - DA O NÚMERO INTEIRO
num = math.trunc(numero)
# Por fim, imprimi o resultado da operação de num na tela.
print(num)