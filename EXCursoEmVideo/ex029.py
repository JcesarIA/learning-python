vel = int(input('qual a velocidade em que voce está? '))
if vel <= 80:
    print('parabéns continue dirigindo com cuidado!')
else:
    multa = (vel-80) * 7.00
    print('Voce passou a {} em uma via de 80 e recebeu R$ {:.2f} de multa.'.format(vel, multa))
