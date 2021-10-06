tri1 = float(input('Digite o primeiro Segmento: '))
tri2 = float(input('Digite o segundo segmento: '))
tri3 = float(input('Digite o terceiro segmento: '))
me1 = tri1
me2 = tri2
maior = tri3
if tri3 < tri1 < tri2:
    me1 = tri1
    me2 = tri3
    maior = tri2
if tri2 < tri3 <tri1:
    me1 = tri2
    me2 = tri3
    maior = tri1
if me1 + me2 > maior:
    print('o triangulo pode ser formado.')
else:
    print('o triangulo não pode ser formado.')
