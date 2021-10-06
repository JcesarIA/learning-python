name = input('Digite seu nome: ').strip().lower()
n = name.split()
print('seu primeiro nome é {}'.format(n[0]))
print('seu ultimo nome é {}'.format(n[len(n)-1]))
