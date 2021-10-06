expre = input('Digite uma expressão para ver se é valida: ')
lista = []
for p in expre:
    if p == '(':
        lista.append('(')
    elif p == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if lista == 0:
    print('Expressão válida')
else:
    print('Expressão inválida')