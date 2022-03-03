ls = []
for c in range(0,5):
    ls.append(int(input(f'Digite um valor para a Posição {c}: ')))
print('-='*40)
print(f'Você digitou os valores {ls}')
print(f'O maior valor foi {max(ls)} nas posições ',end='')
for c,valor in enumerate(ls):
    if valor == max(ls):
        print(f'{c}... ',end='')
print(f'\nO menor valor digitado foi {min(ls)} nas posições ',end='')
for c,valor in enumerate(ls):
    if valor == min(ls):
        print(f'{c}... ',end='')