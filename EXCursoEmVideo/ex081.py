lista = []
cont = 0
while True:
    lista.append(int(input('Digite um valor: ')))
    cont += 1
    e = input('quer continuar[S/N]: ').upper().strip()[0]
    while e not in 'SN':
        e = input('Ooção invalida[S/N]: ').upper().strip()[0]
    if e == 'N':
        print('Saindo')
        break
print(f'Foram digitados {cont} Números')
print(f'Os valores digitados em ordem drescente {sorted(lista, reverse=True)}')
if 5 in lista:
    print(f'O número 5 foi digitado e aparece na posição {lista.index(5)}')
else:
    print('O número 5 não foi digitado.')
