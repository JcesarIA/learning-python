import random
import emoji
choice = int(input('Estou pensando em um numero de 0 a 5 chute um: '))
num1 = random.randint(0, 5)
if choice == num1:
    print(emoji.emojize('parabéns!!! eu pensei no numero {}'.format(choice)))
else:
    print(emoji.emojize('Voce errou :broken_heart: o numero que eu pensei era {}'.format(num1)))
