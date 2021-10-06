dias = int(input('Quantos dias o carro foi alugado: '))
km = int(input('Quantos kms foram rodados com o carro: '))
#pkm = km * 0.15
#pd = dias * 60
#total = pd + pkm
total = (dias * 60) + (km * 0.15)
print('o preço total é  R${:.2f}'.format(total))
