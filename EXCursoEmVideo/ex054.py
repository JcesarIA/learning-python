from datetime import date
atual = date.today().year
menor = 0
maior = 0
for c in range(1, 8):
    nascimento = int(input('Digite o ano de nascimento da {}° pessoa: '.format(c)))
    if atual - nascimento < 18:
        menor += 1
    elif atual - nascimento >= 18:
        maior += 1
print('Nas datas analisadas existem,{} maiores e {} menores'.format(maior, menor))
