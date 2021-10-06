from random import randint
from time import sleep
print('vamos jogar JOKENPO')
pc = randint(0, 2)
player = int(input('''Escolha uma opção
0) PEDRA
1) PAPEL
2) TESOURA
Sua escolha: '''))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
if player == 0 and pc == 1:
    print('O computador escolheu PAPEL')
    print('O Jogador escolheu PEDRA')
    print('Você PERDEU')
elif player == 0 and pc == 2:
    print('O Computador escolheu TESOURA')
    print('O Jogador escolheu PEDRA')
    print('Voce VENCEU')
elif player == 1 and pc == 0:
    print('O Computador escolheu PEDRA')
    print('O Jogador escolheu PAPEL')
    print('Você VENCEU')
elif player == 1 and pc == 2:
    print('O Computador escolheu TESOURA')
    print('O Jogador escolheu PAPEL')
    print('Você perdeu')
elif player == 2 and pc == 0:
    print('O Computador escolheu Pedra')
    print('O Jogador escolheu TESOURA')
    print('Você PERDEU')
elif player == 2 and pc == 1:
    print('O Computador escolheu PAPEL')
    print('O Jogador escolheu TESOURA')
    print('O Jogador VENCEU')
elif player == 0 and pc == 0:
    print('Os dois escolheram PEDRA')
elif player == 1 and pc == 1:
    print('Os dois escolheram PAPEL')
elif player == 2 and pc ==2:
    print('Os dois escolheram TESOURA')
else:
    print('Escolha invalida!')
