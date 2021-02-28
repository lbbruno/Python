from datetime import datetime
frame = '*' * 60
print(frame)
print('{:*^60}'.format(' Confederação Nacional de Natação '))
print(frame)

anoAtual = datetime.now().year
anoNasc = int(input('Informe o ano de nascimento do atleta: '))
idade = anoAtual - anoNasc
categoria = str('')

if idade < 10:
    categoria = 'Mirim'
elif idade < 15:
    categoria = 'Infantil'
elif idade < 20:
    categoria = 'Junior'
elif idade == 20:
    categoria = 'Sênior'
else:
    categoria = 'Master'

print('Idade: {} | Categoria: {}'.format(idade, categoria))