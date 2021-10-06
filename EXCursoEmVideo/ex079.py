list = []
while True:
    val = int(input('Digite um valor a ser adicionado: '))
    if val not in list:
        list.append(val)
        print('Valor Adicinado com sucesso')
        e = input('Quer continuar[S/N]? ')[0].upper()
        while e not in 'SN':
            e = input('Opção invalida tente novamente[S/N]: ')[0].upper()
        if e == 'N':
            break
    elif val in list:
        print('Valor já está na lista tente novamente!')
        continue
print(f'Os valores digitados foram {sorted(list)}')

