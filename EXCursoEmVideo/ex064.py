acum = 0 #soma dos números
num = 0 #quantidade de números
flag = 0 #gatilho de parada
while flag != 999:
    n1 = int(input('Digite um número[999 para parar.]: '))
    if n1 == 999:
        flag = 999
    else:
        acum += n1
        num += 1
print(f'Voce digitou {num} números e a soma deles é {acum}')
