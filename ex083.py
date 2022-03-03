'''e = input('Digite a expressão: ')
dir = e.count('(')
esq = e.count(')')
soma = dir + esq
if soma % 2 == 0:
    print('Sua expressão está valida!')
else:
    print('Sua expressão está errada!')'''

li = [input('Digite a expressão: ')]
dir = 0
esq = 0
for c in li:
    for i in c:
        if i == '(':
            esq += 1
        elif i == ')':
            dir += 1
if esq == dir:
    print('Sua expressão está certa!')
else:
    print('Sua expressão está errada!')