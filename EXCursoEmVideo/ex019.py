from random import choice
a1 = input('Primeiro aluno: ')
a2 = input('segundo aluno: ')
a3 = input('terceiro alino: ')
a4 = input('quarto aluno: ')
lista = [a1, a2, a3, a4]
print('o aluno escolhido foi: {}'.format(choice(lista)))
