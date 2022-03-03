v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))
v3 = int(input('Terceiro valor: '))
v4 = int(input('Quarto valor: '))
tup = (v1,v2,v3,v4)
print(f'O valor 9 apareceu {tup.count(9)} vezes.')
if 3 in tup:
    print(f'O valor 3 foi digitado pela primeira vez na {tup.index(3) + 1}° posição.')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram ',end='')
for c in tup:
    if c % 2 == 0:
        print(c,end=' ')