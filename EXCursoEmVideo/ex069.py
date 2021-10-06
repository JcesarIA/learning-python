maior = 0
h = 0
m = 0
while True:
    print('*-'*20 ,'\nCADASTRO.\n','*-'*20 )
    idade = int(input('Digite a idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = input('Digite o sexo[M/F]: ').strip().upper()[0]
    if idade >= 18:
        maior += 1
    if sexo == 'M':
        h += 1
    if sexo == 'F' and idade < 20:
        m += 1
    flag = ' '
    while flag not in 'SN':
        flag = input('Voce quer continuar[S/N]: ').upper().strip()[0]
    if flag in 'Nn':
        break
print(f'O programa finalizou com {maior} pessoas maiores, {h} homens e {m} mulheres menores de 20 anos.')
