i = 0 #idade do homem mais velho
h = ''#nome do homem mais velho
id = 0 #média de idade
m = 0 #mulheres abaixo dos 20 anos
for c in range(1,5):
    print('-='*10, f'{c}° pessoa', '-='*10)
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo[M/F]: ').strip().upper()
    id += idade
    if sexo == 'M' and idade > i:
        i += idade
        h += nome
    if sexo == 'F' and idade < 20:
        m += 1
print(f'A média de idade do grupo é {id / 4}')
print(f'O homem mais velho tem {i} e se chama {h}')
print(f'O total são de {m} Mulher(s) abaixo dos 20 anos')
