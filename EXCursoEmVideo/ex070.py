total = 0
maior = 0
nmaior = ''
mil = 0
while True:
    print('-'*20,'\nCaixa Automatico')
    print('-'*20)
    nome = input('Digite o nome do produto: ')
    preço = float(input('Digite o preço do produto: '))
    if preço > maior:
        maior = preço
        nmaior = nome
    if preço >= 1000.00:
        mil += 1
    total += preço
    escolha = ' '
    while escolha not in 'SN':
        escolha = input('Quer continuar[S/N]? ').upper().strip()[0]
    if escolha == 'N':
        break
print(f'O total deu R${total:.2f}')
print(f'O nome do produto com maior valor foi {nmaior} e o preço foi R${maior:.2f}')
print(f'{mil} produtos custaram mil ou mais')
