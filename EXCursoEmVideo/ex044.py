from time import sleep
preço = float(input('Digite o valor do produto R$'))
choice = int(input('''Escolha uma opção
1) A vista / boleto:: 10 % de desconto
2) A vista no cartão: 5% de desconto
3) 2x no cartão: preço normal
4) 3x ou mais: 20 % de juros
Sua escolha? '''))
print('Adicionando ao carrinho...')
sleep(1)
if choice == 1:
    total = preço * 0.90
    print('O total com o pagamento no boleto é de R${:.2f}'.format(total))
elif choice == 2:
    total = preço * 0.95
    print('O total com o pagamento a vista é de R${:.2f}'.format(total))
elif choice == 3:
    print('O total em 2x no cartão é de R${:.2f} e as parcelas serão de R${:.2f}'.format(preço, preço / 2))
elif choice == 4:
    parcelas = int(input('Quantas parcelas? '))
    total = preço * 1.20
    print('O total em 3x ou mais no cartão é de R${:.2f}'.format(total))
    print('As parcelas serão de R${:.2f}'.format(total / parcelas))
else:
    print('Opção invalida de pagamento.')
