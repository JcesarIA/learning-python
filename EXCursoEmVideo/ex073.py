times = (
    'Bragantino', 'Bahia', 'Ceará', 'Fortaleza', 'Athletico-PR', 'Flamengo', 'Atlético-GO', 'Cuiabá', 'Sport',
    'Juventude',
    'Internacional',
    'São Paulo', 'Fluminense', 'Grêmio', 'Atlético-MG', 'América-MG', 'Palmeiras', 'Corinthians', 'Chapecoense',
    'Santos')
print(f'Tabela de classificação Brasileirão 2021 {times}')
print(f'Os 5 primeiros são {times[:5]}')
print(f'Os 4 ultimos são {times[16:]}')
print(f'Os times em ordem alfabetica é {sorted(times)}')
print(f'O Chapecoense está na {times.index("Chapecoense")+1}º Posição')
