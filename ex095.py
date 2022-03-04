time = []
dados = {}
ls = []
while True:
    dados.clear()
    dados['nome'] = input('Nome do Jogador: ').strip().capitalize()
    qtd = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
    cont = 0
    total = 0
    ls.clear()
    while cont < qtd:
        v = int(input(f'Quantos gols na partida {cont}? '))
        ls.append(v)
        total += v
        cont += 1
    dados['gols'] = ls[:]
    dados['total'] = total
    time.append(dados.copy())
    while True:
        op = input('Quer continuar? [S/N] ').strip().upper()
        if op == 'S' or op == 'N':
            break
        print('ERRO! Escolha uma opção valida ( [S/N] )')
    if op == 'N':
        break
print('-='*50)
print('cod', end='')
for i in dados.keys():
    print(f'{i:<15}',end='')
print()
for k, v in enumerate(time):
    print(f'{k:>3}' ,end='')
    for d in v.values():
        print(f'{str(d):<15}',end='')
    print()

print('-='*50)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com código de {busca}!')
    else:
        print(f' --- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}')
        for i, g in enumerate(time[busca]["gols"]):
            print(f'No jogo {i+1} fez {g} gols.')
print('PROGRAMA FINALIZADO!')