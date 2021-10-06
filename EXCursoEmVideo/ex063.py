ve = int(input('Quantos números quer imprimir? '))#a quantidade de numeros que serão impressos
c = 0 # contador
num1 = 0
num2 = 1
if ve < 0:
    print('Digite um numero valido!')
else:
    while c < ve:
        print(num1)
        fib = num1 + num2
        num1 = num2
        num2 = fib
        c += 1
