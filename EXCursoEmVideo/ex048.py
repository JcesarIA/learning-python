n = 0
a = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        a += 1
        n += c
print('A soma dos {} numeros impares divisiveis por 3 entre 1 e 500 é de {}'.format(a, n))
