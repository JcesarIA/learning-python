valor = float(input('Qual o valor da casa? R$'))
parcelas = int(input('Quantos anos de financiamento? ')) * 12
salario = float(input('Qual sua renda mensal? R$'))
max = salario * 0.30
parc = valor // parcelas
if parc > max:
    print('Seu empréstimo foi reprovado pois o seu salario é incompativel')
elif parc <= max:
    print('Seu empréstimo foi aprovado!')
    print('Voce Pagará R${:.2f} em {} meses'.format(parc,parcelas))
print('Obrigado e tenha um bom dia!')
