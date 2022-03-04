dados = {}
ls = []
dados['nome'] = input('Nome do Jogador: ').strip().capitalize()
qtd = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
cont = 0
total = 0
while cont < qtd:
    v = int(input(f'Quantos gols na partida {cont}? '))
    ls.append(v)
    total += v
    cont += 1
dados['gols'] = ls
dados['total'] = total
print('-='*50)
print(dados)
print('-='*50)
for k,v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*50)
print(f'O jogador {dados["nome"]} jogou {qtd} partidas.')
for i,v in enumerate(dados['gols']):
    print(f'=> Na partida {i}, fez {v} gols.')
print(f'Foi um total de {dados["total"]} gols.')