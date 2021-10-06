from random import randint
num = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
print(f'Os valores sorteados são: {num}')
print(f'O maior número é {sorted(num)[4]}')
print(f'O menor número é {sorted(num)[0]}')
