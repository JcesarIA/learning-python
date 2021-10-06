from random import randint
from time import sleep
quant = int(input('Quantos jogos voce quer? '))
jogo_temp = []
jogo_todos = []
n = 1
for c in range(quant):
    while n <= 6:
        num = randint(1, 60)
        if num not in jogo_temp:
            jogo_temp.append(num)
            n += 1
    jogo_todos.append(jogo_temp[:])
    jogo_temp.clear()
    n = 1
    print(f'JOGO {c+1}: {jogo_todos[c]}')
    sleep(1)
print(f'BOA SORTE')