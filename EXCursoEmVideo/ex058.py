from random import randint
e = randint(0,  10)#Escolha aleatória do numero
p = int(input('Pensei em um numero de 0 a 10, Consegue acertar? '))#input do jogador
c = 1#contador
while p != e:
    p = int(input('Errou, Voce pode tentar novamente: '))
    c += 1
print('Parabéns voce acertou!')
print(f'Levou somente {c} tentativas')
