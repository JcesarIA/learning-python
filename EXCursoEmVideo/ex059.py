from time import sleep
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
menu = '''
Escolha uma opção:
[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa
Sua opção: '''
sair = False
while not sair:
    e = int(input(menu))
    if e == 1:
        print(f'\nA soma de {num1} + {num2} = {num1 + num2}')
    elif e == 2:
        print(f'\nA mutiplicação de {num1} * {num2} = {num1 * num2}')
    elif e == 3:
        if num1 > num2:
            print(f'\nO número {num1} é maior que {num2}')
        elif num2 > num1:
            print(f'\nO número {num2} é maior que {num1}')
        else:
            print('Os dois valores são iguais')
    elif e == 4:
        num1 = int(input('\nDigite o primeiro número: '))
        num2 = int(input('\nDigite o segundo número: '))
    elif e == 5:
        print('Obrigado.')
        sair =True
    else:
        print('Opção invalida, tente novamente.')
    sleep(2)
print('Programa finalizado')
