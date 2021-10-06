a = []
b = []
c = []
while True:
    a.append(int(input('Digite um número: ')))
    e = input('Deseja continuar[S/N]?').upper().strip()[0]
    while e not in 'SN':
        e = input('Opção invalida[S/N]:').upper().strip()[0]
    if e == 'N':
        break
for i, v in enumerate(a):
    if a[i] % 2 == 0:
        b.append(v)
    else:
        c.append(v)
print(f'Voce digitou {len(a)} números e eles são {a}')
print(f'Voce digitou os seguintes números pares {b}')
print(f'Voce digitou os seguintes números impares {c}')

'''cont = 0
while True:
    a.append(int(input('Digite um numero: ')))
    if a[cont] % 2 == 0:
        b.append(a[cont])
    else:
        c.append(a[cont])
    cont += 1
    e = input('Deseja continuar[S/N]?').upper().strip()[0]
    while e not in 'SN':
        e = input('Opção invalida[S/N]:').upper().strip()[0]
    if e == 'N':
        break
print(f'Voce digitou {cont} números e eles são {a}')
print(f'Voce digitou os seguintes números pares {b}')
print(f'Voce digitou os seguintes números impares {c}')'''
