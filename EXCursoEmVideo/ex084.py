pessoas = []
todos = []
maior = 0
menor = 0
while True:
    pessoas.append(input('Digite o nome da pessoa: '))
    pessoas.append(float(input('Digite o peso da pessoa: ')))
    for c in pessoas:
        if len(todos) == 0:
            maior = pessoas[1]
            menor = pessoas[1]
        if pessoas[1] > maior:
            maior = pessoas[1]
        if pessoas[1] < menor:
            menor = pessoas[1]
    todos.append(pessoas[:])
    pessoas.clear()
    e = input('quer continuar[S/N]? ').upper().strip()[0]
    while e not in 'SN':
        e = input('Opção invalida[S/N]: ').upper().strip()[0]
    if e == 'N':
        break
print(f'{len(todos)} Pessoas foram cadastradas')
print(f'O maior peso registrado foi {maior:.1f}Kg, o registro foi feito no nome de: ', end='')
for c in todos:
    if c[1] == maior:
        print(c[0], end='. ')
print(f'\nO menor peso registrado foi {menor:.1f}Kg, o registro foi feito no nome de: ', end='')
for c in todos:
    if c[1] == menor:
        print(c[0], end='. ')
