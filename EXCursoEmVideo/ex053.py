frase = input('Digite uma frase: ').strip().upper()
lista = frase.split()
junto = ''.join(lista)
inverso = ''
for c in range(len(junto)-1, -1, -1):
    inverso += junto[c]
print(junto, inverso)
if inverso == junto:
    print('È um palindromo')
else:
    print('Não é um palindromo')
