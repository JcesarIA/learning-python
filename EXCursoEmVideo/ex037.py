num = int(input('Digite um numero para ser convertido: '))
print('''selecione a conversão:
1)Binario
2)Octal
3)Hexadecimal''')
escolha = int(input('sua escolha: '))
if escolha == 1:
    print('A conversão de {} para binario é {}'.format(num, bin(num)[2:]))
elif escolha == 2:
    print('A cpnversão de {} para octal é {}'.format(num, oct(num)[2:]))
elif escolha == 3:
    print('A conversão de {} para hexadecimal é {}'.format(num, hex(num)[2:]))
else:
    print('Escolha invalida')
