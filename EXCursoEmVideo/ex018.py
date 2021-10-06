import math
ang = int(input('Qual o angulo'))
seno = math.sin(math.radians(ang))
coseno = math.cos(math.radians(ang))
tangente = math.tan(math.radians(ang))
print('o coseno de {} é {:.2f}'.format(ang, coseno))
print('o seno de {} é {:.2f}'.format(ang, seno))
print('a tangente de {} é {:.2f}'.format(ang, tangente))
