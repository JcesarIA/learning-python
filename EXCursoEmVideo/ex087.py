matrix = [[0, 0, 0],  [0, 0, 0], [0, 0, 0]]
par = 0
col3 = 0
maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matrix[l][c] = int(input(f'Digite o valor para a posição [{l}][{c}]: '))
print('-=' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matrix[l][c]:^5}]', end='')
        if matrix[l][c] % 2 == 0:
            par += matrix[l][c]
    print()
print('-=' * 30)
print(f'A soma dos números pares é {par}')
for l in range(0, 3):
    col3 += matrix[l][2]
print(f'A soma dos numeros inseridos na 3 coluna é {col3}')
for num in matrix[1]:
    if num > maior:
        maior = num
print(f'O maior número na segunda linha é {6}')
