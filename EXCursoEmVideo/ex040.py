nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
print('Sua nota é {}'.format(media))
if media < 5:
    print('Voce foi reprovado!')
elif 5 < media <= 6.9:
    print('Voce está de recuperação!')
elif media > 7:
    print('Voce foi aprovado!')
