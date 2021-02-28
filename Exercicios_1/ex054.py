from datetime import datetime

anoatual = int(datetime.now().year)
maior = 0
menor = 0
for i in range(1, 8):
    nasc = int(input('Digite o ano de nascimento da {}° pessoa:'.format(i)))
    idade = anoatual - nasc
    if idade >= 18:
        maior += 1
    else:
        menor += 1
print('''Existem {} pessoas menores de idade.
Existem {} pessoas maiores de idade.'''.format(menor,maior))
