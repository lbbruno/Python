from time import sleep
from random import randint


def titulo(txt):
    print(f'\033[034m{"="*40}\n{txt:^40}\n{"="*40}\033[038m')


def linha():
    print('-'*40)


def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos: Não vota.'
    elif idade < 18 or idade > 65:
        return f'Com {idade} anos: Voto não é obrigatório.'
    else:
        return f'Com {idade} anos: Voto é obrigatório.'


# MAIN

titulo('Função Voto Obrigatório')
anonasc = int(input("Ano de nascimento: "))
print(voto(anonasc))
