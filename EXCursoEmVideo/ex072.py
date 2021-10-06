numeros = ('zero', 'um', 'dois', 'três', 'Quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    pos = int(input('Digite um numero de 0 a 20[-1 sair] : '))
    if pos < 0:
        break
    if pos > 20:
        print('Número invalido tente novamente.')
    else:
        print(f'{pos} por extenso é: {numeros[pos]}')

print('Obrigado e volte sempre.')
