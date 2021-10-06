from datetime import datetime
Nascimento = int(input('Insira a data do seu nascimento: '))
idade = datetime.today().year - Nascimento
if idade <= 9:
    print(f'Com {idade} Anos sua categoria é Mirim. ')
elif idade <= 14:
    print(f'Com {idade} Anos sua categoria é Infantil. ')
elif idade <= 19:
    print(f'Com {idade} Anos sua categoria é Júnior ')
elif idade <= 25:
    print(f'Com {idade} Anos sua categoria é Sênior ')
elif idade > 25:
    print(f'Com {idade} Anos sua categoria é Master ')

