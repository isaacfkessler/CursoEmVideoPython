pessoa = {}
galera = []
soma = 0
while True:
    pessoa.clear()
    pessoa['nome'] = input('Nome: ').capitalize().strip()
    while True:
        pessoa['sexo'] = input('Sexo: [M/F] ').upper().strip()
        if pessoa['sexo'] == 'M' or pessoa['sexo'] == 'F':
            break
        print('ERRO! Por favor, Digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        op = input('Quer continuar? [S/N] ').strip().upper()
        if op == 'N' or op == 'S':
            break
        print('Erro! Opção invalida. Escolha entre [S/N]')
    if op == 'N':
        break
print('-='*40)
media = soma / len(galera)
print(f'Ao todo temos {len(galera)} pessoas cadastradas')
print(f'A média de idade do grupo é de {media:.1f} anos.')
print('As mulheres cadastradas foram ', end='')
for p in galera:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}',end=' ')
print()
print('Lista das pessoas que estão acima da média: ', end='')
for p in galera:
    if p['idade'] > media:
        print(f'{p["nome"]}',end=' ')
print()
print('<< ENCERRADO >>')