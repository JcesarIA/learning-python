from time import sleep
num1 = int(input('Qual o primeiro numero? '))
num2 = int(input('Qual o segundo numero? '))
print('ANALISANDO...')
sleep(3)
if num1 > num2:
    print('O numero {} é maior que {}'.format(num1, num2))
elif num2 > num1:
    print('O numero {} é maior que {}'.format(num2, num1))
else:
    print('Os numeros são iguais')
print('tenha um bom dia!')
