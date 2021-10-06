alt = float(input('Digite a sua altura: '))
peso = float(input('Digite seu peso: '))
imc = peso / (alt ** 2)
print('Seu imc é de {:.2f}'.format(imc))
if imc < 18.5:
    print('Voce está abaixo do peso')
elif imc < 25:
    print('Voce está no peso ideal!')
    # elif 18.5 <= imc < 25
elif imc < 30:
    print('Voce está com sobrepeso')
elif imc < 40:
    print('Voce está obeso!')
else:
    print('Voce está com obesidade mórbida!')
