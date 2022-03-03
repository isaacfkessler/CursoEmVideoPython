s = str(input('Digite o seu sexo [M/F] : ')).upper().strip()
while s != 'M' and s != 'F':
    print('Erro! Você digitou um valor errado.')
    s = str(input('Digite o seu sexo [M/F] : ')).upper().strip()
if s == 'F':
    print('Sexo FEMININO cadastrado! ')
else:
    print('Sexo MASCULINO cadastrado! ')