lista = []
print(lista)
for c in range(0, 5):
    i = int(input('Digite um valor: '))
    if c == 0 or i > lista[-1]:
        lista.append(i)
        print('Adicionando a última posição.')
    else:
        pos = 0
        while pos < len(lista):
            if i <= lista[pos]:
                lista.insert(pos, i)
                print(f'Adicionando na posição {pos}')
                break
            pos += 1
print(f'A lista Ordenada é {lista}')


