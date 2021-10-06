n = int(input('Digite um numero para fazer a fatoração: '))  # input do numero a ser fatorado
v = n
f = 1
print(f'{n}! = ', end='')
while v > 0:
    print(f'{v}', end='')
    print(' x 'if v > 1 else' = ', end='')
    f *= v
    v -= 1
print(f)
