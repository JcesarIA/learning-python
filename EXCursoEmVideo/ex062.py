n = int(input('Digite o numero inicial de uma pa: ')) #var de inicio pa.
r = int(input('Digite a razão da pa: ')) #var razão
c = 0 #contador
total = 0
while c <10:
    print(f'{n} ', end='')
    n += r
    c += 1
    total += 1
    if c == 10:
        new = int(input('Quer imprimir mais quantas? '))
        c -= new
        if new == 0:
            print(f'O programa finalizou com {total} termos mostrados')
