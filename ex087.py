ls = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = 0
st = 0
for c in range(0,3):
    for i in range(0,3):
        ls[c][i] = int(input(f'Digite um valor para [{c}, {i}]: '))
print('-='*50)
for c in range(0,3):
    for i in range(0,3):
        print(f'[{ls[c][i]:^5}]',end='')
    print()
print('-='*50)
for c in ls:
    for i in c:
        if i % 2 == 0:
            soma += i
print(f'A soma dos valores pares é {soma}')
for i in range(0,3):
        st += ls[i][2]
print(f'A soma dos valores da terceira coluna é {st}')
print(f'O maior valor da segunda linha é {max(ls[1])}')