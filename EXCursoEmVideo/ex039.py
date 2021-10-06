from datetime import datetime
atual = datetime.today().year
print('{}'.format(atual))
print('ALISTAMENTO MILITAR {}'.format(atual))
sexo = int(input('''Digite seu sexo:
 1) Feminino
 2) Masculino
  Digite o numero correspondente: '''))
if sexo == 2:
    ano = int(input('Informe o ano do seu nascimento: '))
    alis = atual - ano
    print('Quem nasceu em {} tem {} anos em 2021'.format(ano, alis))
else:
    print('Pessoas do sexo feminino não precisam se alistar')
    exit(print('Obrigado e tenha um bom dia'))
alis = atual - ano
if alis < 18 and sexo == 2:
    saldo = 18 - alis
    print('Ainda falta(m) {} ano(s) para seu alistamento'.format(saldo))
    ano = atual + saldo
    print('o seu ano de alistamento é {}'.format(ano))
elif alis > 18 and sexo == 2:
    saldo = alis - 18
    print('Você está {} anos atrasado com seu alistamento, Visite uma junta militar imediatamente'.format(saldo))
    ano = atual - saldo
    print('Você deveria ter se alistado em {}'.format(ano))
elif alis == 18 and sexo == 2:
    print('Você precisa se alistar esse ano!')
print('Obrigado e tenha um bom dia!')
