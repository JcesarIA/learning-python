prod = ('Lapís', 1.75, 'Borracha', 2.00, 'Caderno', 15.00, 'Estojo', 25.00, 'Transferidor',
        4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'livro', 34.90)
h1 = 'LISTAGEM DE PREÇOS'
print(f'{h1:^33}')

for c in range(0, len(prod)):
    if c % 2 == 0:
        print(f'{prod[c]:.<30}', end='')
    else:
        print(f'R${prod[c]:>6.2f}')
