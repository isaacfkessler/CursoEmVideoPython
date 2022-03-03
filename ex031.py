# Solicita a distância ao usuário
d = float(input('Qual vai ser a distância da sua viagem? : '))
# Se a distancia for menor do que 200
# Criei váriavel que calcula o valor, com preço de 0.50
if d <= 200:
    valor = d * 0.50
    print('O valor cobrado será de R${} '.format(valor))
# SE FOR MAIOR DO QUE 200 KM
# Calcula com preço de 0.45
else:
    valor = d * 0.45
    print('O valor cobrado será de R${} '.format(valor))