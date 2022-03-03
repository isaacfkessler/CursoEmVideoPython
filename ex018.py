import math
angulo = float(input('Digite um angulo: '))

# USEI FUNÇÃO "radians" para converter de graus para radiano, pois é o que as funções "sin,cos,tan" lêem.
sen = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))
print('O seno é {:.2f}'.format(sen))
print('O cosseno é {:.2f}'.format(cos))
print('A tangente é {:.2f}'.format(tan))