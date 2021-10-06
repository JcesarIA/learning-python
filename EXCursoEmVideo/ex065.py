num = int(input('Digite um número: '))
maior = num
menor = num
nums = 1
total = num
escolha = input('Quer continuar[S/N]: ').strip().upper()
if escolha == 'N':
    exit(print('Você só digitou um número.'))
while escolha == 'S':
    num = int(input('Digite um número: '))
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    nums += 1
    total += num
    escolha = input('Quer continuar[S/N]: ').strip().upper()
print(f'Você digitou {nums} números, o maior deles foi {maior} o menor foi {menor}\n '
      f'A média entre eles foi {total / nums}')
