c = 0
s = 0
while True:
    n = int(input('Digite um valor (999 para parar): '))
    if n == 999:
        break
    c += 1
    s += n
print(f'Foram digitados {c} valores e a soma entre eles é de {s}')
