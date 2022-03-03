# Importei a data do computador, usando Função DATE da biblioteca DATETIME
from datetime import date
# Solicito ao usuário o ano
ano = int(input('Qual ano você está? 0 - Ano atual: '))

# Se a opção digitada for 0
# PUXO A FUNÇÃO DATE PARA PEGAR DATA ATUAL DO COMPUTADOR
if ano == 0:
    ano = date.today().year
    # PARA DESCOBRIR SE É BISSEXTO, DEVEMOS DESCOBRIR SE O ANO É DIVISIVEL POR 4
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print('O ano é BISSEXTO!')
    else:
        print('O ano não é BISSEXTO!')
else:
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print('O ano é BISSEXTO!')
    else:
        print('O ano NÃO é BISSEXTO!')