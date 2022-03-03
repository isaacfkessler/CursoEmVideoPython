# Solicita ao usuário um número
numero = int(input('Digite um número de 0 a 9999: '))
# Matematica para pegar ultimo número
u = numero // 1 % 10
# Matemática para pegar o penultimo número
d = numero // 10 % 10
# Matemática para pegar o segundo número
c = numero // 100 % 10
# Matemática para pegar o primeiro número
m = numero // 1000 % 10
# Imprimi cada unídade referente ao seu respectivo valor.
print('Unidade : {} '.format(u))
print('Dezena : {} '.format(d))
print('Centena : {} '.format(c))
print('Milhar : {} '.format(m))
