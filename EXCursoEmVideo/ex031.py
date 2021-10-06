kms = float(input('Digite o tamanho de sua viagem em kms: '))
if kms <= 200:
    valor = kms * 0.50
    print('O valor da sua viagem é: R${:.2f}'.format(valor))
else:
    valor = kms * 0.45
    print('O valor da sua viagem é: R${:.2f}'.format(valor))
