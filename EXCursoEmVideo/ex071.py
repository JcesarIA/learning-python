valor = int(input('Digite um valor a ser sacado: '))
ced = 0
nota = 50
while True:
    if valor >= nota:
        valor -= nota
        ced += 1
    else:
        if ced > 0:
            print(f'{ced} notas de R${nota}')
        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 1
        ced = 0
        if valor == 0:
            break
print(f'Obrigado')
