while True:
    num = int(input('Quer ver a tabuada de qual número? (Numero negativo para finalizar) '))
    if num < 0:
        break
    for p in range(1, 11):
        print(f'{num} x {p} = {num*p}')
print('Programa finalizado.')
