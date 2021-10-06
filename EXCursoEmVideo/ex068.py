from random import randint
v = 0
print('-*'*20)
print(f'Vamos jogar Impar ou Par!')
print('-*'*20)
while True:
    pc = randint(1, 10)
    ps = int(input('Digite um valor de 0 a 10: '))
    escolha = ' '
    while escolha not in 'PI':
        escolha = input("Par ou Impar[P/I]: ").strip().upper()[0]
    print(f'O Computador escolheu {pc}')
    if (pc + ps) % 2 == 0:
        print(f'{pc} + {ps} = par')
        if escolha == 'P':
            print('Você venceu, vamos jogar de novo?')
            v += 1
            continue
        elif escolha == 'I':
            print('Você perdeu!')
            break
    elif (pc + ps) % 2 != 0:
        print(f'{pc} + {ps} = Impar')
        if escolha == 'I':
            print('Você venceu, vamos jogar de novo?')
            v += 1
            continue
        elif escolha == 'P':
            print('Você perdeu!')
            break
print(f'Vitórias consecutivas {v}')
