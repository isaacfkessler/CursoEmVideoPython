ls = [[], []]

for c in range(1, 8):
    v = int(input(f'Digite o {c}° valor: '))
    if v % 2 == 0:
        ls[0].append(v)
    else:
        ls[1].append(v)
print('-='*40)
ls[0].sort()
ls[1].sort()
print(f'Os valores pares digitados foram: {ls[0]}')
print(f'Os valores ímpares digitados foram: {ls[1]}')
