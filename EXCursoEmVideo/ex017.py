from math import sqrt
a = float(input('digite o tamanho do cateto oposto: '))
b = float(input('digite o tamanho do cateto adjacente: '))
c = sqrt(a**2 + b**2)
print('a medida da hipotenusa é : {:.2f}'.format(c))
