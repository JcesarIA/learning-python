palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis',
'estudar', 'praticar', 'trabalhar', 'mercado', 'programador', 'futuro')
for p in palavras:
    print(f'\nEm {p.upper()} temos ', end='')
    for letra in p:
        if letra in 'aeiou':
            print(letra, end=' ')
