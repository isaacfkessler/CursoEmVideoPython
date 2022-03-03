from random import randint
tup = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print('Os valores sorteados foram: ',end='')
for c in tup:
    print(c,end=' ')
tupo = sorted(tup)
'''print(f'\nO maior valor sorteado foi {tupo[4]}')
print(f'O menor valor sorteado foi {tupo[0]}')'''
print(f'\nO maior valor sorteado foi {max(tup)}')
print(f'O menor valor sorteado foi {min(tup)}')