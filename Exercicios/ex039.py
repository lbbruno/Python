from datetime import datetime
anoAtual = int(datetime.now().year)
anoNasc = int(input('Informe o seu ano de nascimento: '))
ano = anoAtual - anoNasc
if ano < 18:
    print('Ainda vai se alistar no exercito.')
elif ano == 18:
    print('Está em época de se alistar no exercíto.')
else:
    print('Já passou da época do alistamneto.')

