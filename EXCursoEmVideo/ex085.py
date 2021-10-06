lista = [[], []]
for c in range(1, 8):
    num = int(input(f'Digite o {c}° número:'))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)
print(f'Os Numeros pares digitados foram: ', end='')
for c in lista[0]:
    print(c, end=' ')
print('\nOs Numeros impares digitados foram: ', end='')
for c in lista[1]:
    print(c, end=' ')
