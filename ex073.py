tabela = ('Atletico MG','Flamengo','Palmeiras','Fortaleza','Corinthians','Bragantino','Fluminense',
          'América MG','Atlético GO','Santos','Ceará','Internacional','São Paulo','Athletico PR',
          'Cuiabá','Juventude','Gremio','Bahia','Sport','Chapecoense')
for cont,c in enumerate(tabela):
    print(f'{cont + 1}° {c}')
print('-='*30)
print(f'Lista de times do Brasileirão: {tabela}')
print('-='*30)
print(f'Os 5 primeiros são {tabela[:5]}')
print('-='*30)
print(f'Os 4 últimos são {tabela[-4:]}')
print('-='*30)
print(f'Times em ordem alfabética: {sorted(tabela)}')
print('-='*30)
print(f'O Chapecoense está na {tabela.index("Chapecoense") + 1}° posição')