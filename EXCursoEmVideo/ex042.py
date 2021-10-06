tri1 = float(input('Digite o primeiro Segmento: '))
tri2 = float(input('Digite o segundo segmento: '))
tri3 = float(input('Digite o terceiro segmento: '))
if tri1 < tri2 + tri3 and tri2 < tri1 + tri3 and tri3 < tri1 + tri2:
    print('O triangulo pode ser formado e é um ', end='')
    if tri1 == tri3 == tri2:
        print('EQUILATERO')
    elif tri1 != tri2 != tri3 != tri1:
        print('ESCALENO')
    else:
        print('ISOSCELES')
else:
    print('O triangulo não pode ser formado')
