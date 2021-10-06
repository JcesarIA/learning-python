sal = float(input('Qual o seu salario? R$'))
if sal <= 1250:
    print('O seu novo salario será de R${:.2f}'.format(sal * 1.15))
else:
    print('O seu novo salario será de R${:.2f}'.format(sal * 1.10))
