lista = []
alunos = []
while True:
    lista.append(input('Digite o nome do aluno: '))
    lista.append(float(input('Nota 1: ')))
    lista.append(float(input('Nota 2: ')))
    alunos.append(lista[:])
    lista.clear()
    e = input('Quer continuar[S/N]: ')
    while e not in 'SsNn':
        e = input('Tente novamente[S/N]: ')
    if e in 'Nn':
        break
c = 0
print(f'{"No.":<4} {"NOME":<10}{"MÈDIA":>8}')
print('-' * 30)
for a in range(len(alunos)):
    media = (alunos[a][1] + alunos[a][2]) / 2
    print(f'{a:<4}{alunos[a][0]:<10}{media:>8}')
while True:
    nta = int(input('Digite o número para mostra as notas[999 para parar]: '))
    if nta == 999:
        break
    print(f'As Notas de {alunos[nta][0]} são n1 = {alunos[nta][1]} n2 = {alunos[nta][2]}')
print('Finalizando.')
