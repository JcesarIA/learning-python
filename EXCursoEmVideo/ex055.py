maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input(f'Digite o {c}° peso: '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if menor > peso:
            menor = peso
print(f'O maior peso inserido foi o {maior} e o menor peso colocado foi o {menor} ')
