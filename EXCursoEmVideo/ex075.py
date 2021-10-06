tuple = (int(input('Digite um valor')),
         int(input('Digite um valor')),
         int(input('Digite um valor')),
         int(input('Digite um valor')))
print(f'Valores digitados: {tuple}')
print(f'O numero 9 aparece {tuple.count(9)} vezes')
if 3 in tuple:
    print(f'O numero três apareceu na {tuple.index(3)+1}° posição')
else:
    print('O número 3 não foi digitado')
print(f'Os números pares digitados foram: ', end='')
for c in tuple:
    if c % 2 == 0:
        print(c, end=' ')

