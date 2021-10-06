frase = input('Digite uma frase: ').strip().lower()
print('A letra A aparece {} vezes'.format(frase.count('a')))
print('A primeira vez que a letra A aparece é na posição {}'.format(frase.find('a') + 1))
print('A ultima vez que a letra A aparece é na posição {}'.format(frase.rfind('a') + 1))
