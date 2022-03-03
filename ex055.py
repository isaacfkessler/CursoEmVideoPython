# REFAZER

maior = 0
menor = 0

for c in range(1, 6):
    peso = float(input('Digite o peso da {}° pessoa: '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print('O mais pesado foi {} KG'.format(maior))
print('O mais leve foi {} KG'.format(menor))
