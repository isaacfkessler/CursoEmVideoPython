print('='*30)
print('    10 TERMOS DE UMA PA')
print('='*30)

termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
for c in range(0,10):
    print('{}'.format(razao * c),end=' → ')
print('ACABOU')