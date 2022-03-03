from time import sleep
from random import choice
print('=-'*15,'JOKENPÔ','=-'*15)
print('ESCOLHA UMA OPÇÃO:')
print('PEDRA | PAPEL | TESOURA')
opcao = input(': ').upper()
escolha = choice(['PEDRA','PAPEL','TESOURA'])
sleep(0.5)
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO')
print('=-'*30)
if escolha == opcao:
    print('Deu empate!')
elif opcao == 'PAPEL' and escolha == 'PEDRA':
    print('Você me venceu!')
    print('EU ESCOLHI {}'.format(escolha))
elif opcao == 'TESOURA' and escolha == 'PAPEL':
    print('Você me venceu!')
    print('EU ESCOLHI {}'.format(escolha))
elif opcao == 'PEDRA' and escolha == 'TESOURA':
    print('Você me venceu!')
    print('EU ESCOLHI {}'.format(escolha))
elif opcao != 'PEDRA' and opcao != 'TESOURA' and opcao != 'PAPEL':
    print('GAME FINALIZADO!')
    print('VOCÊ DIGITOU UM COMANDO INVALIDO.')
else:
    print('OPS! VOCÊ PERDEU PRA MIM!')
    print('Eu escolhi {}'.format(escolha))