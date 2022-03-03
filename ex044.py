# REFAZER EXERCICIO
print(f'\033[35m{" LOJA BARCELONA ":=^40}\033[m')

preco = float(input('Qual o valor do produto? R$'))
print('QUAL A FORMA DE PAGAMENTO?')
print('1 - A VISTA DINHEIRO / CHEQUE COM 10% DE DESCONTO')
print('2 - A VISTA NO CARTÃO COM 5% DE DESCONTO')
print('3 - EM ATÉ 2X NO CARTÃO COM PREÇO NORMAL')
print('4 - 3X OU MAIS NO CARTÃO COM 20% DE JUROS')
opcao = int(input(': '))
if opcao == 1:
    desc = preco - (preco * 0.10)
    print('A modalidade escolhida foi A VISTA')
    print('E O PREÇO FINAL É DE R${:.2f}'.format(desc))
elif opcao == 2:
    desc = preco - (preco * 0.05)
    print('A modalidade escolhida foi A VISTA NO CARTÃO')
    print('E O PREÇO FINAL É DE R${:.2f}'.format(desc))
elif opcao == 3:
    parcelas = int(input('Quantas parcelas? '))
    if parcelas == 2:
        print('A modalidade escolhida foi EM ATÉ 2X NO CARTÃO')
        print('Sua compra será parcelada em {}x de R${:.2f} SEM JUROS'.format(parcelas,preco / parcelas))
        print('E O PREÇO FINAL É DE R${:.2f}'.format(preco))
    else:
        print('Opa! Você escolheu a opção errada!')
elif opcao == 4:
    parcelas = int(input('Quantas parcelas? '))
    if parcelas >= 3:
        desc = preco + (preco * 0.20)
        print('A modalidade escolhida foi 3X OU MAIS NO CARTÃO')
        print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(parcelas,desc / parcelas))
        print('E O PREÇO FINAL É DE R${:.2f}'.format(desc))
    else:
        print('Opa! Você escolheu a opção errada!')
else:
    print('OPÇÃO NÃO ENCONTRADA!')
