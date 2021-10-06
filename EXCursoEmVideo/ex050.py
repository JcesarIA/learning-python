acum = 0
for c in range(1, 7):
    num = int(input('Digite um numero: '))
    if num % 2 == 0:
        acum += num
print('A soma dos números pares são {}'.format(acum))
