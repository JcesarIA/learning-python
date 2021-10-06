s = 0
while True:
    n = int(input('Digite um numero [999 para parar]: '))
    if n == 999:
        break
    s += n
print(f'A soma dos números digitados são {s}')
