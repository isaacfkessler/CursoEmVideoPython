matriz = [[0, 0, 0], [0, 0, 0,], [0, 0, 0,]]
for c in range(0,3):
    for i in range(0,3):
        matriz[c][i] = int(input(f'Digite um número para a posição [{c}] [{i}]:  '))
print('-='*30)
for c in range(0,3):
    for i in range(0,3):
        print(f'[{matriz[c][i]:^5}]',end='')
    print()