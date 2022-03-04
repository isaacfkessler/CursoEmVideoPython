######################## REFAZER SEMPRE #################################

ficha = []
while True:
    nome = input('Nome: ').capitalize().strip()
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    ficha.append([nome,[n1, n2],media])
    while True:
        op = input('Deseja continuar? [S/N] ').upper().strip()
        if op == 'N' or op == 'S':
            break
    if op == 'N':
        break
print('-='*30)
print(f'{"No.":<4}{"NOME:":<10}{"MÉDIA":>8}')
print('-'*26)
for cont,a in enumerate(ficha):
    print(f'{cont:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'*35)
    opc = int(input('Mostrar notas de qual aluno? 999 interrompe : '))
    if opc == 999:
        print('FINALIZANDO...')
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')