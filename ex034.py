################ DESCOBRIR AUMENTO DO SALÁRIO FUNCIONÁRIO ##################
# Solicito ao usuário o salario dele
salario = float(input('Digite o seu salário atual : R$'))

# Se o salário for maior do que 1250
## É dado 10% de aumento
if salario > 1250:
    aumento = salario * 0.10
    print('Seu aumento é de 10% e você terá um aumento de R${}'.format(aumento))
# Se o salário for menor ou igual a 1250
## É dado 15% de aumento
else:
    aumento = salario * 0.15
    print('Seu aumento é de 15% e você terá um aumento de R${}'.format(aumento))