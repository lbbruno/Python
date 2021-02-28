div1 = '='*40
div2 = '-'
print(f'{div1}\n{"Calculo de Aposentadoria":^40}\n{div1}')

    # Bibliotecas
from datetime import datetime

    # Inicialização de variáveis
pessoa = dict()
ano = datetime.now().year
    # Principal
pessoa['nome'] = str(input('Nome: '))
pessoa['idade'] = int(ano - int(input('Ano de Nascimento: ')))
pessoa['ctps'] = int(input('Carteira de Trabalho (0 não tem) :'))
if pessoa['ctps'] != 0:
    pessoa['contratação'] = int(input('Ano de contratação: '))
    pessoa['salário'] = float(input('Salário: '))
    pessoa['aposentadoria'] = 35 - (ano - pessoa['contratação'])+ pessoa['idade']
print(div1)
for k, v in pessoa.items():
    print(f'\t- {k} => {v}')

print(div2)
