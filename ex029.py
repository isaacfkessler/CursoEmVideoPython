# Solicita a velocidade do carro ao usuário
v = int(input('Qual é a velocidade do carro? : '))

# Se a velocidade for maior do que 80, exibe a multa
if v > 80:
    # Calcula o valor da multa
    multa = (v - 80) * 7
    print('Você foi multado em R${} ! '.format(multa))

# SENÃO, Exibe ao usuário mensagens de dentro do limite da via.
else:
    print('Você estava no limite da via!')
    print('Portanto, não será multado.')