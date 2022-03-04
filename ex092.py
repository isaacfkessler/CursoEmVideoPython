from datetime import date
ls = {}
ls['nome'] = input('Nome: ').capitalize().strip()
ano = int(input('Ano de Nascimento: '))
atual = date.today().year
ls['idade'] = atual - ano
ls['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if ls['ctps'] != 0:
    anoc = int(input('Ano de Contratação: '))
    ls['contratação'] = anoc
    ls['salário'] = float(input('Salário: '))
    idadec = (anoc - ano) + 35
    ls['aposentadoria'] = idadec
print('-='*50)
for k,v in ls.items():
    print(f'- {k} tem o valor {v}')