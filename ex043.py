peso = float(input('Qual é o seu peso? : '))
altura = float(input('Qual é a sua altura? : '))
imc = peso / (altura**2)

print('O seu IMC é {:.2f}'.format(imc))
if imc < 18.5:
    print('ABAIXO DO PESO')
elif imc < 25:
    print('PESO IDEAL')
elif imc < 30:
    print('SOBREPESO')
elif imc < 40:
    print('OBESIDADE')
else:
    print('OBESIDADE MORBIDA')