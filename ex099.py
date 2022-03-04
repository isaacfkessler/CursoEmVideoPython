def maior(* num):
    print('-='*40)
    print('Analisando os valores passados...')
    for i in num:
        print(f'{i} ',end='')
    print(f'Foram informados {len(num)} valores ao todo.')
    c = 0
    m = 0
    while c < len(num):
        if num[c] > m:
            m = num[c]
        c += 1
    print(f'O maior valor informado foi {m}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
