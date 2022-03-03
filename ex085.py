ls = []
p = []
i = []
ls.append(p)
ls.append(i)
print(ls)
for c in range(0,7):
    v = int(input('Digite um valor: '))
    if v % 2 == 0:
        p.append(v)
    else:
        i.append(v)
print('-='*50)
p.sort()
i.sort()
print(f'Os valores pares digitados foram: {ls[0]}')
print(f'Os valores impares digitados foram: {ls[1]}')